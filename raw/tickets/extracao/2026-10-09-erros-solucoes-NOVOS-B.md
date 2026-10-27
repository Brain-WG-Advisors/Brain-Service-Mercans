# Erros e soluções: lote NOVOS-B (36 tickets atribuídos a nós, obtidos pela API)

- **Lote:** NOVOS-B
- **Data da análise:** 2026-10-09
- **Nota:** Tickets atribuídos a nós obtidos pela API do YouTrack em 2026-10-09; não constavam da análise de 2026-10-08.
- **IDs (36):** HRBS-11928, HRBS-11970, HRBS-12113, HRBS-1272, HRBS-1534, HRBS-1535, HRBS-1629, HRBS-1715, HRBS-1763, HRBS-182, HRBS-1958, HRBS-222, HRBS-2278, HRBS-2339, HRBS-2489, HRBS-2621, HRBS-5047, HRBS-6138, HRBS-6163, HRBS-6165, HRBS-6847, HRBS-6856, HRBS-7074, HRBS-8192, HRBS-8303, HRBS-835, HRBS-8399, HRBS-841, HRBS-8439, HRBS-8650, HRBS-9646, HRBS-9807, SR-204, SR-205, SR-206, SR-263
- **Fonte:** `raw/tickets/api/2026-10-09/<ID>.md` (metadados, descrição, todos os comentários, nomes dos anexos). Os anexos e os Google Docs de análise citados nos comentários **não** estão no texto: o que eles dizem aparece como "não consta".
- **Cruzado com:** `correcoes.md`, `mercans-pipeline/shared/country_failure_log.md` (F1–F47) e F48–F59 propostos em `revisoes/2026-10-08-catalogo-erros-tickets.md` (seção 4.2).
- **Convenções:** sem nomes/IDs de empregados dos clientes nem salários individuais (omitidos mesmo quando aparecem no ticket); nomes da equipe Mercans e de quem pediu ficam. [INCERTO] marca inferência minha. "Análise nossa" = comentário de Wallisson no ticket.
- **Observações gerais do lote:**
  - Oito tickets (HRBS-1272, 1534, 1535, 1715, 1763, 222, 835, 841) têm "Resolvido" entre 2025-12-29 10:41 e 10:46 UTC: parece fechamento em lote, não data da solução [INCERTO]. Use a data do último comentário como data real.
  - O campo "País" nem sempre é o país do ticket (HRBS-835 e HRBS-841 dizem India, mas pedem SOP de Jordânia e Egito; o país é o do reporter).
  - Vários tickets terminam com "Resolved" sem confirmação do cliente (HRBS-1534, 1535, 1715, 6847, 8650, 8439, 11970).

---

## HRBS-11928 — Senegal/Gabão/Congo/Moçambique: payslip em idioma local pronto?
- **País / Cliente / Tipo / Estado atual / Criado / Resolvido:** Senegal (pergunta cobre 4 países) / Baker Hughes / Service Request / Resolved / 2026-07-16 / 2026-07-18
- **Linha do tempo:**
  - 2026-07-16 Daniel Kelvin Balogun (reporter): pergunta se os payslips em idioma local de Moçambique, Senegal, Gabão e República do Congo estão prontos, com ETA e responsável.
  - 2026-07-16 Pradeep Duraisamy (L2 Support) acusa recebimento e repassa a Compliance.
  - 2026-07-17 Manju Shetija: Senegal e Gabão estão "under research", detalhes para desenvolvimento até o fim do mês; pede que Wallisson responda pelos outros.
  - 2026-07-18 Wallisson: Congo pronto em francês (aba FR completa, códigos de WT corretos e taxas estatutárias 2026); Moçambique pronto em português (aba PT completa).
  - 2026-07-20 Wallisson envia links de dois Google Sheets (CG_Compliance_Payslip_Generator e Mozambique Compliance_Payslip_Generator).
- **Problema relatado:** não saber o status e o ETA dos payslips em idioma local para 4 países.
- **Erro identificado:** nenhum. Pedido de informação de status.
- **Causa raiz:** não há lugar único e visível com o status de artefatos por país [INCERTO]; o reporter precisou abrir ticket para saber.
- **Solução aplicada:** resposta de status e entrega dos links em 2 dias (Congo e Moçambique); Senegal e Gabão ficaram "em pesquisa" sem ETA de entrega do artefato além de "fim do mês".
- **O que não aconteceu / ficou aberto:** ETA e responsável pelo desenvolvimento (pedidos no ticket) não constam; não consta se Senegal/Gabão foram entregues; "ready" significa payslip Generator pronto, não desenvolvido no sistema (não consta distinção).
- **Tipo de erro:** T11.
- **Lição para o pipeline:** F54 (matriz de cobertura/status por país não publicada) cobre a causa; o painel países × etapa do `00-INDEX.md` seria a resposta. Separar "artefato pronto" de "desenvolvido no produto".

## HRBS-11970 — Espanha: finiquito (carta de liquidação) não é gerado
- **País / Cliente / Tipo / Estado atual / Criado / Resolvido:** Espanha / Mercans (interno) / Service Request / Resolved / 2026-07-17 / 2026-08-04
- **Linha do tempo:**
  - 2026-07-17 Gulnaaz Parveen: o sistema não gera o finiquito, obrigatório em toda rescisão; cita Art. 49.2 do Estatuto de los Trabajadores; conteúdo exigido (dados, data/motivo, salário pendente, férias, pagas extras prorrateadas, indenização, campos de assinatura) e suporte a "no conforme" (direito de contestar em 20 dias úteis). Anexa 2 exemplos de finiquito.
  - 2026-07-20 Wallisson: cria SR-365 "ES: FINIQ-001_Finiquito_Spec" para desenvolvimento.
  - 2026-07-21 Gulnaaz pede manter o ticket aberto até o fechamento e pergunta ETA.
  - 2026-08-03 Wallisson pede que ela feche; Gulnaaz responde que não vê o andamento e pergunta se o relatório já foi desenvolvido e concluído.
  - 2026-08-04 ticket Resolved (sem comentário de resposta).
- **Problema relatado:** documento legal (finiquito) ausente do produto.
- **Erro identificado:** lacuna de escopo: documento de rescisão não coberto pelo conjunto de relatórios/artefatos da Espanha [INCERTO que algum estivesse planejado]. Responsável: nosso escopo (research/design).
- **Causa raiz:** lista de relatórios obrigatórios da Espanha não incluía documentos de rescisão (research/escopo) [INCERTO].
- **Solução aplicada:** spec criada (SR-365). Base legal citada pelo cliente: Art. 49.2 ET (sem verificação nossa no ticket).
- **O que não aconteceu / ficou aberto:** resposta à pergunta final ("já está desenvolvido?"); ETA; ticket resolvido sem confirmar entrega; a exigência "no conforme" e prazo de 20 dias úteis não têm fonte nem verificação no ticket.
- **Tipo de erro:** T6, T5.
- **Lição para o pipeline:** F54 (cobertura de relatórios não publicada) e F19/F43 no sentido inverso (documento de rescisão é caso de "populações/ciclos": desligamento). Ticket não pode ir a Resolved com pergunta de status aberta (reforço F6 da seção 4.1 do catálogo).

## HRBS-12113 — Espanha: Bonificación Formación Continua (FUNDAE) no relatório de Seguridad Social
- **País / Cliente / Tipo / Estado atual / Criado / Resolvido:** Espanha / Mercans (Live/BAU) / Service Request / Resolved / 2026-07-21 / 2026-08-03
- **Linha do tempo:**
  - 2026-07-21 Gulnaaz Parveen pede confirmar que o conceito faz parte da regulação atual; aparece no relatório de Seguridad Social processado hoje no A3; anexa DCL de 2026-06.
  - 2026-07-23 Wallisson confirma: é uma bonificação da Seguridad Social por formação (FUNDAE), aparece no Sistema de Liquidación Directa como código 763; nada a construir, o produto já trata no Fichero de Bases (SR-79); é crédito da empresa, não por trabalhador, e só é reportado quando a TGSS indica bonificação ativa.
  - 2026-08-03 Wallisson e Gulnaaz trocam quem fecha o ticket.
- **Problema relatado:** dúvida se a bonificação é vigente e se o produto a cobre.
- **Erro identificado:** nenhum identificado. Não consta verificação de que SR-79 de fato contém o código 763 ou o tratamento "só quando a TGSS indica crédito ativo".
- **Causa raiz:** não se aplica.
- **Solução aplicada:** resposta informativa (2 dias). Fonte da afirmação: sem fonte no ticket (nem citação do manual/Diseño Lógico do RED).
- **O que não aconteceu / ficou aberto:** nenhum cruzamento com a spec SR-79 visível no ticket; mecanismo "crédito ativo informado pela TGSS" não descrito (como o sistema sabe? não consta).
- **Tipo de erro:** T11 (T12 para a falta de fonte).
- **Lição para o pipeline:** nenhuma falha. Boa prática: resposta citar seção/linha da spec SR-79 onde está o 763 (F52: resposta cita versão vigente do artefato).

## HRBS-1272 — Holanda: tabela de imposto de 62901 e 62160; pensão WIA com 30% ruling; pensão EE 21640
- **País / Cliente / Tipo / Estado atual / Criado / Resolvido:** Países Baixos / Magnit Global (REF-02-348) / Change Request / Resolved / 2025-11-03 / 2025-12-29 (data de fechamento em lote [INCERTO])
- **Linha do tempo:**
  - 2025-11-03 Suresh Jalihal pede: 62901 (Transition allowance) na "Green tax table"; 62160 (pagamento do 13º) em tabela especial; WIA pension deve incluir o 30% ruling; pensão EE 21640 calcula mas não paga.
  - 2025-11-03 Mohit Jain: "não fazemos mudanças específicas de cliente"; Manju verifica a pensão com 30% ruling.
  - 2025-11-03 Suresh: 62160 é pagamento mensal e não deve ir em tabela especial (o cliente tem outro elemento); 62901 deve ir em Green por regulação "e está no WTC de Compliance"; reitera pensão 21640 e WIA.
  - 2025-11-10 Wallisson: análise de compliance sobre pensão com NL 30% ruling (em Google Doc; conteúdo não consta).
  - 2025-11-11 Yojana Bonagir pergunta se BIK entram na base do 30% ruling; Wallisson: sim, geralmente (o salário é definido amplamente: tudo que o empregado recebe pelo contrato).
  - 2025-11-14 Suresh agradece. Sem outros comentários.
- **Problema relatado:** quatro pontos de configuração/cálculo (tabela de 2 WTs, base de WIA, pagamento de 21640).
- **Erro identificado:** não fica claro. (1) 62160: o próprio reporter retirou o pedido; (2) 62901 "Green": o reporter afirma que o WTC já diz Green; o ticket não confirma se o entity estava diferente do WTC [INCERTO: possível divergência cliente/entity × WTC]; (3) WIA com 30% ruling "já faz, mas precisa de pequenas mudanças": não consta qual mudança; (4) 21640: não consta resposta.
- **Causa raiz:** não consta.
- **Solução aplicada:** só a análise de pensão × 30% ruling (Google Doc) e a resposta sobre BIK. Os demais itens não têm resposta registrada.
- **O que não aconteceu / ficou aberto:** destino de 62901 e de 21640; qual ajuste de WIA; base legal do "BIK entra no 30%" (a justificativa dada é uma definição genérica de salário, sem artigo da lei).
- **Tipo de erro:** T2, T10, T11.
- **Lição para o pipeline:** F50 (flags/tabela do WT sem base legal registrada) e F52 (resposta fora do artefato: Google Doc). O ponto "BIK na base do 30%" deveria estar no CCG da Holanda com fonte (Wet LB 1964 art. 31a e Uitvoeringsregeling são conhecimento externo; o ticket não cita) [INCERTO].

## HRBS-1534 — Holanda: divergência no cálculo do 30% ruling (dedução pré-imposto)
- **País / Cliente / Tipo / Estado atual / Criado / Resolvido:** Países Baixos / Omnicom (TBWA, REF-03-281, Acceptance) / Question / Inquiry / Resolved / 2025-11-07 / 2025-12-29 (lote [INCERTO])
- **Linha do tempo:**
  - 2025-11-07 Deepak Pardeshi: payslip interno ≠ payslip do cliente no 30% ruling (período de jan/2025); a simulação e o payslip do cliente batem entre si.
  - 2025-11-10 Support (Crina Lorincz) documenta: empregado com 23 dias trabalhados em janeiro; imagens do cálculo.
  - 2025-11-10 Mohit envia planilha de verificação. Deepak pergunta por que o gym allowance foi excluído, "já que é dedução pré-imposto".
  - 2025-11-11 Mohit: o cliente espera que a dedução pré-imposto de pensão reduza a base do 30%. Wallisson confirma: deduções pré-imposto reduzem a base do NL 30% ruling.
  - 2025-11-12 Wallisson: pela pesquisa, salary sacrifice é a única dedução pré-imposto permitida na base (aspecto legislativo); pergunta a Mohit se a lógica do sistema precisa mudar ou já está alinhada.
  - 2025-11-17 Deepak anexa uma planilha "Copy of NL 30% Calculation.xlsx" (sem texto). Fim.
- **Problema relatado:** 30% ruling no payslip interno difere do cliente.
- **Erro identificado:** a base do 30% ruling no cálculo interno não reduz a dedução pré-imposto que o cliente aplica [INCERTO: o ticket não mostra o valor esperado nem qual dedução, pensão ou gym allowance]. Há tensão entre as afirmações de Wallisson: "deduções pré-imposto reduzem a base" (11/11) e "só salary sacrifice é permitido" (12/11); gym allowance (pergunta do cliente) não foi respondida. Responsável: nosso cálculo/configuração (implementação) × interpretação do cliente.
- **Causa raiz:** regra de base do 30% ruling sem definição única no CCG/WTC [INCERTO]; análise em Google Doc (conteúdo não consta). Relacionado a `correcoes.md` ("Holanda: HRBS-10545, lente de provedor de software").
- **Solução aplicada:** parcialmente: princípio confirmado ("deduções pré-imposto reduzem a base"). Nada sobre mudança de configuração. Ticket Resolved sem confirmação do cliente.
- **O que não aconteceu / ficou aberto:** resposta à pergunta de Wallisson (muda a lógica ou já está alinhada?); gym allowance; qual era o valor correto; fonte legal (a análise está em Google Doc, não no ticket).
- **Tipo de erro:** T7, T2, T10.
- **Lição para o pipeline:** F50 (base do 30% sem base legal registrada) + F41 (nenhum oráculo: a planilha de simulação do cliente deveria ser caso de teste) + F52. Check: toda base de benefício fiscal especial (30% ruling) lista quais WTs entram e saem, com fonte.

## HRBS-1535 — Holanda: base tributável 58552 (fiscaal jaarloon) com "× 54"
- **País / Cliente / Tipo / Estado atual / Criado / Resolvido:** Países Baixos / Omnicom (REF-03-278) / Question / Inquiry / Resolved / 2025-11-07 / 2025-12-29 (lote [INCERTO])
- **Linha do tempo:**
  - 2025-11-07 Deepak Pardeshi: o G2N mostra 58552 calculado como "Total Taxable Salary × 54 ÷ 12 (arredondado para baixo) × 54". O cliente contesta: o salário anual fiscal deve ser o total tributável real do ano, a folha é mensal, "÷ 54" é só conversão técnica de folhas de 4 semanas.
  - 2025-11-10 Mohit atribui à pesquisa.
  - 2025-11-11 Wallisson envia análise (Google Doc; título cita "HRBS-1536", ID diferente do ticket).
  - 2025-11-13 Wallisson resume para Yojana: o sistema usava valor dinâmico por período; correto seria valor fixo/projetado anual; "÷ 54" é lógica de 4 semanas, indevida para folha mensal.
  - 2025-11-18 Wallisson devolve a Mohit: dois problemas (entidade mensal configurada com lógica de 4 semanas; 58552 calculado dinamicamente por run, equivalente a salário tributável do período × 12). Remediação: entidade em "Maand"; 58552 como valor armazenado, fixo no ano, = salário fiscal do ano anterior (empregado existente) ou projeção anual (novo, somando salário, férias, 13º, benefícios e subtraindo pensão pré-imposto). Mohit: "não está claro o que fazer"; "precisa ser reverificado com IA".
  - 2025-11-18 Wallisson posta "AI outputs": 58552 deve ser Jaarloon BT fixo; "54" é convenção de sistema; sem limiar de 125.010,01 que exija o fator.
  - 2025-11-19 Wallisson pede a Mohit a norma do "54"; Mohit indica o documento de regras de cálculo do Belastingdienst (rekenvoorschriften geautomatiseerde loonadministratie 2024, p. 7, seção 2.2.1).
  - 2025-11-19 Wallisson, após ler: "54" é o passo Lv (€54) para arredondar o salário anual na tabela de retenção, não é regra para a base tributável; **muda a posição**: para folha mensal, 58552 = salário tributável real do período e YTD = soma acumulada do ano; fórmula atual "floor(T×54÷12)×54" seria incorreta como base fiscal.
- **Problema relatado:** base tributável 58552 no G2N calculada com fator 54, questionada pelo cliente.
- **Erro identificado:** o código 58552 tem definição ambígua no nosso material: ora "salário fiscal anual fixo para a tabela de bijzonder tarief", ora "base tributável do período". Entre 11/11 e 19/11 a nossa própria resposta mudou de uma para a outra sem que a primeira fosse retirada. Também: o próprio nome do código ("taxable base") e o uso (seleção da taxa de pagamentos especiais) podem ser conceitos diferentes que compartilham um WT [INCERTO]. Responsável: nosso artefato (WTC/CCG) e nossas respostas.
- **Causa raiz:** conceito fiscal holandês (jaarloon para tabela de pagamentos especiais × base do período) não está definido no WTC com fonte; resposta construída com apoio de IA sem verificação contra a norma até Mohit apontar a seção 2.2.1; sem exemplo numérico oficial como oráculo (research/design).
- **Solução aplicada:** não há decisão final registrada. A última posição de Wallisson (19/11): 58552 = base do período e YTD acumulado, sem "× 54". Não consta alteração de configuração nem confirmação do cliente.
- **O que não aconteceu / ficou aberto:** reconciliar as duas posições (fixo anual × período); se a entidade foi reconfigurada para mensal; se o G2N foi corrigido; se Mohit concordou; resposta ao cliente (Deepak pediu o G2N atualizado em 17/11 sem retorno visível).
- **Tipo de erro:** T7, T2, T12.
- **Lição para o pipeline:** F52 (resposta de ticket não consolidada, aqui reescrita no próprio ticket) + F37 (afirmação contradita por outra do mesmo conjunto) + F41. NOVO: "Definição fiscal por IA sem oráculo oficial" -> teria sido pega por um check que exige (a) citação de seção da norma oficial e (b) um exemplo numérico oficial (tabela especial) reproduzido antes de responder.

## HRBS-1629 — Jordânia: contribuição patronal na licença-maternidade (11,5% × 0%)
- **País / Cliente / Tipo / Estado atual / Criado / Resolvido:** Jordânia / Ferring / Service Request / Resolved / 2025-11-11 / 2025-12-23
- **Linha do tempo:**
  - 2025-11-11 Mustafa Mohamed Youssef: nova regulação; em maternidade, a contribuição patronal deveria ser 11,5% (14,25% − 2% acidente de trabalho − 0,75% maternidade), empregado 0; hoje o sistema zera ambas no mês cheio de licença. Anexa documento do portal da Seguridade Social ("About The Corporation", seção Maternity Insurance).
  - 2025-11-11 Mohit pede a Manju que avalie.
  - 2025-11-14 e 11-18 Mustafa cobra (precisa para a folha de novembro; vai processar manualmente).
  - 2025-11-24 Wallisson: o comportamento atual (0%/0% em mês cheio) é compatível com a lei vigente (Lei nº 24/2019, art. 4º alterando o art. 45); o cliente aplica lógica anterior a 2019; a SSC paga o subsídio diretamente e o empregador fica suspenso de pagar contribuições.
  - Sem resposta do cliente; ticket Resolved em 2025-12-23.
- **Problema relatado:** cliente espera 11,5% patronal durante a licença-maternidade.
- **Erro identificado:** possivelmente nenhum do nosso lado; divergência cliente × artefato. Mas há ponto frágil: o cliente anexa um documento do próprio portal da SSC; a nossa resposta não reconcilia esse documento com a lei citada e não transcreve o artigo. Responsável: indefinido (cliente × fonte legal) [INCERTO].
- **Causa raiz:** conflito entre fonte do portal (guia ao empregador) e lei (alterada em 2019) sem reconciliação documentada; resposta demorou 13 dias com o cliente processando manualmente.
- **Solução aplicada:** nenhuma mudança; manter 0%/0% (análise de 2025-11-24). Sem confirmação do cliente. Fonte: Lei 24/2019, art. 4º/art. 45 (citado por nós; texto não consta no ticket).
- **O que não aconteceu / ficou aberto:** aceitação ou contestação do cliente; verificação do texto do art. 45; o que o documento do portal diz exatamente; tratamento de mês parcial de licença; exceção citada pelo cliente ("trabalhadores de órgãos governamentais").
- **Tipo de erro:** T10, T1, T12.
- **Lição para o pipeline:** F41 (sem oráculo independente) e F44 (sem varredura final no boletim oficial). NOVO: "Fonte do portal oficial contraditória com a lei citada, sem reconciliação" -> check: quando o cliente anexa guia do regulador, a resposta cita o trecho do guia e o artigo da lei e explica a diferença.

## HRBS-1715 — Holanda: como o "Home Office Allowance - Gross Up" (62151) é calculado
- **País / Cliente / Tipo / Estado atual / Criado / Resolvido:** Países Baixos / Excerpta Medica B.V. (REF-03-275, Acceptance) / Question / Inquiry / Resolved / 2025-11-12 / 2025-12-29 (lote [INCERTO])
- **Linha do tempo:**
  - 2025-11-12 Suresh Jalihal pergunta o método do gross-up de 62151 para um empregado.
  - 2025-11-13 L2 Support (Archit Naik) encaminha a Compliance.
  - 2025-11-17 Wallisson responde: (1) tecnicamente correto se a empresa quer tributar e garantir o líquido, mas é configuração subótima: em 2025 o home-working allowance pode ser pago isento até €2,40 por dia (WKR, gerichte vrijstelling), não combinável com o commute allowance no mesmo dia; (2) gross-up resolvido pela tabela "white/day" (resolve G tal que líquido = G − [imposto(base+G) − imposto(base)]); no caso do empregado, o motor achou o bruto G pela tabela (valores individuais omitidos); (3) Opção A (recomendada): configurar como reembolso líquido isento (€2,40/dia), fora de loon LH, SV-loon e Zvw-loon; Opção B: manter tributável e documentar. Cita RVO, PwC, Belastingdienst (sem links no texto).
  - 2025-11-19 Suresh: "ainda não está claro o cálculo"; pede para incluir na call do dia seguinte. Fim.
- **Problema relatado:** entender o cálculo do gross-up.
- **Erro identificado:** de design do cliente/implementação: elemento tributável com gross-up para algo que normalmente é isento. Não é erro nosso; mas a comunicação não foi clara (reporter não entendeu).
- **Causa raiz:** o cliente configurou o home office como taxable gross-up; o WTC pode não oferecer um WT dedicado de thuiswerkvergoeding isento (não consta se existe) [INCERTO]. Resposta em formato de consultoria fiscal, longa, para consultor de implementação.
- **Solução aplicada:** explicação + recomendação Opção A. Nenhuma mudança confirmada.
- **O que não aconteceu / ficou aberto:** se o cliente adotou a Opção A; confirmação do valor €2,40 e das condições (dias efetivos, estimativa razoável) em fonte oficial no ticket; se o WTC tem WT para a isenção.
- **Tipo de erro:** T11, T2, T10.
- **Lição para o pipeline:** F50 (flag/tratamento sem base legal; aqui o contrário: o WTC deveria listar o WT isento de thuiswerk) e F43. Reforço de `correcoes.md` ("responder com lente de provedor de folha"): resposta deveria ser curta e numérica.

## HRBS-1763 — Holanda: "SVW Loon" não bate com o valor SVW no payslip YTD
- **País / Cliente / Tipo / Estado atual / Criado / Resolvido:** Países Baixos / Federated Hermes (REF-02-541, Production) / Question / Inquiry / Resolved / 2025-11-13 / 2025-12-29 (lote [INCERTO]; último comentário 2025-12-04)
- **Linha do tempo:**
  - 2025-11-13 Suresh Jalihal: no payslip, o campo "SVW loon" não bate com o valor SVW exibido.
  - 2025-11-14 a 11-17 Archit Naik pede o código do relatório e se é novo; Suresh: nunca bateu, é requisito novo.
  - 2025-11-17 Archit encaminha: relatório afetado `netherlands-payslip-ytd`; pede alinhar SVW Loon e coluna SVW.
  - 2025-11-21 e 11-24 Suresh cobra Brenet Õispuu (desenvolvimento).
  - 2025-11-26 Brenet pergunta a Wallisson qual a lógica exata (sem resposta registrada).
  - 2025-12-01 Suresh pede a Brenet copiar para esta entidade a configuração de SVW amount e fiscal loon da entidade Omnicom em Acceptance.
  - 2025-12-04 Suresh: "resolvido por enquanto", pode fechar.
- **Problema relatado:** inconsistência entre dois campos do payslip YTD.
- **Erro identificado:** configuração da entidade/relatório faltando (setup de SVW amount e fiscal loon que existe em outra entidade). Artefato: relatório payslip YTD / configuração de entidade. Responsável: implementação/configuração, não nosso artefato [INCERTO].
- **Causa raiz:** entidade nova sem herdar a configuração de referência; relatório depende de setup por entidade (sincronização/implementação).
- **Solução aplicada:** Brenet replicou a configuração de Omnicom (conforme o pedido de 12/01; não há comentário dele descrevendo a alteração).
- **O que não aconteceu / ficou aberto:** lógica "exata" de SVW loon (pergunta de Brenet a Wallisson sem resposta); não consta documentação do setup.
- **Tipo de erro:** T9, T8.
- **Lição para o pipeline:** F57 (campos do payslip/template) e F45 (consistência entre artefatos); NOVO: "Setup de referência de payslip/relatório não replicável" -> check: definição do campo SVW loon no Payslip Spec com a fórmula, não só config em uma entidade.

## HRBS-182 — Colômbia: arredondamento (aproximação) das contribuições de seguridade social (Decreto 1990/2016)
- **País / Cliente / Tipo / Estado atual / Criado / Resolvido:** Colômbia / Philip Morris International (Live/BAU) / sem tipo (migrado do Freshdesk) / Resolved / 2025-10-14 / 2026-01-15
- **Linha do tempo:**
  - 2025-10-14 Requisição migrada do Freshdesk (agente PMI): ajustar aproximações do PILA conforme Decreto 1990/2016 (que altera o art. 3.2.1.5 do Decreto 780/2016): IBC aproximado ao peso superior mais próximo; contribuições e juros ao múltiplo de 100 mais próximo. Anexa simulação de cálculo.
  - 2025-10-14 Taavi Tokman anexa imagens e simulação (movidas da plataforma anterior).
  - 2025-10-24 Wallisson envia análise em Google Doc ("validada por ICE"): "Análise e orientação sobre aproximações de contribuições de seguridade social na Colômbia" (conteúdo não consta).
  - 2025-10-25 Taavi esclarece que não é o criador original do ticket.
  - 2026-01-15 ticket Resolved (sem comentário).
- **Problema relatado:** o produto não aplica a regra de aproximação da PILA às contribuições do empregador.
- **Erro identificado:** regra de arredondamento estatutário aparentemente não implementada [INCERTO: a análise não está no ticket; não consta se confirmou o gap]. Artefato: CCG/regulation da Colômbia. Responsável: nosso (research/design) ou nenhum, se a análise concluiu que já estava correto.
- **Causa raiz:** convenção de arredondamento do regulador (peso/centena) é detalhe de PILA que a pesquisa pode não ter capturado [INCERTO].
- **Solução aplicada:** análise de compliance (Google Doc). Implementação não consta; fechamento 3 meses depois sem comentário.
- **O que não aconteceu / ficou aberto:** conclusão da análise; se houve mudança no regulation; confirmação do cliente; solicitante original (nome de agente genérico).
- **Tipo de erro:** T7, T1.
- **Lição para o pipeline:** F44/F41 (varredura final de boletim e oráculo) e C-check "regras de arredondamento oficial por contribuição" (scaffolder já cobre arredondamento de pagamento × contabilidade; aqui é aproximação em declaração). NOVO: "Arredondamento declaratório (PILA)" -> check: CCG lista, por declaração, regra de arredondamento oficial com artigo.

## HRBS-1958 — Holanda: mapeamento de endereço na especificação XML
- **País / Cliente / Tipo / Estado atual / Criado / Resolvido:** Países Baixos / Mammoet / Question / Inquiry / Resolved / 2025-11-19 / 2025-12-22
- **Linha do tempo:**
  - 2025-11-19 Yogesh Chavan abre ticket "para pesquisa", com links para HRBS-1556 e para a planilha da spec XML da Holanda; sem pergunta formulada.
  - 2025-11-21 Wallisson entrega análise "Netherlands Address Mapping Compliance" (Google Doc; conteúdo não consta).
- **Problema relatado:** não consta (só links).
- **Erro identificado:** não consta; pelo título da análise, o mapeamento de endereço na spec XML (relatório da Holanda) precisava de verificação [INCERTO]. Campo T4/T5.
- **Causa raiz / Solução:** não consta; a solução está no Google Doc.
- **O que não aconteceu / ficou aberto:** a pergunta nunca foi escrita; não consta se a spec foi alterada.
- **Tipo de erro:** T5, T4 [INCERTO], T11.
- **Lição para o pipeline:** ticket sem pergunta formulada é pedido de pesquisa sem critério de aceite; F48 (diff da spec contra o leiaute oficial) seria o check para o mapeamento de endereço.

## HRBS-222 — Austrália: "Workers Compensation Expense" existe no WTC?
- **País / Cliente / Tipo / Estado atual / Criado / Resolvido:** Austrália / GSK / sem tipo (migrado do Freshdesk) / Resolved / 2025-10-14 / 2025-12-29 (lote [INCERTO]; resposta em 2025-10-20)
- **Linha do tempo:**
  - 2025-10-14 Saravanan Ekambaram: o Workers Compensation Expense está configurado no sistema/WTC de regulação? Será calculado automaticamente pelo percentual de cada estado?
  - 2025-10-20 Wallisson: não; é prêmio de seguro (despesa operacional do empregador) pago a seguradora estadual, não é wage type; o sistema fornece a base (folha tributável) mas o cálculo do prêmio é feito fora da corrida (anual ou trimestral, por estado).
- **Problema relatado:** pergunta de escopo/configuração.
- **Erro identificado:** nenhum. Escopo: despesa do empregador fora do payroll. Sem fonte legal no ticket.
- **Causa raiz:** não se aplica.
- **Solução aplicada:** resposta de 6 dias. Não há consulta ao CCG da Austrália citada; "anual ou trimestral" sem fonte.
- **O que não aconteceu / ficou aberto:** confirmação do cliente; se existe relatório/export de base tributável por estado para facilitar o prêmio (não consta); o payroll tax estadual (outra obrigação) não é mencionado.
- **Tipo de erro:** T11, T6.
- **Lição para o pipeline:** nenhuma falha; F19-like (escopo): resposta correta de descope. Registrar no CCG "workers' compensation = fora de escopo, base fornecida".

## HRBS-2278 — Austrália: salário de intern de 21–31/12 pago na folha de janeiro
- **País / Cliente / Tipo / Estado atual / Criado / Resolvido:** Austrália / GSK / Question / Inquiry / Resolved / 2025-11-27 / 2025-12-11
- **Linha do tempo:**
  - 2025-11-27 Lokesh Kumar Kinkiri: como Super/PAYG são calculados quando ganhos de dezembro são pagos em janeiro; tratar como janeiro ou como acréscimo de dezembro; como o sistema trata Superable Gross, Taxable Gross e payment reason codes em retro; config especial para interns?
  - 2025-12-02 Wallisson: é "payroll cycle lag", não correção de erro; compliance australiana é em base caixa (data de pagamento): evento estatutário é janeiro (custo pode ser provisionado em dezembro no GL); interns com menos de 18 anos exigem teste de >30 horas semanais para Super.
  - 2025-12-04 Lokesh: quer saber o comportamento do sistema em back payment/retro e pede o link exato da fonte ATO.
  - 2025-12-08 Wallisson: para back payments haverá tabela específica (Schedule 5); link do ATO.
- **Problema relatado:** tratamento estatutário de pagamento atrasado entre meses.
- **Erro identificado:** a resposta de 2025-12-02 e a de 2025-12-08 não são consistentes: a primeira diz "ciclo atrasado = ganho normal do novo período"; a segunda diz que "para back payments há Schedule 5". Não fica claro qual método se aplica a este caso. A primeira também não traz fonte; a regra "base caixa" para Super não é qualificada (Super é por ordinary time earnings/pagamento, não consta). Responsável: nossa resposta.
- **Causa raiz:** pergunta composta respondida em tópicos genéricos, sem fonte, sem distinguir "late payment de ganhos regulares" × "back pay" (comunicação).
- **Solução aplicada:** explicação + link para Schedule 5 (ATO). Pergunta final sobre comportamento do sistema com retro não foi respondida explicitamente.
- **O que não aconteceu / ficou aberto:** comportamento de Superable Gross/Taxable Gross/payment reason codes; escolha entre tabela normal e Schedule 5 para este caso.
- **Tipo de erro:** T7, T12, T11.
- **Lição para o pipeline:** F43 (ciclos especiais) + F58 (off-cycle/retro) + F52 (resposta cita fonte e versão). NOVO: "Pergunta de pagamento diferido entre períodos sem regra no CCG (competência × pagamento)" -> check: CCG declara, por imposto/contribuição, se vale data de pagamento ou competência.

## HRBS-2339 — Holanda: diferença de 0,25 no imposto (payslip OAG × cliente)
- **País / Cliente / Tipo / Estado atual / Criado / Resolvido:** Países Baixos / OAG (REF-03-280, Acceptance) / Question / Inquiry / Resolved / 2025-11-27 / 2025-12-11
- **Linha do tempo:**
  - 2025-11-27 Suresh Jalihal: diferença de 0,25 no imposto de um empregado entre payslip do cliente e da Mercans; anexa payslips e calculadora de imposto 2025.
  - 2025-11-28 Support abre nota para o 3º nível.
  - 2025-11-28 Mohit: "Wallisson está confirmando oficialmente, a mudança já foi feita; pode processar e conferir."
  - 2025-12-01 Suresh: payslip agora bate; pode fechar.
- **Problema relatado:** diferença de 0,25 no imposto.
- **Erro identificado:** não consta o que estava errado nem o que foi alterado. Pelo tamanho (0,25) é provável arredondamento [INCERTO]. Artefato: cálculo de imposto/configuração.
- **Causa raiz:** não consta [INCERTO: regra de arredondamento da tabela de retenção; compare o ticket HRBS-1535 sobre arredondamento por múltiplos].
- **Solução aplicada:** "mudança já feita" (por Mohit/desenvolvimento) antes da confirmação de Wallisson; resultado conferido pelo reporter.
- **O que não aconteceu / ficou aberto:** descrição da mudança; se vale para outras entidades; registro da regra de arredondamento.
- **Tipo de erro:** T7 [INCERTO].
- **Lição para o pipeline:** F52 (correção sem registro do que mudou) e F27 (propagar a mudança). Check: ticket de correção registra "antes/depois" e o artefato afetado.

## HRBS-2489 — Holanda: Retro Tax XML com diferença de 104,27 EUR em setembro
- **País / Cliente / Tipo / Estado atual / Criado / Resolvido:** Países Baixos / Sherwin-Williams (REF-LE-01-977) / Incident / Resolved / 2025-12-02 / 2026-01-23
- **Linha do tempo:**
  - 2025-12-02 Katrin Rudi: validação do `system-netherlands-retro-tax-xml` de outubro/2025: o retro de setembro no XML (38.957) difere em 104,27 do All Pay Elements Retro e do G2N (38.852,73), que batem entre si, somando os WTs 2552, 2560, 2562–2565, 2568, 2569, 2572, 2582.
  - 2025-12-03 Romano Fusana (Support) acusa e encaminha a Manju.
  - 2025-12-17 Wallisson pergunta se vem do XML oficial: um empregado aparece duplicado. Katrin: correto, o empregado foi desligado em 2025-09-01 e pagamentos pós-desligamento são reportados separadamente com novo número de relação de renda; mas a primeira relação deveria ter a data de término e não tem.
  - 2026-01-06 Wallisson: a falta da data de término causa a duplicação. Katrin refuta: a duplicação vem do pagamento pós-desligamento 62180 (Settlement Allowance, sujeito a green tax, WT 2582) sob a relação 0002; o problema real é o WT 2564 (Werkgeversheffing Zvw): o WTC diz que 62180 é sujeito só a Zvw, mas a conformidade não diferencia o Zvw da relação atual (0001) da anterior (0002), e o XML repete o mesmo valor (104,82) nas duas relações.
  - 2026-01-23 Wallisson: "como mapeamos o XML da Holanda do zero, assumo que também está resolvido." Ticket Resolved.
- **Problema relatado:** XML de retro tributário não reconcilia com G2N.
- **Erro identificado:** relatório (Retro Tax XML) repete o Zvw do empregador (2564) em duas relações de renda para empregado com pagamento pós-desligamento; também falta a data de término na primeira relação. Artefato: Report Spec / mapeamento XML da Holanda (versão anterior à reescrita). Responsável: nosso artefato. (Diferença citada: 104,27 no diff; 104,82 no valor repetido; o ticket não explica os 0,55 de diferença [INCERTO].)
- **Causa raiz:** população "empregado desligado com pagamento posterior" e relações de renda múltiplas não tratadas na spec/mapeamento (construção do artefato); Wallisson inicialmente atribuiu a causa errada (término) e depois fechou por suposição.
- **Solução aplicada:** XML refeito do zero (nova spec); não consta teste do caso. Resolução por suposição, sem reteste.
- **O que não aconteceu / ficou aberto:** reteste do caso (empregado desligado com pós-pagamento) e confirmação de Katrin; regra de alocação do Zvw por relação; data de término.
- **Tipo de erro:** T5, T7.
- **Lição para o pipeline:** F43 (população "desligados com pagamento posterior" ausente) + F55 (aceite sem amostra/reteste) + F48. Reforço F6: fechar por "assumo resolvido" não vale.

## HRBS-2621 — Holanda: 2559 (WGA EE) e 2554 (Zvw EE) devem constar no XML Retro/Tax Overview?
- **País / Cliente / Tipo / Estado atual / Criado / Resolvido:** Países Baixos / Mercans (treinamento/implementação) / Question / Inquiry / Resolved / 2025-12-05 / 2025-12-16
- **Linha do tempo:**
  - 2025-12-05 Mahmoud Moharam pede pesquisa profunda: 2559 deve constar no XML do Retro tax? Mohit/Manju em licença; Pradeep reatribui.
  - 2025-12-10 Femmie Buckens (Support) questiona: contribuição PAWW não é enviada à DTA (Belastingdienst), vai ao fundo PAWW.
  - 2025-12-12 e 12-15 Moharam cobra, agora incluindo 2554.
  - 2025-12-16 Wallisson: 2559 (WGA EE Contribution) não entra no XML Retro por ser recuperação privada de custo líquido que não reduz o salário fiscal; 2554 (Zvw EE) é exigência estatutária e deve entrar.
- **Problema relatado:** dúvida de tratamento de dois WTs no XML e Tax Overview.
- **Erro identificado:** nenhum erro de artefato mostrado; é decisão de escopo do relatório. A resposta não traz base legal. Atenção: a pergunta de Femmie ("PAW EE") sugere confusão entre PAWW/WGA (a resposta de Wallisson não a esclarece). Tax Overview não foi respondido, só o XML.
- **Causa raiz:** regras de inclusão de WT por relatório não documentadas na spec (T5).
- **Solução aplicada:** resposta 11 dias depois: 2559 fora; 2554 dentro. Fonte: sem fonte no ticket.
- **O que não aconteceu / ficou aberto:** Tax Overview; fonte; se a spec foi atualizada (a reescrita do XML ocorreu em jan/2026 conforme HRBS-2489).
- **Tipo de erro:** T5, T2, T12.
- **Lição para o pipeline:** F48 (spec sem diff contra o leiaute oficial) e F49 (rastreio WT × spec). Check: cada WT da Holanda tem coluna "entra no XML/Tax Overview: sim/não + base".

## HRBS-5047 — Botswana: modelos ITW7a mensal / ITW81 anual e amostra de payslip
- **País / Cliente / Tipo / Estado atual / Criado / Resolvido:** Botswana / WEIR (Implementation) / Service Request / Resolved / 2026-01-30 / 2026-03-16
- **Linha do tempo:**
  - 2026-01-30 Daniel Kelvin Balogun pede modelos dos relatórios estatutários ITW7a mensal e ITW81 anual e amostras de payslip.
  - 2026-01-30 Pradeep: não encontrou esses relatórios nos artefatos de compliance do quadro Monday; repassa a Manju.
  - 2026-02-16 Daniel: precisa do modelo de amostra.
  - 2026-02-27 Daniel: payslip pendente; ITW7a mensal pendente ("o que recebi é anual"); ITW81 anual recebido.
  - 2026-03-16 Resolved (sem comentário). O payslip foi entregue em HRBS-6163 em 2026-03-02.
- **Problema relatado:** faltavam modelos de relatórios estatutários e payslip.
- **Erro identificado:** artefatos do Botswana (relatórios ITW7a mensal) não existiam/disponíveis no quadro de compliance; confusão entre o que foi entregue (anual) e o pedido (mensal). Responsável: nosso (inventário/entrega).
- **Causa raiz:** inventário de artefatos por país não publicado; relatórios mensais e anuais com nomes parecidos.
- **Solução aplicada:** ITW81 anual recebido; payslip via HRBS-6163; ITW7a mensal: não consta que tenha sido entregue.
- **O que não aconteceu / ficou aberto:** ITW7a mensal; resposta de Compliance neste ticket (não há comentário de wgomes).
- **Tipo de erro:** T11, T6.
- **Lição para o pipeline:** F54 (matriz de cobertura S/C/M/N por país).

## HRBS-6138 — Jordânia: relatório estatutário de seguridade social (REF-00-557)
- **País / Cliente / Tipo / Estado atual / Criado / Resolvido:** Jordânia / Mercans (Implementation) / Question / Inquiry / Resolved / 2026-02-24 / 2026-06-15
- **Linha do tempo:**
  - 2026-02-24 Yojana Bonagir pede para construir o relatório de seguridade social da Jordânia e atribuí-lo à entidade REF-00-557 em produção (anexo "Salary-Social Security.xlsx").
  - 2026-03-03 Mohit passa a Manju. 2026-03-19 Wallisson pede esclarecimento. 2026-04-28 Yojana: é relatório estatutário que precisa ser configurado.
  - 2026-06-09 Support cobra. 2026-06-15 Wallisson: ticket criado e enviado ao desenvolvimento (ID não consta).
- **Problema relatado:** relatório estatutário da Jordânia inexistente.
- **Erro identificado:** lacuna de escopo (relatório de seguridade social não coberto). Responsável: nosso (research/escopo).
- **Causa raiz:** o relatório estava fora da lista entregue; pedido inicial vago (sem nome do relatório).
- **Solução aplicada:** spec/ticket de desenvolvimento criado; cerca de 16 semanas entre abertura e ação. Layout/fonte do relatório não constam.
- **O que não aconteceu / ficou aberto:** nome do relatório; ID do ticket de desenvolvimento; ETA.
- **Tipo de erro:** T6, T11.
- **Lição para o pipeline:** F54; processo de suporte (pedido sem nome do relatório; espera de 16 dias para pedir esclarecimento).

## HRBS-6163 — Botswana: amostra de payslip
- **País / Cliente / Tipo / Estado atual / Criado / Resolvido:** Botswana / WEIR (Implementation) / Service Request / Resolved / 2026-02-25 / 2026-03-02
- **Linha do tempo:** 2026-02-25 Daniel pede amostra de payslip; Mohit designa Wallisson; 2026-03-02 Wallisson envia link do "Botswana Payslip" (Google Sheet).
- **Problema relatado:** falta de amostra de payslip.
- **Erro identificado:** nenhum. **Causa raiz:** payslip existia (ou foi produzido) mas não estava acessível ao time de implementação.
- **Solução aplicada:** link entregue em 5 dias. Duplicado parcial com HRBS-5047.
- **O que não aconteceu / ficou aberto:** confirmação de aceite do reporter (a nota em HRBS-5047 de 02-27 dizia "payslip pendente").
- **Tipo de erro:** T11.
- **Lição para o pipeline:** F54/F57 (payslip por país publicado em local único). Sem falha de pipeline.

## HRBS-6847 — Catar: Seguro Social do empregado (WT 2551) com sinal negativo no G2N
- **País / Cliente / Tipo / Estado atual / Criado / Resolvido:** Catar / Accenture (8400, REF-LE-00-188, Live/BAU) / Incident / Resolved / 2026-03-12 / 2026-03-15
- **Linha do tempo:**
  - 2026-03-12 Naila Ali Mirza: o SS do empregado (2551) sai com sinal negativo no G2N (`gross-to-net-new`), mas aparece correto no sistema; o prazo de entrega do relatório é o mesmo dia.
  - 2026-03-12 Archit Naik (L2) detalha: o cliente discorda do valor calculado para um empregado de nacionalidade Catar (diz que a regulação não calcula o valor correto para ele) e exige um valor manual; ao lançar o manual positivo no cartão do empregado, o G2N mostra negativo; o consultor contornou com várias entradas do mesmo valor. Pergunta a Compliance: (1) override manual é permitido num WT estatutário? (2) por que o sinal inverte?
  - 2026-03-15 Wallisson: (1) não, WT 2551 deve ser calculado automaticamente a 7% do salário contributivo (básico + social + moradia) conforme a lei de seguro social (Lei nº 1/2022, segundo ele); a necessidade do manual indica defeito de configuração, provavelmente nacionalidade não definida como "Qatar"; (2) o G2N inverte o sinal (× −1) nos WTs de dedução do empregado, logo o override deve ser lançado negativo para sair positivo.
- **Problema relatado:** sinal invertido no G2N em override manual de 2551.
- **Erro identificado:** nenhum erro nosso evidente. A causa de fundo é do cliente/implementação: lançamento manual com sinal contrário à convenção do G2N e nacionalidade possivelmente não preenchida. A causa "nacionalidade" é "most likely" na resposta, não confirmada [INCERTO].
- **Causa raiz:** convenção de sinal do G2N para WTs de dedução e override manual não documentada para os consultores; dado de nacionalidade possivelmente faltando no cadastro.
- **Solução aplicada:** orientação de lançar o valor negativo e corrigir a nacionalidade, 3 dias depois (o prazo do cliente era o dia 12). Base legal citada: Lei 1/2022 (sem texto no ticket); alíquota de 7%: fonte é a nossa resposta, sem fonte no ticket.
- **O que não aconteceu / ficou aberto:** confirmação de que a nacionalidade era a causa; por que o valor calculado pelo sistema diferia do pedido do cliente (não explicado); aceite do reporter.
- **Tipo de erro:** T10, T9, T7.
- **Lição para o pipeline:** F43 (população: nacional × expatriado) e NOVO: "Convenção de sinal do G2N/overrides manuais não documentada" -> check: guia de implementação por país indica o sinal e a forma de override de WTs estatutários.

## HRBS-6856 — Tunísia: payslip em francês (ticket cita entidade "Algeria")
- **País / Cliente / Tipo / Estado atual / Criado / Resolvido:** Tunísia / Baker Hughes (Implementation) / Service Request / Resolved / 2026-03-12 / 2026-06-09
- **Linha do tempo:**
  - 2026-03-12 Daniel Kelvin Balogun pede traduzir o payslip para francês e adicioná-lo para "Baker Hughes Algeria" (REF-LE-02-524); cola um payslip de teste com moeda DZD, dados de exemplo e códigos de WT.
  - 2026-03-12 Katrin Rudi pede um CR; 2026-03-13 Daniel: sem CR, é tradução direta; francês é obrigatório (cita um link do código do trabalho).
  - 2026-03-16 Taavi Tokman pede ETA. 2026-03-17 Katrin pede a Mohit criar o payslip do país; 2026-03-18 Mohit pede requisitos a Manju.
  - 2026-04-13 e 04-15 Daniel cobra duas vezes.
  - 2026-04-22 Wallisson anexa `TN-PAYSLIP-001-v1_0.xlsx` e pergunta se atende.
  - 2026-05-06 Daniel: atende; pergunta o próximo passo. 2026-05-14 Wallisson: desenvolvimento no ticket SR-252 "TN: Payslip".
  - 2026-06-09 Crina Lorincz: "o problema deve estar corrigido".
- **Problema relatado:** payslip da Tunísia não existia em francês.
- **Erro identificado:** lacuna de artefato (Payslip da Tunísia inexistente). O título e o texto misturam Tunísia e Argélia (moeda DZD é argelina; REF-LE-02-524 é a entidade da Tunísia em HRBS-8439) [INCERTO: rótulo errado do cliente]. Responsável: nosso (escopo) + cliente (rótulo).
- **Causa raiz:** não havia Payslip da Tunísia no pipeline; o pedido entrou como "tradução", sem dono, e passou por 5 pessoas.
- **Solução aplicada:** Payslip v1.0 entregue em 40 dias (2026-04-22) e desenvolvimento via SR-252.
- **O que não aconteceu / ficou aberto:** esclarecer Tunísia × Argélia; data de entrada em produção; o fechamento de 06-09 foi dado pelo Support, sem teste do reporter registrado.
- **Tipo de erro:** T9, T6, T11.
- **Lição para o pipeline:** F57 + F54 (payslip por país na matriz de cobertura, no idioma legal).

## HRBS-7074 — Tunísia: campos de regulação, flags e códigos estatutários "faltando" na entidade
- **País / Cliente / Tipo / Estado atual / Criado / Resolvido:** Tunísia / Baker Hughes (REF-LE-04-042, Acceptance) / Service Request / Resolved / 2026-03-18 / 2026-03-31
- **Linha do tempo:**
  - 2026-03-18 Vaishnavi Mane: ao configurar o WTC da Tunísia, os campos de regulação e flags não estão na entidade e ela não tem a informação para mapeá-los; pede configurar no nível do país e uma planilha de referência.
  - 2026-03-23 Wallisson pergunta o que exatamente falta e se é problema da pesquisa.
  - 2026-03-24 a 03-30 Vaishnavi: não é pesquisa, a regulação é antiga; faltam flags, códigos e campos específicos de país; cobra várias vezes.
  - 2026-03-30 Ruchi Gupta: não há flags de regulação; envia a matriz de taxabilidade; as contas de taxa 52534 (TFP) e 52560 (acidente de trabalho) são input de front-end.
  - 2026-03-31 Ruchi: não há campos/flags específicos do país; lista os códigos de saída: CNSS empregado 2551 / empregador 2550; TFP 2534; FOPROLOS 2532; acidente de trabalho 2560.
- **Problema relatado:** consultora não achava os campos/flags/códigos estatutários da Tunísia na entidade.
- **Erro identificado:** nenhum erro de valor. Lacuna de documentação de handover: códigos de saída e contas de taxa não estavam num documento entregue; a expectativa (flags por país) não existe no modelo. Responsável: nosso (documentação de entrega) + implementação (expectativa).
- **Causa raiz:** modelo de regulação sem flags por país; não havia planilha de configuração (código de saída × conta de taxa × fonte) entregue com o WTC [INCERTO]. Wallisson respondeu em 5 dias só para pedir esclarecimento.
- **Solução aplicada:** Ruchi entregou a matriz de taxabilidade e os códigos de saída em 2 comentários. Códigos: CNSS 2551/2550, TFP 2534, FOPROLOS 2532, acidente 2560; contas de taxa 52534 e 52560. Fonte: nenhuma lei citada.
- **O que não aconteceu / ficou aberto:** a planilha de referência pedida (feita só em comentário); códigos de saída de imposto de renda não listados.
- **Tipo de erro:** T3, T11.
- **Lição para o pipeline:** NOVO: "Handover sem folha de configuração por país (códigos de saída, contas de taxa de entrada, tabelas)" -> check: tabela "saída × empregador/empregado × conta de taxa × base" no pacote de entrega. Parente de F54.

## HRBS-8192 — Kuwait: G2N em 3 casas decimais em vez de 2
- **País / Cliente / Tipo / Estado atual / Criado / Resolvido:** Kuwait / Accenture (5650, REF-LE-02-390, Live/BAU) / Incident / Resolved / 2026-04-14 / 2026-04-23
- **Linha do tempo:**
  - 2026-04-14 Priya Narayanan: o cliente pede que o G2N mostre 2 casas em vez de 3; ela não tem acesso ao HRB.
  - 2026-04-15 Archit Naik (L2): escala/precisão do país está em 3 (padrão do KWD); pergunta se é permitido arredondar para 2 e se muda o país ou só a entidade.
  - 2026-04-15 a 04-21 nove cobranças (Priya, Archit, Joel Jose, Mohit); o relatório vencia em 2026-04-16/17.
  - 2026-04-23 Wallisson: 3 casas é correto e não deve mudar (KWD tem 3 decimais pela ISO 4217, como BHD e OMR); arredondar causaria erro monetário e discrepâncias nos arquivos do PIFSS (devidos até o dia 15; taxas 11,5% empregador / 10,5% empregado); nenhuma mudança no país nem na entidade; a visão em 2 casas é formatação de relatório do lado do cliente.
- **Problema relatado:** preferência de exibição do cliente.
- **Erro identificado:** nenhum. Configuração correta; expectativa do cliente.
- **Causa raiz:** o cliente quer padrão de exibição de relatório; não há opção de formatação por cliente.
- **Solução aplicada:** manter 3 casas (nenhuma mudança), 8 dias depois, com o prazo do cliente já vencido. Fontes: ISO 4217 (sem link); lei e taxas do PIFSS: sem fonte no ticket.
- **O que não aconteceu / ficou aberto:** alternativa de exibição (export/formato) para o cliente não perder o prazo; confirmação do cliente.
- **Tipo de erro:** T10, T11.
- **Lição para o pipeline:** nenhuma falha de pipeline (o scaffolder já define unidades menores da moeda). Falha de processo de suporte (SLA em Tier 1).

## HRBS-8303 — Arábia Saudita: WTs de ajuste 62102/62402 fora da base do GOSI
- **País / Cliente / Tipo / Estado atual / Criado / Resolvido:** Arábia Saudita / Baker Hughes (REF-02-469, Implementation) / Question / Inquiry / Resolved / 2026-04-15 / 2026-04-24
- **Linha do tempo:**
  - 2026-04-15 Aasim Bagwan: 62102 (Adjustment - Basic Salary) e 62402 (Adjustment - Housing Allowance) estão sujeitos a SS segundo o cliente, mas a entidade não os inclui na base.
  - 2026-04-16 a 04-20 Support pede empregado de exemplo e payroll; Aasim envia um empregado UAT e o G2N de janeiro (payroll REF-P179-660).
  - 2026-04-22 Archit Naik encaminha a Compliance: valida se Adjustment de Basic/Housing entra na base contributiva do GOSI e pede aprovação para alterar o mapeamento.
  - 2026-04-23 Mohit pede confirmação adicional: base para sauditas trabalhando em outros países do GCC.
  - 2026-04-24 Wallisson: sim, ambos entram na base: pela Lei de Seguro Social (Decreto Real M/33, alterado pelo M/273, vigente desde julho de 2024), a base é o salário básico e o auxílio moradia efetivamente pagos; "ajuste" é só rótulo da Mercans; o teto de SAR 45.000/mês vale para o total (incluindo ajustes). Sauditas no GCC continuam no GOSI (ramo de anuidades) pelo acordo de extensão do GCC, com a mesma base. Atualização mensal permitida desde fev/2022; acima de 50 anos, o aumento anual da base é limitado a 10% do salário registrado no ano anterior. Ação: adicionar os dois WTs à base do GOSI para REF-02-469 e aplicar o mesmo às entidades relacionadas.
- **Problema relatado:** 62102 e 62402 não entram na base de SS.
- **Erro identificado:** lacuna de mapeamento: WTs de ajuste de componentes que são base do GOSI não herdam a flag do WT principal. Artefato: mapeamento de base de SS (regulation/entidade; não consta se o WTC global também está errado). Responsável: nosso (WTC/regulation) ou implementação [INCERTO]. Wallisson: "não é questão de compliance; é gap de mapeamento confirmado".
- **Causa raiz:** WTs de ajuste/retro criados sem copiar as flags do WT principal (construção do WTC/entidade) [INCERTO].
- **Solução aplicada:** inclusão confirmada em 2026-04-24; a mudança de configuração em si não é confirmada no ticket. Base legal: M/33 e M/273 (sem texto no ticket); teto SAR 45.000 (sem fonte no ticket).
- **O que não aconteceu / ficou aberto:** confirmação de que a alteração foi feita e do resultado em nova corrida; verificação do WTC global (outras entidades com o mesmo gap); distinção de taxas saudita × expatriado (não consta).
- **Tipo de erro:** T2, T3.
- **Lição para o pipeline:** F20 (gaps do WTC) e F49 (varredura por WT). NOVO: "WT de ajuste/retro com flags divergentes do WT principal" -> check: todo par (WT principal, WT de ajuste) tem as mesmas flags de SS/imposto, ou diferença justificada. Mesmo tema em HRBS-8650 (62802/62841).

## HRBS-835 — SOP de compliance da Jordânia (CSOP)
- **País / Cliente / Tipo / Estado atual / Criado / Resolvido:** Jordânia (campo País diz India) / Mercans / Question / Inquiry / Resolved / 2025-10-21 / 2025-12-29 (cliente pediu fechamento em 2025-10-24)
- **Linha do tempo:** 2025-10-21 Aasim Bagwan precisa do SOP da Jordânia (não conseguiu baixar dos artefatos de compliance no quadro Monday) para enviar aos clientes no toolkit de implementação; no mesmo dia Wallisson entrega "Jordan Payroll CSOP Generation" (Google Doc e .docx); 10-24 Aasim agradece.
- **Problema relatado:** artefato não acessível no quadro Monday.
- **Erro identificado:** nenhum de conteúdo. Falha de acesso/distribuição dos artefatos de compliance.
- **Causa raiz:** repositório (Monday) com download falhando [INCERTO]; ver HRBS-5047 (também "não encontramos nos artefatos").
- **Solução aplicada:** SOP gerado e enviado no mesmo dia.
- **O que não aconteceu / ficou aberto:** o nome "Generation" sugere que o SOP foi gerado sob demanda e não existia [INCERTO].
- **Tipo de erro:** T11.
- **Lição para o pipeline:** F54 (inventário de artefatos). Sem erro de pipeline.

## HRBS-841 — SOP de compliance do Egito (CSOP)
- **País / Cliente / Tipo / Estado atual / Criado / Resolvido:** Egito (campo País diz India) / Mercans / Question / Inquiry / Resolved / 2025-10-21 / 2025-12-29 (cliente pediu fechamento em 2025-10-24)
- **Linha do tempo:** igual a HRBS-835: Aasim Bagwan pede o SOP (sem acesso pelo Monday); 2025-10-21 Wallisson entrega "Egypt Payroll CSOP Generation" (Google Doc e .docx); 10-24 Aasim agradece.
- **Problema relatado / Erro / Causa / Solução / Aberto:** como HRBS-835; sem erro de conteúdo; entrega no mesmo dia.
- **Tipo de erro:** T11.
- **Lição para o pipeline:** F54; ver HRBS-835.

## HRBS-8399 — Holanda: remover accrual de holiday allowance nos pagamentos UWV de 70%
- **País / Cliente / Tipo / Estado atual / Criado / Resolvido:** Países Baixos / Omnicom (TBWA Nederland, REF-02-236, Production) / Question / Inquiry / Resolved / 2026-04-17 / 2026-04-28
- **Linha do tempo:**
  - 2026-04-17 Suresh Jalihal: o cliente pede remover o accrual dos 8% de holiday allowance sobre o pagamento de 70% do UWV em licença parental paga (betaald ouderschapsverlof) e licença de nascimento adicional (aanvullend geboorteverlof), pois os 70% já incluem os 8%.
  - 2026-04-24 Wallisson: o pedido do cliente está correto. O UWV calcula o dagloon sobre a renda anual incluindo os 8% e aplica 70%; acumular outros 8% seria dupla contagem. Ação: remover o accrual dos WTs de pagamento UWV 70% (REF-02-236). Se o empregador complementa acima de 70%, o holiday allowance do complemento depende de contrato/CAO.
  - 2026-04-24 Suresh agradece.
- **Problema relatado:** accrual duplicado de 8% sobre benefício que já o inclui.
- **Erro identificado:** configuração de accrual de férias nos WTs de benefício UWV (configuração do cliente/entidade ou WTC global; não consta qual) [INCERTO].
- **Causa raiz:** o accrual de holiday allowance foi aplicado aos WTs de licença paga sem exceção para UWV 70% (design/WTC) [INCERTO].
- **Solução aplicada:** confirmação em 7 dias; a alteração da configuração não consta. Fonte: página do UWV (citada por trechos de sites de terceiros "Eastwing" e "Blue Lynx"; sem link do UWV no ticket).
- **O que não aconteceu / ficou aberto:** se o WTC global foi corrigido para todos os clientes; outras licenças UWV (ziektewet, gravidez); fonte primária.
- **Tipo de erro:** T2, T7, T12.
- **Lição para o pipeline:** F50 (flag sem base legal) e F43 (licenças). Check: cada WT de benefício de seguridade (UWV) tem coluna "inclui holiday allowance sim/não + fonte".

## HRBS-8439 — Tunísia: TFP (Taxe de Formation Professionnelle) não aparece no G2N
- **País / Cliente / Tipo / Estado atual / Criado / Resolvido:** Tunísia / Baker Hughes (REF-LE-02-524, Implementation) / Service Request / Resolved / 2026-04-19 / 2026-04-28
- **Linha do tempo:**
  - 2026-04-19 Daniel Kelvin Balogun: o TFP (2% da base de SS: básico + horas extras + transporte + prêmio; exclui BIK, viagem, fora do país, tax benefit) está zerado para os 8 empregados de teste; o legado do cliente calcula; gap total 1.403,11 TND; base conferida em 4 casas; anexa variance (docx/xlsx).
  - 2026-04-20 a 04-22 Support: dúvida se é formato do G2N; Daniel mostra que o cliente Henkel (REF-LE-00-600) tem o TFP; 04-22 Archit encaminha a Compliance: o WT de TFP existe no catálogo? o Henkel serve de referência? a base está certa?
  - 2026-04-22 Wallisson: causa raiz é configuração, não catálogo: o TFP existe globalmente e nunca foi ativado para REF-LE-02-524. Não criar WT novo; ativar e mapear com taxa 2,00%, contribuição do empregador, base = básico + OT + transporte + prêmio, exclusões BIK/viagem/fora do país/tax benefit, declaração CNSS (DMS mensal), a cada período. Henkel serve só como abordagem e taxa (confirmar se a base exclui BIK); a base é a mesma do CNSS 9,68%. Nota: o legado agrupa TFP + FOPROLOS no SS Company de 20,07% (17,07% + 2% + 1%); no PAC devem ser WTs separados.
  - 2026-04-23/24 Daniel pede ajuda a Mohit: falta National ID nos dados pessoais; as linhas "SS Employee 10%" e "SS Company 10%" do G2N do cliente (base: seguro BIK) não calculam.
  - 2026-04-25 Mohit: TFP do empregador na conta 52534; acidente de trabalho na 52560; CNSS empregado 9,680%, empregador 17,070%; FOPROLOS 1% do empregador; pela regulação atual não existe SS de 10% para empregador nem empregado.
- **Problema relatado:** TFP zerado em todos os empregados.
- **Erro identificado:** configuração: o TFP existe no catálogo global, mas não foi ativado na entidade (implementação). Não é erro de WTC. Segundo ponto: a linha "SS 10%" sobre BIK do cliente não é reconhecida por Mohit; Wallisson afirmou que BIK é excluído da base CNSS/TFP, o que explica não calcular, mas o cliente quer a linha. Responsável: implementação (TFP) / cliente × artefato (10%).
- **Causa raiz:** a ativação da contribuição por entidade é manual e sem checklist; contas de taxa (52534/52560) são input de front-end (ver HRBS-7074). A exclusão de BIK foi confirmada pelos dados UAT do cliente, não por lei: o ticket não cita base legal para ela nem para a alíquota de 2% (sem fonte no ticket).
- **Solução aplicada:** especificação de ativação (04-22) e valores de taxas (04-25). Não consta confirmação de que o G2N passou a mostrar o TFP.
- **O que não aconteceu / ficou aberto:** reteste da corrida UAT; National ID; a linha "SS 10%" sobre BIK; verificar se o Henkel exclui BIK; fonte da alíquota (2%) e da exclusão do BIK.
- **Tipo de erro:** T3, T10, T12.
- **Lição para o pipeline:** NOVO: "Contribuição existente no catálogo não ativada na entidade" -> check: lista de contribuições obrigatórias do país × ativação por entidade, na fase de UAT (variance por WT). F50 e F20 parcialmente (base sem fonte). Ver HRBS-7074.

## HRBS-8650 — Egito: Martyrs Fund (2558) exclui reembolsos e ajuste de T&L da base
- **País / Cliente / Tipo / Estado atual / Criado / Resolvido:** Egito / Baker Hughes (REF-LE-02-731, Live/BAU) / Service Request / Resolved / 2026-04-22 / 2026-04-23
- **Linha do tempo:**
  - 2026-04-22 Daniel Kelvin Balogun: o Martyrs Fund (2558) é calculado como (bruto − 62802 Expense reimbursement − 62841 T&L adjustment) × 0,05%, conferido em 7 empregados; pede confirmação formal de que a exclusão é intencional e correta.
  - 2026-04-23 Archit Naik encaminha a Compliance com as mesmas 3 perguntas.
  - 2026-04-23 Wallisson: a exclusão é legalmente correta. Base: Lei nº 4/2021 (que altera a Lei 16/2018), dedução de 5/10.000 (0,05%) do salário; reembolsos e T&L são recuperação de custo, não remuneração; recomenda documentar a exclusão na política da entidade. Admite que não achou circular da Receita listando os WTs excluídos; a posição vem da definição de "salário" da Lei do Trabalho nº 14/2025 (antes Lei 12/2003).
- **Problema relatado:** pedido de confirmação formal de uma base.
- **Erro identificado:** nenhum. A base está certa por interpretação legal, sem circular específica.
- **Causa raiz:** não se aplica. A base de 2558 por WT estava só na fórmula, sem base legal registrada (F50).
- **Solução aplicada:** confirmação em 1 dia; recomendação de documentar a exclusão. Fonte: Lei 4/2021 (altera Lei 16/2018); Lei do Trabalho 14/2025 (definição de salário); sem circular específica (declarado no ticket).
- **O que não aconteceu / ficou aberto:** documentação nos artefatos (CCG/WTC) não consta; existência de lista oficial de exclusões não consta.
- **Tipo de erro:** T2, T12.
- **Lição para o pipeline:** F50 (flag com base por interpretação precisa de coluna "base legal" no WTC). Ponto positivo: transparência sobre a ausência de circular.

## HRBS-9646 — Holanda: geração do betalingskenmerk (referência de pagamento ao Belastingdienst)
- **País / Cliente / Tipo / Estado atual / Criado / Resolvido:** Países Baixos / Omnicom (OGS Netherlands, REF-LE-02-234, Live/BAU) / Change Request / Resolved / 2026-05-18 / 2026-06-14
- **Linha do tempo:**
  - 2026-05-18 Suresh Jalihal: o cliente enviou documento de como obter a referência de pagamento fiscal; hoje o número é digitado manualmente em Legal Entity HR Fields > Tax Authority Bank Details; pede configurar.
  - 2026-05-21 Romano Fusana: documento em holandês; pede lista objetiva do que fazer; Suresh pede validação da pesquisa.
  - 2026-05-25 Romano encaminha a Wallisson (indicado por Manju). 2026-06-09 Crina Lorincz cobra.
  - 2026-06-14 Wallisson verifica: o anexo é a "Specificatie betalingskenmerk" oficial do Belastingdienst (v1.0, 11/05/2005); o algoritmo de 16 dígitos continua correto e vigente (Handboek Loonheffingen 2026), reconciliado com os dois conjuntos de teste do documento. Algoritmo da Loonaangifte: pos. 1 = dígito verificador (módulo 11 ponderado, pesos da direita para a esquerda 2,4,8,5,10,9,7,3,6,1 repetindo; A = soma(dígito × peso) das pos. 2–16; dígito = 11 − (A mod 11); 10 vira 1; 11 vira 0); pos. 2–9 = dígitos 1–8 do número fiscal; pos. 10 = 6 (Loonaangifte); pos. 11 = último dígito do ano; pos. 12–13 = subnúmero; pos. 14–15 = período (mês 01–12; 4 semanas 71–83; semestre 31/32; trimestre 21–24; ano 40; acerto de fim de ano 60); pos. 16 = 0.
  - Condições para o Produto: (1) não implementar o formato bancário da spec (clieop03, obsoleto), só a derivação do kenmerk, que vai no campo de referência do pagamento SEPA; (2) o loonheffingennummer estático não é o kenmerk por período; (3) só declarações periódicas; naheffingsaanslag/correções usam o kenmerk emitido na notificação; (4) o Belastingdienst muda de ING para Rabobank (conta NL04 RABO 0200 1122 44, a partir de ~1 de maio de 2026): afeta o IBAN do beneficiário, não o kenmerk.
  - Escopo: gerar e exibir o kenmerk na saída da loonaangifte está aprovado; executar o pagamento SEPA exige confirmar se o produto paga.
- **Problema relatado:** número digitado manualmente a cada período.
- **Erro identificado:** nenhum. Melhoria (CR). O risco evitado era implementar a spec de 2005 inteira (clieop03).
- **Causa raiz:** não se aplica.
- **Solução aplicada:** validação com 4 condições (2026-06-14), 27 dias após a abertura. Fonte: spec oficial do Belastingdienst (2005) e Handboek Loonheffingen 2026 (sem link). IBAN novo: sem fonte no ticket; vigência a partir de ~2026-05-01.
- **O que não aconteceu / ficou aberto:** se o produto executa pagamento; se a conta do Belastingdienst foi atualizada onde o IBAN é mantido; quem implementa e prazo; verificação do IBAN em fonte oficial.
- **Tipo de erro:** T12 (fonte verificada), T6 (escopo de pagamento), T11.
- **Lição para o pipeline:** nenhuma falha. É o exemplo de oráculo desejado em F41/F48: reconciliar contra os dois exemplos oficiais do documento. Registrar o algoritmo no CCG/spec da Holanda.

## HRBS-9807 — Holanda: tipos de contrato do DD não mapeiam para o campo global
- **País / Cliente / Tipo / Estado atual / Criado / Resolvido:** Países Baixos / sem cliente (não ligado a entidade) / Question / Inquiry / **Rejected** / 2026-05-20 / 2026-07-09
- **Linha do tempo:**
  - 2026-05-20 Yojana Bonagir: o DD da Holanda tem "Contract Type" (campo global), mas os option mappers não pertencem ao campo global, que só aceita indefinido e fixo; a Holanda tem 5 option mappers; todas as entidades estão usando um tipo novo; pede pesquisa e limpeza dos tipos duplicados; pergunta se Intern e Trainee são a mesma coisa.
  - 2026-05-23 Wallisson pergunta qual versão do DD.
  - 2026-06-09 Support pede a informação a Yojana; sem resposta.
  - 2026-07-09 Support fecha o ticket por falta de resposta (Rejected).
- **Problema relatado:** option mappers de Contract Type do DD da Holanda incompatíveis com o campo global; tipos duplicados.
- **Erro identificado:** DD da Holanda: Contract Type com 5 opções contra campo global de 2 opções; versão do DD não consta. Responsável: nosso DD ou design do campo global [INCERTO]. Intern × Trainee: sem resposta.
- **Causa raiz:** campo global de contrato com enum de 2 valores recebendo opções específicas do país (design).
- **Solução aplicada:** não resolvido; fechado por inatividade 7 semanas depois de Wallisson perguntar a versão.
- **O que não aconteceu / ficou aberto:** pesquisa e limpeza dos duplicados; decisão sobre Intern/Trainee; o problema técnico continua [INCERTO: pode ter sido resolvido fora do ticket].
- **Tipo de erro:** T4.
- **Lição para o pipeline:** F1 (option mapper mismatch DD × specs) e F56 (campo exigido sem correspondente no DD). Reforço F6: ticket fechado por inatividade deixa defeito real aberto; abrir tarefa de DD separada.

## SR-204 — Bulgária: spec do NOI Apêndice 9 (Certificado de licença-doença)
- **País / Cliente / Tipo / Estado atual / Criado / Resolvido:** Bulgária (BG) / sem cliente / sem tipo (fase Product Mapping, BA Ruchi Gupta) / Canceled / 2026-04-13 / 2026-05-20
- **Linha do tempo:**
  - 2026-04-13 Wallisson cria `BG-NOI-001-Appendix-9-Sick-Leave-Certificate-Spec` (link para planilha).
  - 2026-05-11 Lily Li pergunta qual o país correto (título dizia BG) e por que estava atribuída a Katrin (dev). Wallisson: foi criada quando BG ainda não existia. Lily reatribui a Ruchi.
  - 2026-05-20 Ruchi cancela: por e-mail confirmado, fora de escopo (anexo "Scope of Reports Appendix 9 & 10.pdf").
- **Problema relatado:** não aplicável (spec criada por nós).
- **Erro identificado:** spec produzida antes de o escopo de relatórios (Apêndices 9 e 10 do NOI) ser confirmado; atribuição inicial errada (dev em vez de BA). Responsável: nosso (escopo/processo).
- **Causa raiz:** spec criada antes da decisão de escopo; país BG sem projeto na criação.
- **Solução aplicada:** cancelamento após 5 semanas, com base em e-mail de escopo (conteúdo não consta).
- **O que não aconteceu / ficou aberto:** a razão do e-mail de escopo; quem decidiu (não consta).
- **Tipo de erro:** T6.
- **Lição para o pipeline:** F54 (matriz de cobertura antes de gerar specs) + F19/F24 (escopo/mandato).

## SR-205 — Bulgária: spec do NOI Apêndice 10 (Certificado de benefício do segurado)
- **País / Cliente / Tipo / Estado atual / Criado / Resolvido:** Bulgária / sem cliente / sem tipo (fase Product Mapping) / Canceled / 2026-04-13 / 2026-05-19
- **Linha do tempo:** 2026-05-12 Ruchi pede revisar as perguntas na spec; 05-14 Wallisson: perguntas respondidas e opções de campo alinhadas; 05-18 Ruchi: faltam respostas nos campos em vermelho e a seção "Twin details" é difícil de mapear; 05-19 Wallisson: "conforme falei com o Mohit, está fora de escopo". Cancelada.
- **Problema relatado:** não aplicável. **Erro identificado:** spec com campos que a BA não conseguia mapear (seção "Twin details") e escopo não confirmado. **Causa raiz:** como SR-204.
- **Solução aplicada:** cancelamento por decisão de escopo (Mohit, relatada por Wallisson; sem registro direto no ticket).
- **O que não aconteceu / ficou aberto:** o trabalho de cerca de 5 semanas na spec; a decisão sem registro escrito do próprio Mohit no ticket.
- **Tipo de erro:** T6, T5.
- **Lição para o pipeline:** F54; decisão de escopo registrada no ticket, não só em conversa.

## SR-206 — Bulgária: spec do NOI Apêndice 11 (Certificado de benefício de autossegurado)
- **País / Cliente / Tipo / Estado atual / Criado / Resolvido:** Bulgária / sem cliente / sem tipo (fase Product Mapping) / Canceled / 2026-04-13 / 2026-05-13
- **Linha do tempo:** 2026-05-08 Ruchi pede checar o escopo (é para autossegurado); 05-12 Wallisson: "fora de escopo; posso apagar?"; cancelada em 05-13.
- **Problema relatado:** não aplicável. **Erro identificado:** relatório de autossegurado fora do escopo do payroll. **Causa raiz:** como SR-204.
- **Solução aplicada:** cancelamento. **Aberto:** a pergunta "posso apagar?" não teve resposta registrada; risco de perda de versão (F59).
- **Tipo de erro:** T6.
- **Lição para o pipeline:** F54, F19 (relatório de quem não está na folha) e F59.

## SR-263 — Chile: spec do Certificado Anual (SII) / licença médica eletrônica (LME)
- **País / Cliente / Tipo / Estado atual / Criado / Resolvido:** Chile / sem cliente / sem tipo (fase Product Mapping) / Canceled / 2026-05-27 / 2026-07-14
- **Linha do tempo:**
  - 2026-05-27 Wallisson cria `CL-SII-004-CertificadoAnual-Spec` (link). Ruchi Gupta: é informação de licença, ação do empregador; como isso é relevante para o payroll? Wallisson lista pontos em que a LME afeta o payroll: primeiros 3 dias pagos pelo empregador (art. 14 DFL 44), tratamento tributário do subsídio (art. 17 nº 16 LIR), continuidade de SS (Ley 21.735, Circular SUSESO 3883), proração, relatórios (LRE, Previred, DJ 1887) e benchmark de mercado; pede confirmar se já está coberto.
  - 2026-07-14 Ruchi responde ponto a ponto: ação do empregador/configuração de licença; pede WTs específicos e campos de relatório; hoje o produto já computa Pension Reform, AFC e SIS para dias de subsídio, mas não computa os dias de subsídio. Propõe inbound apenas como informação.
  - 2026-07-14 Wallisson cancela: LME inbound não é necessário; o payroll precisa só de datas e tipo de licença (já capturados na configuração de licença); a continuidade de SS no subsídio (EV/SIS) já está construída e depende dessas datas.
- **Problema relatado:** não aplicável (spec criada por iniciativa nossa).
- **Erro identificado:** spec criada sem avaliar se o payroll consome o documento; o título (SII/Certificado Anual) não coincide com o conteúdo discutido (licença médica eletrônica) [INCERTO]. Os argumentos legais iniciais usaram "parece/pode" sem WTs ou campos concretos. Responsável: nosso (escopo).
- **Causa raiz:** pesquisa que gera spec para todo documento regulador relacionado, sem o filtro "o payroll usa?" (research/escopo).
- **Solução aplicada:** cancelada 48 dias depois; datas e tipo de licença bastam. Base: art. 14 DFL 44, art. 17 nº 16 LIR, Ley 21.735, Circular SUSESO 3883 (apenas citadas; sem texto no ticket).
- **O que não aconteceu / ficou aberto:** verificar se "primeiros 3 dias" e isenção do subsídio estão realmente tratados (afirmação sem teste no ticket); os dias de subsídio continuam dependendo da configuração de licença pelo empregador.
- **Tipo de erro:** T6, T12.
- **Lição para o pipeline:** F19 (HR-scope) + F54. Check: a spec só nasce com a linha da matriz de cobertura "consumida pelo payroll: sim, WT/campo X".

---

## Sem conteúdo analisável

- **HRBS-6165** (Namíbia, WEIR, Rejected, 2026-02-25 a 2026-03-26): pedido de modelos de relatório estatutário e payslip; Mitali Farkase diz que não tem os modelos (estão com Manju); Taavi Tokman fecha em 2026-03-26 "por término de contrato". Sem informação técnica. T11, T6; F54.

---

## (1) Tabela-resumo

| ID | País | Tipo(s) | Artefato | Resolvido? | F-xx / NOVO |
|---|---|---|---|---|---|
| HRBS-11928 | Senegal/Gabão/Congo/Moçambique | T11 | Payslip | Sim (Senegal e Gabão ainda em pesquisa) | F54 |
| HRBS-11970 | Espanha | T6, T5 | Report Spec (SR-365 criada) | Sim (spec criada; entrega não confirmada) | F54, reforço F6 |
| HRBS-12113 | Espanha | T11 | Report Spec SR-79 (resposta) | Sim | Nenhuma |
| HRBS-1272 | Países Baixos | T2, T10, T11 | WTC / config entidade | Parcial (21640 e 62901 sem resposta) | F50, F52 |
| HRBS-1534 | Países Baixos | T7, T2, T10 | Cálculo / config do 30% ruling | Parcial | F50, F41, F52 |
| HRBS-1535 | Países Baixos | T7, T2, T12 | WTC 58552 / config | Não (posições contraditórias) | F52, F37, F41 + NOVO: definição fiscal por IA sem oráculo |
| HRBS-1629 | Jordânia | T10, T1, T12 | Regulation (sem mudança) | Sim (sem aceite do cliente) | F41, F44 + NOVO: fonte do portal × lei |
| HRBS-1715 | Países Baixos | T11, T2, T10 | WTC / config do cliente (62151) | Parcial | F50, F43 |
| HRBS-1763 | Países Baixos | T9, T8 | Payslip YTD / config entidade | Sim | F57, F45 + NOVO: setup de referência de payslip |
| HRBS-182 | Colômbia | T7, T1 | CCG / regulation | Sim (conteúdo não consta) | F44, F41 + NOVO: arredondamento declaratório (PILA) |
| HRBS-1958 | Países Baixos | T5, T4, T11 | Spec XML | Sim (conteúdo não consta) | F48 |
| HRBS-222 | Austrália | T11, T6 | WTC (resposta) | Sim | Nenhuma |
| HRBS-2278 | Austrália | T7, T12, T11 | Resposta nossa / CCG | Parcial | F43, F58, F52 + NOVO: competência × pagamento |
| HRBS-2339 | Países Baixos | T7 [INCERTO] | Config/cálculo de imposto | Sim | F52, F27 |
| HRBS-2489 | Países Baixos | T5, T7 | Report Spec Retro Tax XML | Sim (por suposição) | F43, F55, F48, F6 |
| HRBS-2621 | Países Baixos | T5, T2, T12 | Report Spec XML / Tax Overview | Parcial (Tax Overview não) | F48, F49 |
| HRBS-5047 | Botswana | T11, T6 | Report / Payslip | Parcial (ITW7a mensal não) | F54 |
| HRBS-6138 | Jordânia | T6, T11 | Report Spec | Sim (spec enviada ao dev) | F54 |
| HRBS-6163 | Botswana | T11 | Payslip | Sim | F54, F57 |
| HRBS-6165 | Namíbia | T11, T6 | Report / Payslip | Rejeitado (término de contrato) | F54 |
| HRBS-6847 | Catar | T10, T9, T7 | Config entidade / G2N | Sim (orientação) | F43 + NOVO: convenção de sinal do G2N |
| HRBS-6856 | Tunísia | T9, T6, T11 | Payslip (TN-PAYSLIP-001 v1.0) | Sim | F57, F54 |
| HRBS-7074 | Tunísia | T3, T11 | Documentação de handover | Sim | NOVO: handover sem folha de configuração; F54 |
| HRBS-8192 | Kuwait | T10, T11 | Config (sem mudança) | Sim | Nenhuma (processo/SLA) |
| HRBS-8303 | Arábia Saudita | T2, T3 | WTC / base GOSI | Sim (mudança não confirmada) | F20, F49 + NOVO: WT de ajuste sem flags do principal |
| HRBS-835 | Jordânia | T11 | CSOP | Sim | F54 |
| HRBS-841 | Egito | T11 | CSOP | Sim | F54 |
| HRBS-8399 | Países Baixos | T2, T7, T12 | WTC / config UWV | Sim (mudança não confirmada) | F50, F43 |
| HRBS-8439 | Tunísia | T3, T10, T12 | Config entidade (TFP) | Sim (reteste não consta) | F50, F20 + NOVO: contribuição existente não ativada |
| HRBS-8650 | Egito | T2, T12 | WTC / base 2558 | Sim | F50 |
| HRBS-9646 | Países Baixos | T12, T6, T11 | Spec/design (betalingskenmerk) | Sim | Nenhuma (oráculo aplicado, F41) |
| HRBS-9807 | Países Baixos | T4 | DD | Não (fechado por inatividade) | F1, F56, F6 |
| SR-204 | Bulgária | T6 | Report Spec | Cancelado (fora de escopo) | F54, F19, F24 |
| SR-205 | Bulgária | T6, T5 | Report Spec | Cancelado | F54 |
| SR-206 | Bulgária | T6 | Report Spec | Cancelado | F54, F19, F59 |
| SR-263 | Chile | T6, T12 | Report Spec | Cancelado | F19, F54 |

## (2) Padrões recorrentes no lote

- **Escopo e cobertura (F54):** 11 tickets (HRBS-11928, 11970, 5047, 6138, 6165, 835, 841 e SR-204/205/206/263) nascem de relatório, payslip ou SOP que não estava na lista nem localizável. Três specs da Bulgária e a do Chile foram produzidas e depois canceladas por escopo.
- **Holanda concentra 12 tickets** (1272, 1534, 1535, 1715, 1763, 1958, 2339, 2489, 2621, 8399, 9646, 9807). Temas: base do 30% ruling, 58552, Retro Tax XML, flags do WTC sem fonte, tipos de contrato do DD. As respostas moram em Google Docs, não no CCG/WTC.
- **Resposta nossa contraditória ou sem fonte (F52/F37):** HRBS-1535 (duas definições de 58552 no mesmo ticket, com apoio de IA), HRBS-2278 (base caixa × Schedule 5), HRBS-1534 ("pré-imposto reduz" × "só salary sacrifice"), HRBS-1629 (lei × guia do portal).
- **Base legal ausente ou por interpretação (F50):** 62102/62402 (GOSI), 2558 (Egito), TFP 2% e exclusão de BIK (Tunísia), UWV 70% (Holanda, só fontes secundárias), 2554/2559 (Holanda, sem fonte).
- **Defeito de configuração por entidade, não de artefato:** TFP não ativado (8439), SVW loon (1763), WT de ajuste fora da base (8303), nacionalidade/sinal no G2N (6847). Faltam checklist de ativação por entidade e documentação de handover (7074).
- **Fechamento sem confirmação:** HRBS-2489 ("assumo resolvido"), 11970, 1534, 1535, 9807 (fechado por inatividade com defeito real aberto), 8303 e 8399 sem confirmação da mudança; 8 tickets fechados em lote em 2025-12-29.
- **Latência:** HRBS-6138 (~16 semanas), 6856 (~3 meses), 8192 (8 dias em Tier 1 com prazo do cliente vencido), 1629 (13 dias com o cliente processando manualmente).
- **Convenções não documentadas:** o G2N inverte o sinal em deduções (6847) e o KWD usa 3 casas (8192).

## (3) Soluções reutilizáveis

1. **Holanda, XML Retro/Tax Overview (HRBS-2621, 2489):** 2559 (WGA EE) não entra no XML (recuperação privada, não reduz salário fiscal; a contribuição PAWW vai ao fundo, não à DTA); 2554 (Zvw EE) entra. Empregado desligado com pagamento posterior (ex.: 62180 Settlement Allowance, green tax 2582) vira segunda relação de renda; o WT 2564 (Zvw empregador) deve ser alocado por relação e a primeira relação deve ter data de término. Fonte: sem fonte no ticket (posição de Wallisson e de Katrin Rudi).
2. **Holanda, 30% ruling e UWV (HRBS-1272, 1534, 8399):** BIK entram na base do 30% ruling; dedução pré-imposto (salary sacrifice) reduz a base (contradição interna a resolver: ver HRBS-1534). O UWV 70% da licença parental paga e do aanvullend geboorteverlof já inclui os 8% de holiday allowance no dagloon: sem accrual nos WTs UWV (complemento do empregador depende de contrato/CAO). Fonte: UWV via sites secundários; lei sem artigo no ticket.
3. **Holanda, betalingskenmerk (HRBS-9646):** 16 dígitos: dígito verificador (módulo 11, pesos 2,4,8,5,10,9,7,3,6,1 da direita), número fiscal (8 dígitos), 6, último dígito do ano, subnúmero (2), período (2), 0. Só declarações periódicas; não implementar clieop03; IBAN do Belastingdienst muda de ING para Rabobank (NL04 RABO 0200 1122 44, a partir de ~2026-05-01). Fonte: spec oficial do Belastingdienst (v1.0, 2005) e Handboek Loonheffingen 2026; IBAN sem fonte no ticket.
4. **Tunísia (HRBS-8439, 7074):** CNSS empregado 9,680%, empregador 17,070%, FOPROLOS 1% do empregador, TFP 2% do empregador sobre a mesma base do CNSS (básico + OT + transporte + prêmio; sem BIK, viagem, fora do país, tax benefit); contas de taxa de entrada 52534 (TFP) e 52560 (acidente de trabalho); códigos de saída CNSS 2551/2550, TFP 2534, FOPROLOS 2532, acidente 2560; não existe SS de 10%. TFP e FOPROLOS são WTs separados (não replicar a linha agrupada de 20,07% do legado). Fonte: Mohit Jain (HRBS-8439, 2026-04-25) e Ruchi Gupta (HRBS-7074); sem lei no ticket para os 2% e para a exclusão de BIK.
5. **WT de ajuste herda a base do WT principal (HRBS-8303, 8650):** 62102 e 62402 entram no GOSI, com teto de SAR 45.000/mês sobre o total; sauditas no GCC mantêm a base. No Egito, 2558 (Martyrs Fund) = 0,05% do salário, excluindo 62802 e 62841 (Lei 4/2021 que altera a Lei 16/2018; definição de salário na Lei do Trabalho 14/2025; sem circular específica).
6. **Kuwait (HRBS-8192):** o KWD tem 3 casas decimais (ISO 4217); a precisão do país não se altera por pedido de exibição; 2 casas é formatação de relatório do cliente.
7. **G2N (HRBS-6847):** o G2N inverte o sinal (× −1) dos WTs de dedução do empregado; override manual deve ser lançado negativo; WT estatutário (2551 do Catar) deve ser calculado pela regulação (7% do salário contributivo) e não por override; conferir a nacionalidade no cadastro. Fonte: Wallisson, sem lei no texto.
8. **Colômbia, PILA (HRBS-182):** IBC aproximado ao peso superior; contribuições e juros ao múltiplo de 100 mais próximo (Decreto 1990/2016, art. 3.2.1.5 do Decreto 780/2016). Se foi implementado: não consta.
9. **Jordânia, maternidade (HRBS-1629):** posição nossa: 0% empregador e 0% empregado em mês cheio de licença (Lei 24/2019, art. 4º que altera o art. 45); o cliente discorda (11,5%); sem aceite. Tratar como posição aberta até conferir o texto do artigo.
10. **Escopo (SR-204/205/206/263):** certificados de licença/benefício (NOI Bulgária, Apêndices 9–11) e a LME do Chile não são consumidos pelo payroll; o payroll precisa só de datas e tipo de licença, e a continuidade de SS (EV/SIS) já está construída no Chile.
