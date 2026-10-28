# Lituânia — SIR (Statutory Integration Requirements) — conferência

Origem: call do Wallisson (27/10, etapa 3: SIR para o time de Configuração) e SteerCo Accenture LT & LU (27/10: "statutory filing integration and also leave integration"). Método do pipeline (Stage 6): levantar os canais por órgão e montar um documento-índice com o detalhe de cada órgão.

Hub: [[Lituania]] · Reports: [[Research Pipeline/Lithuania/2026-10-27-reports/CONFERENCIA]] · Atualização 2026: [[Research Pipeline/Lithuania/2026-10-27-atualizacao-2026/CONFERENCIA]].

## Arquivos
- `LT-SIR-001-v1.0.docx` — gerado por `build_lt_sir.py` (o texto e as fontes estão no script).
- `research/VMI-integracao.md` — pesquisa da VMI (agente; afirmações-chave reconferidas por mim).
- `ticket-configuracao.md` — rascunho do e-mail para o time de Configuração.

## Fontes (S1–S9 do documento)
- Sodra, lidas por mim no navegador (o site bloqueia script): página e instrução do SAM + `sam-v07.mxfd` (S1); "Elektroninių pranešimų teikimas internetu" (S2); PDF DataService v1.0 2016-01-19, lido com pdf.js (S3); instrução do NP-SD2, pontos 57–76 (S4). Extratos em `raw/docs/oficiais/LT/2026-10-27-Sodra-SAM/`.
- VMI: regras GPM313/GPM312 e MXFDs (S5); VA-72 §21 e §26 (S6, conferido no `.docx`: os 3 modos de entrega); especificação do web service v2.01 (2010) e WSDL atual (S7); página "Žiniatinklio paslauga" (S8: confirmação em 3 dias, senão "ištrinta… pateikimas nebus įskaitytas"; só representantes de PJ); notícia de 2026-08-27 e ajuda para estrangeiros (S9). Pasta `raw/docs/oficiais/LT/2026-10-27-VMI-integracao/` (`_FONTES.md` com URL e md5).

## Checagens
1. **Fonte:** cada linha do documento cita S1–S9; o que não tem fonte está na seção 7 como NOT LOCATED.
2. **Mecânica:** o docx abre; `inspect_docx.py`: 48 parágrafos, 6 tabelas, lint C29 limpo.
3. **Contas:** não há cálculo no SIR.
4. **Coerência:** prazos e versões batem com as specs (SAM v1.0; GPM313/GPM312 v1.1). Para alinhar o canal do web service, a célula Report Matrix H2 das duas specs v1.1 passou a citar o EDSWebServiceUploadFile (VA-72 §21).
5. **Revisão independente:** 1ª passada com 12 achados (0 críticos), todos aplicados:
   - "não confirmado = não entregue" citado só na S8;
   - prazo da VMI (data de transmissão × de confirmação) movido para lacuna;
   - "p." trocado por point/page;
   - prazo completo do NP-SD2;
   - http × https no WSDL;
   - IN-03 reescrito;
   - aceite do NP-SD2 no DataService movido para lacuna;
   - PT do SAM movido para lacuna;
   - texto sobre estrangeiros atenuado;
   - 5 lacunas novas;
   - versões dos arquivos do EDS incluídas.
   
   2ª passada: os 12 resolvidos; 2 pontos novos e leves corrigidos (§24 na chave S6; aba File Structure das duas specs v1.1 com os 3 canais, igual à H2). Validador das specs: PASS.

## Lacunas principais (seção 7)
- Canal de máquina para receber da Sodra os dados de atestado médico (IN-03).
- XSD do FFData; ambientes de teste; canal de máquina dos avisos da VMI.
- Se o DataService aceita o NP-SD2; data de entrega da VMI (transmissão × confirmação); confirmação por operador estrangeiro depois de 1º/09/2026.

## Seções do documento (fonte do LT-SIR-001-v1.0)
- [[Research Pipeline/Lithuania/2026-10-27-SIR/sections/s00_control|s00_control]]
- [[Research Pipeline/Lithuania/2026-10-27-SIR/sections/s01_inbound|s01_inbound]]
- [[Research Pipeline/Lithuania/2026-10-27-SIR/sections/s02_outbound|s02_outbound]]
- [[Research Pipeline/Lithuania/2026-10-27-SIR/sections/s03_auth|s03_auth]]
- [[Research Pipeline/Lithuania/2026-10-27-SIR/sections/s04_tech|s04_tech]]
- [[Research Pipeline/Lithuania/2026-10-27-SIR/sections/s05_errors|s05_errors]]
- [[Research Pipeline/Lithuania/2026-10-27-SIR/sections/s06_sla|s06_sla]]
- [[Research Pipeline/Lithuania/2026-10-27-SIR/sections/s07_sources|s07_sources]]
- [[Research Pipeline/Lithuania/2026-10-27-SIR/sections/s08_gaps|s08_gaps]]
- A seção 8 (lacunas G1–G12) está nas Pendências do hub [[Lituania]].

## Frentes que mexeram
| Data | Frente | O quê |
|---|---|---|
| 2026-10-27 | pipeline | SIR v1.0 (rascunho), pesquisa Sodra/VMI e ticket para Configuração; nada enviado |
| 2026-10-27 | pipeline | Drive: LT-SIR-001-v1.0.docx em 19 - Statutory Integrations (pasta nova); md5 conferido |
| 2026-10-27 | pipeline | SIR refeito no formato do BE-SIR-001 (gerador `build_sir_docx_lt.py`, cópia do build_sir_docx.py da Bélgica; seções em `sections/s00–s08`): mesmo conteúdo e fontes S1–S9, reorganizado em registro inbound/outbound, autenticação, técnico, erros, prazos, fontes e lacunas (G1–G12). Lint C29 limpo. Drive 19: docx substituído no mesmo arquivo/link (md5 1261f547…). `build_lt_sir.py` antigo fica só como histórico |
| 2026-10-28 | pipeline | Entregue: task SR-479 criada (modelo SR-469/470, link do SIR Google Doc 1GTMgEM1…) e e-mail a Mohit + Katrin (Configuration) enviado pelo usuário |
| 2026-10-28 | geral | Links das notas para o grafo do Obsidian (seções/pesquisas/arquivos principais); conteúdo não alterado |
