# Prompt: F2, extração do YouTrack / HRBlizz

> Usar no Claude Code. Script: `scripts/youtrack_fetch.ps1` (ver `scripts/LEIA-ME.md`). **Só leitura** (a API é usada só com GET).
> Escopo: tickets criados ou atualizados de 2026-01-01 até a data da coleta. Plano: [[PLANO]] §3, §4, §5 F2.
> Pré-requisito: decisão 0.6 (nome da variável do token no `.env`). **Nunca ler nem exibir o `.env`.**

## Por que a consulta precisa mudar
O padrão do script é `for: me updated: <Since> .. Today`, ou seja, só os tickets atribuídos ao usuário. O histórico do serviço inclui tickets em que respondemos sem ser o responsável (HRBS-, CT-, SR-). O inventário define a consulta certa em duas etapas.

## Prompt

```
F2 do PLANO: YouTrack. Só leitura. Escopo 2026-01-01 → hoje.

PASSO 1. Inventário (DryRun; nada é gravado)
Rode, uma de cada vez, e mostre a contagem de cada uma:
  a) .\scripts\youtrack_fetch.ps1 -TokenVar <VAR> -DryRun -Query "for: me updated: 2026-01-01 .. Today"
  b) .\scripts\youtrack_fetch.ps1 -TokenVar <VAR> -DryRun -Query "commenter: me updated: 2026-01-01 .. Today"
  c) .\scripts\youtrack_fetch.ps1 -TokenVar <VAR> -DryRun -Query "project: HRBS, CT, SR updated: 2026-01-01 .. Today"
     (se a (c) passar de ~1.500, quebre por mês ou por projeto e mostre os números)
Proponha a consulta final: o objetivo é cobrir TODO ticket em que Compliance perguntou, respondeu ou entregou,
sem trazer os milhares de tickets de outros times. Sugestão de ponto de partida: (a) ∪ (b) ∪ os tickets da (c)
que citam Compliance/CCG/WTC/DD/spec. PARE para eu aprovar a consulta.
Grave a lista aprovada (ID, projeto, título, estado, criado, resolvido, país inferido do título) em
inventarios/youtrack.md. Marque os 58 tickets já ingeridos (raw/tickets/txt-utf8/) como "já ingerido em 2026-10-02"
(eles não são reextraídos, salvo se tiveram atividade depois de 2026-09-29).

PASSO 2. Coleta
- Rode o script com a consulta aprovada (sem -DryRun). Ele grava em raw/tickets/api/AAAA-MM-DD/<ID>.md + _indice.md.
- Confira: arquivos gravados = itens do inventário. Liste as falhas (timeout, 403) e rode de novo só essas.

PASSO 3. Extração em cartões → extracoes/AAAA-MM-DD-youtrack-<lote>.md
Lotes por país (ou país × trimestre se o país tiver > 40 tickets). Subagentes Sonnet, um por lote, com estas regras:
- Para cada ticket: tipo (pergunta de compliance / defeito em spec / pedido de artefato / handover / outro time),
  país, artefato, o que foi perguntado, o que NÓS respondemos (com data), se a resposta se manteve.
- Sinais de ERRO NOSSO (viram cartão "erro+causa", candidato a correcoes.md):
  autocorreção nossa em comentário posterior; BA/Dev apontando defeito na spec que entregamos; ticket reaberto;
  "Here should be..."; versão nova do artefato por causa do ticket; resposta contestada com fonte.
- Decisão: quem decidiu, quando e em que comentário. Versão: artefato + versão + data citados.
- Nível: B se o ticket está Resolved e a resposta foi aceita; C se está aberto ou não houve fecho; A só se
  o comentário cita a lei/fonte oficial (registre a fonte A, não o ticket).
- Chave PAÍS | ARTEFATO | ITEM. Procure em correcoes.md, no hub e em extracoes/ antes de criar.
- Ticket sem nada que mude a resposta certa → "descartado: <motivo>" no inventário (ex.: só acknowledgment,
  pedido de acesso, duplicado de <ID>).
- Sem dados pessoais (nomes ou IDs de funcionários de cliente → [omitido]).
Você revisa os cartões dos subagentes: confira por amostra a citação no raw e se o tipo e o nível estão certos.

PASSO 4. Validação → 100% dos cartões de risco alto + 10% sorteados dos demais. Espere ✔/✘.

PASSO 5. Ingestão e fechamento
- Hubs: seção Suporte (Data | Ticket | Assunto | Resolução | Mudou artefato?), Decisões, Artefatos (versão).
- correcoes.md: erros nossos confirmados. Correção nova → pergunta no Conjunto B.
- servicos/suporte.md: padrões recorrentes novos (≥ 3 tickets com o mesmo padrão).
- Métricas em inventarios/youtrack.md e no painel. Registre a data da coleta como "-Since" da próxima rotina.
- log.md, commit + push. Resumo: tickets por país · erros nossos encontrados · padrões · perguntas para mim.
```
