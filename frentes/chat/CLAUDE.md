# Frente 3 — Chat - Mercans

Esta pasta é a janela **Chat**. Vale tudo do `CLAUDE.md` da raiz do cérebro; aqui só o que é desta frente.

**Raiz do cérebro:** `C:\Users\instituto\Documents\brain-service` (`../..` daqui). Os caminhos abaixo são relativos à raiz, salvo `estado.md` (nesta pasta).

## Abrir a sessão (substitui o "Abrir a sessão" da raiz)
1. Ler `correcoes.md`, `frentes/chat/estado.md` e as últimas linhas de `log.md`.
2. Pedir ao usuário as conversas desde a última triagem (colar ou exportar). Salvar o material em `raw/chats/AAAA-MM-DD-<assunto>.md` antes de triar.
3. Gravar a triagem em `rascunhos/AAAA-MM-DD-triagem-chat.md`: **agir / só saber / ignorar**, com quem pediu, país e o que é pedido a nós. Itens de outros times → `fronteiras.md`.
4. Entregar o resumo curto ao usuário.

## Regras desta frente
- Respostas ao chat são só rascunho para o usuário colar.
- Ticket é da janela Suporte: se uma conversa mexer em ticket, anotar em "Pendentes" e avisar o usuário.
- Escreve só o seu `estado.md` e as triagens de chat. Compartilhados: "Janelas paralelas" na raiz.
- "Fecha a sessão": nota `sessoes/AAAA-MM-DD-chat.md` e reescrita só do `estado.md` desta pasta. Sem commit.

## Chrome falhou (roteiro fixo, decidido em 2026-10-27)
Uma mensagem só ao usuário, com a ação exata:
1. `list_connected_browsers`. Se vazio: "abra o Chrome e clique no ícone da extensão Claude".
2. `tabs_context_mcp`. Se a aba sumiu: "reabra a aba <URL> e me avise".
3. Se o clique ou a leitura falhar 2 vezes: parar e dizer o que tentei e o que o usuário precisa fazer (ex.: dispensar um diálogo, fazer login).
