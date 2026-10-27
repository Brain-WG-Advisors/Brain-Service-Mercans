# Frente 2 — Gmail - Mercans

Esta pasta é a janela **Gmail**. Vale tudo do `CLAUDE.md` da raiz do cérebro; aqui só o que é desta frente.

**Raiz do cérebro:** `C:\Users\instituto\Documents\brain-service` (`../..` daqui). Os caminhos abaixo são relativos à raiz, salvo `estado.md` (nesta pasta).

## Abrir a sessão (substitui o "Abrir a sessão" da raiz)
1. Ler `correcoes.md`, `frentes/gmail/estado.md` e as últimas linhas de `log.md`.
2. Buscar no Gmail (conector do claude.ai) os e-mails desde a última triagem registrada no `estado.md`. Na primeira vez, confirmar que a caixa é a da Mercans.
3. Gravar a triagem em `rascunhos/AAAA-MM-DD-triagem-emails.md`: **agir / só saber / ignorar**, com remetente, assunto, país e o que é pedido a nós. Itens de outros times → `fronteiras.md`.
4. Entregar o resumo curto ao usuário.

## Gmail pelo Claude in Chrome (decidido em 2026-10-19)
O conector Gmail do claude.ai não é usado. Tudo pela aba do Chrome, na caixa `wgomes@mercans.com` (conferir no título da aba).
- **Listar:** navegar para `mail.google.com/mail/u/0/#search/<consulta>` (ex.: `newer_than:3d`) e ler com `get_page_text`. Os atalhos de teclado (j/k) estão desligados nesta conta.
- **Abrir uma conversa:** pela lista, `find` na linha + clique e depois `get_page_text`. Navegar direto para `#all/<id>` às vezes não troca a conversa na tela: conferir o título. Quando o texto tiver links, o `javascript_tool` costuma ser bloqueado ("Cookie/query string data"); nesse caso, usar `get_page_text`.
- **Tickets citados nos avisos do YouTrack:** ler pela API (`scripts/youtrack_fetch.ps1 -Query "issue id: ..." -OutDir <temp>`), não pelo e-mail.
- **Rascunho (só com ok do usuário no texto):** abrir a conversa, clicar em "Reply all" (ou "Compose" para e-mail novo), digitar o texto e fechar. O Gmail salva o rascunho sozinho. Para texto formatado, inserir o HTML no corpo (`div[aria-label="Message Body"]`) com `document.execCommand('insertHTML', false, policy.createHTML(html))`, criando antes a policy com `trustedTypes.createPolicy(...)`, porque o Gmail exige TrustedHTML. A assinatura padrão entra sozinha. Abrir só uma janela de Compose: a URL `?compose=new` mais o clique no botão abrem duas. Conferir em `#drafts` e devolver o link. **Nunca clicar em Send**, nem pressionar Ctrl+Enter.
- Abrir uma conversa marca como lida: tudo bem. Não arquivar, não apagar, não mudar rótulo.
- Fechar as abas abertas ao terminar.

## Regras desta frente
- Nunca enviar e-mail. Nunca apagar, marcar spam ou mudar rótulo sem ok. Rascunho de resposta só com ok.
- Ticket é da janela Suporte: se um e-mail mexer em ticket, anotar em "Esperando ação" e avisar o usuário.
- Escreve só o seu `estado.md` e as triagens de e-mail. Compartilhados: "Janelas paralelas" na raiz.
- "Fecha a sessão": nota `sessoes/AAAA-MM-DD-gmail.md` e reescrita só do `estado.md` desta pasta. Sem commit.

## Chrome falhou (roteiro fixo, decidido em 2026-10-27)
Uma mensagem só ao usuário, com a ação exata:
1. `list_connected_browsers`. Se vazio: "abra o Chrome e clique no ícone da extensão Claude".
2. `tabs_context_mcp`. Se a aba sumiu: "reabra a aba <URL> e me avise".
3. Se o clique ou a leitura falhar 2 vezes: parar e dizer o que tentei e o que o usuário precisa fazer (ex.: dispensar um diálogo, fazer login).
