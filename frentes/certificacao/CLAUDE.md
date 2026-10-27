# Frente 5 — Certificação - Mercans (Internal Certification / Análise de Reports)

Esta pasta é a janela **Certificação**. Vale tudo do `CLAUDE.md` da raiz do cérebro; aqui só o que é desta frente.

**Raiz do cérebro:** `C:\Users\instituto\Documents\brain-service` (`../..` daqui). Os caminhos abaixo são relativos à raiz, salvo `estado.md` (nesta pasta).
**Pasta de trabalho:** `C:\Users\instituto\Documents\internal-certification` (pacotes, validadores, workbooks). Ler o `CLAUDE.md` de lá: ele manda no método e nas regras de pasta.

## Onde está o material (ligado, não copiado)
| O quê | Onde (em `internal-certification\`) |
|---|---|
| Contexto, contatos das SBCs, regras de pasta | `CLAUDE.md` |
| Método em 8 etapas, situação, decisões, regras anti-trava | `PLANO_DE_ACAO_VALIDACOES.md` |
| Prompt de rodada ponta a ponta | `PROMPT_VALIDACOES_PONTA_A_PONTA.md` |
| Painel (Painel, Achados, Ações) | `Acompanhamento_Internal_Certification.xlsx` |
| Pacotes | `<País>\<Cliente> - <AAAA-MM>\01 Received` (imutável) e `02 Validation` |
| Validadores | `validators\<cc>\`, `Netherlands\_tool\` (nl-payroll-validator v1.5) |
| Fontes oficiais por país/ano | `references\<país>\<ano>\` + `sources.md` |
| Kit para outras máquinas | `Internal_Certification_Kit_v2_Windows.zip` |
| Correção da ponte do Chrome | `_chrome_fix\` |
| Serviço e lições | `servicos/analise-reports.md` (no cérebro) |

## Abrir a sessão (substitui o "Abrir a sessão" da raiz)
1. Ler `correcoes.md`, `frentes/certificacao/estado.md` e as últimas linhas de `log.md`.
2. Ler `internal-certification/CLAUDE.md` e `internal-certification/PLANO_DE_ACAO_VALIDACOES.md` (§2 situação, §4 decisões, §4.1 regras anti-trava).
3. Ver se chegou arquivo novo: `01 Received` de cada pacote mais novo que o `received.txt`; Gmail/Chat só pela janela da frente correspondente (pedir lá, não ler daqui).
4. Entregar um painel curto: pacote pronto para validar / esperando SBC / esperando decisão do usuário.

## Trabalho
- Método: 8 etapas do `PLANO_DE_ACAO_VALIDACOES.md` (modelo: Holanda, skill `nl-payroll-validator`). 100% dos registros, fonte primária oficial em vigor, contracheque como âncora.
- Saída de cada pacote: `<País>/<Cliente> - <AAAA-MM>/02 Validation/<CC>_<Cliente>_<AAAA-MM>_Validation.xlsx`, `followups.md` (cobranças em rascunho), resumo EN + PT.
- Painel consolidado: `internal-certification/Acompanhamento_Internal_Certification.xlsx` (abas Painel, Achados, Ações).
- Validamos e reportamos; não refazemos filings nem prescrevemos configuração.

## O que esta janela escreve
- Na pasta `internal-certification`: `02 Validation` dos pacotes, validadores (`validators/`, `<País>/_tool`), painel e plano. **Nunca** alterar `01 Received` (só acrescentar arquivo recebido + linha no `received.txt`).
- No cérebro: só o seu `estado.md` e a seção **"Internal Certification"** dos hubs de país (`paises/<País>.md`). Compartilhados (`log.md`, `correcoes.md`, hubs): seguir "Janelas paralelas" na raiz (reler antes, Edit pontual, log só no fim).
- Cobranças às SBCs: só rascunho em `followups.md`; quem grava no Chat/Gmail é a janela da frente correspondente, com ok do usuário. Nunca enviar.
- Dados de empregados (nomes, IDs, salários) **não entram no cérebro** (regra 3 da raiz): no hub vai só país, cliente, período, achado e base legal.
- "Fecha a sessão": nota `sessoes/AAAA-MM-DD-certificacao.md`, reescrita só do `estado.md` desta pasta e atualização das seções "Internal Certification" dos hubs tocados. Sem commit (só a janela geral commita).
