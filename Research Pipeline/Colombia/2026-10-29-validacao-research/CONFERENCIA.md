# Conferência — validação da research CO (modelo da França)

> Hub: [[Colombia]] · Proposta: [[PROPOSTA]] · Frente: `frentes/validacaoco`

## Fonte
- Método da França (lido em 2026-10-29, só leitura): `fr-research-validation/fr-research-validation/CLAUDE.md`, `HANDOFF.md`, `docs/test-plan.md`, `docs/runbook.md`.
- Pedido: weekly de 2026-09-29 (`raw/reunioes/2026-09-29-research-team-weekly.txt`) e de 2026-10-07 (`raw/reunioes/2026-10-07-research-team-weekly.txt`: validação externa = portais oficiais, software de terceiro, comparação com outros fornecedores de folha).
- Artefatos CO vigentes (hub, 26/10): CCG v1.4, WTC v1.6, DD v1.3, SIR v1.1, 7 specs v1.0.
- Cobertura por artefato (§4 da proposta, pedido de 29/10): XSD da nómina local em `CO-compliance/integration-sources/dian-ne/caja/...V1-0/Schemes/` (versão × Res. 227/2025 a conferir); PILA `raw/docs/oficiais/CO/2026-10-13-Res-MSPS-467-2025-PILA.pdf`; validação BAU (entrada, não repetida): `co-report-crosscheck/04-output/CONFIRMACAO-PROCESSOS-CO-2026-10-26.xlsx`.
- Opções de oráculo (pesquisa web 29/10): Calculadora Laboral MinTrabajo (`mintrabajo.gov.co/atencion-al-ciudadano/tramites-y-servicios/mi-calculadora`, segundo radionacional.co, 14/02/2024; site deu timeout desta máquina); calculadoras privadas de retención proc. 1 (gerencie.com, siemprealdia.co, buk.co); módulos Odoo `l10n_co_payroll_full` / `l10n_co_payroll_pila` (apps.odoo.com). Nenhum motor oficial programável encontrado para DIAN/UGPP/PILA.
- Saída do provedor da PMI: `co-report-crosscheck/03-client-reports-masked/` (21 arquivos, setembro/2026, mascarados pelo kit). `02-client-reports-raw/` e `99-local-only/` não abertos.

## Decisões
- 2026-10-29 (usuário): research CO não está em produção → correção = nova versão, sem ticket ao Development (P1). Iniciação aprovada: plano v0.3, F1 em curso.
- 2026-10-29 (usuário): entre os gates vale a opção recomendada, registrada aqui.
- (pendente) oráculos C/D (Manju/Marko).

## Achados da F1 (candidatos a defeito, classificação final no GB)
Base: Res. MSPS 1529/2026 (texto assinado, `raw/docs/oficiais/CO/2026-10-29-Res-MSPS-1529-2026-PILA.txt`) × CO-PILA-003/007 v1.0 (`co-report-crosscheck/05-final`). As specs citam "AT2 v30 (…24-07-2026)" e "AT3 v15". O AT2 v30 oficial foi baixado em 29/10 (MinSalud, 336 p.): `raw/docs/oficiais/CO/2026-10-29-MinSalud-AT2-v30-2026-07-24-PILA-activos.pdf` (md5 f83af022…) + `.txt`. AT3 v15 (24-07-2026, 133 p.) também baixado: `raw/docs/oficiais/CO/2026-10-29-MinSalud-AT3-v15-2026-07-24-PILA-pensionados.pdf` + `.txt`.
| # | Candidato | Lei (página) | Spec | Conferido por mim |
|---|---|---|---|---|
| D1 | Tipo 75: o obrigatório é o campo **81 "Fecha de retiro"**; a spec põe o obrigatório no campo 80 (ingresso) e deixa o 81 opcional | p.22: "Este campo debe ser obligatorio cuando se reporte el tipo de cotizante '75…'" (campo 81); o art. lista os campos 4, 5, 75 e 81, sem o 80 | PILA Spec G155 (80 obrigatório p/ 75), G156 (81 opcional); FO D123 | **Sim, confirmado também no AT2 v30 (24-07-2026), p.98**: campo 80 "Es un campo opcional cuando se reporte la novedad de ingreso"; campo 81 "Este campo debe ser obligatorio cuando se reporte el tipo de cotizante '75…'". A spec cita o AT2 v30 e inverteu os campos |
| D2 | Tipo 51: IBC de pensão por faixa de dias (1–7 = ¼ SMLMV; 8–14 = 2/4; 15–21 = ¾; 22–30 = 1), ARL com 30 dias; a spec fala de horas (campo 96) "em vez do piso de 1 SMMLV" | pp.22–23 (definição do 51, campo 36 = dias laborados, tabela de faixas, campo 38 = 30 dias) | FO D114; PILA Spec G153; PSS C10/C29 | **Sim, confirmado no AT2 v30 (texto limpo)**: campo 42 IBC pensão por faixa (1–7 dias ¼ SMLMV … 22–30 dias 1 SMLMV); campo 38 = 30 dias e campo 44 IBC ARL = 1 SMLMV; CCF também por faixa (campos 39/45); campo 96 (horas) é só opcional |
| D3 | Tipo 75: falta validação contra o arquivo da ADRES, código da administradora, nome igual, base | pp.25–26, 50–51 (agente; não reaberto) | M67, FO D123 | Sim: p.25–26 (75 contribui a saúde, pensão, ARL, CCF, SENA, ICBF; base = salário ≥ 1 SMMLV proporcional aos dias; código da administradora "MINOOS" no OCR, valor exato a ler no PDF; operador valida contra arquivo da ADRES) |
| D4 | Subtipos 3, 4, 12: documento ≠ PA e CD | p.27 (agente) | M68 | Sim: p.27 "el tipo de documento del cotizante deberá ser diferente a: PA. Pasaporte y CD. Carné diplomático"; M68 sem a restrição |
| D5 | Planilla N: usar os valores da última planilla de correções | p.18 (agente) | PSS C41, M85, FO D78 | Sim: p.18 "se deberán tener en cuenta los valores reportados para el periodo de ese cotizante en la última planilla de correcciones" |
| D6 | PC (PEP-TUTOR) usado nos tamanhos mas ausente das listas de tipo de documento | pp.5–6, 19–22 (agente) | 003 M5/M12/M65; 007 linhas 58/67/114 | Sim: p.5 "PC ~ Permiso Especial … (PEP-TUTOR) … longitud … hasta 8"; Field Options lista CC, PA, CD, SC, PE, PT, sem PC |
| D7 | 75 ausente da lista de tipos da planilla E | pp.9–10 (agente) | FO D75 | Parcial: p.9 "E. Planilla empleados: Es utilizada cuando se paguen los aportes de los siguientes tipos de cotizantes:" — a lista de códigos está ilegível no PDF; conferir na imagem da página |
| D8 | SIR v1.1 desalinhado dos artefatos vigentes: cita "CO-CCG-001 v1.1", "CO-DD-001 v1.0" e "six Report Specs" (faltam a CO-PILA-007 e o fluxo de pensionistas); base da PILA só "Res. 2388/2016 and Anexo Técnico 2" (sem Anexo 3 nem Res. 1529/2026) | Linha de base: CCG v1.4, DD v1.3, 7 specs | `linha-de-base/CO-SIR-001-v1.1-captura-2026-10-29.md` (Controle; §0; Apêndice A) | Sim |
Prazos (agente): campos de ID desde pagamentos de 1/10/2026; 51, N e subtipos desde 1/9/2026; 75 desde 1/11/2026; planilla W desde 1/4/2027 (fora do escopo). Correção: nova versão (research não está em produção, P1).

## Resultado da rodada completa (29/10, F1–F4 sem paradas, a pedido do usuário)
- 8 pacotes de verificação (CCG A/B, WTC, PILA, NE, formulários 350/220/2276/cesantías, DD, SIR+Payslip) + oráculo da lei (98 casos; `oracle/`, resultados congelados `results-20261029-173102.json` antes de ler a research) → achados em `achados/*.md`.
- Reconferência adversarial independente: `achados/VERIFICADO-1.md` e `VERIFICADO-2.md` (157 achados; 6 refutados; duplicatas fundidas).
- **Comparativo final: `COMPARATIVO-FINAL-CO-v1.0.xlsx`** (`scripts/build_comparativo.py`): 144 mudanças possíveis — S1 2 · S2 22 · S3 58 · S4 52; 94 confirmadas, 32 prováveis, 8 sem fonte primária lida.
- Conferido pessoalmente: D1, D2 (AT2 v30 p.98 e definição do 51); A-01 (DUR 1625 art. 1.2.4.1.13: 20% sobre indenização para renda > 204 UVT, ET 401-3).
- Limites: col-nomina-co (pseudo-oráculo) bloqueado pela permissão automática; secretariasenado.gov.co fora do ar (CST/ET por normograma DIAN e cópias locais); nenhum artefato alterado; nada no Drive.

## Revisão aplicada (29/10, pedido do usuário "faça essa revisão")
- Aplicadas as mudanças CONFIRMADAS do comparativo em DRAFTs `-DRAFT-COVAL-2026-10-29` (pasta `revisao/`, md5 em `revisao/MD5-DRAFTS.txt`): CCG v1.5 (docx com controle de alterações), WTC v1.7, DD v1.4, PILA-003/007 v1.1, NE (DIAN-001) v1.1, 002/004/005/006 v1.1, Payslip v1.2, SIR v1.2 (redline para colar no Google Doc). Regras: `revisao/REGRAS-EDICAO.md`; decisões: `revisao/DECISOES-RODADA2.md`.
- 3 rodadas + 2 conferências independentes (`revisao/CONFERENCIA-DRAFTS.md` → `CONFERENCIA-DRAFTS-R2.md`); rodada 3 fechou os resíduos. Conferido por mim: Ley 100 art. 15 num. 2 (estrangeiros = afiliação voluntária); 004 K52/K63 = 7.407.000; PILA-003 G155/G156 (75 → campo 81); Payslip H55 = 192.000; WTC B229 = "Birth and Marriage Allowance" (Global WTC 62591).
- Nada no Drive nem nos finais; promoção só com ok do usuário.

## Test 4 — folha real de setembro (PMI, mascarada) × oráculo (30/10, aprovado pelo usuário)
- `test4-folha-setembro/RELATORIO-TEST4.md` (+ `resultados.json`, `scripts/`). PII: `pii_audit_masked.py` rodado antes (9 colunas para olhar; a única vista de perto, E.P.S, traz nomes de operadoras de saúde). Relatório sem IDs/nomes/salários.
- 261 empregados; 5.232 linhas de folha: 4.502 batem, 342 tolerância (≤ 3,24 COP), 324 sem dado, 55 divergências, 7 lacunas do oráculo. Indenização art. 64: 684 de 726 divergem (tabela mais favorável, fração truncada, variável fora da base).
- **Novo achado (85%):** exoneração ET 114-1 — PILA-003 (v1.0 e DRAFT, Payroll Scope Summary C34) testa "total devengado and health IBC" < 10 SMMLV, como o provedor; CE S4 exp. 25302/2022 (citada na 26984/2024, `raw/docs/oficiais/CO/2026-10-22-CE-S4-26984-2024-SENA-normograma.htm`, conferido por mim) conta só o salarial. Contradição interna com o CCG v1.4 ("salary < 10 minimum wages").
- **Novo ponto aberto (50%):** salário integral + excesso Ley 1393 — ordem (40% → 70% ou 70% + excesso) sem fonte local que decida.
- **Possível lacuna (70%):** base da indenização art. 64 com variável não definida na research.
- Erros do provedor sem impacto na research (aviso ao BAU): retenção sem o 25% (ET 206 num.10) em 5 empregados; incapacidade a 100%; base patronal menor que o IBC em 2.
- Oráculo: `para_base` soma o excesso Ley 1393 nos parafiscais (art. 30 só alcança Ley 100 arts. 18 e 204) → corrigir em versão nova do oráculo (decisão técnica reversível).

## Decisões do Test 4 por pesquisa oficial (30/10) — `pesquisa-2026-10-30/DECISOES-TEST4.md`
- **114-1 (90%):** teste dos 10 SMMLV só com salário do mês (+ trava PILA: IBC saúde < 10 SMMLV). DIAN Concepto 8380/2024 e 7196/2025 (conferidos por mim: "Los pagos no constitutivos de salario no se encuentran incluidos dentro del cálculo"); CE S4 25302/2022 e seguintes; Decreto 1828 art. 7 eliminado do DUR pelo Decreto 2201/2016. → PILA-003 muda (C34/M36/M150).
- **Integral + Ley 1393 (80%):** IBC = 70% do integral + excesso dos 40% (Ley 100 art. 18; CE SU 25185/2021, 25907/2022). → CCG l. 481 e oráculo mudam.
- **Art. 64 (85–90%):** base com variável (CST 127; média da última anualidade, CSJ SL1659-2025); fração proporcional. Provedor erra; research ok, falta escrever a base.
- **Excesso Ley 1393 (95%):** entra em saúde, pensão e ARL (DL 1295/1994 art. 17); não em SENA/ICBF/CCF. → oráculo `para_base` corrigir.
- Fora do pedido: limite de 40% só alcança pagos desalarizados por pacto (SU 25185); não salariais por natureza ficam fora do IBC e do teste.

## Fechamento: finais limpos (30/10, modelo da França, passos 1–4 aprovados pelo usuário)
- **Linha de base:** `final/baseline/BASELINE.md`.
  - Autoverificação 45/45; comparação research × oráculo com 69 PASS e 20 FAIL, todos ligados a um achado (19 fecham nos finais; CCG-44 é limitação do oráculo).
  - Test 4 v2: 742 divergências, 0 atribuídas à research.
  - md5 do oráculo `c09f0e6f…`.
- **Finais:** em `final/` (CCG v1.5, WTC v1.7, DD v1.4, 7 specs v1.1 em `final/specs/` com o nome sem versão, igual ao Drive; Payslip v1.2; SIR v1.2 como texto para colar). Os md5 estão em `final/MD5-FINAIS.txt`. Os changelogs ficam em `final/changelogs/`.
- **Ferramentas:**
  - `final/scripts/release.py`: cirurgia no XML, aceita as alterações controladas, tira o azul e aplica as edições declaradas em `release_edits.py`;
  - `release_crosscheck.py` → `final/RELEASE-CROSSCHECK.md`: PASS, 0 falhas.
- **Test 0:** `final/test0/TEST0.md`.
  - 15 achados corrigidos, entre eles a Circular 101/2025 revogada (24 parágrafos do CCG e WTC), o recargo dominical do Payslip, o FSP na Ley 797 arts. 7 e 8, o RAIS no ET 55 e os dois limites do 114-1 propagados.
  - 6 achados e 7 dúvidas ficam para decisão do usuário (reclassificações no WTC).
- Nada foi ao Drive, a `~/mercans-pipeline`, a ticket ou e-mail.

## Rodada 5 (02/11)
- **Fonte:** [[TABELA-RODADA5]] (`pesquisa-2026-11-02/`, lotes A, B e C). Passo 0 decidido pelo usuário: teto de 3.800 UVT de fundos voluntários e AFC/AVC (ET 126-1/126-4) anual, pelo acumulado, sem ÷ 12 (DUR 1625 art. 1.2.1.22.43 "por año"; CE S4 rad. 24047/2021, "máximos anuales"; trecho conferido no texto local da sentença).
- **Antes → depois (resumo):**
  - tetos de 790 e 1.340 UVT: de 1/12 por mês para anual pelo acumulado (exemplos do CCG e Payslip recalculados; ex. T105 4.994.989,65 → 3.947.554,80);
  - teto de 3.800 UVT: de ÷ 12 para anual pelo acumulado (CCG T228R5 e P602, WTC Tax Credit A34);
  - cesantías de não residente: sem retenção (o 20% vira opção desligada);
  - casilla 59 / N33: 13.000.000 → 12.000.000;
  - número de regras da NE no SIR (519);
  - elementos NE das linhas Y do WTC e linha 346;
  - tarifa ARL com ponto decimal;
  - DD: banco só para meios com conta, mais o código 98;
  - CCG: Circular 101 revogada trocada pela lei.
- **Release:** CCG v1.6, WTC v1.8, DD v1.5, specs 001/003/004/005/006 v1.2, Payslip v1.3 e SIR v1.3 em `final/`. As specs 002 e 007 continuam v1.1. Os finais de 30/10 foram movidos para `final/_historico/2026-10-30/`. Os md5 estão em `final/MD5-FINAIS.txt` e os changelogs em `final/changelogs/`, cada um com a seção 2026-11-02.
- **Conferência:**
  - DRAFT-R5: `revisao/rodada5/CONFERENCIA-R5.md`, PASS. Os DRAFT-R5 se reproduzem idênticos a partir do histórico.
  - Release: `final/RELEASE-CROSSCHECK-R5.md`, PASS, 0 falhas. Cada final é o DRAFT-R5 aceito e sem o azul; os arquivos abrem, sem erro de fórmula, e o `validate_workbook` dá PASS.
  - Scripts: `final/scripts/release_r5.py`, `release_r5_edits.py`, `release_crosscheck_r5.py` e `build_changelogs_r5.py`.
- Nada foi ao Drive, a `~/mercans-pipeline`, a ticket ou e-mail.

## Antes → depois
- Nada alterado em artefato.

## Conferência
- Res. MSPS 1529/2026 baixada (cerlatam.com; SIDN bloqueado): `raw/docs/oficiais/CO/2026-10-29-Res-MSPS-1529-2026-PILA.pdf` (58 p., md5 4a323a88…) + `.txt` extraído. Impacto em CO-PILA-003/007 em análise.

## Frentes que mexeram
| Data | Frente | O quê |
|---|---|---|
| 2026-10-29 | validacaoco | Pasta criada; proposta (método aplicável, oráculo, suíte) |
| 2026-10-29 | validacaoco | Proposta §4–§6: cobertura por artefato, meta 100 %, 6 pontos abertos |
| 2026-10-29 | validacaoco | [[PLANO-DE-ACAO]] v0.1 (PMBOK 8 + IEEE 1012 + ISO 29119): EAP, gates G0–G5, RACI, riscos; espera G0 |
| 2026-10-29 | validacaoco | PLANO-DE-ACAO v0.2: inventário medido (~9.000 unidades; WTC 3.600 marcações), risco, garantia por artefato, 3 gates, 13–18 sessões; [[MENSAGEM-MANJU-DRAFT]] (não enviada) |
| 2026-10-29 | validacaoco | PLANO v0.3 + [[PESQUISA-2026-10-29]]: definições SEVOCAB, base de teste (NE vigente; PILA Res. 1529/2026 nova), md5 specs, Payslip resolvido, França 05–09/10; hub CO: pendência Res. 1529 + nota SMMLV |
| 2026-10-29 | validacaoco | F1 iniciada (P1 confirmada); Res. 1529/2026 baixada para raw/docs/oficiais/CO |
| 2026-10-29 | validacaoco | F1: Res. 1529/2026 × CO-PILA-003/007 → 7 candidatos a defeito (D1–D2 conferidos) |
| 2026-10-29 | validacaoco | SIR v1.1 lido pelo Claude in Chrome (sem MCP) → `linha-de-base/`; candidato D8 |
| 2026-10-29 | validacaoco | RTM-CO-v0.1.xlsx (10.798 itens: alto 4.497, médio 4.204, baixo 2.097; `scripts/build_rtm.py`); D3–D6 conferidos por mim, D7 parcial |
| 2026-10-29 | validacaoco | AT2 v30 oficial baixado (MinSalud); D1 e D2 confirmados nele |
| 2026-10-29 | validacaoco | AT3 v15 oficial baixado (MinSalud) |
| 2026-10-29 | validacaoco | Rodada completa: COMPARATIVO-FINAL-CO-v1.0.xlsx (144 mudanças possíveis; 2 S1, 22 S2) |
| 2026-10-29 | validacaoco | Revisão aplicada em DRAFTs COVAL (CCG v1.5, WTC v1.7, DD v1.4, 7 specs v1.1, Payslip v1.2, SIR v1.2 redline); conferência independente R2 + rodada 3 |
| 2026-10-30 | validacaoco | Test 4: folha PMI set/2026 mascarada × oráculo (5.958 linhas); 1 achado novo (114-1), 1 ponto aberto (integral × Ley 1393) |
| 2026-10-30 | validacaoco | Pesquisa oficial: 4 decisões do Test 4 (114-1 só salário; integral 70% + excesso; art. 64 com variável; excesso fora dos parafiscais) |
| 2026-10-30 | validacaoco | Pesquisa oficial pendentes specs/DD/Payslip/SIR (27 itens): 21 mudam, 3 só nota, 1 aberto (S-07), 2 já feitos — `pesquisa-2026-10-30/PENDENTES-SPECS-DD.md`; NE-04 conferido por mim (DIAN 14745/2025: "el DSNE no admite valores negativos") |
| 2026-10-30 | validacaoco | Pesquisa CCG/WTC (23 itens: 20 mudam, 2 não, 1 aberto) + [[TABELA-CONSOLIDADA]] (54 itens: 46 mudam, 5 nota, 2 abertos); corrigido: teto 1.340 UVT fica na retenção (DUR 1.2.4.1.6 par. 3, conferido) |
| 2026-10-30 | validacaoco | Rodada 4 nos DRAFTs COVAL (44 de 46 aplicados; A-03/F-01 já estavam) + oráculo v2 (suíte e Test 4 rerodados: lacunas 7→0; 114-1 confirma 8 erros do provedor; E251 p/ revisão manual); conferência independente R4 (`revisao/CONFERENCIA-DRAFTS-R4.md`); PILA-003 C34 conferida por mim |
| 2026-10-30 | validacaoco | Fechamento (modelo França) passos 5–6: `final/simulations/` (simulação 103 casos 0 dif.; impostos 467 linhas 0 dif.; lei × provedor agregado) e `final/design/` (57 regulações, memo, matrizes do WTC v1.7). Pendente: reconferir o design contra os finais aceitos (item 13 art. 64 já decidido no CCG P980 — leitura sem as inserções controladas) |
| 2026-10-30 | validacaoco | Fechamento no modelo da França: linha de base congelada (`final/baseline/`), finais limpos (`final/`), `release_crosscheck.py` PASS, Test 0 (15 corrigidos, 6+7 para decisão) |
| 2026-10-30 | validacaoco | 2ª passada pós-release (consistência CCG × specs/WTC/Payslip, PR-01 a PR-08, [[CONSISTENCIA-DECISOES]]): NE `@Porcentaje` dominical = percentual legal (DIAN Concepto 013840/2025); WTC Employer Sick Pay sem OPEN ITEM 1/2 (C-543/2007; MinSalud 2023), alto risco +10 pts, PILA 57–60 em branco/zero; Payslip/CCG Ley 1393 art. 32; capa do CCG 30/10. `release_crosscheck` PASS; changelogs, MD5-FINAIS, design (contagens 53/5/22, memo item 10) e skill (01/02/04/06, zip) refeitos |
| 2026-11-02 | validacaoco | Rodada 5 ([[TABELA-RODADA5]]) + passo 0 (teto de 3.800 UVT anual) nos DRAFT-R5 (`CONFERENCIA-R5` PASS) e release: CCG v1.6, WTC v1.8, DD v1.5, 5 specs v1.2, Payslip v1.3, SIR v1.3 (`RELEASE-CROSSCHECK-R5` PASS); finais de 30/10 em `final/_historico/2026-10-30/` |
| 2026-11-02 | validacaoco | Resíduos antes da subida ao Drive (`final/scripts/release_residuos.py`; `RELEASE-CROSSCHECK-R5` seção "Resíduos" PASS): CCG Mód. 12 Ex. 4 (E) teto anual 790 UVT pelo acumulado + capa 2 Nov; DD H7 e NE NIE066/Population Rules só com códigos do mapper (42, 45, 47, 98); 2.500 UVT do ET 55 anual → só o design (`58151`) mudou; skill (01, 04, 05, SKILL, 07, zip) e design README atualizados; cópias em `final/_historico/2026-11-02-antes-residuos/` |
