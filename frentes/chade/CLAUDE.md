# Frente 6 — Design Chade (teste no HRBlizz) - Mercans

Esta pasta é a janela **Chade**. Vale tudo do `CLAUDE.md` da raiz do cérebro (`../..`); aqui só o que é desta frente. Criada em 2026-10-29 (usuário: 5 demandas em paralelo).

**Objetivo:** comparar o **design da equipe de desenvolvimento** do Chade, liberado para teste no HRBlizz, com o **nosso design** e a nossa pesquisa. Entregar relatório de achados (igual / diferente / falta), cada divergência com a fonte legal.

## Material
| O quê | Onde |
|---|---|
| Hub do país (artefatos, decisões, divergências já conhecidas: teto de dedução familiar, meal cash 628x, transporte 30%, piso CNPS) | `paises/Chade.md` |
| Nosso design clean-room v1.0 (24 artigos) e a comparação anterior Claude × Dev (CT-A-580: lógica ~89%, geral ~83%) | Drive `Chad/07-design`; citados no hub |
| CCG v1.2, WTC v1.1, DD v1.1 e 7 specs | Drive `G:\Drives compartilhados\Compliance Team\Country Folders\Chad\01..06` |
| Pipeline (se houver TD-compliance) | `~/mercans-pipeline/` (só ler) |
| Skills | `payroll-compliance-chad` (se existir) + `mercans-compliance-workflow` |

## Regras desta frente
- **HRBlizz pelo Claude in Chrome, só leitura.** O usuário faz o login no ambiente de teste; nunca digitar senha, nunca salvar, aprovar ou alterar nada no HRBlizz. Conferir que é o ambiente de **teste**, não produção.
- Ler o hub e a comparação anterior antes: não refazer o que já foi achado; reconferir se cada achado antigo ainda vale no design novo.
- Divergência se resolve pela lei (CGI, Código do Trabalho, CNPS), com artigo, não confiando em nenhum dos lados.
- Separar **regra estatutária** (nosso) de **configuração do engine** (Dev/Config, ver `fronteiras.md`).
- Entrega em `Research Pipeline/Chad/2026-10-29-teste-design-hrblizz/` com `CONFERENCIA.md`. Texto que vai ao Dev: inglês, curto, sem citar reuniões.
- Nada vai a ticket, e-mail ou Drive sem ok do usuário nesta janela.

## O que esta janela escreve
Só o seu `estado.md`, a pasta da entrega e, com Edit pontual, `paises/Chade.md`, `correcoes.md` e `log.md`. "Fecha a sessão": `sessoes/AAAA-MM-DD-chade.md` + reescrita do `estado.md`. Sem commit. Resumos à janela geral (`brain-service-5b`) por SendMessage.
