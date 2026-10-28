# Fronteiras do serviço

> O que **não** é nosso, para quem vai e onde termina a nossa entrega.
> Nomes de pessoas aparecem só como papel/contato do lado Mercans. "[INCERTO]" = responsável ou limite não está claro nas fontes.

| Assunto | Responsável | Nossa entrega termina em... |
|---|---|---|
| Produção / ativação do país (deploy, go-live) | Dev (Andre faz deploys de país inteiro; reescrita à mão em produção após acceptance) (chat: design-dev-kb). Time de ativação [INCERTO] | CCG, WTC, DD, Report Specs, SIR, Payslip entregues e aprovados; [[design]] quando pedido |
| Desenho oficial de regulação em produção | Configuration Analyst / Dev (Mohit, Ruchi, Lily, Suman, Luci) (chat: design-dev-kb) | Pesquisa (verdade legal) e, quando pedido, design gerado com IA para comparação |
| Colunas azuis x laranja de WTC e DD | Azuis: nós. Laranja: Dev (chat: design-dev-kb; chat: mercans-compliance) | Colunas azuis preenchidas |
| Coluna Formula do WTC e defeitos de fórmula do engine (ex.: per diem UA; 58163/58118 ES) | Dev (chat: mercans-compliance; tickets: UA) | Posição estatutária correta + achado de fórmula reportado ao Dev |
| Regras de motor (ex.: gross-up só na base do PIT; separação PIT/Military Levy na UA) | Dev / Product; o desenho final (motor ou PE agregado) está sem decisão entre Compliance, BA e Dev (tickets: UA) | Regra legal explicada |
| Retro e parâmetros do engine; TT/TRG de designers novos | Configuração do engine (Dev), na development call; não é toggle de compliance (chat: design-dev-kb) | Regra estatutária |
| Status de configuração (S/C/M/N) e mapeamento de produto | Config/Product (time do Kine, Mohit) (chat: mercans-compliance; chat: compliance-research) | Confirmar posição estatutária; não prescrever configuração |
| Faixa numérica de códigos Mercans para país novo no WTC (ex.: Colômbia: 102 linhas `CO-` com código DERIVED, coluna "Mercans Code" vazia no WTC v1.6) | Config/Product [INCERTO quem atribui] (F6-20261027-CO-C30; `raw/pipeline/Colombia/2026-10-27/qa/CO-QA-REPORT.md` l. 554–557; validação humana pendente) | WTC com códigos mnemônicos; não afirmar código numérico de linha `CO-` até sair a faixa |
| Mapeamento de produto de Report Spec e atribuição de código de PE | BA (Lily Li, Ruchi Gupta) (tickets: OUT, UA, ES-B) | Spec entregue e queries da BA respondidas |
| Planilhas Income Nature / Income Key e colunas de BA Mapping | BA (Lily Li); não editar sem aprovação explícita (chat: mercans-compliance; chat: compliance-research) | Nunca editamos |
| WTC do cliente (ex.: Altium) e WTs "cinza" | Cliente / team lead; mantemos só o master WTC (tickets: UA) | Master WTC |
| Desenvolvimento e bugs de geração de relatório (Fichero de Bases, CRA, XML UA, M111, M296) | Dev (tickets: ES-A, ES-B, UA) | Spec correta e confirmada; erro de portal com spec confirmada vai ao Dev |
| Reports no sistema (Custom Reports, ex.: `netherland-ssc-pdf`) | Reports Team; Configurations não trata reports (tickets: OUT) | Dizer se o report é statutory |
| Interface inbound (ex.: ES-TGSS-INT-IN-001), integração em si | Integration (Illya Virchenko / Config Factory) (tickets: ES-A, ES-B; chat: compliance-research) | Pesquisa e SIR; requisitos em nível de step |
| Eventos de HR/onboarding (AFI MA/MB/MC/MG, Alta/Baja/Cambios) | HR/onboarding, fora da spec de Bases; SR-432 pode ser a spec separada [INCERTO] (tickets: ES-A) | Spec do outbound AFI (SR-432) |
| Operação em SILTRA, testes em A3/portais | Operação/implementação (Gulnaaz) e cliente (tickets: ES-A, ES-B) | Spec validada contra amostra A3 |
| Submissão em portal (AEAT, e-impots, e-CNPS) | Cliente; integração outbound-dominante: HRBLIZZ gera o arquivo, o cliente submete (chat: mercans-compliance) | Arquivo/spec do filing |
| Configuração de entidade e dados de implementação (ex.: HRBS-12074) | Implementação (tickets: AF) | Resposta estatutária |
| Se uma entidade/cliente novo muda a configuração, e quando abrir a entidade (ex.: "New test entity PMI", Cinthya/Nabil, 28/10) | Implementação / Config, com o Development (Mohit) para a parametrização | Só a configuração padrão do país no nível da lei (CCG, WTC master, DD, specs, SIR). Decisão do usuário em 2026-10-28: dizer isso de forma explícita e não opinar sobre a entidade |
| Arquivos criptografados do cliente (OLE2 do Chade), itens de sistema/dados/SOP fora da CCG | Implementação/Operações (Govind Thakur) (chat: mercans-compliance) | CCG e artefatos |
| Dados e decisões do cliente (ordem judicial, arrears, classificação de expat/não residente, split tributável/não tributável de previdência, leave-relief do 30% ruling NL, variante de gross-up, qualificação de stock options) | Cliente / empregador (tickets: OUT, UA; chat: mercans-compliance) | Posição legal e opções |
| Posição fiscal específica do cliente (isenção, regime) | Cliente (documentos) e autoridade (DGI) (tickets: AF) | Lista do que falta (convention, agrément, ruling, declaração) |
| Obrigação do empregador x o que o engine calcula | Empregador x Dev (chat: compliance-research; chat: mercans-compliance) | Separar as duas na pesquisa |
| Leave module (saldo de férias) | Leave module / configuração (tickets: UA) | Regra legal |
| Product spec (ex.: gross-up limitado a 20 PEs; advance payroll com dois runs) | Product/Dev (Mohit/Lily) (tickets: UA) | Pesquisa/CCG |
| Labor law e HR (leave e work accident no D12 RO; recrutamento; performance; е-болнични e УП-2 na Bulgária) | Fora do escopo de payroll (chat: design-dev-kb; chat: mercans-compliance) | Posição estatutária de folha |
| Setor público (servidores, militares, autônomos, cooperados) | Fora: a Mercans atende só o setor privado (chat: mercans-compliance) | DD só do setor privado |
| Integração YouTrack <-> Arbites / QCRM | Time QCRM (chat: compliance-research) | Fora do nosso projeto |
| Ferramenta de automação do trigger (n8n / Zapier) | Consultoria externa em apoio (Kriztian, outro time); o research constrói sozinho, sem dev dedicado (chat: compliance-research) | Escolha da ferramenta em aberto |
| Shared Drive de compliance e service account | TI (aprovação Andre Voolaid) (chat: mercans-compliance; chat: compliance-research) | Pedido |
| Chave da API Anthropic no Passbolt | Jasper Guevarra (chat: compliance-research; chat: mercans-compliance) | — |
| Design de payslip (facelift) após "Submitted for design" | Design (a confirmar) (chat: compliance-research) | Artefato marcado "Submitted for design" |
| Aprovação de designs feitos por IA | Seniors de design, human-in-the-loop (chat: design-dev-kb) | Design entregue para revisão |
| IP e docs internos do engine; liberação de IP para IA | Andre (chat: design-dev-kb) | — |
| Country settings | Só o compliance team; integration team sem acesso (chat: design-dev-kb) | — |
| Tickets de Singapura (ex.: HRBS-15679, variâncias de CPF AW em run de cliente) | Não é responsabilidade nossa (decisão do usuário, 2026-10-14); Support/Compliance Product (Mohit) | Nada a responder |
| Workflow de aprovação de declarações (HU) | Fronteira HRB x engine não definida [INCERTO] (chat: design-dev-kb) | — |
| Contradições de pesquisa | Dono da pesquisa (Wallisson), não a BA (chat: design-dev-kb) | Contradição resolvida no artefato |
| Gaps bloqueantes no guia | Dev abre gap query, compliance responde (chat: design-dev-kb) | Resposta ao gap |
| Mapeamento de tax codes | Report spec (compliance), não o WTC (chat: design-dev-kb) | Report spec |
| Itens de HR x payroll (eventos SD) e formatos de banco/GL | Implementation/Integration (tickets: OUT) | Informar o dono de cada item |
| Pagamento de benefício de SS pelo empregador (HU); dependentes e nacionalidade | Módulo de terceiro / campos de HR (chat: design-dev-kb) | Input |
| Taxas e valores de autoridades (PAS DGFiP, AT/MP CARSAT, UF/UTM do Chile) | A própria autoridade; publicados e digitados pelo operador (chat: design-dev-kb) | Como obter e vigência |
| Itens FR fora da folha (Egapro, bilan social, BDESE, ACEMO, SIPSI, SEPA, GL, feed HRMS, migração, EDI, PASRAU, TNS/SSI, L1224-1) | Cliente / HRMS / pagamentos e interfaces / parceiro EDI / pagador terceiro / contador / advogado (chat: design-dev-kb) | Fora da SIR/CCG |
| Setup do orquestrador Hermes no `DESKTOP-TKRQLF7` | [INCERTO] (chat: mercans-compliance) | — |

Ver também: [[00-INDEX]], [[suporte]]
