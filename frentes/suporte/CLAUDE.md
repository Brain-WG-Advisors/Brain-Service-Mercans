# Frente 1 — Suporte - Mercans (YouTrack)

Esta pasta é a janela **Suporte**. Vale tudo do `CLAUDE.md` da raiz do cérebro; aqui só o que é desta frente.

**Raiz do cérebro:** `C:\Users\instituto\Documents\brain-service` (`../..` daqui). Os caminhos abaixo são relativos à raiz, salvo `estado.md` (nesta pasta).

## Abrir a sessão (substitui o "Abrir a sessão" da raiz)
1. Ler `correcoes.md`, `frentes/suporte/estado.md` e as últimas linhas de `log.md`.
2. Rodar `scripts/youtrack_fetch.ps1 -DryRun -Query "for: me #Unresolved"` e comparar com a tabela do `estado.md`: o que entrou, o que saiu, o que teve comentário novo.
3. Entregar um painel curto: urgente hoje / esperando o usuário / esperando outros.

## Trabalho
- Protocolo "responde o ticket X" do `CLAUDE.md` da raiz (skills antes, fonte primária, apresentar antes de gravar, nunca enviar).
- Rascunhos de resposta: `rascunhos/AAAA-MM-DD-respostas-fila.md` e `rascunhos/AAAA-MM-DD-youtrack-drafts/`.
- **Painel de entrega no navegador** (decidido em 2026-10-23): antes de gravar um lote de entregas, montar `<pasta do lote>/entrega/dados.json` e rodar `python -I scripts/painel_entrega.py <dados.json> --abrir`. Sai uma aba por entrega (texto pronto, afirmações × fonte relida por mim / só agente, palavras, itens além do pedido, pendências, checklist, decisão ✅/✏️/⛔ no título da aba) + `00-painel.html`. O usuário mede e decide nas abas; só então gravar. Páginas locais, nunca publicadas (dados de cliente). Exemplo: `rascunhos/2026-10-23-shruti/entrega/`.

## O que esta janela escreve
- Só o seu `estado.md` (tabela de tickets) e os rascunhos de tickets.
- Compartilhados (`log.md`, `correcoes.md`, hubs de país): seguir "Janelas paralelas" na raiz (reler antes, Edit pontual, log só no fim).
- "Fecha a sessão": nota `sessoes/AAAA-MM-DD-suporte.md` e reescrita só do `estado.md` desta pasta. Sem commit (só a janela geral commita).
