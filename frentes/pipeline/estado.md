# Estado — Frente 4: Research Pipeline (Mercans)

> Escrito **só pela janela "Pipeline - Mercans"**. Criado em 2026-10-15 a partir de [[revisoes/2026-10-15-licoes-aprendidas/00-LICOES-CONSOLIDADAS]]. Reescrever a cada "fecha a sessão" desta janela.

## Instruções vigentes
- 2026-10-27 (usuário): **Specs** → importar a versão nova no `.gsheet` atual da spec. **WTC, CCG e DD** → criar uma versão nova (arquivo Google novo com o número da versão), atualizar o link no ticket e atualizar no monday.

## Pipeline vigente (atualizado em 2026-10-17)
- Script `~/mercans-pipeline/mercans_pipeline_v2_9.sh`, agora com **cabeçalho v2.12**. Failure log: F1–F57 (F51, F52, F54, F55 e F58–F66 continuam propostas) e F67–F74. Checks: C1–C73, com lacunas (C51, C52, C54, C55, C58–C68, C72 sem uso). Contratos 1.4.0.
- A v2.12 fecha as lacunas P0–P2 da matriz FR (`revisoes/2026-10-17-matriz-cobertura-FR-pipeline.md`). Cobertura: 5/25/33 → **18/38/7** (Total/Parcial/Nenhuma). Detalhe em `~/mercans-pipeline/IMPROVEMENT_LOG.md` (entrada de 2026-10-17).
- **Backup do estado v2.11:** `~/mercans-pipeline/_backup/v2.11-2026-10-17/` (132 arquivos) + `_backup/v2.11-2026-10-17.md5`; cada arquivo editado tem também `.bak-20261017-v212` ao lado.
- **Testes:** 13 conjuntos, todos "ALL EXPECTATIONS MET" (`shared/_test-runs/2026-10-17-v2.12/mutation-tests.txt`). Regressão no FR-compliance só de leitura (`.../regression-FR/`): só FAIL esperados e explicados.
- Piloto num país novo **não rodou**: o usuário vai iniciá-lo.
- **17/10, fechamento da v2.12:**
  - Script renomeado para `mercans_pipeline_v2_12.sh`; as cópias com o nome antigo foram para `_backup/script-history/`.
  - Pipeline portável: raiz = pasta do script ou `MERCANS_PIPELINE_HOME`; `pipeline.config.example` criado.
  - C41 aceita valor substituído no ano quando há sucessor (fonte BOSS *Assiette générale* §490/§530). Testes acrescentados, **não rodados** por ordem do usuário.
  - Pacote em `~/mercans-pipeline/dist/v2.12/`: 2 zips de chat, plugin Code, INSTALL, CHANGELOG e SECURITY-SCAN.
  - Backup em `_backup/v2.12-pre-portability-2026-10-17/`.
  - **Não commitado:** o git é da janela geral.
- **18/10, comparação com o claude.ai:** a skill do time (methodology de 31/08, pipeline v2.9) está duas versões atrás. No pacote:
  - methodology com a tabela da v2.11 e texto neutro (sem nomes de colegas);
  - compliance-workflow nova (aviso de layout do Payslip + líquido ao centavo);
  - 3 zips e `ANNOUNCEMENT.md`.

  Comparação em `rascunhos/2026-10-18-comparacao-skills-claude-ai-v2.12.md`. **Espera o usuário:** subir os zips (Owner da org ou cada pessoa) e avisar o time.

## Países no Research Pipeline (`Documents\Research Pipeline`)
| País | Material | Situação |
|---|---|---|
| Colômbia | `Colombia/CO-compliance/` (+ zip) | v1.2 montada sobre base defasada; linhagem do Drive vigente (WTC/CCG v1.4). Correções pendentes em [[Colombia]] |
| França | `França/` (+ zip) | Validação contra modele-social/DSN-Val concluída (pasta `fr-research-validation`); pendências em [[Franca]] (incluída em 17/10: os 3 números do Ex. 1 da CCG v1.0, só registro) |
| Costa do Marfim | `Costa do Marfim/2026-10-16-teto-CNPS/` | Teto CNPS PF/AM/AT-MP 70 000 → 75 000 (16/10): WTC v1.3, CNPS-001 v1.4, CNPS-002 v1.5, CCG v1.3, Design v1.2 copiados para o Drive (`CONFERENCIA.md`). **Usuário importa** no Drive |

## Em andamento
- **Lituânia — correções da validação de 28/10** ([[Research Pipeline/Lithuania/2026-10-28-validacao/CONFERENCIA]], resumo em `PASSE-DE-BASTAO.md`): SAM v1.1, GPM313/312 v1.2, SIR v1.1 em local + revalidação. 29/10: esta janela é a "Process Lithuania" do Maestri (a `frentes/lituania` não será usada). "Sim" do usuário veio pela janela geral → confirmar aqui antes de gravar.
- **Lituânia (27–28/10): entrega da call concluída e publicada** (CT-4285, SR-419/420/421, SR-479, e-mail Mohit+Katrin, HRBS-15253) — [[sessoes/2026-10-28-pipeline]]. Abertos no hub: licenças (11/11), formulários SD, 2027.
- **Skill CO recompilada (28/10)** em `Research Pipeline/Colombia/2026-10-28-skill/` — **espera o usuário** revisar e instalar no claude.ai; avisar a janela Chat (pedido do Ram).
- WTC BE séries 62/65/"74" contra o Global WTC (pedido da Suman, prazo BE dia 30; 21/10): D1–D4 aprovadas ("ok nas 4"). BE-WTC-001-v1.1.xlsx gerado e conferido (+468 linhas, 361–828, azul; validate PASS), em `Research Pipeline/Belgium/2026-10-21-wtc-series-62-65-74/`. Global 1.2 conferida (idêntica nas 3 séries). Copiado para o Drive `Belgium › 03 - WTC` em 21/10 (md5 ok). Usuário importou a **v1.2** no `.gsheet` (conferido em 21/10 pelo Chrome: VC 1.0/1.1/1.2, linha 23671 com 19,88%, 768 códigos numéricos de 6201 a 79499 = arquivo local) e avisou a Suman. Skill BE atualizada em 21/10 (`Research Pipeline/Belgium/2026-10-21-skill-refresh/payroll-compliance-belgium.zip`, linhagem do Drive, descrição em 863 caracteres). Substituída (v2) e **publicada para a organização** no claude.ai em 21/10. 22/10: Suman confirmou "74" = 79 e pediu a aba All Codes do Global 1.1 → **WTC v1.3 local** (+355 códigos, linhas 829–1183, conferida). v1.3 no Drive em 22/10 (md5 ok). v1.3 importada no `.gsheet` em 22/10 (conferida). Mensagem enviada pelo usuário; 23/10 Suman: "Only 62,65 and 79" → v1.3 é a final. **Skill BE v4 publicada** para a organização em 23/10 citando a v1.3. Frente WTC/skill BE concluída. WTC v1.2 (linha 23671 → 19,88% + moderação até 5,12%, fonte ONSS) copiada para o Drive em 21/10 (md5 ok) e skill **v3 publicada** para a organização.
- Auditoria de idioma BE (14 arquivos, 16/10): relatório pronto em `rascunhos/2026-10-16-BE-auditoria-idioma.md` (3 159 violações em DD + 5 specs NSSO/FEDRIS; 1 001 duvidosas). **Esperando o usuário:** 6 decisões listadas no fim do relatório; nenhuma correção feita.

## Esperando o usuário (decisões)
- Piloto (Portugal), quando o usuário iniciar. É o que prova: a suíte `official_examples` real, a etiquetagem `[[FACT:]]` numa build real, os plugins e tabelas de códigos do país (ou `validation_exemptions` registradas pelo dono) e o Teste 0 escrito pelo agente.
- Depois do piloto: C1–C33 passam a bloquear? (decisão D2).
- F51, F52, F54, F55 e F58–F66 (`revisoes/2026-10-09-catalogo-erros-tickets-v2.md`): só F48, F49, F50, F53, F56 e F57 entraram, e só na medida da v2.12; F58 e F65 entraram como linhas do C40.
- C41 marca como problema 42 fatos FR com `effective_to` vencido (grade PAS 2025, SMIC até 31/05). É comportamento da v2.11, não da v2.12. Aceitar valor substituído no arquivo de fatos? Recomendação: aceitar quando houver um fato sucessor.
- FR (só registro, artefatos congelados): o builder FR ainda gera resíduos limpos à mão no binário (C71); o log de promoção de 09/10 não certifica 21 arquivos (C73); o SIR FR reprova no C53 (11 pontos).
- OD-13: ticket HRBS edita o artefato ou escala para CT?
- Segurança: rotacionar a chave da Anthropic exposta (`servicos/research-pipeline.md`).

## Próximo do backlog
1. Piloto (usuário inicia) e calibração dos checks v2.12 com os dados do país.
2. Estender o C69 aos exemplos fora do Mod. 12 (CCG F-11 e Ex. 3 continuam "Nenhuma").
3. Estender o C35 (validador/XSD oficial) a todo país com XSD.
4. Lint de residual (C29/C42) cobrindo `references/` das skills, com teste negativo.
5. Calibrar C20 e C8.
6. Builder parte da maior versão publicada (Drive); nada só em `.gsheet`.

Correções de conteúdo ainda não aplicadas às skills/artefatos (CI, CG, LT, CO, UA, ES, BE, DK, NL, KZ, FR, IE/BW/GB/NA): §5 das lições.
