# Serviço 3 — Suporte

> Etapa 3: tickets e dúvidas sobre o que entregamos. Método de resposta: skill `mercans-compliance-workflow`.
> Índice: [[00-INDEX]] · Fora do escopo: [[fronteiras]]

## O que recebemos (entradas)
- Tickets YouTrack (HRBS-, CT-, SR-...), em geral Service Request, Tier 3, Support Group "Compliance Support" (tickets: extração 2026-10-02).
  - **HRBS-**: pergunta ou confirmação de compliance, normalmente de implementação/BAU/cliente sobre um país (ex.: Baker Hughes em Namíbia, Congo, Gabão e Côte d'Ivoire; Altium na Ucrânia). Campo State (86-28) com gate Support Group = "Compliance Support" (chat: mercans-compliance).
  - **SR-**: pedido de **Report Spec** (ex.: SR-79 Fichero de Bases, SR-80 AFI, SR-83 M190 na Espanha; SR-160/161/162/163/414/415 na Ucrânia; SR-221/232 no Chile) ou payslip (SR-316 China, SR-340 Ucrânia), geralmente com a BA (Lily Li, Ruchi Gupta) em ciclo de queries (tickets: ES-A, ES-B, UA, OUT).
  - **CT-** / **CT-A-**: tickets de design/spec de regulação e KB de regulation specs (ex.: CT-A-485 "SPAIN - Regulation Specifications", CT-A-620 spec Côte d'Ivoire, CT-4321 Regulation Handover Checklist). CT- usa o campo Status (86-14) (tickets: ES-B, AF; chat: mercans-compliance).
- Queries diretas da BA sobre specs (colunas de perguntas na própria planilha, destaques por cor) (tickets: ES-A).
- Pedidos de confirmação estatutária que viram revisão de WTC/G2N do cliente (tickets: AF, UA).
- E-mails e chats: não há registro nas fontes; Google (Chat, Drive, Gmail) sem acesso [INCERTO].
- Tickets resolvidos também alimentam a automação drift-sync (ticket "Resolved" -> checagem de drift no CCG) (chat: compliance-research).

## O que entregamos (saídas)
- Resposta fundamentada (com fonte)
- Correção do artefato, quando for o caso
- **Resposta direta e humana**, sem estrutura robótica, com corte de tamanho; em inglês nos tickets. Feedback do solicitante em 2026-09-28: mais detalhada, em inglês, "sem aparência de IA" (tickets: AF; chat: mercans-compliance).
- Quando falta arquivo nomeado para fechar o ticket, pedir explicitamente (chat: mercans-compliance).
- Gap de produto declarado como gap (não mapeamento chutado) quando não há wage type no WTC (tickets: ES-A).
- [[rascunhos/2026-10-14-respostas-fila|2026-10-14-respostas-fila]]: Rascunhos de resposta da fila de 14/10 (SR-432 ES etc.) com fontes primárias de UA e ES
- [[rascunhos/2026-10-15-respostas-fila|2026-10-15-respostas-fila]]: Rascunhos de resposta de 15/10 (SR-162 D5 etc.) com a prova ao lado de cada afirmação

## Como sabemos que ficou certo (qualidade)
- Posição estatutária confirmada em **fonte primária** e **declarada com nível de confiança**; resolver só o que foi pedido ("verificar" não é "corrigir"); achados próprios só se críticos de compliance e fora do texto do ticket (chat: mercans-compliance).
- **Conferir a versão mais recente** do WTC/arquivo do enunciado antes de contestar (caso 65815 na Espanha: contestação baseada em cópia antiga foi retirada) (tickets: ES-B).
- **Spec corrigida contra o desenho oficial da autoridade** e conferência byte a byte com amostra real (A3) e saída da HRB (M190, M111, AFI, CRA, Bases) (tickets: ES-A, ES-B).
- Valor citado por quem pediu **não entra como confirmado** sem checar a skill/fonte oficial (valores de CO e NL, UAH da Ucrânia) (tickets: OUT, UA).
- Um só arquivo de spec: atualizar o arquivo linkado na descrição do ticket e registrar a versão no Version Control (tickets: ES-A).
- Destaques por cor na planilha: laranja = corrigido; verde = novo/atualizado; rosa/magenta/roxo = queries da BA (tickets: ES-A). Estilo da coluna de resposta nas specs: inglês, veredito primeiro, uma linha, sem `$` paths (decisão 2026-09-23) (chat: mercans-compliance).
- Resposta que muda artefato: registrar no Version Control e no hub do país (ciclo KCS abaixo).
- [[rascunhos/2026-10-16-auditoria-tickets|2026-10-16-auditoria-tickets]]: Auditoria independente (janela Certificação) dos rascunhos de ticket: afirmações, fonte primária, cobertura

## Ciclo KCS (registro no fluxo)
1. Fechou ticket → "fechei o ticket X"
2. Entra no hub do país
3. Se revelou erro → [[correcoes]]
4. Se mudou artefato → versão atualizada no hub
- [[rascunhos/2026-10-20-resposta-muhammad-monday-escrita|2026-10-20-resposta-muhammad-monday-escrita]]: Resposta ao Muhammad sobre escrita negada no board Monday (permissões owners)
- [[rascunhos/2026-10-26-muhammad-status-automacao-tickets|2026-10-26-muhammad-status-automacao-tickets]]: Resposta ao Muhammad sobre status da automação de tickets (tracked changes, ID no comentário)

## Padrões recorrentes de ticket
- **Spec com dezenas de queries da BA:** Fichero de Bases (SR-79), AFI (SR-80/SR-432: 78 queries em uma coluna, 76 em outra), CRA (SR-81), M190 (SR-83). Respostas em lote, spec única consolidada, validação com amostra A3 como etapa padrão (tickets: ES-A, ES-B; chat: mercans-compliance).
- **Resposta nossa corrigida depois:** 65894 anunciado no changelog e inexistente (UA); contestação do 65815 baseada em cópia antiga (ES); parecer HRBS-14996 de 22-09 corrigido em 23-09 (CI); respostas divergentes para o valor do 563 e para o período-base de sick leave (6 x 12 meses, UA) ainda por resolver (tickets: UA, ES-A, ES-B, AF).
- **Tickets sem resposta nossa e SLA negativo:** Namíbia/Congo de jul-ago/2026 (HRBS-12072, 12101, 12110, 12111, 12483, 14055) e gaps de Colômbia (PMI, 5 tickets) ficam como fila de pendências do Wallisson; SLA "Paused / SLA Exempt" ou "Breached" é comum (tickets: AF, OUT, ES-B).
- **Perguntas novas depois do Resolved:** o solicitante continua perguntando no ticket já resolvido (UA, ~2026-09-22, sem resposta no snapshot); tratar como pendência, não como ticket novo [INCERTO se há regra] (tickets: UA).
- **"Não é compliance, é outra coisa":** pedido de labor law (leave, work accident no D12 RO), item de HR (eventos MA/MB/MC/MG na AFI), config de cliente, classificação de expat do cliente, report/automação de Dev. Responder a posição estatutária e devolver o resto (ver [[fronteiras]]) (tickets: ES-A, OUT, UA; chat: design-dev-kb).
- **WTC do cliente x WTC de compliance:** identificar exatamente qual contribuição estatutária o item do cliente representa antes de aceitar ou rejeitar (CAMU solidarité 0,5% x CAMU 2,27%; "CNAMGS/FNH" na CI = AT/MP e PF+AM) (tickets: AF).
- **Nome de regime não é isenção:** isenção fiscal só com instrumento específico confirmado por ano (HRBS-14996) (tickets: AF).
- **Piso x teto** confundidos pelo cliente (SMIG x teto CNPS na CI) (tickets: AF; chat: mercans-compliance).
- **Defeito achado na revisão vai para ticket separado**, não se resolve no ticket da pergunta (GTN da CI) (tickets: AF).
- **Erro de portal com spec já confirmada vai para o Dev** (M111, M296); erro de spec (campos fundidos, posições erradas) é nosso (tickets: ES-B).
- **Inbound x outbound** confundidos em respostas curtas: responder sempre com o nome completo do arquivo/spec (tickets: ES-A).
- **Conflito de versionamento com outros times:** apagar versão anterior em que a BA já trabalhava gerou reclamação (SR-221); não renomear nem criar estrutura no WTC alheio sem aval (tickets: OUT).
- **Pedido recorrente da BA:** "true XML sample" (não schema) para D1/D5/D6/4DF na Ucrânia; coluna de report code no WTC (Chile, SR-221 e SR-232) (tickets: UA, OUT).
- **Fronteira com Reports (NL):** Reports só mexe em Custom Reports com spec; perguntam a Compliance se o report é statutory (tickets: OUT).
- **Ticket fora do lugar:** HRBS-13860 (Naersa, Irlanda) caiu no grupo errado, é L2/integração e não compliance (tickets: AF).
- **Em aberto (OD-13):** HRBS- de Compliance Support edita artefato direto ou escala para CT-? Exemplo-base: HRBS-11078 (chat: mercans-compliance).
- [[rascunhos/2026-10-05-fila-tickets|2026-10-05-fila-tickets]]: Fila de tickets sem resposta nossa (snapshots até 29/09), montada a partir dos hubs de país
- [[rascunhos/2026-10-15-perguntas-fila|2026-10-15-perguntas-fila]]: Perguntas em aberto da fila YouTrack em 15/10 (último pedido feito a nós por ticket)

## Países
[[Africa-do-Sul]] · [[Alemanha]] · [[Australia]] · [[Bahrein]] · [[Belarus]] · [[Belgica]] · [[Botsuana]] · [[Bulgaria]] · [[Canada]] · [[Chade]] · [[Chile]] · [[China]] · [[Chipre]] · [[Colombia]] · [[Congo]] · [[Costa-Rica]] · [[Costa-do-Marfim]] · [[Dinamarca]] · [[Egito]] · [[Espanha]] · [[Estonia]] · [[Filipinas]] · [[Finlandia]] · [[Franca]] · [[Gabao]] · [[Guine-Equatorial]] · [[Holanda]] · [[Hungria]] · [[India]] · [[Indonesia]] · [[Irlanda]] · [[Kuwait]] · [[Libano]] · [[Lituania]] · [[Malasia]] · [[Marrocos]] · [[Mocambique]] · [[Namibia]] · [[Noruega]] · [[Portugal]] · [[RD-Congo]] · [[Reino-Unido]] · [[Romenia]] · [[Singapura]] · [[Suecia]] · [[Tailandia]] · [[Tchequia]] · [[Ucrania]] · [[Vietna]]
