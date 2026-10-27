# Skill payroll-compliance-belgium — refresh de 2026-10-21

Pedido: usuário (21/10), depois da WTC v1.1. Pedido original da Suman: "uploaded the skill file?" (CT-4580). Ligado a [[Belgica]].

## Base
- Pacote anterior: `~/mercans-pipeline/BE-compliance/08-skill/payroll-compliance-belgium(.zip)`, de 16/09 (Stage 11). **Não alterado** (fica como backup).
- Fontes novas (todas do Drive, em `fontes/`):
  | Artefato | Arquivo | md5 |
  |---|---|---|
  | CCG | `BE-CCG-001-v1.0_export-2026-10-21.docx` (export do `.gdoc` pelo Chrome, com ok do usuário) | `fdccaeb0350614ab371d3bbd335c0929` |
  | WTC | `BE-WTC-001-v1.1.xlsx` (= Drive), depois `BE-WTC-001-v1.2.xlsx` (= Drive, v3 da skill) | `40597553aa126f026574c41cc18bcf56` / `407411a16d27f98e04698782a9c76b72` |
  | DD | `BE-DD-001-v1.0_export-2026-10-16.xlsx` (o `.gsheet` não muda desde 17/09) | `9e29fca8066ad1c93b25cdcc8944cfd3` |
  | Report Specs | 9 × `*_v1.1.xlsx` copiados de `12- Country Report Codes` | ver `fontes/specs/` |

## O que foi conferido antes
- **CCG do Drive × CCG v1.2 do pipeline:** o Drive tem a correção de 13/10 (patronal básica 19,88% + moderação até 5,12%, não 24,92%), mais 2 linhas de quebra de texto. A export de hoje (o `.gdoc` foi modificado às 15:36) tem **texto idêntico** à de 16/10; a mudança de hoje é só em comentários (Suman/Wallisson de 09 e 13/10).
- **DD do Drive v1.0 × DD v1.4 do pipeline:** todas as abas são idênticas, exceto Version Control (20 células) e Introduction (5 células).
- **WTC:** Drive v1.1 de 21/10 (`2026-10-21-wtc-series-62-65-74/`).

## O que mudou no pacote
- `references/01-ccg.md`: regenerado da CCG do Drive (`docx2md.py` do refresh de 16/09).
- `references/02-wtc.md`: regenerado da WTC v1.1 do Drive (`xlsx2md.py`), + apêndice com as notas de build do Version Control do workbook do pipeline (o VC do Drive é curto), copiadas sem mudança.
- `references/04-reports-spec.md`: regenerado das 9 specs v1.1 (Field Explanation em inglês).
- `references/05-data-dictionary.md`: regenerado do DD do Drive.
- `03-sir.md`, `06-payslip.md`, `07-qa-report.md`: sem mudança.
- `SKILL.md`:
  - tabela "Version of record" pela linhagem do Drive (CCG v1.0, WTC v1.1, DD v1.0, specs v1.1);
  - bloco "Refreshed 21 October 2026": WTC 62/65/79, correção 19,88% e aviso de que a linha 23671 do WTC ainda diz 24,92%;
  - contagens 359 → 827 (descrição, item 19, tabela de roteamento);
  - **descrição encurtada para 863 caracteres** (a anterior tinha cerca de 1.560; o limite de upload do claude.ai é 1.024).
- Script: `regen_refs.py`.

## Conferência
- Índices de navegação: 53 / 6 / 90 / 8 entradas em 01/02/04/05, todas apontando para a linha certa (0 erros).
- O 02-wtc.md contém 6201…79499, o VC 1.1 e o apêndice. O 01-ccg.md tem 19,88% (5×); 24,92% só na nota de revisão e numa faixa da tabela de retenção (não é a taxa patronal).
- Lint (TODO/TBD/placeholder) no SKILL.md: 0.
- Zip: `payroll-compliance-belgium.zip` (8 arquivos, testzip OK, md5 `3cb83ed0a5c7ec81fb27249240c96f5f`).

## Achados fora do pedido
- **WTC linha 23671** (Employer global social security contribution), coluna F: "basic employer contribution 24.92%" → deveria seguir a CCG (19,88% + moderação salarial até 5,12%). Já estava assim na v1.0; continua na v1.1. Precisa de decisão do usuário (WTC v1.2 ou correção no `.gsheet`).
- A capa interna da CCG do Drive diz "Version 1.2 — 16 September 2026", mas o arquivo se chama v1.0.

## Upload (2026-10-21, com ok do usuário: "2")
- Feito pelo Claude in Chrome na conta do usuário. Na skill existente (`skill_01TZ6Ef55Sf8hkgws8FXL6CA`; o link do CT-4580 é `plugin_01B2QitMRW2tyDyFjvsVgT2R`): menu › Substituir › zip de hoje → **v2** com 8 arquivos (conteúdo conferido na aba Conteúdo).
- **Publicada para a organização** ("Disponível para todos"), com nota de versão; a tela confirmou "Publicado v2 — v2 está ativa para sua organização". Antes ela era só da conta do usuário (v1, 16/09, não publicada).
- A versão publicada fica congelada: edições futuras exigem nova publicação.

## Frentes que mexeram
- 2026-10-21 · Pipeline · refresh do pacote (4 referências + SKILL.md), zip gerado.
- 2026-10-21 · Pipeline · skill substituída (v2) e publicada para a organização no claude.ai, com ok do usuário.

## v3 (2026-10-21, com ok do usuário: "sobe a v1.2 no Drive e republica a skill")
- `regen_refs.py` passa a ler a WTC v1.2. Regenerados os 4 arquivos: 01, 04 e 05 **idênticos byte a byte** aos da v2; `02-wtc.md` difere só em título, origem, linha 1.2 do VC, linha 23671 e nota do apêndice (mesmo nº de linhas; índice intacto).
- `SKILL.md`: tabela Version of record → WTC v1.2; aviso "row 23671 still states 24.92%" trocado por "WTC v1.2 applies the same correction"; roteamento → v1.2. Menções históricas à v1.1 (o que a v1.1 acrescentou) ficaram.
- Zip: 8 arquivos, mesma estrutura, conteúdo = pasta; md5 `04681ac7137bfaa76e53048ae4289b79`.
- claude.ai: Substituir → v3 (8 arquivos) → Publicar para organização com nota de versão; tela: "Publicado v3 — v3 está ativa para sua organização".
- 2026-10-21 · Pipeline · skill v3 publicada para a organização.

## v4 (2026-10-23, com ok do usuário: "ok, republica a skill com a v1.3")
- Suman confirmou no DM (23/10, 1h20): só as séries 62, 65 e 79. A aba All Codes do Global WTC 1.1, reconferida em 23/10 (depois da edição da Lily Li), continua com 489/142/413 = 1.044 códigos nessas séries, soma 68.848.684 = códigos da v1.3 menos 65880–65899.
- `fontes/BE-WTC-001-v1.3.xlsx` (md5 `def7afa421b56337aa3b306591f369de` = Drive). `regen_refs.py` passa a ler a v1.3. Regenerados os 4 arquivos: 01, 04 e 05 idênticos aos da v3 (`diff -rq` contra `_v3/`); só o `02-wtc.md` difere.
- `SKILL.md`: descrição (frontmatter) → "v1.3, 1,182 rows"; tabela Version of record → WTC v1.3 (1.182 linhas); bullet novo da v1.3 (355 linhas 829–1183: 62 = 1, 65 = 14, 79 = 340, contados no xlsx); residuais e roteamento → v1.3, slots 361–1183.
- Zip: 8 arquivos; md5 `b33e42482f9873bd61db2565900468c3`.
- claude.ai: Substituir → v4; no claude.ai, conferido o texto do SKILL.md (v1.3, 1.182 linhas, 340) e do 02-wtc.md (título v1.3, 79240, 79999); Publicar para organização com nota de versão; tela: "Publicado v4 — v4 está ativa para sua organização".
- 2026-10-23 · Pipeline · skill v4 publicada para a organização.
