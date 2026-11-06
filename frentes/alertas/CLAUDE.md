# Frente 9 — Alertas (mudanças estatutárias e Compliance Calendar) - Mercans

Esta pasta é a janela **Alertas**. Vale tudo do `CLAUDE.md` da raiz do cérebro (`../..`); aqui só o que é desta frente. Criada em 2026-11-05 pela janela geral, por decisão do usuário: **uma frente só para tudo de alertas, responsável por dar início e fechar cada alerta**.

**Objetivo:** toda mudança estatutária que afeta os países da Mercans vira um alerta conferido na fonte oficial, chega ao Development pelo caminho certo e é fechada quando entra em produção. Junto, o Compliance Calendar de cada país fica certo e completo.

## O que esta frente cobre (decisão do usuário, 2026-11-05)
1. **Kit "Statutory Updates Tracking 2026" (Manju, e-mail de 05/11).** Roda segunda e quinta às 12:00 e gera uma planilha para o Development por rodada (saída em `~/mercans-pipeline/statutory-update-tracker/outputs`). Primeira tarefa: instalar (ver `estado.md`).
2. **Alerta estatutário por país:** documento "Alerta 2026" do país (ex.: Lituânia, CT-4285) e board do monday **Compliance Statutory Alerts Tracking [2025-2026]** (18227732675: Research Status, Development Status, Mercans Alert Link, Alerts 2026 Link, YouTrack Task).
3. **AI-Generated Alerts (Usema/Manju):** conferir valores e efeito na folha antes da aprovação (ex.: OASDI 2027 na SSA, 19/10; living wage UK, 05/11).
4. **Compliance Calendar (HRB System Settings).** Pedido do Marko: calendário em produção para uns 60 países, 1 a 2 por semana, prioridade aos países com clientes ativos (BAU master list). Inclui o baseline de alertas da Shruti. Saiu da frente Certificação em 2026-11-05.
5. **SCA (Statutory Change Alert, automação):** acompanhar; a construção não começou e ninguém foi designado (pacote de automação do Samuel, 27/10).

## Ciclo de um alerta (início → fim)
1. **Entrada:** planilha do kit, AI-Generated Alert, e-mail/chat/ticket ou reunião. Registrar na hora em `estado.md` (fila de alertas), com data e origem.
2. **Triagem:** país está na carteira? Já está ativo (regra 9)? É nosso ou de outro time ([[fronteiras]])?
3. **Pesquisa:** fonte primária oficial, artigo inteiro, vigência (regra 1). Sem fonte → não vira alerta ([[pesquisar-e-decidir]], [[ler-artigo-inteiro-antes-de-afirmar]]).
4. **Registro no cérebro:** hub do país (valor com vigência e fonte; valor antigo recebe data de fim, regra 2) e a pasta da entrega em `Research Pipeline/<País>/AAAA-MM-DD-alerta-<assunto>/CONFERENCIA.md`.
5. **Alerta e monday:** atualizar o documento de alerta do país e o board (Research Status) — **só com ok do usuário** (Drive e monday).
6. **Passagem ao Development:** artefato entregue muda **na versão atual com change log, nunca documento novo** (regra 10, regra da Manju de 05/11); avisar o Dev antes de mexer; ticket de alteração quando o país é ativo (regra 9). O texto do ticket vai à frente Suporte e o e-mail à frente Gmail, pelo usuário.
7. **Fechamento:** Dev liberou em produção (ticket fechado, Development Status no monday) → marcar fechado em `estado.md`, linha no hub e no `log.md`. Alerta só fecha com a prova de que entrou.

## Compliance Calendar: método (conferência da Espanha, 19/10; conselho à Shruti, 20/10)
1. Baseline pelo calendário oficial de cada órgão (imposto, previdência, trabalho), não pela lista da ferramenta: obrigação, frequência, data legal e link da página exata.
2. Obrigações recorrentes estendidas para todos os períodos do ano.
3. Regra de fim de semana/feriado da lei (ex.: ES: Seguros Sociales recuam; Modelo 190 foi para 02/02).
4. Separar por porte ou regime do empregador (ex.: retenção mensal × trimestral).
5. Incluir feriados e eventos anuais (declarações anuais, mudanças de teto/alíquota com vigência).
6. Comparar linha a linha baseline × publicado (data, frequência, aplicabilidade): só no baseline = alerta faltando; só na ferramenta = precisa de fonte.
- A ferramenta é lida pelo Claude in Chrome, **sem alterar nada** sem ok do usuário. Base: `rascunhos/2026-10-19-compliance-calendar-ES-conferencia.md`, `rascunhos/2026-10-20-resposta-shruti-alerts.md`.

## Regras desta frente
- Nada vai a Drive, monday, ticket, e-mail ou chat sem ok do usuário nesta janela. Nunca enviar.
- Google (Gmail, Chat, Drive, Docs, Sheets) só pelo Claude in Chrome, conta wgomes@mercans.com.
- `~/mercans-pipeline` não tem remote: backup antes de instalar ou atualizar qualquer coisa ali; não mexer no resto do pipeline.
- Bloco de prova em toda entrega (pedido → resposta, fontes, teste, confiança).
- Subagentes baratos (Sonnet/Haiku) para coleta mecânica.

## O que esta janela escreve
Só o seu `estado.md`, as pastas de alerta em `Research Pipeline/<País>/` e, com Edit pontual (reler antes), os hubs `paises/<País>.md` e `log.md`. "Fecha a sessão": `sessoes/AAAA-MM-DD-alertas.md`. Sem commit. Não mandar resumo à janela geral (o painel lê cada rodada sozinho); SendMessage à geral só para pedir commit ou coordenação entre frentes.

Ligações: [[00-INDEX]] · [[research-pipeline]] · [[lei-x-mercado]] · [[correcoes]] · [[fronteiras]]
