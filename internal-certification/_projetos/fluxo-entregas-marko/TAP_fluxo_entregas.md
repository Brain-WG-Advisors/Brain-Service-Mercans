# Termo de abertura (TAP): fluxo das entregas ao governo, países da nossa carteira (rascunho, 29/10/2026)

> **Linha de base do projeto.** Substitui, como referência de escopo, prazo e critério de aceite, o [[CAMINHO_0_a_100]] e as seções de ações do [[PLANO_fluxo_entregas_v0.2]], que ficam como histórico. Mudança na linha de base só com o ok do usuário (§10).
> Pedido: [[revisoes/2026-10-28-pedido-marko-fluxo-entregas|nota de 28/10]] · Fonte do pedido: weekly 27/10, 10:16–13:59 (`raw/reunioes/2026-10-27-research-team-weekly.txt`, l. 72–80).
> **Modelo exato:** `Vietnam_Payroll_Filing_Step_by_Step_Guide.pptx` (Manju, 27/10/2026, 38 slides). Cópia em `raw/drive/2026-10-29-modelo-manju/`, com o texto extraído em `.txt`; original no Drive em `Country Folders/Vietnam/12- Country Report Codes/`.

## 1. Objetivo (o que o Marko definiu)
Toda entrega de payroll ao governo, em cada país da nossa carteira, sai do sistema da Mercans e chega à autoridade de forma automática, sem digitação e sem terceiro (Manju, 13:08). O projeto entrega, por país:
- o caminho certo de cada entrega, com fonte oficial;
- o caminho de hoje;
- o que falta no sistema.

Ao Marko vai o plano com o status e as datas (13:08).

## 2. Escopo
**Dentro:**
- todas as entregas de payroll ao governo (impostos, previdência e seguros sociais, outros órgãos) e os pagamentos correspondentes;
- os países: os 12 da certificação (NO, DK, NL, SE, UK, UA, FI, EE, IE, KZ, AZ, RU), salvo decisão D1.

**Fora:**
- validar specs ou o cálculo (isso é a certificação; Manju, 10:08);
- corrigir ou refazer entregas;
- contatar a autoridade;
- os países da Manju e da Shruti, que recebem o método no fim.

## 3. Produto por país (critério de pronto = as 8 seções do modelo do Vietnã)

| # | Seção (slide do modelo) | Pronto quando |
|---|---|---|
| S1 | Legenda (sl. 2): SYSTEM STEP, PORTAL STEP, CUSTOMER ACTION, AUTHORITY e a marca [Verify] | Igual ao modelo |
| S2 | **Canal por report** (sl. 3): rota-alvo × rota de hoje ou provisória | Todas as entregas do país, com fonte oficial na rota-alvo e evidência na rota de hoje |
| S3 | **Canal por pagamento** (sl. 4): valor, prazo, como e a quem | Todos os pagamentos ao governo |
| S4 | **Por parte (Tax / Social security / Other / Payments):** visão do modelo com passos numerados por ator (sl. 6); setup único da Mercans, ou seja, registro como agente ou intermediário (sl. 7); passo a passo de cada entrega (sl. 8, 11, 12); rota provisória com o caminho de cliques no portal (sl. 9–10) | Cada entrega com os passos numerados e o ator de cada passo |
| S5 | **Licenças e roteiro** (sl. 28–30): condições de registro, 4 frentes de trabalho (Rulings, Entidade e licenças, Product build, Operação provisória) e o caminho crítico | O que falta no sistema e no registro, com dono e prioridade |
| S6 | **Perguntas abertas à autoridade** (sl. 32) | O que a fonte não resolve, marcado [Verify] |
| S7 | **Onboarding do cliente** (sl. 33): procuração, certificado, conta e canal por entidade | Checklist do país |
| S8 | **Índice de links** (sl. 34–37) | Toda fonte citada; as oficiais baixadas em `raw/docs/oficiais/<CC>/` |

**Formato:** o conteúdo é escrito em `paises/<CC>_fluxo_entregas.md`, nas seções S1–S8. No fim, o mesmo conteúdo vira um deck `.pptx` com o layout do modelo do Vietnã (decisão D2).
**Regra de fonte:** cada afirmação da rota-alvo (S2–S5) vem de fonte oficial lida, com artigo ou página. O que não tiver fonte vai para S6, marcado [Verify]. A rota de hoje vem de evidência (recibo, arquivo, SOP, ticket ou resposta do BAU). Prática manual não é base (Manju, 12:21).

## 4. Insumos já disponíveis (de onde partimos)

| Insumo | Serve para | Onde |
|---|---|---|
| Modelo do Vietnã (Manju) | Formato e nível de detalhe | `raw/drive/2026-10-29-modelo-manju/` |
| SOP do Taiwan (BAU APAC, 08/10) | Exemplo de "como é hoje" escrito pelo BAU | Mesma pasta |
| **SOPs de compliance de NO, DK, NL e IE** ("Summary of Periodic Statutory Filings": entrega, frequência, prazo e quem envia) | Lista de entregas (S2) e rota de hoje documentada, a reconfirmar porque a da NL é de 2021 | Drive, `Country Folders/<País>/01 - SOP/` |
| CCG, SIR e specs de cada país | Lista completa de entregas | Drive e `Research Pipeline/` |
| Pacotes da certificação (recibos e arquivos enviados) | Evidência da rota de hoje (NO, UK, DK, UA, KZ) | `internal-certification/<País>/` |
| Fontes oficiais já baixadas | Rota-alvo | `raw/docs/oficiais/` e `references/` |
| Tickets, reuniões e chats | Rota de hoje (portal, upload, login) | `scripts/buscar.py` |
| Contatos do BAU | Perguntas só para as lacunas | monday, BAU Master Client List |

## 5. EAP (estrutura analítica: pacotes de trabalho)

| WP | Pacote | Saída | Depende de |
|---|---|---|---|
| WP0 | Linha de base: este TAP e as decisões D1–D4 | TAP aprovado | Usuário |
| WP1 | Lista de entregas por país: SOP + CCG/SIR + pacote (S2/S3, colunas "report" e "pagamento") | 12 listas | — |
| WP2 | Pesquisa da rota-alvo (S2, S4 e S5, com o setup de agente/intermediário e a assinatura do cliente) | Seções com fonte | WP1 |
| WP3 | Rota de hoje: garimpo de evidência (pacotes, SOPs, buscar.py) | S2 "hoje" com fonte | WP1 |
| WP4 | Perguntas às lacunas: uma onda ao BAU e ao Dev, depois uma cobrança | Respostas arquivadas | D3 |
| WP5 | Fechar cada país: S4 com os passos, S5 a S8 | 12 documentos prontos (§3) | WP2–WP4 |
| WP6 | Deck no layout do modelo + visão geral de 1 página + gráfico por país | Relatório | WP5, D2 |
| WP7 | Método para a Manju e a Shruti (passos, modelo, tempo por país) | Guia do método | WP5 |

## 6. Matriz RACI

| Pacote | Certificação (esta janela) | Usuário | BAU do país | Dev/implementação | Manju | Marko |
|---|---|---|---|---|---|---|
| WP0 | R | **A** | — | — | — | — |
| WP1–WP3, WP5 | **R** | A | C | C | — | — |
| WP4 | R (rascunhos) | **A** (envia) | C (responde) | C (responde) | — | — |
| WP6 | R | A | — | — | I | I |
| WP7 | R | A | — | — | **I → C** (a partir de 10/11) | — |

R = executa · A = aprova · C = consultado · I = informado. Nada vai a terceiros sem o envio do usuário.

## 7. Cronograma e caminho crítico

| Data | Marco | Pacotes |
|---|---|---|
| 29–30/10 | **M0:** TAP aprovado e onda BAU + Dev enviada (pergunta da NO na frente) | WP0, WP4 |
| 30/10–31/10 | **M1:** 12 listas de entregas prontas | WP1 |
| 30/10–04/11 | **M2:** rota-alvo e rota de hoje (evidência) prontas nos 12 países, com subagentes em paralelo (4 de cada vez) e as citações conferidas por mim | WP2, WP3 |
| 04/11 | Prazo das respostas; 05/11: uma cobrança | WP4 |
| 06/11 | **M3:** 12 documentos fechados; lacunas sem resposta ficam [Verify], com o motivo | WP5 |
| 09/11 | **M4:** deck, visão geral e gráficos; sua revisão | WP6 |
| a partir de 10/11 | **M5:** método e resultado apresentados à Manju | WP7 |
| **até 17/11** | **Marco externo NO:** a resposta do Dev sobre systembruker e tilgangspakker precisa chegar antes do corte do Altinn II | WP4 |

**Caminho crítico:** M0 (envio) → respostas do BAU e do Dev (04/11) → WP5 (06/11) → WP6 (09/11). A pesquisa (WP2) não está no caminho crítico se começar em 30/10. Ela tem 4 dias de folga contra as respostas.

## 8. Riscos

| Risco | Prob. | Impacto | Resposta |
|---|---|---|---|
| R1 O BAU não responde até 04/11 | Média | Rota de hoje incompleta | O garimpo (WP3) sai antes, as perguntas cobrem só as lacunas, há uma cobrança e o resto fica "[Verify]" sem travar |
| R2 Sem contato do Dev | Alta hoje | O risco de 17/11 na NO não fica confirmado | Decisão D3, hoje |
| R3 Site da autoridade bloqueia download (captcha, geobloqueio) | Média (AZ, RU, KZ) | Rota-alvo sem fonte | Salvar pelo navegador e marcar [Verify] no S6 |
| R4 SOP desatualizado (NL de 2021) | Alta | Rota de hoje errada | SOP só como ponto de partida; vale o recibo ou a resposta do BAU |
| R5 Escopo crescer (mais países) | Baixa | Prazo | Decisão D1 agora; o resto entra por controle de mudança (§10) |
| R6 Retrabalho de formato | Baixa (o modelo foi encontrado) | Prazo | S1–S8 fixados neste TAP |

**Premissas:**
- o modelo do Vietnã é o formato esperado (Manju, 10:16; arquivo de 27/10, o mesmo dia da weekly);
- o BAU master no monday continua válido.

**Restrições:**
- não falar com a Manju antes do M5;
- nada é enviado sem o usuário;
- sem dados pessoais.

## 9. Medição do avanço (para o status ao Marko)
Cada país vale de 0 a 8, uma unidade por seção S1–S8 pronta pelo critério do §3. O avanço do projeto é a soma das seções prontas dividida por 96 (12 países × 8 seções).

**Hoje: 2,5 de 96 = 3%.** Só a Noruega tem conteúdo. Conta: S1 = 0 (sem legenda), S2 = 0,5 (1 entrega de ~2), S4 = 0,5 (tabela por ator, sem passos numerados), S5 = 0,5, S6 = 0,5 e S8 = 0,5 (fontes citadas, sem índice de links) → 2,5 seções. O resto ainda não está no formato do modelo. Os insumos do §4 já existem, por isso a curva deve subir rápido a partir de 30/10.

## 10. Controle de mudanças e comunicação
- **Mudança de escopo, prazo ou formato:** só com o ok do usuário. Fica registrada neste TAP com a data.
- **Status:** a cada fim de rodada, no `estado.md` da frente, que o painel lê. Sem resumo para a janela geral.
- **Instrução vigente:** não acionar a Manju antes do M5.

## 11. Decisões para aprovar o TAP (só o usuário)
- **D1, países:** os 12 da certificação. Espanha e Lituânia estão em produção e ficaram de fora. **Recomendo** os 12 agora e ES e LT logo depois, como teste do método. Se não houver resposta, sigo com os 12.
- **D2, formato final:** deck `.pptx` no layout do Vietnã (recomendo, porque é o que a Manju e o Marko já conhecem) ou só documento. Se não houver resposta, faço o deck.
- **D3, contatos:** quem responde pela NL (sugiro o Umesh), a quem perguntar na IE e o contato do Dev. Este último não tem opção padrão: sem ele, a pergunta da NO não sai.
- **D4, início:** ok para os subagentes de pesquisa (só leitura e download de fonte oficial) a partir de hoje.

## Bloco de prova
- **Pedido → resposta:** o projeto está planejado com escopo, produto, critério de pronto, EAP, RACI, cronograma, caminho crítico, riscos, medição e controle de mudança. O formato é o do modelo real da Manju, não suposição.
- **Fontes:**
  - weekly 27/10, l. 72–80 (relida em 29/10);
  - `Vietnam_Payroll_Filing_Step_by_Step_Guide.pptx` (38 slides, texto extraído e lido por inteiro);
  - `Taiwan_Statutory_Filings_Step_by_Step_Guide.pdf` (p. 1–5 lidas);
  - SOPs de DK e NL (busca de "upload", "submit" e "Summary of Periodic Statutory Filings");
  - listagem do Drive `Country Folders/<País>/01 - SOP/`.
- **Teste:** a medição do §9 foi refeita seção a seção sobre o `NO_fluxo_entregas.md`.
- **Confiança 95%:** o formato e o escopo estão com fonte. Os 5% são das datas M1–M3, estimadas porque nenhum país foi feito ainda no formato completo. A primeira semana mede e recalibra.
