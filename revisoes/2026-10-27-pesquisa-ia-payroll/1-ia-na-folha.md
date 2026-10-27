# Pesquisa 1 — IA / ML / redes neurais aplicadas a payroll e payslip

> Anexo de [[revisoes/2026-10-27-pesquisa-ia-payroll|Pesquisa: IA e redes neurais em payroll]] (relatório único). Números-chave reabertos na fonte em 2026-10-27 pela janela geral.

Data da pesquisa: 2026-10-27. Só leitura na web. Todas as fontes abaixo foram abertas (WebFetch), exceto onde marcado "(só resultado de busca)". Afirmações que vêm apenas de material de marketing/press release do fornecedor estão marcadas **[não confirmado]** (sem verificação independente).

Páginas que recusaram acesso (403) e por isso NÃO são citadas como lidas: sap.com (Explain pay / Joule payroll AI), ukg.com (press releases de payroll agents), oracle.com (press release), patents.justia.com, gusto.com.

---

## 1. Detecção de erros e anomalias na folha (e fraude)

**O que é.** Em vez de só regras fixas (falta conta bancária, ID duplicado), um modelo aprende o "normal" da folha (por empregado, grupo, país, histórico) e sinaliza desvios. Técnicas: Isolation Forest, One-Class SVM, autoencoders (erro de reconstrução como score), LSTM/autoencoder em séries de pagamento, e combinações regra + ML + rede neural final.

**Como funciona (técnico).**
- *Isolation Forest*: isola pontos raros com poucos cortes aleatórios; escala bem, não precisa de rótulo.
- *Autoencoder*: comprime e reconstrói o registro (ex.: linha de lançamento / linha de folha); registro com erro de reconstrução alto = anômalo.
- *Cadeia de detectores + MLP*: vários detectores não supervisionados alimentam uma rede neural que dá probabilidade de fraude (patente SAP).
- *Comparação com histórico*: variação por empregado contra baseline de N períodos (o que os fornecedores chamam de "anomaly detection").

**Casos concretos.**
- **SAP SE — patente US11276124B2** (depósito 2019-07-02, concessão 2022-03-15): projeções de dados (folha, RH, banco) → máquinas de ML não supervisionadas (outliers/padrões) encadeadas → motor final MLP que dá flag ou probabilidade 0–1; "treino indireto": regras aplicadas a um subconjunto e a rede aprende correlações mais amplas; saída vai para auditor humano. https://patents.google.com/patent/US11276124
- **Alight Solutions — patente US11494850B1**, "Applied artificial intelligence technology for detecting anomalies in payroll data" (cessionária Alight, segundo o resultado de busca; a página da patente deu 403). https://patents.google.com/patent/US11494850 (só resultado de busca)
- **Schreyer et al., 2017/2018 — "Detection of Anomalies in Large Scale Accounting Data using Deep Autoencoder Networks"**: autoencoders em lançamentos contábeis reais (2 bases), F1 32,93 e 16,95, menos falsos positivos que baselines; validado por contadores. Não é folha, mas é a referência técnica para lançamentos recorrentes. https://arxiv.org/abs/1709.05254
- **Sun et al., 2016 — Extended Isolation Forest, estudo de caso empresarial** (dados de acesso de usuários; o resultado de busca diz que era ao sistema de folha, o abstract só diz "enterprise dataset"). https://arxiv.org/abs/1609.06676
- **Ganji, 2026 — "AI-Driven Payroll Anomaly Detection in Oracle Cloud Payroll System"** (IJSRET v.12): comparou Isolation Forest, One-Class SVM, rede neural e regressão logística; regressão logística "moderadamente bem", os demais sofreram com falsos positivos. Não diz se os dados são reais. Revista de baixo impacto — usar com cautela. https://zenodo.org/records/19988211
- **Zalaris (set/2026) — guia prático**: ML compara com histórico do empregado e do grupo de pares, multi-fator, baseline por equipe/local, monitoramento antes do fechamento, feedback dos casos investigados. Exige revisão humana, alerta explicado (ex.: "net pay +42% contra baseline de 6 meses por novo adicional e hora extra retroativa") e trilha de auditoria; cita NIST AI RMF. https://zalaris.com/resources/blog/ai-powered-payroll-anomaly-detection-what-is-it-and-how-can-it-be-safely-implemented
- **Fraude de folha / ghost employees**: o resultado de busca atribui ao ACFE Report to the Nations 2024 duração média de 18 meses e perda mediana de US$ 50.000 por caso (só resultado de busca; relatório não aberto). A patente SAP cita US$ 7,2 bi/ano.

**Relevância para nós.** Não operamos a folha, mas o que estes modelos marcam como anomalia é exatamente o que nossos artefatos definem como "normal": WTC (que wage type é tributável/incide em quê), DD (campos obrigatórios e domínios), Report Specs (totais que precisam bater). Regras de validação explícitas no DD/WTC são as "features" e os "rules" que alimentam esses detectores.

---

## 2. Leitura e extração de holerites (OCR / Document AI)

**O que é.** Modelos que leem PDF/imagem de payslip e devolvem JSON (empregador, empregado, período, proventos, descontos, líquido, YTD). Duas famílias: OCR + modelo de layout (LayoutLM) e "OCR-free" (Donut, VLMs).

**Casos concretos.**
| Serviço | O que extrai | Limite relevante | Fonte |
|---|---|---|---|
| **Azure Document Intelligence – `prebuilt-payStub.us`** (v4.0 GA, API 2024-11-30) | OCR + deep learning; proventos, deduções, líquido → JSON | **Só locale en-US**; outros países exigem modelo custom (neural até 50.000 páginas/1 GB de treino) | https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/prebuilt/pay-stub |
| **Google Document AI – Payslip Parser** (post 2023-01-09) | Proventos (bônus, comissão, HE, férias, regular) com taxa/horas, impostos e deduções (atual e YTD), depósitos, filing status | **Treinado em dados dos EUA**; "uptraining" para outras regiões (ex.: UK) | https://cloud.google.com/blog/products/ai-machine-learning/more-powerful-w2-and-payslip-processing-with-document-ai |
| **Amazon Textract – Analyze Lending** (nov/2022) | Classifica páginas de dossiê de crédito; do pay stub extrai gross/net atual e YTD, taxa horária, filing status federal/estadual | Foco em hipoteca EUA | https://aws.amazon.com/about-aws/whats-new/2022/11/amazon-textract-analyze-lending-accelerate-loan-document-processing/ (só resultado de busca) |
| **UiPath – Payslips ML package** | Empregador, empregado (nome, ID, cargo), dias pagos, férias, HE, banco/conta, total de proventos e de deduções | Doc não diz línguas | https://docs.uipath.com/document-understanding/automation-cloud/latest/classic-user-guide/payslips-ml-package.md |

- **Han et al., abr/2026 — pipeline multiestágio para documentos financeiros escaneados (KYC)**: 120 documentos de produção, ~3.000 páginas multilíngues; pré-processamento → OCR multilíngue → filtro de páginas → extração por VLM; melhor 87,27% (PaddleOCR + MiniCPM); até +31,9 p.p. sobre VLM direto; filtro de página é o fator dominante, sobretudo fora do inglês. https://arxiv.org/abs/2604.26462
- LayoutLM/Donut: não encontrei artigo acadêmico específico de payslip com esses modelos; a literatura é de recibos/faturas (LayoutLM: https://arxiv.org/abs/1912.13318, só resultado de busca).

**Relevância para nós.** Os modelos prontos são **EUA-cêntricos**; para os países que atendemos, um extrator precisa de um esquema por país — que é o nosso Payslip Spec + WTC. Uso interno viável: ler payslips de exemplo de cliente/ticket e comparar com o Payslip Spec (campos obrigatórios por lei), sempre com conferência humana.

---

## 3. Cálculo, validação e reconciliação com IA (gross-to-net, LLMs)

**Achado central: LLM não calcula folha com confiabilidade; o padrão é motor determinístico + LLM para explicar/verificar/documentar.**

- **Remote — HRmark e PayMark (2026-10-21)**: 12 sistemas de IA; 2.500 perguntas de direito do trabalho em 50 países e 2.000 payslips reais de 50 países. Melhor em HR (Claude Fable 5.1, esforço alto): 69%. **Melhor em cálculo de payslip (GPT-6 Astra): 26%** totalmente corretos (payslip só conta se total do empregado, do empregador e líquido batem). Maior fonte de erro: **deduções do empregado**. Esforço alto custa ~3× para +1,6 p.p. Conclusão: insuficiente para uso autônomo, exige verificação humana. https://remote.com/blog/ai-payroll-benchmark
- **TaxCalcBench (Bock et al., jul/2025)**: modelos de fronteira acertam **menos de 1/3** das declarações federais (simplificadas); erros: uso de tabelas, aritmética, elegibilidade; "infraestrutura adicional" necessária. https://arxiv.org/abs/2507.16126v1
- **Maclean et al. (jan/fev 2026) — "Evaluating Semantic and Syntactic Understanding in LLMs for Payroll Systems"**: dataset sintético em níveis (do horista ao multi-estado com câmbio); GPT, Claude, Gemini, Grok, Perplexity; casos simples quase determinísticos, complexos precisam de fórmula explícita/suporte computacional; "unreliable on exact numerical calculation and producing easily auditable outputs". https://arxiv.org/abs/2601.18012
- **SEGER-ES (Governo do Espírito Santo, 2026) — "IA aplicada à folha de pagamento: da extração à estruturação de regras"** (Matos, Coutinho, Couto Neto, Toneto): agentes de IA (ChatGPT, Copilot, **Claude Code**) fizeram **engenharia reversa de centenas de rubricas** sem documentação num sistema de folha de 20+ anos, estruturando as regras num template; Claude Code foi o mais eficaz e processou todas as rubricas em Markdown → PDF. Resultado: padronização e documentação das regras. https://seger.es.gov.br/media/Gestao_do_conhecimento/2026/2_trabalho_ia-aplicada-a-folha-de-pagamento-da-extracao-a-estruturacao-de-regras.pdf (li só o resumo, a 1ª página do PDF)
- "Explain pay" / copilot: SAP ECP usa Joule para explicar mudanças no pagamento ao empregado (só resultados de busca; sap.com deu 403) **[não confirmado]**.

**Relevância para nós.** Confirma o nosso método: valor estatutário vem de fonte primária + conta refeita mecanicamente (script/planilha), não do LLM. O caso SEGER é quase idêntico ao nosso trabalho (catálogo de wage types/rubricas estruturado a partir de fonte) e é uma referência pública citável de LLM gerando documentação de rubricas.

---

## 4. O que os grandes fornecedores anunciam

| Fornecedor | Produto / data | O que diz fazer | Status da prova | Fonte (aberta) |
|---|---|---|---|---|
| **ADP** | ADP Assist (GA 2024-01-31; matéria 2024-02-15) | Detecta anomalias (ex.: esqueceu de bater saída) e registros fiscais faltantes e corrige; "antes não tínhamos detecção de anomalias" (N. Lariviere) | Entrevista à imprensa | https://www.techtarget.com/enterprise-software/news/366570019/ADP-deploys-GenAI-for-payroll-HR-customer-service?amp=1 |
| **ADP** | Innovation Day 2025-09-03 | Anomalias com sugestão de correção, "até 30 min por ciclo"; monitoramento de compliance global; dados de 1,1 mi empresas/140+ países | **[não confirmado]** | https://www.cpapracticeadvisor.com/2025/09/03/adp-announces-new-ai-powered-product-enhancements-at-innovation-day/168408/ |
| **Workday** | Illuminate, 2025-09-16 | Payroll Agent "automates payroll tasks and enables compliance up to 4x faster" | **[não confirmado]** | https://newsroom.workday.com/2025-09-16-Workday-Illuminate-TM-Expands-with-New-AI-Agents-for-HR%2C-Finance%2C-and-Industry |
| **Workday** | Autopilot agents, 2026 | Payroll Agent monitora antes da rodada, audita retroativos, sinaliza anomalias, rascunha comunicação ao empregado para revisão; ações logadas; empresa decide o que é automático; early adopter **início de 2027** | **[não confirmado]**, não disponível | https://investor.workday.com/news-and-events/press-releases/news-details/2026/Workday-Launches-Autopilot-Agents-That-Get-Real-Work-Done-Across-HR-Finance-and-IT/default.aspx |
| **Oracle** | Fusion HCM, 2025-09-16 | Payroll Run Analyst: identifica irregularidades e explica causas (novas admissões, retroativos não processados, mudança salarial) no contexto de uma rodada; sem custo extra; customizável no AI Agent Studio | **[não confirmado]** | https://siliconangle.com/2025/09/16/oracle-expands-fusion-hcm-13-new-ai-agents-hr-automation/ |
| **SAP** | SuccessFactors ECP + Joule | Joule explica pagamento/holerite ao empregado; Payroll Control Center com regras de validação (há anos) | sap.com 403; só busca + learning.sap.com (só autoatendimento/holerite) | https://learning.sap.com/courses/discovering-sap-solutions-for-core-hr-and-payroll/unlocking-synergies-by-combining-core-hr-and-payroll-with-sap-business-ai- |
| **Dayforce (Ceridian)** | Autonomous Payroll + Co-Pilot, 2023-11-02 | Motor de cálculo contínuo simula a folha durante o período; Co-Pilot alerta anomalia com "motivo sugerido"; sem métricas | **[não confirmado]** | https://www.dayforce.com/blog/payroll-ai-new-innovations-simplify-anomaly-detection |
| **Deel** | AI Workforce (beta), ago/2025 | "Payroll Detective" sinaliza anomalias antes do pagamento conferindo variáveis contra regras; "Border Buddy" geolocaliza IP vs regras fiscais; 150+ países, "2.000+ especialistas"; sem menção a revisão humana | **[não confirmado]** | https://www.deel.com/blog/deel-launches-ai-workforce/ |
| **Papaya Global** | Workforce OS, 2024-11-19 | "Payroll Data Validation Agent"; -80% tempo, "100% compliance" | **[não confirmado]** (números de marketing) | https://gpa.net/blogs/global/global-papaya-global-launches-new-suite-of-ai-based-payroll-and-payments-solutions |
| **Remote** | Payroll próprio 100+ países, 2025-05-06; benchmark 2026-10-21 | Motores de cálculo "AI-powered"; sem métricas no anúncio; o benchmark próprio mostra que LLM sozinho não calcula | anúncio [não confirmado]; benchmark com metodologia publicada | https://remote.com/blog/product/remote-expands-ai-driven-payroll-to-100-countries-giving-teams-a-faster |
| **Rippling** | Payroll "AI-native" | Página só diz comparar pay run com anteriores para pegar discrepâncias; nada específico de ML | **[não confirmado]** | https://www.rippling.com/en-GB/products/payroll |
| **UKG** | Payroll AI agents / Pro Pay (2026) | Detecção de anomalia contra até 5 anos de histórico, explica e prepara correção para revisão | ukg.com 403; só resultado de busca **[não confirmado]** | https://www.ukg.com/company/newsroom/ukg-launches-next-generation-payroll-ai-agents-unlock-productivity-efficiency-and-elevated-employee-engagement |
| **Gusto** | Gus (set/2024) | Assistente; folha dentro de ChatGPT/Claude/Slack | gusto.com 403; só busca **[não confirmado]** | https://www.cpapracticeadvisor.com/2024/09/16/gusto-introduces-gus-ai-assistant-for-small-businesses/110546/ (só resultado de busca) |

**Padrão comum:** (1) anomalia = comparação com histórico/pares antes de fechar a rodada; (2) "explicar o porquê" em linguagem natural; (3) agentes que rascunham e humanos aprovam; (4) o cálculo continua no motor de regras configurado — a IA não substitui a configuração estatutária. Multipaís: Deel/Papaya/ADP afirmam cobertura de 140–160 países, sem métricas públicas por país.

---

## 5. Acadêmico, limitações e riscos

| Ano | Estudo | Achado | Fonte |
|---|---|---|---|
| 2016 | Sun et al., Extended Isolation Forest | Anomalia sem precisar de exemplos rotulados | https://arxiv.org/abs/1609.06676 |
| 2017/18 | Schreyer et al., autoencoders em lançamentos | F1 32,9 / 17,0; menos falsos positivos | https://arxiv.org/abs/1709.05254 |
| 2022 | Patente SAP US11276124B2 | Detectores encadeados + MLP; saída para auditor | https://patents.google.com/patent/US11276124 |
| 2025 | TaxCalcBench | < 1/3 de acerto em cálculo de imposto | https://arxiv.org/abs/2507.16126v1 |
| 2026 | Ganji, Oracle Cloud Payroll | Falsos positivos altos nos modelos não supervisionados | https://zenodo.org/records/19988211 |
| 2026 | Maclean et al., LLM em payroll | Complexo exige fórmula explícita/ferramenta | https://arxiv.org/abs/2601.18012 |
| 2026 | Han et al., extração de docs financeiros | 87% campo; pipeline > VLM direto | https://arxiv.org/abs/2604.26462 |
| 2026 | SEGER-ES, rubricas com Claude Code | Documentação de rubricas legadas por IA | link acima |
| 2026 | Remote PayMark | 26% de payslips 100% corretos (melhor modelo) | https://remote.com/blog/ai-payroll-benchmark |

**Riscos.**
- **Erro em cálculo legal**: os benchmarks mostram 26–33% de acerto completo; deduções e tabelas são o ponto fraco. Qualquer número estatutário vindo de LLM precisa de fonte primária e conta refeita.
- **Falsos positivos** e explicabilidade: alertas sem motivo não são acionáveis; os fornecedores sérios (Zalaris, Oracle, Dayforce) vendem "explicação do porquê" + trilha de auditoria.
- **EU AI Act**: sistemas do Anexo III ponto 4 ("emprego, gestão de trabalhadores") são alto risco. O **Digital Omnibus — Regulamento (UE) 2026/1744, publicado no JO em 2026-07-24** — adiou as obrigações de alto risco do Anexo III de 2026-08-02 para **2027-12-02** (transparência, supervisão humana, FRIA, informação a representantes dos trabalhadores). Continuam valendo já: AI literacy, GDPR (decisão automatizada com efeito jurídico), regras nacionais (ex.: transparência algorítmica em ES/PT) e acordos coletivos. https://www.cuatrecasas.com/en/global/labor-and-employment/art/digital-omnibus-on-ai-how-does-it-impact-employment-relations — Não achei fonte aberta dizendo se cálculo/validação de folha em si é "alto risco"; a leitura defensável é que detecção de fraude que leve a medida contra um empregado se aproxima de "gestão de trabalhadores" (interpretação, não confirmada).
- **Dados pessoais**: payslips têm dados sensíveis; extração/LLM em nuvem exige base legal e minimização (coerente com a regra 3 do cérebro).

---

## O que isso significa para nós

1. **Nosso valor é o "gabarito".** Todos os detectores e agentes (ADP, Oracle, Workday, Deel) dependem de regras/configuração corretas por país; WTC, DD e Report Specs são essa camada. Vale escrever nos artefatos **regras de validação explícitas e testáveis** (ex.: "campo X obrigatório se Y", "base de INSS = soma dos WT com flag Z", limites e tetos com vigência) — viram diretamente regras de PCC/validação e features de anomalia.
2. **LLM não é fonte de cálculo.** Remote PayMark (26%) e TaxCalcBench (<1/3) sustentam a regra que já usamos: fonte primária + conta refeita por script. Bom argumento citável em ticket/QA quando alguém propuser "o modelo calcula".
3. **Uso de LLM onde ele é forte:** extrair e estruturar regras de texto legal e de configurações legadas para templates (caso SEGER-ES com Claude Code, rubricas → template), redigir CCG/DD a partir de fatos já citados, comparar versões, explicar diferenças em linguagem natural.
4. **Payslip Spec como esquema de extração.** Modelos prontos de payslip são en-US; para outros países, nosso Payslip Spec + WTC é o esquema que um extrator custom precisaria. Teste interno possível: extrair holerite de exemplo e conferir campos obrigatórios contra o Spec (sem dado pessoal no cérebro).
5. **Tickets de "anomalia" vão crescer.** Clientes com ADP/Workday/Oracle/Dayforce receberão alertas de variação; muitos virarão perguntas "isto está certo pela lei?". Ter no hub do país as **causas típicas de variação legítima** (retroativos, mudança de teto/alíquota com vigência, 13º/abonos sazonais) acelera a resposta.
6. **Explicabilidade como requisito de artefato.** Cada regra no WTC/DD com fonte e vigência permite que o alerta diga "por quê" — exatamente o que o mercado (Zalaris, Oracle "explain contributing factors") vende.
7. **EU AI Act/GDPR:** para países UE, registrar no hub que obrigações de alto risco do Anexo III passaram para 2027-12-02 (Reg. 2026/1744) e que GDPR/regras nacionais de transparência algorítmica já valem — útil se cliente perguntar sobre IA na folha (resposta é de fronteira: orientação jurídica não é nosso escopo).
8. **Cautela com números de fornecedor.** "100% compliance", "4x mais rápido", "99,7%" não têm metodologia pública; não reproduzir em entregáveis.
