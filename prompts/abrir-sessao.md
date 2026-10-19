# Prompt: abrir sessão

> Colar no início de **toda** sessão do Claude Code nesta pasta. Trocar `<FASE/FONTE>` ou deixar em branco para o Claude propor.
> Plano: [[PLANO]] · Regras: [[CLAUDE]]

---

```
Sessão do Brain Service. Foco de hoje: <FASE/FONTE, ex.: "Fase 1" ou "F1 monday" — ou deixe que você propõe>.

Antes de qualquer ação:
1. Leia CLAUDE.md, PLANO.md (inteiro) e correcoes.md.
2. Mostre o Painel de progresso (PLANO §10) e diga em 3 linhas: onde estamos, o que bloqueia, o que você recomenda para hoje.
3. Confirme comigo: a fase/fonte, o prompt que vai seguir (PLANO §5) e o critério de saída dela.
4. Liste as decisões da Fase 0 que esta fase precisa e que ainda estão em aberto. Se alguma bloquear, pare e pergunte.

Regras desta sessão:
- Uma fase/fonte só. Assunto novo → PLANO §11, não desvio.
- Padrão de dado sólido (PLANO §3): todo cartão com nível A/B/C/D, chave PAÍS | ARTEFATO | ITEM e caminho em raw/.
- Inventário antes de extrair (PLANO §4). Nada é ingerido sem a minha validação (100% dos de risco alto + 10% dos demais).
- Só leitura nas ferramentas da Mercans (monday, Chrome, YouTrack).
- Na dúvida, pergunte. Não complete lacunas.
- Tarefas mecânicas em subagentes Sonnet/Haiku; você coordena e revisa.

Ao terminar: métricas no inventário, linha no log.md, painel atualizado, commit + push e um resumo
(o que entrou · o que ficou em dúvida · próximo passo).
```
