# Fluxo das entregas: o caminho do 0 ao 100% (rascunho, 29/10/2026)

> **Destino, sem rediscutir:** o que o Marko definiu ([[revisoes/2026-10-28-pedido-marko-fluxo-entregas|nota de 28/10]], §§1, 3, 4 e 5). Toda entrega ao governo sai do sistema e chega à autoridade de forma automática, sem digitação e sem terceiro. Para cada entrega, o resultado mostra o que o sistema, o cliente e a autoridade fazem e o que falta.
> Este documento só traça o **caminho mais curto até lá**. Plano: [[PLANO_fluxo_entregas_v0.2]] · 1º país pronto: [[paises/NO_fluxo_entregas|Noruega]] · Melhorias: [[internal-certification/_melhorias/2026-10-29-propostas-melhoria|propostas 29/10]].

## 1. O que é o 100% (a régua)
Um país chega a 100% quando tem os 5 itens da nota (§4), cada um com fonte:

| Item | Pronto quando | De onde vem |
|---|---|---|
| I1 Lista de entregas | Todas as entregas de payroll ao governo, com a autoridade, a frequência e o prazo | Pesquisa nossa e artefatos (CCG, SIR, specs). Quem confirma que não falta nenhuma é o BAU (pergunta 3). |
| I2 Como deveria ser | Para cada entrega: o canal oficial (API, XML, portal), o registro como agente ou a procuração, e a assinatura do cliente, com fonte oficial baixada | Pesquisa nossa |
| I3 Como é hoje | Para cada entrega: quem gera o arquivo, por onde envia, com o login de quem, se corrige antes e se há terceiro | Recibos e arquivos dos pacotes, e depois o BAU e o Dev |
| I4 O que falta e quem resolve | Cada lacuna com o dono (Development, Config ou registro na autoridade) e a prioridade | I2 comparado com I3 |
| I5 Arquivo final validado | O report enviado foi conferido | Certificação |

Cada item vale 1, ½ (só parte das entregas ou sem fonte para tudo) ou 0.

## 2. Onde estamos hoje (medido em 29/10)

| País | I1 | I2 | I3 | I4 | I5 | % | Evidência |
|---|---|---|---|---|---|---|---|
| NO | ½ | ½ | ½ | ½ | 1 | **60%** | `paises/NO_fluxo_entregas.md`: a-melding feita com R1–R3 e S05; pagamento com KID ainda não visto. A certificação foi fechada (Audit Report de 16/10). |
| UK | ½ | 0 | ½ | 0 | 1 | **40%** | ACKs do HMRC e IRmarks conferidos. O FPS e o EPS levam no envelope o login do Government Gateway **do empregador** (UK F-01): hoje o envio sai com a credencial do cliente, não como agente da Mercans. |
| DK | ½ | 0 | ½ | 0 | 1 | **40%** | "Afstemning SKAT" no pacote mostra que o eIndkomst chegou. Não sabemos o canal nem quem é o registrado. |
| UA | ½ | 0 | ½ | 0 | 1 | **40%** | Recibo da DPS do J0500111, com 0 erros. Falta o recibo do 1-PV (C-10). Não sabemos de quem é a assinatura eletrônica (КЕП). |
| KZ | ½ | 0 | ½ | 0 | 1 | **40%** | O 200.00 foi aceito pela KGD em 25/09. A folha roda no 1C ZUP local, fora do HR Blizz (F-06). |
| SE | ½ | 0 | 0 | 0 | 1 | **30%** | O Kvittens no pacote é de outra empresa (SE-ONEID F-01), então não há prova de como a AGI desta empresa foi enviada. |
| NL | ½ | 0 | 0 | 0 | 1 | **30%** | Os 3 pacotes estão sem recibo do Digipoort (NL-QUEST F-08, NL-EXCERPTA F-06, NL-SHERWIN F-01). |
| FI, EE, IE, AZ, RU | 0 | 0 | 0 | 0 | 0 | **0%** | Sem pacote (C-11, C-12, C-13, D-01). |
| **12 países** | | | | | | **24%** | Média: (60 + 4 × 40 + 2 × 30) / 12 |

**Leitura:** o item mais atrasado é o I2 ("como deveria ser"), que só depende de nós. O I5 está quase completo nos 7 países com pacote. O I3 e o I4 dependem das respostas do BAU e do Dev.

## 3. O roteiro mais curto: 4 frentes ao mesmo tempo

| Frente | O que faz | Depende de | Como acelera |
|---|---|---|---|
| **A. Pesquisa "como deveria" (I1 + I2)** | Os 11 países que faltam, com o modelo da Noruega. Para cada país: a lista de entregas (do CCG e do SIR do país e da skill), o canal oficial, a regra de agente ou procuração e a assinatura do cliente. As páginas oficiais são baixadas para `raw/docs/oficiais/<CC>/`. | Ninguém | 1 subagente por país, 4 de cada vez, com modelo barato para baixar e localizar. O modelo forte só confere as citações (regra: reler na fonte primária). A Noruega levou 1 sessão; os 11 países levam de 3 a 4 dias úteis. |
| **B. Perguntas ao BAU e ao Dev (I3)** | Uma onda só, com os rascunhos prontos ([[mensagens_BAU_v0.1]]) | **3 respostas suas:** quem responde pela NL, a quem perguntar na IE e o contato do Dev | É a única frente com espera de terceiros, por isso **sai primeiro**: as respostas chegam enquanto a frente A trabalha. A pergunta da Noruega ao Dev vai na frente, por causa do prazo de 17/11. |
| **C. Garimpar o "como é hoje" que já está escrito (I3)** | Antes das respostas, buscar nos tickets, reuniões e chats (`python scripts/buscar.py "<termo>" --fonte tickets|reunioes|chats`) termos como Altinn, Digipoort, Gateway, portal, upload, manual, KEP/ЭЦП e power of attorney, por país | Ninguém | Script local, sem ler tudo. O que achar entra no I3 com a fonte; a pergunta ao BAU passa a só confirmar. |
| **D. Gerador do relatório (I4 → relatório)** | Um script lê os `paises/<CC>_fluxo_entregas.md` e gera a matriz e um gráfico por país (sistema / manual / terceiro / não sabemos) | Ninguém | Feito uma vez, rodado no fim. Cada novo país (Manju, Shruti) entra sem trabalho extra. |

**Ordem dos países na frente A:**
1. **UK, DK, UA, KZ, SE e NL**, onde já há o I5 e parte do I3. Com o I2 feito, chegam a cerca de 70% sem esperar ninguém.
2. **FI, EE, IE, AZ e RU**, só com pesquisa. O I3 vem pelo BAU.

## 4. Marcos

| Data | Marco | % esperado (12 países) |
|---|---|---|
| 29–30/10 | Suas 3 respostas e o envio da onda BAU + Dev (pergunta da NO na frente) | 24% |
| 03/11 | Frente A pronta nos 6 países com pacote; frente C rodada nos 12; script D pronto | ~50% |
| 04/11 | Prazo das respostas do BAU e do Dev; frente A pronta nos 5 sem pacote | ~65% |
| 05/11 | Uma cobrança só, a quem não respondeu | — |
| 06/11 | I3 e I4 preenchidos com as respostas; o que faltar fica marcado "a confirmar", com o motivo | ~90% |
| 09/11 | Relatório gerado + método + melhorias; sua revisão | 100% nos que responderam |
| a partir de 10/11 | Apresentar à Manju (método pronto para ela e a Shruti) e depois ao Marko | — |
| **até 17/11** | **Noruega:** a resposta do Dev sobre systembruker e tilgangspakker precisa chegar antes do corte do Altinn II | — |

O 100% real depende do BAU responder. Quem não responder até 06/11 aparece no relatório como "a confirmar", sem atrasar os outros.

## 5. O relatório final (o que o Marko recebe)
1. **Uma página de visão geral:** os 12 países × entregas, cada célula com a cor do estado: gerado e transmitido pelo sistema; gerado pelo sistema e enviado à mão; manual; terceiro; não sabemos.
2. **Um gráfico por país** com as mesmas categorias (nota, §5).
3. **Uma ficha por entrega:** sistema × cliente × autoridade, hoje × como deveria, o que falta, quem resolve e a prioridade. É o formato do Vietnã e do Taiwan.
4. **O que falta no sistema**, consolidado: a lista para o Development e a Config, com prioridade.
5. **Melhorias**, ligadas ao caminho:

| Do caminho | Melhoria | Por quê |
|---|---|---|
| I3 sem recibo em 7 de 11 pacotes | **M-07:** o sistema guarda o recibo da autoridade em cada entrega | Quando a transmissão é pela API, o recibo volta sozinho. É a prova de aceite que a certificação não encontrou. |
| UK: envio com a credencial do empregador dentro do arquivo | **M-08:** tirar as credenciais do arquivo, e o modelo de agente com autorização do cliente | No modelo do Marko (Mercans como agente, com autorização do cliente), a Mercans deixa de guardar a senha do cliente. |
| NO: a-melding só por systembruker a partir de 17/11 | Configurar o systembruker e pedir aos clientes que aprovem os tilgangspakker | Evita multa e surpresa, o objetivo do Marko. |
| KZ e UA: folha no 1C, fora do HR Blizz | **M-20:** definir o escopo e o plano de trazer para o sistema | São as entregas "manuais" do relatório. |
| Certificação: pacote incompleto, SBC lenta | **M-01, M-02, M-04, M-06:** checklist, conferência de entrada, um contato por país, uma onda por SBC | O mesmo canal serve à certificação e ao projeto, sem perguntar duas vezes. |
| Os demais achados | M-09 a M-19 | Vão como anexo: qualidade do que o sistema gera. |

## 6. O que destrava hoje (só você)
1. Quem responde pela NL? Sugiro o Umesh. Se não responder, sigo com ele.
2. A quem perguntar na IE? Se não responder, a IE fica só com pesquisa e marcada "a confirmar".
3. Quem é o contato do Dev/implementação? Sem ele, a pergunta da Noruega (17/11) não sai.
4. Ok para eu começar a frente A (subagentes) e a frente C hoje? Elas só leem e pesquisam, sem enviar nada.

## Bloco de prova
- **Pedido → resposta:**
  - onde estamos, medido: §2;
  - roteiro (paralelo, automação, terceiros, ordem): §3;
  - marcos: §4;
  - relatório e melhorias ligadas ao caminho: §5.
- **Fontes:**
  - itens e entregas da nota de 28/10 (§§4 e 5);
  - % por país: os pacotes em `frentes/certificacao/estado.md` (tabela Pacotes) e os achados citados na aba Achados do painel (29/10);
  - Noruega: `paises/NO_fluxo_entregas.md`;
  - fontes oficiais existentes em `raw/docs/oficiais/` (NO 1, DK 9, NL 4, GB 3, UA 55 arquivos; SE, FI, EE, IE, KZ, AZ e RU com 0) e `internal-certification/references/` (DK, KZ, NO, SE).
- **Teste:** a média dos 12 países foi refeita: (60 + 160 + 60) / 12 = 24,2%.
- **Confiança 80%:**
  - a régua de 5 itens com ½ ponto é nossa, montada sobre a nota de 28/10;
  - os % futuros são estimativa, calculada a partir do tempo da Noruega (1 sessão);
  - "envio com a credencial do empregador" no UK é leitura do achado F-01, ainda não confirmada pelo Dev.
