# Prompt: Fase 6, rotina (semanal e mensal)

> Usar no Claude Code. Plano: [[PLANO]] §6 Fase 6. Meta: **~20 min do usuário por semana**. O Claude faz a coleta e a extração; o usuário valida e decide.
> Começa depois da medição final. Durante a construção, use a versão semanal só para YouTrack + monday, para não acumular atraso.

## Semanal (sugestão: segunda-feira)

```
Rotina semanal do Brain Service. Data da última rotina: <AAAA-MM-DD> (veja o log.md se eu não disser).

1. YouTrack: .\scripts\youtrack_fetch.ps1 -TokenVar <VAR> -Since <última data> -Query "<consulta aprovada em inventarios/youtrack.md>"
   → inventário curto → cartões (regras de prompts/extracao-youtrack.md, Passo 3).
   Enquanto o Conjunto C tiver menos de 20 perguntas, proponha até 2 tickets resolvidos para a quarentena C
   (eles NÃO são ingeridos agora).
2. monday (só leitura): itens novos ou alterados desde a última data no RCA (18396554143) e no board de alertas
   vigente (decisão 0.10) → cartões (regras de prompts/extracao-monday.md).
3. Pipeline (se o cenário 1 da 0.7): git pull no clone e resumo dos commits → cartões de "versão final" e "erro+causa".
4. Registros "fechei o ticket X" da semana sem hub atualizado → completar.
5. Validação: 100% dos de risco alto + 10%, num lote só (meta: ≤ 15 cartões por semana). Espere ✔/✘.
6. Ingestão → publicação incremental no Projeto (sync/upload dos arquivos alterados) → pergunta no Conjunto B
   para cada correção nova → pacote de skill se houver correção estatutária.
7. log.md ("AAAA-MM-DD | rotina | ..."), painel do PLANO, commit + push. Resumo em 5 linhas.
Se a semana passar de 40 cartões, avise: é sinal de mudança grande (lei nova, país novo) e pede uma sessão própria.
```

## Mensal (primeira segunda-feira do mês)

```
Rotina mensal do Brain Service.
1. KPIs K1–K4 do mês anterior em testes/kpis.md (definições congeladas no próprio arquivo).
2. Rodada de manutenção do teste: 10 perguntas sorteadas do A + todas do B criadas no mês, 2 vezes cada,
   no Projeto. Os ❌ viram ação (prompts/fase-5-medicao.md, Parte 2, passo 3).
3. "Revisa o cérebro" (lint de prompts/fase-4-consolidacao.md, Passo 2): só o relatório, aplicação depois da aprovação.
4. Pacotes de skill pendentes há mais de 30 dias: lista para cobrar o dono das skills.
5. Relatório de meia página ao patrocinador (modelos/relatorio-patrocinador.md, versão curta), se ele pediu acompanhamento mensal.
6. log.md, painel, commit + push.
```
