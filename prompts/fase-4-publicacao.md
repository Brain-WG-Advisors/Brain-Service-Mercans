# Prompt: Fase 4, publicação no claude.ai

> Usar no Claude Code. Plano: [[PLANO]] §5 Fase 4. Pré-requisitos: decisões 0.3 (quem publica as skills) e 0.4 (GitHub nos Projetos).
> Dois destinos: **(a) Projeto "Brain Service"** (estado, decisões, histórico, correções) e **(b) skills de país** (conteúdo estatutário corrigido).

## Pacote do projeto (o que sobe e o que não sobe)
| Sobe | Por quê |
|---|---|
| `correcoes.md` | Fonte nº 1 das instruções |
| `paises/*.md` (todos os hubs) | Estado, versão vigente, decisões, tickets |
| `servicos/*.md`, `fronteiras.md`, `00-INDEX.md` | Como o serviço funciona e o que não é nosso |

| **Não** sobe | Por quê |
|---|---|
| `raw/`, `extracoes/`, `inventarios/` | Material bruto e de trabalho; confunde e pode ter dado sensível |
| `testes/` | O gabarito não pode vazar para o modelo testado |
| `rascunhos/`, `revisoes/`, `PLANO.md`, `log.md`, `CLAUDE.md`, `prompts/`, `scripts/` | Coisas da oficina |

Tamanho em 2026-10-19: cerca de 70 mil palavras (cabe no conhecimento de um Projeto).

## Prompt

```
Fase 4 do PLANO: publicação no claude.ai.

PASSO 1. Pré-checagem do pacote
- Confira se os arquivos do pacote (tabela "Sobe" de prompts/fase-4-publicacao.md) não têm: dado pessoal de
  funcionário de cliente, token/chave, link para raw/ ou para extracoes/ (troque por "fonte: <ticket/doc>").
- Confira se correcoes.md e os hubs estão coerentes (resultado da Fase 3). Liste o que bloquear.
- Meça palavras e arquivos. Se GitHub (0.4) = sim: diga quais pastas selecionar no "Add content → GitHub".
  Se não: gere publicar/AAAA-MM-DD/ com cópia exata dos arquivos do pacote (fora do git, para upload manual).

PASSO 2. Instruções do projeto
- Mostre o texto de prompts/projeto-claude-ai.md para eu colar em Instructions. Não mude sem me mostrar a diferença.

PASSO 3. Pacotes de correção por skill
- Para cada país, liste as correções de correcoes.md e os cartões confirmados que AINDA NÃO estão na skill
  payroll-compliance-<país> (consulte a skill para conferir item a item).
- Gere rascunhos/AAAA-MM-DD-pacote-skill-<PAIS>.md no formato do pacote da Ucrânia
  (rascunhos/2026-10-05-pacote-skill-UA.md): arquivo da skill afetado (SKILL.md / references/xx.md), trecho
  atual, trecho proposto, fonte nível A e origem.
- Ordene os países pelo número de correções de risco alto. Entregue a quem publica as skills (decisão 0.3).

PASSO 4. Teste de fumaça (depois que eu montar o projeto)
- Gere 5 perguntas (fora dos Conjuntos A e B) que só se acertam lendo correcoes.md e um hub, e o critério
  de cada uma. Eu rodo no projeto e colo as respostas; você corrige. Aprovação = 5/5 citando a fonte.

PASSO 5. Registro
- Hub de cada país com pacote entregue: "Pendências → skill: pacote de AAAA-MM-DD entregue a <quem>".
- log.md: o que subiu (commit do pacote), versão das instruções, resultado da fumaça. Painel do PLANO. Commit.
```

## Manutenção do projeto (rotina)
- A cada ingestão relevante: atualizar o pacote (GitHub: "sync"; upload: substituir os arquivos alterados).
- A cada skill republicada: rodar de novo as perguntas do Conjunto A daquele país.
