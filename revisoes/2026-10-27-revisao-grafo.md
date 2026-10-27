# Revisão do grafo (Fase R, passo 2), 2026-10-27

> Plano: [[PLANO]] Fase R · Índice: [[00-INDEX]] · Log: [[log]]
> Método: script sobre todos os `.md` do vault, resolvendo `[[links]]` como o Obsidian (pelo nome do arquivo). Fora da contagem: `raw/`, `_arquivo/`, `.git`, `02-client-reports-raw/`, `99-local-only/`.
> **Só diagnóstico: nada foi corrigido.** Correções com aprovação.

## Números
| Medida | Valor |
|---|---|
| Notas `.md` no vault | 1.378 |
| Links `[[ ]]` resolvidos | 1.437 |
| Notas sem nenhum link (nem entra, nem sai) | 1.152 |
| Notas que ligam para fora, mas ninguém liga para elas | 123 |
| Nomes de link quebrados | 8 |
| Nomes ambíguos (mesmo nome de arquivo em 2+ lugares) | 268 |

**Leitura:** a camada de conhecimento (00-INDEX, correcoes, fronteiras, 50 hubs, 4 serviços) está ligada. Quase todas as 1.152 notas sem link são arquivos de trabalho, não conhecimento:

| Pasta | Notas sem link |
|---|---|
| `frentes/` (214 no espelho `frentes/pipeline/mercans-pipeline`) | 513 |
| `Research Pipeline/` | 194 |
| `fr-research-validation/` | 175 |
| `rascunhos/` | 131 |
| `testes/` | 61 |
| `internal-certification/` | 57 |

## Achados, por prioridade

### 1. Cópias dentro do vault confundem o grafo (alta)
- **Achado:** `publicar/2026-10-27/` é uma cópia de 57 notas (00-INDEX, correcoes, fronteiras, serviços, hubs).
- **Efeito:** o Obsidian vê dois `correcoes`, dois `00-INDEX` etc. Links como `[[research-pipeline]]`, `[[suporte]]` e `[[design]]` podem cair na cópia.
- **Medida:** na contagem, a cópia de `publicar/` aparece com 110 ou mais ligações de entrada, no lugar da nota de `servicos/`.
- **Outras cópias:**
  - `frentes/pipeline/mercans-pipeline` (atalho para `~/mercans-pipeline`) e `fr-research-validation/` repetem os changelogs da França.
  - `entregas/` repete `Research Pipeline/Costa do Marfim`.
- **Proposta:** no Obsidian, em Settings → Files and links → **Excluded files**, excluir:
  - `publicar/`
  - `frentes/pipeline/mercans-pipeline/`
  - `fr-research-validation/`
  - `raw/`
  - `_arquivo/`

  Isso não apaga nada. Só tira essas pastas do grafo e da busca.

### 2. Hubs sem ligação com o resto da rede (alta) ✅ resolvido em 2026-10-27

**Correção do diagnóstico (recontagem sem as cópias do item 1):**
- O item 2 abaixo estava superestimado. Com `publicar/` no vault, o script resolveu `[[research-pipeline]]`, `[[design]]` e `[[suporte]]` para a cópia.
- **Todos os hubs já ligam para os serviços**, pela tabela "Situação".
- `correcoes.md` liga para os **18 países que têm correção**. Os outros 32 hubs não têm entrada lá, então não falta link.
- Faltava só: 42 hubs sem `[[fronteiras]]` e 7 sem `[[correcoes]]`.
- **Feito:** a linha 3 (cabeçalho) de 43 hubs recebeu ` · Correções: [[correcoes]]` e/ou ` · Fronteiras: [[fronteiras]]`, e `modelos/pais.md` recebeu a mesma linha.
- **Recontagem:** 0 hubs com lacuna (só `paises/README.md`, que não é país).
- Recontagem sem as cópias: 640 notas, 927 links, 470 notas sem link (a maioria de trabalho).

Texto original (antes da recontagem):
- **Serviços:** 49 dos 49 hubs de país não ligam para nenhuma nota de `servicos/`. Só o README, que não é país, foge a esse padrão.
- **Fronteiras:** 43 hubs não ligam para [[fronteiras]].
- **Correções:** 7 hubs não ligam para [[correcoes]]: Austrália, China, Índia, Kuwait, Romênia, Tailândia e Vietnã.
- **Volta das correções:** [[correcoes]] liga só para 18 hubs. Os 32 hubs abaixo não recebem link de lá. É preciso conferir se eles têm entrada em correcoes e só falta o link, ou se não têm erro registrado:
  - África do Sul, Alemanha, Austrália, Bahrein, Belarus, Botsuana, China, Chipre, Costa Rica, Dinamarca
  - Estônia, Filipinas, Finlândia, Guiné Equatorial, Índia, Indonésia, Kuwait, Líbano, Malásia, Marrocos
  - Moçambique, Namíbia, Noruega, Portugal, RD Congo, Romênia, Singapura, Suécia, Tailândia, Tchéquia, Vietnã
- **Proposta:** acrescentar em cada hub uma linha fixa de navegação, a partir de `modelos/pais.md`:
  - `Serviços: [[research-pipeline]] · [[design]] · [[suporte]] · [[analise-reports]] · Fronteiras: [[fronteiras]] · Correções: [[correcoes]]`
  - Em `correcoes.md`, ligar cada entrada ao hub do país.

### 3. Entregas e conferências fora da rede (alta)
As pastas de entrega têm um `CONFERENCIA.md` (regra de 16/10 do [[CLAUDE]]), mas nenhum hub liga para elas. Casos de 2026-10:
- **Bélgica:** 3 entregas: specs em inglês, refresh da skill, WTC 62/65/74.
- **Egito:** fundo dos mártires.
- **Singapura:** HRBS-16029 (CPF).
- **Taiwan:** SR-110.
- **Argélia:** HRBS-3466 (DAS v2.2).
- **Colômbia:** a auditoria do lote 1 está ligada? Conferir.

**Proposta:** no hub, seção "Entregas" com uma linha por entrega: data, ID e link para o `CONFERENCIA.md`.

### 4. Países com trabalho e sem hub (média)
| País | Onde há trabalho |
|---|---|
| **Argélia** | `Research Pipeline/Algeria/` (HRBS-3466) |
| **Taiwan** | `Research Pipeline/Taiwan/` (SR-105 a SR-110, hoje). Já existe um link `[[Taiwan]]` quebrado na CONFERENCIA. |
| **Cazaquistão** | `internal-certification/references/Kazakhstan/` |

**Proposta:** criar o hub a partir de `modelos/pais.md`, com os itens que já existem. A Dinamarca, a Noruega e a Suécia têm hub e também têm pasta em `internal-certification`. Falta o link do hub para essas pastas.

### 5. Notas de conhecimento que ninguém liga (média)
- **`extracoes/`:** 8 arquivos, entre eles os cartões do pipeline de 27/10 (BE, CO, FR) e o `VALIDACAO`. Proposta: ligar a partir de [[PLANO]] (painel F6) e de cada hub.
- **`revisoes/`:** 5 relatórios (2026-10-05, catálogos de erros de 08/10 e 09/10, matriz FR, gabarito T001/T003/T024). Proposta: ligar a partir de [[00-INDEX]] ou de [[correcoes]].
- **`frentes/*/estado.md`** e **`sessoes/`:** 5 sem entrada. Proposta: ligar a partir de [[ESTADO]] e de [[rotinas]].
- **`rascunhos/`:** 131 sem link. É normal, porque são rascunhos. Ligar só os que viraram decisão.

### 6. Links quebrados (baixa)
| Link | Onde | O que fazer |
|---|---|---|
| `[[NEEDS-ARTEFACT]]` (29) | arquivos do pipeline | É marcador de texto do pipeline, não link. Some com a exclusão do item 1. |
| `[[{{Pais}}]]`, `[[País]]` | `modelos/` | Esperado (modelo). |
| `[[Taiwan]]` | CONFERENCIA SR-110 | Resolve com o hub novo (item 4). |
| `[[certificacao-so-validar]]`, `[[cem-por-cento-antes-de-apresentar]]`, `[[trello-atalhos-teclado]]` | sessão de 21/10 (gmail) e rascunho de 20/10 | Apontam para memórias do Claude, que ficam fora do vault. Trocar por texto ou por regra do CLAUDE.md. |
| `[[servicos]]` | PLANO.md (Fase R) | ✅ Corrigido agora (erro meu ao escrever a Fase R). |

### 7. Nomes repetidos (baixa)
- `CLAUDE.md` aparece 4 vezes, `estado.md` 5 vezes, `CONFERENCIA.md` em cada entrega e `README`/`sources` em várias pastas.
- Dentro de pastas, é o padrão e não atrapalha. Só atrapalha quando alguém escreve `[[CONFERENCIA]]` ou `[[estado]]` sem o caminho.
- **Proposta:** nesses casos, linkar com o caminho, por exemplo `[[frentes/suporte/estado]]`.

## Ordem sugerida das correções
1. Excluir as cópias no Obsidian (item 1). São 5 minutos, feitos por você nas configurações do Obsidian.
2. Linha de navegação nos 49 hubs, mais o link de cada entrada de `correcoes.md` para o hub (item 2). Edição mecânica, com conferência.
3. Seção "Entregas" nos hubs com `CONFERENCIA.md` (item 3).
4. Hubs novos: Argélia, Taiwan e Cazaquistão (item 4).
5. Links de entrada para `extracoes/`, `revisoes/`, `estado.md` e `sessoes/` (item 5) e os links quebrados restantes (item 6).
