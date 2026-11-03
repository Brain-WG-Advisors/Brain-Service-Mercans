# Estado — Frente 5: Certificação (Internal Certification – Reports)

> Escrito **só pela janela "Certificação - Mercans"**. Criado em 2026-10-15 a partir de `internal-certification/PLANO_DE_ACAO_VALIDACOES.md` (§2, 14/10), do painel `Acompanhamento_Internal_Certification.xlsx` (14/10) e das sessões de 07–14/10 (Claude Desktop, VS Code e janela geral). Reescrever a cada "fecha a sessão" desta janela.

**Objetivo:** validar os statutory reports que o HRBLIZZ produz em 12 países, com o pacote real enviado pela Primary SBC (report + recibo, G2N, contracheques, GL, banco, master). Validamos e reportamos; achados vão para implementation/dev.
**Pasta:** `C:\Users\instituto\Documents\internal-certification` · Método: [[analise-reports]].

## Instruções vigentes
- **(02/11, usuário) E-mail, Chat e Suporte por esta frente:** sempre que o pedido envolver e-mail, Chat ou suporte, esta janela usa o Claude in Chrome direto. Não pedir nada à janela/aba Gmail. Rascunho fica em **Rascunhos (draft)** no Gmail; enviar só quando o usuário pedir.
- **(02/11, usuário) Formato das mensagens a terceiros:** uma pergunta por linha, com opções; tabela para confirmar ou corrigir; ~10 linhas obrigatórias; o resto como opcional. Certificação e projeto do Marko numa mensagem só por pessoa. **Padrão fixo para todos os países:** `internal-certification/_projetos/fluxo-entregas-marko/PADRAO_email_SBC.md` (regras, modelo, checklist, fila). Só entra pergunta com fonte: item "Not provided" do Audit Report final ou Not tested ainda aberto; sem tabela (uma pergunta simples por declaração). **(02/11, usuário) Vale para os 10 contatos, inclusive os rascunhos, de forma flexível.** Padrões assumidos: DK → Deepak com Rakshitha em Cc; AZ/KZ → perguntas do projeto vão à Pari e à Malika.
- **(29/10, usuário via janela geral)** Não mandar resumo à janela geral: o painel `http://127.0.0.1:8765/frentes.html` lê cada fim de rodada. Usar SendMessage à brain-service-5b só para o que só ela faz (commit, coordenação entre frentes).

- **(29/10, usuário) Projeto do Marko:**
  - **escopo:** todos os países que são nossos (com cliente ativo no BAU Master), não só os 12 da certificação;
  - **contatos:** quem responde por cada país e o contato do Dev são descobertos por esta janela, sem perguntar ao usuário;
  - **subagentes:** liberados, sem pedir ok;
  - **piloto:** a Noruega, completa, antes de abrir os demais;
  - **formato:** o deck. A Manju não tem modelo próprio e vai seguir o nosso; o guia do Vietnã é referência de estrutura;
  - **distribuição:** dividir as tarefas entre os agentes com inteligência.
  - **Gmail (29/10, usuário):** "pare de pedir coisas para aquela janela… analise o email usando o claude in chrome e você mesmo envie". Neste projeto, esta janela lê, confere e **envia** os e-mails ao BAU pelo Claude in Chrome, sem passar pela janela Gmail. O envio é **só quando o usuário pedir**, e a cada e-mail.
  - **Enviados:** **29/10, Umesh (NO/NL)**, Cc Marko e Manju; prazo 04/11. É o início da medição do tempo de resposta do BAU no piloto NO. Próximo: Marju (EE/FI).
  - **Fato novo (agenda do usuário, 29/10):** reunião "Ukraine Migration Project Plan – 1C to HRBlizz" em 30/10, 9:30. A UA está migrando do 1C para o HR Blizz, e isso entra no "como é hoje" da Ucrânia.
  - **Contato (29/10, usuário):**
    - por enquanto só o BAU (o Primary SBC do BAU Master). O Dev fica de fora;
    - **sem call**: tudo por escrito;
    - ~~mensagem nova por pessoa, sem a Manju e o Marko em cópia~~ **(mudou em 29/10, usuário):** por **e-mail**, com **Marko (mtaylor@mercans.com) e Manju (mshetija@mercans.com) em Cc**. Vale para as mensagens ao BAU deste projeto. A instrução de não acionar a Manju fica superada nesse ponto;
    - base nos transcripts: weekly 27/10 12:15 ("take from BAU team") e a call com o Vinícius em 27/10 (1:03:39–1:05:19).

## Pacotes

| Pacote | País | Período | Pass / Finding / Not tested | Recibo prova aceite? | Situação | Próximo passo |
|---|---|---|---|---|---|---|
| Henkel Norway AS | [[Noruega]] | set/26 | 34 / 9 / 4 | Sim (A-melding GODKJENT) | ✅ Fechado · Audit Report 16/10 | Cobrar Umesh (C-01): GL "CORRECTED", carro, OTP, sindicato |
| Sherwin-Williams Denmark A/S | [[Dinamarca]] | set/26 | 18 / 5 / 2 | Sim (Afstemning SKAT) | ✅ Fechado · Audit Report 16/10 | Arquivo eIndkomst efetivamente enviado (C-02) |
| KGS Fire & Security Danmark ApS | [[Dinamarca]] | set/26 | 15 / 5 / 4 | Sim | ✅ Fechado (banco = Out of scope) · Audit Report 16/10 | Tipo do seguro-saúde; master (C-03) |
| Quest Software B.V. | [[Holanda]] | set/26 | 60 / 9 / 5 | Não | ⏳ Falta recibo Digipoort | Audit Report v1.1 emitido 14/10; v1.2 (correção Whk) + relatório interno v1.0 em 16/10, a mostrar à Manju; cobrança C-15 em rascunho (item 2 corrigido) |
| Sherwin Williams (Valspar B.V.) | [[Holanda]] | set/26 | 48 / 18 / 5 | Não (recibo é de outro LH) | ⏳ Falta recibo | C-16 em rascunho |
| Excerpta Medica B.V. | [[Holanda]] | set/26 | 60 / 5 / 5 | Não | ⏳ Falta recibo | C-14 em rascunho |
| One Identity Sweden AB (559400-9267) | [[Suecia]] | set/26 | 19 / 6 / 6 | Não (Kvittens é da Quest Software AB) | ✅ Validado · Audit Report 16/10 (qualified) | C-04: Kvittens, master, banco |
| Mastercard (Rep. office) | Cazaquistão | out/26 | 21 / 7 / 4 (v1.1) | Sim (200.00 3T/26 aceito KGD 25/09) | ✅ Validado · Audit Report 19/10 (qualified) | 200.00 recebido 19/10; ИПН ok (faixa 15%); F-06 High: folha "outubro" declarada como 3º mês do 3T; GL não existe (1C ZUP). C-18 em rascunho (confirmar o mês) |
| Altium | [[Ucrania]] | ago/26 | 33 / 13 / 12 | Sim para J0500111 (DPS 21/09, 0 erros); falta 1-PV | ✅ Validado · Audit Report 16/10 (qualified) | XML desempacotado; recibo do 1-PV (C-10) |
| Altium | [[Ucrania]] | set/26 | 9 / 4 / 7 | Não | 🔄 Audit Report INTERIM 19/10 (sem opinião sobre o report) | C-17 em rascunho: report de set + DPS, contracheques/GL/banco, 1-PV mensal e recibos, julho; reemitir como final |
| McDermott UK | [[Reino-Unido]] | set/26 | 50 / 4 / 17 | ⚠️ Ver nota 1 | ✅ Validado · Audit Report 16/10 (aceite HMRC: IRmarks conferem) | Workbook v1.1: NT-01/A02 → Pass, novos RF-02 (FPS após payday), MD-01, MD-02; master 69 = FPS 69 |
| A confirmar | Azerbaijão | set/26 | — | — | ⏸️ Pulado (zip AES, senha no e-mail) | Decisão D-01 do usuário |
| — | [[Finlandia]], [[Estonia]] | — | — | — | ⏳ Sem arquivos | C-11: cobrar Marju (2ª vez) |
| — | [[Irlanda]] | — | — | — | ⏳ Sem SBC | C-13: definir com Manju/Marko |
| — | Rússia | — | — | — | ⏳ Sem contato | C-12: Olga apresentada pela Sadaf (09/10); pedido em rascunho no Gmail desde 09/10, envio não confirmado |

**Notas**
0. **29/10:** painel atualizado (células em azul; backup no scratchpad da sessão). UK e KZ: recibo = Sim e situação conforme os Audit Reports. Entraram na aba Achados KZ F-06, UK RF-02, MD-01 e MD-02. KZ F-01 foi descartado (correto). C-09 concluída; C-05 parcial; C-17 e C-18 acrescentadas. Propostas de melhoria (rascunho): [[internal-certification/_melhorias/2026-10-29-propostas-melhoria|propostas 29/10]].
1. **UK — divergência no painel (resolvida em 29/10 no painel; o workbook de 07/10 não foi revisado, pela regra de 16/10):** o painel dizia "Falta recibo", mas os ACKs do HMRC (FPS e EPS de set/26, recebidos 29/09) foram colados pelo Srikanth no Chat em 09/10 e arquivados em `United Kingdom/McDermott UK - 2026-09/01 Received/HMRC_acknowledgements_FPS_EPS_202609 (from Chat).txt`; os IRmarks batem com os arquivos validados. Atualizar o painel e o workbook UK (recibo → Pass) na próxima sessão desta frente.
2. **Ucrânia ago/26:** recibo da DPS do J0500111 (aceito 21/09/2026) já está no pacote; o que falta é o recibo do 1-PV.

## Ações para implementation (painel, aba Ações)
- A-01 NO: contribuição sindical fora da base do trekk e sem fradrag na A-melding (High).
- A-02 DK: seguro-saúde do empregador não tributado na KGS (High).
- A-03 DK: indenização no campo 0069 pelo líquido (Medium).
- A-04 SE: payout de férias acumuladas na tabela mensal (High) — aguarda decisão D-02.
- A-05 DK: base do Store Bededag / ferietillæg — aguarda decisão D-03.
- A-06: templates de contracheque (NO/DK/SE/KZ).
- A-07: pedir sempre o arquivo como enviado + recibo da autoridade.

## Esperando o usuário
- Aprovar as cobranças em rascunho (`followups.md` de cada pacote): C-01 a C-05, C-14 a C-16.
- Decisões D-01 (abrir zip AZ), D-02 (SE, SFL 11:17), D-03 (DK, Store Bededag).
- Regra (16/10): só validar e emitir Audit Report dos pacotes completos; não revisar workbooks depois de validado. KZ, UA set/26, AZ ficam fora até chegar o report principal.

## Projeto do Marko: fluxo das entregas (registrado em 28/10, separado da certificação acima)
> Recebido da janela geral em 28/10. **Não contatar ninguém.** **Plano de ação vigente: [[internal-certification/_projetos/fluxo-entregas-marko/PLANO_fluxo_entregas_v0.2|v0.2]]** (28/10), com 10 ações, onda única ao BAU em 29–30/10, respostas até 04/11 e plano por país em 09/11. A v0.1 fica como histórico (matriz, exemplo da NO, lista de países).
> Nota completa: [[revisoes/2026-10-28-pedido-marko-fluxo-entregas]]. Fontes lidas em 28/10: weekly 27/10 (04:31–13:59), call com o Vinícius 27/10 (59:38–1:06:14 e 1:32:49–1:33:24), weekly 07/10, call com a Manju 09/10, bi-weekly 21/10, Espanha 27/10 (22:18–24:58).

- **Decisões do usuário (28/10):**
  - **ele mesmo envia** as mensagens à Manju e aos times;
  - o mapa de contatos já existe no monday (BAU Master Client List), então não precisa montar outro;
  - perguntas curtas, só as necessárias;
  - uma mensagem por pessoa, em uma onda só;
  - o fluxo inclui todos os times (BAU, implementação/Config, Dev).
- **Linha de base (29/10): [[internal-certification/_projetos/fluxo-entregas-marko/TAP_fluxo_entregas|TAP]]**, com o formato do guia do Vietnã da Manju, encontrado no Drive (cópia em `raw/drive/2026-10-29-modelo-manju/`). Avanço (29/10, fim do dia):
  - **NO:** piloto v1.0 no formato S1–S8 (`paises/NO_fluxo_entregas.md`), à espera da aprovação do usuário para virar padrão;
  - **dados:** 6 agentes rodaram (`dados/`: monday, lista de entregas, evidência de hoje e contato Dev, rota-alvo de UK/DK/SE/NL, de FI/EE/IE e de UA/KZ/RU). AZ ficou sem fonte, porque os sites não abrem;
  - **mensagens:** `mensagens_v0.2.md` pronta (Dev: Illya; BAU com os contatos do monday). Urgente: EE (TSD sem XML desde 01/10; prazo 10/11) e NO (17/11).
  - **Próximo:** com o ok do piloto, montar os 11 países no formato.
- **Instrução vigente (29/10):** não acionar a Manju agora. Primeiro fazemos o caminho com os nossos 12 países. No fim, apresentamos a ela o método e o resultado.
- **O pedido:** para cada país em produção, levantar como cada entrega ao governo é feita **hoje** (o sistema gera ou é feita à mão, por qual canal, com ou sem terceiro, se é corrigida antes do envio) e como **deveria** ser (o sistema gera, a Mercans é registrada como agente, o arquivo vai por XML/API com a assinatura do cliente). Depois, listar o que falta e montar um plano com datas para o Marko.
  - Não é a validação das specs. A Manju disse em 27/10 10:08: "that is different than what I'm asking now".
  - O modelo é o documento da Manju para o Vietnã e o Taiwan.
- **Entregas:**
  - primeiro, o plano com o status e a data de fim por país;
  - no fim, um relatório com um gráfico por país, mostrando o que o sistema gera, o que é manual e o que falta.
- **Ordem:**
  - começar pela Europa;
  - medir o tempo com 1 país antes de prometer datas (regra de 07/10).
- **Quem faz:** o Vinícius executa, como tarefa secundária depois de Lituânia e Espanha. A Manju faz os países dela e os da Shruti.
- **Onde encontra a certificação em andamento:**
  - **Países:** a lista Europa de 07/10 (DK, RO, FI, MT, HU, LV, DE, CH, FR, IE, NL, ES) tem 4 países em comum com os 12 da certificação: DK, FI, IE e NL. Os outros países europeus da certificação (NO, SE, UK, EE) também estão em produção.
  - **Contatos do BAU:** são os mesmos de cada país (Umesh, Srikanth, Malika, Nataliia, Marju...). Por isso, perguntar uma vez só por país.
  - **Arquivos:** os `01 Received` já têm os arquivos enviados e os recibos (A-melding, FPS/EPS com IRmark, DPS, 200.00 na KGD). Isso cobre o item 5 da nota ("validação dos arquivos finais").
  - **Como é hoje, já visto nos pacotes:** no KZ a folha roda no 1C ZUP local, fora do HRBLIZZ, e o 200.00 é entregue pelo portal da KGD.
- **Pendente de confirmar com a Manju (§8 da nota):**
  - a lista de países e a ordem (os 9–10 do BAU master de cada um, ou os ~60 em produção);
  - o documento do Vietnã e do Taiwan, para usar como modelo;
  - se existe prazo do Marko, ou se propomos o prazo depois de medir 1 país;
  - um contato único com o BAU por país para a certificação e para este projeto.

## Onde ficou cada coisa
- Sessão VS Code (07–14/10, `8ae80473…`): validações NO/DK/SE/KZ, painel, Holanda completa + Audit Report.
- Sessão Claude Desktop (08–09/10): coleta inicial no Chat/Gmail, validações UK/UA, 8 cobranças em rascunho (7 Chat + 1 Gmail Olga).
- Janela geral do cérebro (14/10): kit v2, plano de ação, coleta KZ/AZ/DK/NO, correção da ponte do Chrome (`internal-certification/_chrome_fix/`).
