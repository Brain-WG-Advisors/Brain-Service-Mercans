# Brain Service — Cérebro do Serviço

Este é o cérebro do **serviço que prestamos para a Mercans** (compliance de payroll). Não é o cérebro da Mercans inteira: cobre só o que entregamos e sustentamos.

Responda e escreva sempre em **português do Brasil** (termos técnicos e nomes de artefatos podem ficar em inglês).

## O serviço (escopo)
```
[1. Research Pipeline] → [2. Design] → (Produção / ativação: outro time) → [3. Suporte]
        nosso                nosso            FORA DO ESCOPO                 nosso
```
- **Research Pipeline:** pesquisa estatutária do país e geração dos artefatos (CCG, WTC, DD, Report Specs, SIR...).
- **Design:** o que é desenhado a partir do research (detalhar em `servicos/design.md`).
- **Suporte:** tickets e dúvidas sobre os artefatos que entregamos.
- O que é de outros times fica em `fronteiras.md`. Não documente o trabalho de outros times além da fronteira.

## Início de toda sessão
Ler o `PLANO.md` (modelo de construção e painel de progresso) e seguir o Protocolo de sessão dele: uma fase ou fonte por sessão; ao final, log, painel, commit e resumo.

## Estrutura da pasta
| Caminho | O que é |
|---|---|
| `00-INDEX.md` | Centro do cérebro: catálogo do serviço + painel países × etapa. |
| `servicos/` | Uma nota por serviço: o que recebemos, o que entregamos, como sabemos que ficou certo, o que já deu errado. |
| `paises/<País>.md` | Hub do país: etapa atual, artefatos e versões, decisões, valores com vigência, tickets. |
| `correcoes.md` | Erros já cometidos e a versão correta. **Ler antes de qualquer resposta.** |
| `fronteiras.md` | O que não é nosso e para quem vai. |
| `raw/` | Material bruto (exportações de chats, tickets, documentos). **Nunca editar nem apagar.** `raw/reunioes/` e `raw/drive/` ficam fora do git. |
| `extracoes/` | Cartões extraídos de cada coleta (o filtro entre `raw/` e as notas). |
| `testes/` | Teste de exatidão rodado no claude.ai (antes × depois). |
| `revisoes/`, `rascunhos/` | Relatórios de revisão e rascunhos de resposta/pacotes (não enviados). |
| `scripts/` | Scripts de coleta (ex.: `youtrack_fetch.ps1`). |
| `modelos/` | Modelos de nota. Usar sempre ao criar nota nova. |
| `prompts/` | Prompts prontos (ex.: extração de conhecimento dos projetos do Claude). |
| `log.md` | Registro cronológico, só acrescentar no fim. |
| `PLANO.md` | Plano de ação de implantação. |
| `_arquivo/` | Projeto antigo (automação Trello). Não faz parte do cérebro; não ler, salvo pedido. |

## Comandos
Quando o usuário disser:

- **"ingere isto" / "ingere raw/..."**
  1. Ler o material (se veio colado no chat, salvar antes em `raw/<tipo>/AAAA-MM-DD-<assunto>.md`).
  2. Extrair: decisões, regras, valores (com vigência + fonte), erros corrigidos, pendências, quem pediu.
  3. Atualizar as notas afetadas (país, serviço, `correcoes.md`), criando a partir de `modelos/` quando não existirem.
  4. Ligar tudo com `[[links]]` e atualizar `00-INDEX.md`.
  5. Registrar em `log.md` o que entrou e quais notas mudaram.
  6. Listar ao usuário o que foi alterado e o que ficou em dúvida (não inventar para preencher lacunas).

- **"responde X" / qualquer pergunta sobre o serviço**
  1. Ler `correcoes.md`.
  2. Procurar no cérebro (`paises/`, `servicos/`) e nas skills Mercans (abaixo).
  3. Responder citando a nota/fonte. Se o cérebro não tiver a informação, dizer isso claramente.
  4. Se a resposta gerou conhecimento novo, perguntar se deve ser registrado.

- **"fechei o ticket X" / "entreguei Y"** (registro no fluxo de trabalho, método KCS)
  1. Registrar no hub do país (seção Suporte ou Histórico) com data, ID e resumo.
  2. Se o ticket revelou erro em artefato ou resposta anterior → entrada em `correcoes.md`.
  3. Se mudou artefato → atualizar versão no hub do país.
  4. Linha em `log.md`.

- **"revisa o cérebro"** (lint)
  Procurar: contradições entre notas, valores sem vigência ou sem fonte, notas sem links (órfãs), links quebrados, países com etapa desatualizada, `correcoes.md` que já deveriam ter ido para as skills. Entregar um relatório; só corrigir com aprovação.

## Regras
1. **Todo valor estatutário** (alíquota, teto, faixa, prazo) leva **vigência** (`a partir de AAAA-MM-DD`) e **fonte** (lei/site oficial/documento). Valor sem fonte é marcado `⚠️ sem fonte`.
2. **Nunca sobrescrever valor antigo:** quando muda, a linha antiga recebe data de fim e a nova é acrescentada.
3. **Sem dados pessoais** de funcionários de clientes (nomes, IDs, salários individuais). Usar só o necessário: país, cliente (se preciso), ID do ticket.
4. **Não duplicar as skills.** As skills `payroll-compliance-<país>`, `mercans-pipeline-methodology` e `mercans-compliance-workflow` já têm o conhecimento estatutário e o método. O cérebro guarda o que falta nelas: decisões, histórico de entregas, tickets, correções, estado de cada país. Quando precisar do conteúdo da skill, **linkar/citar** em vez de copiar.
   - **Exceção: "Ficha do país (da skill)"** no hub (decidido em 2026-10-02): resumo curto do que mais importa para nós (escopo e ano fiscal, armadilhas confirmadas, o que mais dá errado, lacunas abertas, relatórios principais), extraído do `SKILL.md` e do `07-qa-report.md`. Leva a data de leitura da skill. Tabelas completas (alíquotas, faixas, WTC, DD) continuam só na skill; para responder com valor exato, ler a skill. Se ficha e skill divergirem, vale a skill e a ficha é atualizada.
5. **Na dúvida, perguntar.** Não completar lacunas com suposição.
6. Notas em Markdown, nomes de arquivo sem acento e com hífen (`paises/Belgica.md`), links no formato `[[Belgica]]`.
7. `raw/` é imutável; `log.md` só cresce.
8. **Versão vigente de artefato = a de maior número de versão** (a planilha/arquivo com a atualização mais recente). Ex.: WTC Espanha V4.4. Quando fontes citarem versões diferentes, registrar a maior como vigente e as outras como histórico. (decidido em 2026-10-05)

## Fontes de conhecimento
| Fonte | Como entra |
|---|---|
| Projetos do Claude da Mercans (pipeline, compliance research, Design & Development, tickets) | Usuário cola `prompts/extracao-projeto.md` em cada projeto e salva a resposta em `raw/chats/`. |
| YouTrack (`https://youtrack.hrblizz.dev`) | `scripts/youtrack_fetch.ps1` (ver `scripts/LEIA-ME.md`). Token fica no `.env` da raiz: **nunca ler, exibir ou copiar o `.env`.** |
| monday | Conector do claude.ai (só leitura). Boards e o que coletar: `PLANO.md` 4.2. |
| Skills Mercans/país | Consultar via Skill quando necessário; não copiar. |
| Google (Drive, Meet/transcrições) | Sem conector (bloqueio da Mercans). Coleta pelo Claude in Chrome, só leitura, depois do ok do chefe: `prompts/coleta-chrome.md`. |
