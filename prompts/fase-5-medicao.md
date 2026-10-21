# Prompt: Fase 5, medição final (e rodadas de MVP)

> Usar no Claude Code. Plano: [[PLANO]] §6 Fase 5 e §7. A Parte 1 também serve para a **rodada 2 do Conjunto A no MVP** (Fase 2).
> Pré-requisitos: projeto publicado com todas as fontes ingeridas; Conjunto C com ~20 perguntas em quarentena; KPIs K1–K4 com linha de base.

## Parte 1: preparar a rodada (Claude Code)

```
Fase 5 do PLANO: preparar a rodada <final | MVP>.
1. Congele o teste: testes/exatidao.md no commit atual (anote o hash). Nenhuma pergunta ou gabarito muda depois disso.
2. Confira a quarentena C: nenhum ticket do Conjunto C foi ingerido (procure os IDs em paises/, correcoes.md e extracoes/).
   Se algum vazou, tire a pergunta do C, registre o motivo e não substitua na mesma rodada.
3. Gere testes/rodadas/AAAA-MM-DD-perguntas.txt: A (30) + B (todas) + C (todas), numeradas, sem o conjunto
   indicado (ordem embaralhada, para eu não saber de qual conjunto é cada uma).
4. Anote a configuração: Projeto "Brain Service" (versão das instruções = hash de prompts/projeto-claude-ai.md),
   data do último sync do pacote e skills ativas (com a data de republicação das que receberam pacote).
```

## Parte 2: rodar e corrigir

**Usuário (ou Claude in Chrome):**
- Dentro do Projeto "Brain Service", um chat novo por pergunta, **2 vezes cada uma**.
- Respostas inteiras em `testes/rodadas/AAAA-MM-DD/T-xxx-r1.md` e `-r2.md`.

**Claude Code:**

```
Corrija a rodada testes/rodadas/<AAAA-MM-DD>/ (protocolo de prompts/fase-1-linha-de-base.md, Parte 3).
Depois:
1. Totais por conjunto (A, B, C), por país e por tipo (V/M/R/P). Instáveis à parte.
2. Comparação com as rodadas anteriores do A (1 = sem brain; 2 = MVP).
3. Para cada ❌ e ⚠️ instável, a causa, com evidência:
   FALTA NO BRAIN (a informação não estava no pacote) · FALTA NA SKILL (pacote não aplicado ou skill antiga) ·
   ERRO DO MODELO (a informação estava lá e foi ignorada ou mal lida; cite onde estava) · GABARITO (o gabarito é que
   está errado; vai para decisão minha).
   E a ação: o que muda (nota, instrução do projeto, pacote de skill), dono e data.
4. Erros conhecidos repetidos: quais e onde estavam documentados.
```

## Parte 3: KPIs e relatório

```
1. Atualize testes/kpis.md até o mês corrente. Compare: linha de base (2026-01 a 2026-10) × meses após o MVP.
   Atenção a efeito sazonal (ex.: fim de ano fiscal) e a mudanças de volume: mostre também os valores absolutos.
2. Preencha modelos/relatorio-patrocinador.md → rascunhos/AAAA-MM-DD-relatorio-<final|mvp>.md.
   Recomendação ao patrocinador, com base nas metas da 0.8:
   - metas atingidas → MANTER E ESCALAR (rotina + próximos países/skills);
   - A ok e C abaixo da meta → AJUSTAR (o brain sabe o que viu, mas não generaliza: revisar instruções e cobertura);
   - A abaixo da meta → CORRIGIR PUBLICAÇÃO (o conhecimento não está chegando: sync, instruções, skills);
   - nenhuma melhora e KPIs parados → ENCERRAR ou repensar (com as causas).
3. log.md, painel do PLANO, commit + push. Mostre o rascunho do relatório para eu revisar antes de enviar.
```
