# Teste de exatidão

> Arquivo: `testes/exatidao.md`. Roda **no claude.ai**, onde o time trabalha. Ver [[PLANO]] §7 e [prompts/fase-1-linha-de-base.md](../prompts/fase-1-linha-de-base.md).
> **Conjunto A** = 30 perguntas de [[correcoes]] (Fase 1). **Conjunto B** = correções novas da coleta (Fase 3). **Conjunto C** = ~20 perguntas **cegas**, de tickets resolvidos depois da data do MVP, em quarentena (não ingeridos até a medição final).
> Cada pergunta roda **2 vezes** (`T-xxx-r1.md`, `T-xxx-r2.md` em `testes/rodadas/AAAA-MM-DD/`). Duas ✅ = ✅; divergência = ⚠️ instável (não conta como acerto). Um ❌ vira ação com dono; não basta anotar.
> **Este arquivo nunca sobe para o Projeto do claude.ai** (o gabarito vazaria).

## Perguntas (colar só a coluna Pergunta)
| # | Conj. | País | Tipo (V/M/R/P) | Pergunta |
|---|---|---|---|---|
| T-001 | A | [[Espanha]] | M | |

## Gabarito (não colar no claude.ai)
| # | Resposta correta | Fonte (nível) | ✅ se... | ⚠️ se... | ❌ se... / erro conhecido | Origem |
|---|---|---|---|---|---|---|
| T-001 | | | | | | [[correcoes]] AAAA-MM-DD |

## Rodadas
| Data | Rodada | Configuração (projeto/skills ativos) | Conj. | ✅ | ⚠️ (instável) | ❌ | Nota | Repetiu erro conhecido |
|---|---|---|---|---|---|---|---|---|
| AAAA-MM-DD | 1: linha de base | claude.ai com skills, sem projeto | A | | | | X/30 | N |

## Resultado por pergunta
| # | Rodada 1 | Rodada 2 | Causa do ❌/⚠️ (falta no brain / falta na skill / erro do modelo / gabarito) | Ação · dono · data |
|---|---|---|---|---|
| T-001 | | | | |

## Quarentena do Conjunto C (data de corte = data do MVP: AAAA-MM-DD)
| # | Ticket | Resolvido em | País | Pergunta derivada | Ingerir depois de |
|---|---|---|---|---|---|
| C-001 | | | | | medição final |
