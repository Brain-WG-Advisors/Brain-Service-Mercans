# Plano de ação: fluxo das entregas ao governo (pedido do Marko) — v0.2

> **Estado:** em execução a partir de 28/10/2026. Esta versão substitui a [[PLANO_fluxo_entregas_v0.1|v0.1]], que fica como histórico. Ela incorpora as decisões do usuário de 28/10.
> Origem: [[revisoes/2026-10-28-pedido-marko-fluxo-entregas]] · Frente: [[frentes/certificacao/estado]].
> O modelo de matriz por país, o exemplo da Noruega e a lista de países continuam na v0.1, §§2 e 4.

## Decisões (usuário, 28/10)
- **Quem envia:** o usuário envia todas as mensagens. Esta janela só prepara os rascunhos e consolida as respostas.
- **Contatos:** vêm do board BAU Master Client List no monday. Não montamos mapa novo.
- **Times:** o fluxo passa por todos (BAU/payroll, implementação/Config, Development) até a autoridade (call com o Vinícius, 27/10, 01:01:31–01:03:46).
- **Perguntas:** curtas e só as necessárias: 3 ao BAU e 1 ao Dev/implementação.
- **Envio:** uma onda só, com uma mensagem por pessoa cobrindo todos os países dela. Sem semana de piloto separada: a primeira resposta serve de teste.

## Partida e chegada (29/10, decisão do usuário: sem trabalhar por fases)
- **Chegada** (weekly 27/10, 10:16–13:59): para cada país, o documento no modelo do Vietnã/Taiwan. Para cada entrega:
  - o que o sistema, o cliente e a autoridade fazem;
  - o registro da Mercans como agente;
  - o XML gerado pelo sistema, autorizado e assinado pelo cliente e transmitido sem intervenção manual;
  - o manual que restar, documentado passo a passo;
  - a lista do que falta no sistema.

  Depois, o plano com status e datas.
- **Partida**, o que já temos:
  - os pacotes da certificação com o arquivo enviado e o recibo (NO, UK, DK, UA, KZ; NL e SE sem recibo válido);
  - as fontes oficiais baixadas (NO, DK, SE, KZ);
  - os contatos do BAU (monday);
  - os hubs e as skills de cada país.
- **Como:** um documento por país (`paises/<CC>_fluxo_entregas.md`), preenchido direto com o que já temos. Perguntas ao BAU e ao Dev só para o que o arquivo não mostra. 1º país: [[paises/NO_fluxo_entregas|Noruega]] (29/10).

- **Caminho do 0 ao 100% (29/10):** [[CAMINHO_0_a_100]]. Hoje estamos em 24% nos 12 países. O caminho tem 4 frentes em paralelo (pesquisa com subagentes, onda BAU/Dev, garimpo com `buscar.py`, gerador do relatório) e marcos até 09/11.

## Mudança de 29/10 (decisão do usuário)
- **Ainda não falamos com a Manju.** Primeiro fazemos o caminho completo com os **nossos países**: os 12 da certificação, vindos do BAU Master list (NO, DK, NL, SE, UK, UA, FI, EE, IE, KZ, AZ, RU).
- **Ao terminar**, sinalizamos à Manju o caminho que traçamos, como método pronto, para ela e a Shruti usarem nos países delas.
- **Muda nas ações:**
  - a ação 1 sai;
  - na ação 4, o contato do Dev/implementação é indicado pelo usuário;
  - a ação 9 passa a ser "apresentar à Manju o caminho e o resultado dos nossos países".

## Ações

| # | Ação | Quem | Quando | Pronto quando |
|---|---|---|---|---|
*Tabela refeita em 29/10, sem a Manju até a ação 8.*

| # | Ação | Quem | Quando | Pronto quando |
|---|---|---|---|---|
| 1 | Rascunhos aos responsáveis do BAU dos nossos 12 países ([[mensagens_BAU_v0.1]]) e ao Dev/implementação | Certificação | 29/10 ✅ | Rascunhos prontos, com a fonte de cada entrega |
| 2 | Decidir: quem responde pela NL, a quem perguntar na IE, contato do Dev/implementação; conferir o board no monday | Usuário | 29/10 | 3 respostas dadas |
| 3 | Enviar todas as mensagens de uma vez (BAU + Dev) | Usuário | 29–30/10 | Todas enviadas; data registrada |
| 4 | Pesquisar na fonte oficial como cada entrega deveria ser (canal, registro/agente, assinatura), enquanto as respostas não chegam. Começar pela Noruega (Altinn 3). | Certificação | 29/10–06/11 | Coluna "como deveria" com fonte em cada linha |
| 5 | Prazo das respostas | Times | 04/11 | Respostas arquivadas |
| 6 | Uma cobrança só, para quem não respondeu | Usuário (rascunho: Certificação) | 05/11 | Enviada |
| 7 | Tabela por país: como é hoje × como deveria ser × o que falta × quem resolve, com o tempo gasto por país | Certificação | 05–06/11 | Tabela preenchida; lacunas com motivo |
| 8 | Fechar o "caminho": o método (passos, perguntas, modelo da tabela, tempo por país) + o resultado dos 12 países + a proposta de datas para os demais | Certificação monta, usuário revisa | 09/11 | Aprovado pelo usuário |
| 9 | Apresentar à Manju o caminho e o resultado, para ela e a Shruti aplicarem nos países delas | Usuário | A partir de 10/11 (na primeira weekly depois do fechamento) | Apresentado; ajustes registrados |
| 10 | Plano com datas e relatório com gráfico ao Marko | Manju/usuário | Depois da ação 9 | A definir com a Manju |

## Perguntas

**Ao BAU**, com a lista de entregas do país:
1. O arquivo é gerado pelo HR Blizz e enviado como está? Se não, o que vocês mudam ou preparam fora do sistema?
2. Como é enviado: direto do sistema, upload no portal da autoridade ou por terceiro? Com o login ou registro de quem?
3. Há alguma outra entrega a órgão do governo nesses países que não está na lista?

**Ao Dev/implementação:** por país, o HR Blizz transmite direto à autoridade ou só gera o arquivo? A autorização do cliente para a Mercans enviar (procuração ou certificado) é configurada no onboarding?

## Regras
- A resposta do BAU serve só para entender. O "como deveria" vem da pesquisa com fonte oficial (Manju, weekly 27/10, 12:21).
- As cobranças da certificação (C-01..C-05, C-14..C-18) seguem separadas, para não atrasar esta onda.
- País sem confirmação de que está em produção fica "a confirmar" (v0.1, §4).
