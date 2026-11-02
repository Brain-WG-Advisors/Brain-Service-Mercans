# Pacote v2.12 corrigido para o time — conferência (2026-10-29)

Origem: Manju não conseguia iniciar o pipeline (call de 29/10). Diagnóstico em `log.md` (29/10, linha "Manju sem conseguir iniciar o pipeline"): skills só na conta do usuário, script não enviado, e-mail dizia "três zips" mas foi um zip com três dentro.

## O que foi feito
- **Skills publicadas para a organização** (claude.ai, ok do usuário): mercans-pipeline-methodology v2 e mercans-artifact-toolkit v1 ("Disponível para todos"); mercans-compliance-workflow v3 no lugar da v1 ("Nenhuma alteração no acesso": vale para quem já tinha a v1).
- **Guia novo** `START-HERE.md` (inglês): A = chat (só conferir as skills), B = Git Bash + script como antes (plugin opcional; o script não depende dele, conferido: só chama `claude -p`), tabela "If it stops" com as mensagens reais do pre-flight do script.
- **Pacote** `mercans-pipeline-v2.12-package.zip` (fora do git, `*.zip`): START-HERE, INSTALL, CHANGELOG, SECURITY-SCAN, `code/` (plugin com o script e `shared/`) e `chat/` com os 3 zips de skill (reserva). Fonte: `~/mercans-pipeline/dist/v2.12/` (só lido).

## Conferência
| Item | Resultado |
|---|---|
| Script do pacote = script em uso | md5 `e702b2ce…` igual (`~/mercans-pipeline/mercans_pipeline_v2_12.sh` × `dist/v2.12/code/.../pipeline/`) |
| `shared/` do pacote × pipeline em uso | só faltam no pacote `FR_regime_scope_note.txt` (usado só se país = FR) e pasta local de trabalho; `si-runbook/` não existe em nenhum dos dois (o script testa com `-f`) |
| 11 arquivos obrigatórios do pre-flight | todos presentes |
| Teste do passo 4 (extração limpa, `GENERATE_PROMPTS_ONLY`, país fictício TL) | pre-flight OK (`Claude CLI: ok`, `All v2.4 reference files present`), prompts das etapas 1–12 gravados; termina em `STAGE 13 HALTED (C43)`, esperado sem build (avisado no guia) |
| Zip | `testzip` sem erro, 107 entradas, sem `__pycache__`; maior caminho interno 122 caracteres (descompactar em pasta curta, ex. `C:\mercans\v2.12`) |
| Segurança | `SECURITY-SCAN.md` de 17/10: 0 chaves/tokens, 0 caminhos da máquina, sem dados de cliente |

Não testado: instalação do plugin numa máquina limpa (`/plugin marketplace add`) e uma rodada real.

## Pendente
- Usuário: enviar o e-mail (rascunho `rascunhos/2026-10-29-email-pipeline-v2.12-correcao.md`) com o zip.
- Se a compliance-workflow não aparecer para alguém: pedir acesso a um admin da organização.

## Linhas por frente
- 2026-10-29 · geral · pacote, guia, publicação das skills e conferência acima.
- 2026-10-29 · geral · guia: caminho Git Bash (como o time usava) como principal, plugin opcional, aviso para renomear a pasta v2.9 antes de copiar; zip refeito (md5 ac470902…).
- 2026-11-02 · geral · página para o time (inglês, interativa): `pipeline-v2.12-team-guide.html`, publicada como artifact privado https://claude.ai/artifact/1MskqAxbGBtxY34KCAKGKa (só abre depois de compartilhada pelo usuário). Conteúdo tirado do START-HERE e do CHANGELOG-v2.12.
- 2026-11-02 · geral · a pedido do usuário (o time usa só Git Bash): zip simples `mercans-pipeline-v2.12-gitbash.zip` (1,3 MB, 81 entradas, testzip ok) = só a pasta `pipeline/` + README.txt de 3 passos; script md5 e702b2ce… igual ao em uso. Sem plugin, agentes nem skills (já publicadas na organização).
- 2026-11-02 · geral · zip Git Bash copiado para o Drive (Research Team Folder/02. AI Pipelines), md5 5f729415… = local.
- 2026-11-02 · geral · enviado pelo usuário: Chat à Manju (passos Noruega + pasta do Drive) e e-mail a todos com a pasta 'pipeline v2.12'. Pendência 'enviar o e-mail com o zip' fechada.
