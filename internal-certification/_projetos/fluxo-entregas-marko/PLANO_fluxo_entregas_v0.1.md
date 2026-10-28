# Plano: fluxo das entregas ao governo, do sistema à autoridade (pedido do Marko) — v0.1 RASCUNHO

> **Estado:** rascunho para o usuário aprovar (28/10/2026). Não foi enviado nem mostrado à Manju ou ao Marko, e ninguém foi contatado.
> Origem: [[revisoes/2026-10-28-pedido-marko-fluxo-entregas]] (janela geral, 28/10) · Frente: [[frentes/certificacao/estado]] · Serviço: [[analise-reports]].
> Abreviações das fontes: **W27** = `raw/reunioes/2026-10-27-research-team-weekly.txt` · **V27** = `raw/reunioes/2026-10-27-call-wallisson-lituania-espanha.txt` · **W07** = `raw/reunioes/2026-10-07-research-team-weekly.txt` · **M09** = `raw/reunioes/2026-10-09-call-manju-wallisson.txt` · **B21** = `raw/chats/2026-10-21-research-team-biweekly-marko-transcript.txt` · **IC** = `internal-certification/`.

## 1. Objetivo e escopo
- **Objetivo:** para cada país em produção, mostrar como cada entrega ao governo é feita hoje e como deveria ser, ou seja, gerada pelo sistema e transmitida sem intervenção manual nem terceiro. Daí sai o que falta (Dev, Config ou registro na autoridade) e um plano com datas (W27 13:08; nota §1).
- **Entra:** toda entrega de payroll a autoridade: tax, social security e também pensão e sindicato quando são estatutários (M09 02:18). Por entrega, entram o registro, a assinatura, o canal e o prazo (W27 10:41–11:30).
- **Não entra:**
  - a validação das specs e dos pacotes, que é a certificação interna (W27 10:08 "that is different");
  - a auditoria do ano das folhas, que é do BAU (Espanha 27/10 22:55);
  - o compliance calendar, que é outro pedido (M09 06:07).
  - A certificação entra só como fonte: os arquivos enviados e os recibos que estão nos `01 Received`.

## 2. Modelo de entrega por país (uma linha por entrega ao governo)

| Report | Autoridade | Frequência / prazo | Como deveria ser (canal oficial, registro/agente, assinatura; fonte) | Como é hoje (BAU) | Diferença | Quem resolve | Prioridade |
|---|---|---|---|---|---|---|---|

**Exemplo preenchido: Noruega** (cliente Henkel Norway AS, set/26). As fontes S## estão em `IC/references/Norway/2026/sources.md`, lidas em 14/10.

| Report | Autoridade | Frequência / prazo | Como deveria ser | Como é hoje | Diferença | Quem resolve | Prioridade |
|---|---|---|---|---|---|---|---|
| A-melding: renda, forskuddstrekk, AGA, dados ao NAV/SSB | Skatteetaten (recebe pelo Altinn) | Mensal, até o dia 5 do mês seguinte (a-opplysningsforskriften § 2-1, S21; S22) | **Canal:** "Integrasjon mot Skatteetatens API – Fra 2026 er dette den eneste måten å sende inn a-melding fra system" (S05). Formato XSD v2.3 (S01), com retorno A03 (S02, S03). **Registro/agente e assinatura:** ⚠️ falta pesquisar como o sistema se autentica e em nome de quem envia (delegação do cliente no Altinn 3, prazo de transição 31/05/26 citado em S05). Fonte ainda não lida. | **Pela evidência:** o recibo `tilbakemelding (13).json` (IC/Norway/…/Henkel Norway.zip) traz `"kildesystem":"HR Blizz"`, `altinnReferanse`, entrega em 2026-10-02T15:24 e `"mottakstatus":"mottatt"` sem `avvik`. O arquivo foi gerado pelo HR Blizz e aceito. **Falta perguntar ao BAU (Umesh):** quem transmitiu (API direto ou upload no Altinn), se houve correção antes do envio e se há terceiro. | A confirmar com a resposta do BAU. Achados da certificação no mesmo pacote: sindicato sem fradrag (A-01, High) e GL "CORRECTED" (C-01). Isso indica correção fora do sistema, mas ainda não está confirmado. | A definir | Alta: tem cliente ativo e recibo |
| Pagamento de forskuddstrekk e AGA (KID) | Skatteetaten | Forskuddstrekk: 1º dia útil depois do pagamento do salário. AGA: a cada 2 meses, no dia 15 (skattebetalingsloven § 10-10, S13; S22) | Pagamento com o KID que vem no retorno A03 (`innbetalingsinformasjon`, S02). ⚠️ Falta pesquisar se o pagamento faz parte do escopo de "entrega". | ⚠️ Não perguntado. O pacote tem o bank file `NO_7073_EE Bank File…xml`, mas não foi conferido se ele inclui o pagamento ao fisco. | — | A definir | A confirmar o escopo |
| Outras entregas (ex.: inntektsmelding ao NAV para reembolso de licença médica) | NAV | Por evento | ⚠️ Falta pesquisar. Não está nas fontes S01–S24. | ⚠️ Não perguntado | — | — | A confirmar |

**O que falta para fechar a Noruega:**
1. pesquisar a fonte oficial do registro, da autenticação e da delegação (Altinn 3/API);
2. perguntar ao BAU as 4 perguntas da §5;
3. decidir se pagamento e entregas por evento entram no escopo (pergunta à Manju, §3 fase 0).

**Outros países com pacote e recibo na certificação.** Esta é só a coluna "evidência"; o resto da linha fica a preencher. Fonte: `frentes/certificacao/estado.md`, tabela Pacotes.

| País | Entrega com recibo no pacote | O que o recibo já mostra |
|---|---|---|
| Reino Unido | FPS e EPS set/26 (HMRC) | "HMRC has received the HMRC-PAYE-RTI-FPS document… IRmark…", colado pelo Srikanth em 09/10 (`IC/United Kingdom/McDermott UK - 2026-09/01 Received/HMRC_acknowledgements_FPS_EPS_202609 (from Chat).txt`). Envio eletrônico com IRmark; quem envia está a confirmar. |
| Dinamarca | eIndkomst (Afstemning SKAT) | Aceito. O arquivo efetivamente enviado ainda não chegou (C-02). |
| Ucrânia | J0500111 (DPS, 21/09, 0 erros) e 1-PV | DPS aceito; falta o recibo do 1-PV (C-10). |
| Cazaquistão | 200.00 3T/26 (KGD, aceito 25/09) | A folha roda no **1C ZUP local, fora do HRBLIZZ**: "GL não existe (1C ZUP)", F-06. É um caso de "como é hoje" em que o sistema não gera a entrega. |
| Holanda (3 clientes), Suécia | Loonaangifte (Digipoort) e AGI (Skatteverket) | Sem recibo válido: falta o recibo (C-14 a C-16) ou o Kvittens é de outra entidade (C-04). |

## 3. Fases

| Fase | Entregável | Pronto quando | Depende de |
|---|---|---|---|
| **0. Alinhamento com a Manju** | 1 página com as respostas aos 4 pontos do §8 da nota: lista de países e ordem; documento do Vietnã/Taiwan como modelo; prazo do Marko; contato único com o BAU por país. Também: se pagamento e entregas por evento entram (§2). | As 4 respostas estão registradas no `estado.md`, o modelo do Vietnã/Taiwan está salvo no cérebro e o usuário aprovou este plano. | O ok do usuário para falar com a Manju. A Manju disse que faz o mesmo nos países dela e nos da Shruti (W27 13:59). |
| **1. Piloto em 1 país (recomendado: NO)** | O modelo da §2 preenchido para a NO, com fonte em cada célula de "como deveria", a resposta do BAU em "como é hoje" e o **tempo gasto por etapa** (pesquisa, espera do BAU, montagem). | Não sobra nenhuma célula ⚠️ sem justificativa, a resposta do BAU está arquivada e as horas foram medidas. "Single country timing evaluation" (W07). | Fase 0; resposta do Umesh (BAU NO); fonte do Altinn 3/API. |
| **2. Europa em produção, por ordem** | O modelo preenchido por país, na ordem da §4. | Cada país da lista tem todas as linhas preenchidas ou um motivo registrado (BAU sem resposta, fonte paga). | Fase 1 (o tempo por país define as datas); contatos do BAU (board "BAU Master Client List", monday 2072701698, `IC/CLAUDE.md` l. 36). |
| **3. Relatório ao Marko** | Um documento para ler de relance, com um gráfico por país: o que o sistema gera, o que é manual e o que falta (V27 01:05:26). Antes dele vai o plano com status e datas (W27 13:08). | O usuário aprova e a Manju revisa antes de ir ao Marko. | Fase 2, completa ou com corte parcial que a Manju aceite. |

## 4. Países da fase 2 (Europa em produção)

**Origem:**
- **BAU** = board BAU Master Client List, clientes ativos (`IC/CLAUDE.md` l. 36–50);
- **W07** = lista de "live BAU countries" de 07/10 (resumo automático da reunião, a conferir);
- **Hub** = `paises/<País>.md`, campo `etapa_producao`.

| País | Origem | Em produção? | Pacote/recibo na certificação | Prioridade proposta |
|---|---|---|---|---|
| Noruega | BAU (Umesh; Marju: reMarkable ainda em implementação) | Sim: há folha real de set/26 (Henkel) | Pacote ✅ + recibo A-melding ✅ | 1 (piloto) |
| Reino Unido | BAU (Srikanth, Christina) | Sim: McDermott set/26 | Pacote ✅ + ACK HMRC ✅ | 2 |
| Dinamarca | BAU (Rakshitha) + W07 | Sim: Sherwin-Williams, KGS set/26 | Pacote ✅ + recibo ✅ (falta o arquivo enviado) | 3 |
| Holanda | BAU (Umesh, Athul, Suresh) + W07 + Hub ("Omnicom em Live/BAU") | Sim: 3 clientes set/26 | Pacote ✅, recibo ❌ | 4 |
| Suécia | BAU (Athul) | Sim: One Identity set/26 | Pacote ✅, recibo de outra entidade | 5 |
| Ucrânia | BAU (Nataliia) | Sim: Altium ago-set/26 | Pacote ✅ + DPS ✅ (falta 1-PV) | 6 |
| Finlândia | BAU (Marju) + W07 | Sim pelo BAU; sem pacote | ❌ (C-11) | 7 |
| Estônia | BAU (Marju) | Sim pelo BAU; sem pacote | ❌ (C-11) | 8 |
| Irlanda | BAU (sem Primary SBC) + W07 + Hub ("Omnicom em Live/BAU") | Sim pelo hub | ❌ (C-13) | 9 |
| Espanha | W07 + Hub (em produção, Dev Drew/Brenet) | Sim | Fora da certificação | 10 |
| Lituânia | Hub ("Accenture Lithuania em Live/BAU") | Sim pelo hub | Fora da certificação | 11 |
| Romênia, Malta, Hungria, Letônia | Só W07 | **A confirmar** | Fora da certificação | Depois da confirmação |
| Alemanha, Suíça | Só W07; pesquisa ainda em andamento (B21) | **A confirmar** | — | Depois da confirmação |
| França | W07; o hub diz "go-live em fevereiro" | **A confirmar** (as fontes divergem) | — | Depois da confirmação |
| Portugal | Não está na W07 nem no BAU da certificação | **A confirmar** | — | — |

Ficam fora da fase 2 por não serem da Europa, a confirmar com a Manju se entram depois: Cazaquistão, Azerbaijão e Rússia (BAU Sadaf).

## 5. Perguntas ao BAU (uma mensagem por país)
Para cada entrega que o país faz ao governo (V27 01:04:28–01:05:04: "tenta ser direto nas perguntas"):
1. O sistema (HR Blizz) gera o arquivo, ou vocês montam à mão ou em outra ferramenta?
2. Por qual canal enviam: API ou sistema direto, portal da autoridade, ou um terceiro?
3. Vocês corrigem algo antes de enviar? O quê, e com quê (Excel, Claude, outro)?
4. Há terceiro envolvido (contador, provedor, outro time)?

**Como juntar à certificação:**
- No mesmo contato com o BAU, vão as 4 perguntas e o que a certificação já cobra do país. Exemplo NO: C-01 (GL "CORRECTED", carro, OTP, sindicato).
- Hoje existem 10 cobranças em rascunho (C-01 a C-05, C-14 a C-18) esperando o ok do usuário. Antes de enviar, decidir se cada uma ganha as 4 perguntas, para não perguntar duas vezes (nota §8).
- Quem grava é a janela Chat ou Gmail, com o ok do usuário.
- Pela fala da Manju, a resposta do BAU serve **só para entender**. O "como deveria" vem da pesquisa com fonte oficial (W27 12:21).

## 6. Quem faz o quê: **decisão do usuário**
| Opção | O que se sabe |
|---|---|
| Vinícius | O usuário passou a tarefa a ele em 27/10, como secundária depois de Lituânia e Espanha (V27 59:38–01:06:14, 01:32:49). Ele já mandou e-mails ao BAU pedindo amostras ("Falta 2 só, mas eles não respondem", V27 01:04:24). |
| Frente Certificação (esta janela) | Já tem os pacotes, os recibos, as fontes NO/DK/SE/KZ e os mesmos contatos do BAU. |
| Samuel | Ajuda nas automações (nota §6). Poderia, por exemplo, gerar o modelo e o gráfico da fase 3. |

Sugestão para decidir, sem decidir: quem faz o piloto e quem faz a fase 2 podem ser pessoas diferentes.

## 7. Riscos e o que falta
- **O BAU não responde:**
  - Rakshitha (DK), Athul (NL/SE) e Sadaf (RU/AZ/KZ) não tinham respondido em 07/10 (`IC/CLAUDE.md` l. 41–49);
  - o Vinícius tem 2 países sem resposta (V27 01:04:24);
  - mitigação: perguntar junto da cobrança que já existe, com a Manju em cópia.
- **Fonte oficial do canal e do registro:**
  - o "como deveria" exige a regra da autoridade sobre agente ou registro e sobre assinatura (W27 11:30);
  - para a NO, essa parte ainda não foi lida (§2);
  - em alguns países a fonte é paga ou fechada (Suíça paga, Alemanha exige entidade legal: W07).
- **Acessos:**
  - para ver como o sistema transmite (API direto ou export), pode ser preciso acesso ao HR Blizz ou ao portal;
  - ⚠️ não sabemos se temos esse acesso. Perguntar na fase 0.
- **Lista de países incerta:** a lista W07 vem de um resumo automático e o hub da França diverge dela. Tratar como "a confirmar" até a fase 0.
- **Sobreposição com a Manju:** ela faz os países dela e os da Shruti (W27 13:59). Na fase 0, dividir os países para não haver duplicação.

## 8. Datas
- **Datas por país:** só depois do piloto (regra W07, "Single country timing evaluation").
- **Proposta para o piloto:**
  - fase 0 até **30/10/2026**;
  - piloto NO de 02/11 a **06/11/2026** (fim do piloto).
- **Em que se baseia:**
  1. as fontes oficiais da NO já estão baixadas e registradas (S01–S24, 14/10), e o recibo já foi lido; falta só a parte do registro/Altinn 3;
  2. no pedido de 07/10, o BAU da NO (Umesh) respondeu em 2 dias: o pacote chegou em 09/10 (`IC/Norway/…/received.txt`);
  3. a validação completa da NO (pacote, fontes e Audit Report) levou de 14/10 a 16/10, uma tarefa maior que esta.
- **Risco para a data:** se o Umesh demorar mais de 5 dias úteis, o piloto fecha com "como é hoje" pendente, e o tempo de espera vira um dado do próprio piloto.
- **Depois do piloto:** tempo por país × número de países da §4, dividido entre quem fizer (§6). Essa é a data a propor à Manju e ao Marko.

## Bloco de prova
- **Pedido → resposta:** os 8 itens pedidos estão nas §§1–8, nesta ordem.
- **Fontes:** reuniões com o minuto citado; NO pelas fontes S## e pelo recibo JSON; lista de países pelo `IC/CLAUDE.md` l. 36–50, W07 e hubs.
- **Teste:** os campos `kildesystem`, `altinnReferanse`, `leveringstidspunkt` e `mottakstatus` foram lidos direto do `tilbakemelding (13).json` dentro do zip, sem extrair.
- **Confiança 80%:** está de pé como rascunho de plano. Falta confirmar:
  - a lista de países (fase 0);
  - a fonte do registro e do Altinn 3 na NO;
  - a lista W07, que vem de um resumo automático e não foi conferida no texto falado.
