# Prompt: Fase 4, consolidação

> Usar no Claude Code. Plano: [[PLANO]] §6 Fase 4. Roda **duas vezes**: a intermediária (depois de F1 + F2) e a final (depois de F5/F6).
> Entradas: hubs, [[correcoes]], `extracoes/`, `inventarios/` e [revisoes/2026-10-05-revisao.md](../revisoes/2026-10-05-revisao.md) (37 propostas, 33 perguntas).
> Saída: `revisoes/AAAA-MM-DD-consolidacao.md` (relatório) → decisões do usuário → aplicação → pacotes por skill.
> **Nada é alterado antes da aprovação do usuário** (regra "revisa o cérebro" do [[CLAUDE]]).

## Prompt

```
Fase 4 do PLANO: consolidação <intermediária | final>. Só leitura até eu aprovar.

PASSO 1. Propostas antigas (revisão de 2026-10-05)
- Para cada uma das 37 propostas e 33 perguntas de revisoes/2026-10-05-revisao.md, diga se a coleta (F1–F6)
  já resolveu: RESOLVIDA (por qual cartão/fonte, com nível) · AINDA VALE · SUPERADA (fato novo muda a proposta).
- Para as que AINDA VALEM e são de risco alto: reapresente com a evidência atual, para eu decidir.

PASSO 2. Contradições (lint completo)
Procure e classifique por risco (alto = valor estatutário, versão vigente, correção):
- mesma chave PAÍS | ARTEFATO | ITEM com valores diferentes entre hub, correcoes.md, ficha da skill e cartões;
- valor estatutário sem vigência ou sem fonte (⚠️ sem fonte), ou com fonte só de nível C;
- versão vigente que fere a regra 8 (não é a de maior número) ou que diverge entre hub, monday (Artifacts) e Drive;
- [INCERTO] que algum cartão novo já pode resolver;
- links quebrados, notas órfãs, países do painel com etapa desatualizada em relação ao monday;
- cartões validados (✔) e ainda não ingeridos; cartões ingeridos sem registro no log.
Para cada contradição: as versões em conflito, a fonte e o nível de cada uma, o que a regra 2 do PLANO §4 indica
(A > B > C; mesmo nível → a mais recente) e a proposta. Quando a regra não resolver, pergunta para mim.

PASSO 3. Correções → skills
Para cada país, liste as entradas de correcoes.md e os cartões confirmados que AINDA NÃO estão refletidos
na skill payroll-compliance-<país>. Consulte a skill item a item e cite o arquivo e a seção.
Status por item: NA SKILL (já refletido) · FALTA NA SKILL (vai para o pacote) · CONFLITA COM A SKILL (a skill
diz outra coisa: qual tem fonte melhor?).
Ordene os países por número de itens de risco alto em FALTA/CONFLITA.

PASSO 4. Relatório → revisoes/AAAA-MM-DD-consolidacao.md
Seções: 1. Como responder (aprovo N, rejeito N) · 2. Propostas de risco alto · 3. Contradições · 4. Perguntas
de 1 linha · 5. Correções × skills por país · 6. Números (antes/depois: [INCERTO], ⚠️ sem fonte, contradições).
PARE para eu responder.

PASSO 5. Aplicação (só o aprovado)
- Regra 2 do CLAUDE: a linha antiga recebe data de fim e a nova é acrescentada. Nada é apagado.
- Gere os pacotes rascunhos/AAAA-MM-DD-pacote-skill-<PAIS>.md (formato de publicacao.md, Passo 3).
- log.md (o que mudou, quais notas), painel do PLANO, commit + push.
- Critério de saída: zero contradição aberta de risco alto e pacotes gerados para todos os países com FALTA/CONFLITA.
```
