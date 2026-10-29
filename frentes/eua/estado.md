# Estado — frente eua

> Escrito só pela janela desta frente. Criado em 2026-10-29 pela janela geral; reescrever a cada "fecha a sessão".

## Instruções vigentes
- Todos os 50 estados + DC (decisão do usuário, 2026-10-29). A variação de lei de estado para estado é o ponto central: cada estado com a sua research sobre a camada federal comum.
- 29/10 (usuário, pela janela geral): a research dos EUA roda **nesta janela**, não na frente Pipeline (ocupada com a Lituânia). Trazer daqui o método da Pipeline; não mexer na janela Pipeline nem nos arquivos dela (só ler).

## Método adotado da frente Pipeline (lido em 2026-10-29 de `frentes/pipeline/CLAUDE.md` e `estado.md`)
- **Pipeline v2.12** (`~/mercans-pipeline/mercans_pipeline_v2_12.sh`, contratos 1.4.0, failure log F1–F57 + F67–F74, checks C1–C73): **só leitura e execução de validadores**. `~/mercans-pipeline` não tem remote: nada é gravado lá por esta janela.
- **Orquestração:** skill `country-build` com os 4 agentes (`compliance-scaffolder` → `compliance-source-hunter` → `artifact-builder` → `compliance-qa-auditor`), auditor ao fim de cada artefato, máx. 3 rodadas, parada humana depois do mandato selado (Step 4).
- **BASE desta frente:** `Research Pipeline/USA/US-compliance/` (não `~/mercans-pipeline/US-compliance`). Decisão técnica reversível de 29/10. Os appends em `~/mercans-pipeline/shared/` (failure log, playbook, portal registry) ficam como propostas em `US-compliance/_shared-appends/`, para a frente Pipeline aplicar com ok do usuário.
- **Validador de contrato:** `python ~/mercans-pipeline/shared/schemas/validate_contract.py` depois de cada agente.
- **Lições** (`revisoes/2026-10-15-licoes-aprendidas/00-LICOES-CONSOLIDADAS.md`): fonte primária decide; vigência por fato; matriz de cobertura por país (G-T6, inclui tributos locais/regionais e residência × trabalho); limites com período, acumulador e arredondamento (G-T7); spec testada no validador/XSD oficial quando houver; exemplos calculados, não digitados; trilha de auditoria fora do entregável.
- **Versão/Drive:** nome `{CC}-{TYPE}-{SEQ}-vX.Y`; linhagem do Drive prevalece; nada vai ao Drive/monday sem ok; edição de xlsx por XML (toolkit), destaque `FFDDEBF7`.

## Observações próprias dos EUA
- Jurisdição subnacional = 51 (50 estados + DC). No Step 5, um source-hunter **por estado** (e por bloco federal), com shard de registro próprio — nunca serial (Canadá: 12 h 43 m num agente só).
- Multi-estado (Marko, 21/10): trabalha num estado e mora em outro, reciprocidade, crédito de residente, convenience rule. Domínio próprio no mandato.
- Filing estadual por **provedor terceiro**, sem ADP (Marko, 21/10) → SIR = processo do terceiro; pesquisar o processo.
- "Tabelas a manter e subir" (Marko) → `USA-TABELAS/` com vigência; virada de ano é requisito.
- Imposto local (cidade/condado/school district): municipal é irrelevante na maioria, mas NY/PA/OH/MD/MI/IN/KY etc. entram na matriz como Coberto/Parcial/Fora.

## Em andamento
- 29/10: inventário (Drive USA = esqueleto vazio; pipeline sem nada) + proposta em [[Research Pipeline/USA/PROPOSTA-ESTRUTURA|PROPOSTA-ESTRUTURA]].
- 29/10: country-build iniciado em `Research Pipeline/USA/US-compliance/`. Defaults enquanto o usuário não decide: ano 2026, setor privado, USD, pacote único.
  - Step 1 ✅ scaffold (manifest PASS; tier geral T4 provisório; 53 unidades FED+MULTI+51; 65 US-MQ, sendo 11/13/14 do usuário).
  - Step 2: FED-MULTI, G1, G2, G3, G4 voltaram (maioria parcial); G5, G6 rodando. **Bloqueio:** muitos sites .gov recusam fetch automático (MA, ME, MI, MO, MT, IL, IN, KS, ID, NE, AZ, DC, SSA, federalregister); download com user-agent de navegador foi **negado** pelo classificador (contorno de bot-check) → não usar Chrome nem curl nesses hosts sem ok do usuário. Opções ao usuário: (1) ele baixa os PDFs, (2) libera o navegador, (3) selar com NOT LOCATED (default).
  - Step 2 (lançado): 7 source-hunters (Sonnet) em paralelo — FED-MULTI + G1..G6 (estados) → `_register-shards/mandate-*.csv` e `_research/mandate-answers/*.md`. Depois: Step 3 (selar) e Step 4 (parada humana).

## Esperando o usuário
- Pacote único × por estado (default: único); ano fiscal (default 2026); estados com cliente (Yoyo/BAU).
- Atualizar `frentes/eua/CLAUDE.md` com o método adotado (está aqui no estado.md; CLAUDE.md só com ok do usuário).
