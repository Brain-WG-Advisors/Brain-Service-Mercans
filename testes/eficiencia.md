# Eficiência das conversas (medida semanal)

> Rodar `python scripts/medir_eficiencia.py` toda semana (sugestão: ao "abrir o dia" de segunda) e acrescentar a linha nova. Origem: análise dos prompts [[revisoes/2026-10-27-padroes-prompts|2026-10-27]]; regras aplicadas no [[CLAUDE]] ("Respostas eficientes") em 2026-10-27. Exatidão: [[testes/exatidao]].
> Contagem por expressões regulares (ordem de grandeza). "Checagem de confiança" = o usuário teve de perguntar "100%?/tem certeza?"; "aprovação pura" = "sim/ok/pode/próximo" sem mais nada.

## Linha de base (antes das regras de 27/10)
| Semana | Mensagens | Conversas | Msgs/conversa | Checagem de confiança | Correção | Aprovação pura |
|---|---|---|---|---|---|---|
| 2026-S41 | 160 | 13 | 12 | 4 (2%) | 2 (1%) | 5 (3%) |
| 2026-S42 | 447 | 20 | 22 | 68 (15%) | 12 (3%) | 30 (7%) |
| 2026-S43 | 761 | 16 | 48 | 64 (8%) | 20 (3%) | 74 (10%) |
| 2026-S44 (até 27/10) | 312 | 6 | 52 | 21 (7%) | 11 (4%) | 65 (21%) |

## Meta (a partir de 2026-S45)
- Checagem de confiança: abaixo de 2% (o bloco de prova responde antes da pergunta).
- Aprovação pura: abaixo de 8% (fazer sem perguntar em lista aprovada).
- Correção: abaixo de 2%.

## Medições depois das regras
| Semana | Mensagens | Conversas | Msgs/conversa | Checagem de confiança | Correção | Aprovação pura |
|---|---|---|---|---|---|---|
