# EG — seguro social a partir de 01/01/2027 (HRBS-15790), 2026-10-25

**Pedido:** HRBS-15790 (Mustafa): piso 3.200 / teto 19.300 / EE 11,5% / ER 19,25% a partir de 01/01/2027. Análise: `rascunhos/2026-10-23-shruti/HRBS-15790-egito-SI-2027.md`.

**Fonte:**
- Lei 148/2019, art. 19, último parágrafo (+1% a cada 7 anos desde 01/01/2020, meio a meio, total máx. 26%): `raw/docs/oficiais/EG/2026-10-22-lei-148-2019-seguro-social-nosi.pdf`, p. 25.
- Regulamento Executivo (Decreto PM 2437/2021), art. 53 (piso/teto +15% ao ano por 7 anos, arredondando para cima até a centena) e art. 57 (aumento no ramo de velhice): `raw/docs/oficiais/EG/2026-10-22-decreto-pm-2437-2021-regulamento-lei-148-gazette.pdf`, p. 46 e 48.
- NOSI, 30/11/2025 (valores de 2026): `raw/docs/oficiais/EG/2026-10-23-nosi-noticia-2025-11-30-piso-teto-2026.html`.

**Decisões do usuário (25/10):**
- Arquivo ativo = o linkado no Monday (board Compliance Artifacts, grupo "Egypt (AI)"). CCG: item "Country Research Guide" → `EG-CCG-001-v1_4-statutory-leave-country-standard.docx` (Docs id `1HDiBMTMRrSxScRZDmmCaS25wzVC7-q_M`). WTC/DD: item "EGPYT WTC - DEVELOPMENT" (Phase 3, Mohit) → `EG_WTC_and_Taxability_Matrix` (id `198zMBqHg7A3E2mmxE8jTtcRbXsuM0I63Iyh-45_aAzY`).
- Atualizar só o CCG; a Matrix é do Mohit (espelha a configuração) e não é editada: as mudanças vão descritas no comentário.
- Numeração: CCG v1.5. Valores de 2026 mantidos, 2027 acrescentado com vigência.
- Ordem: arquivos → comentário com pergunta ao Mohit sobre a task → task só se ele pedir.

## Arquivos
| Arquivo novo | Base | Alterações |
|---|---|---|
| `EG-CCG-001-v1.5.docx` (md5 `81bd396bd20ae97f474fb250ebd2e877`) | `raw/docs/drive-exports/2026-10-25/EG-CCG-001-v1_4-statutory-leave-country-standard.docx` (cópia do Drive, md5 `507fea21f97a0649c4026479780eadfb`; capa interna "v1.1") | 56 parágrafos + rodapé |
| `EG_WTC_and_Taxability_Matrix.xlsx` | — | **não alterado** (do Mohit); export de 25/10 em `raw/docs/drive-exports/2026-10-25/` (md5 `fa37ff0f974788105e672fc4101ec7e7`) |

Script: `aplicar_ccg.py` (cada edição declara o trecho antigo; aborta se não aparecer exatamente 1 vez). Log completo antes → depois: `conferencia-ccg-log.txt`. Destaque: sombreamento `DDEBF7` nos 56 runs alterados.

## Antes → depois (resumo)
- Capa: v1.1 → v1.5; Status "QA Patched — 2026-05-27" → "Regulation Update — 2026-10-25 (social insurance from 1 January 2027)"; rodapé v1.1 → v1.5.
- §2.2 (INSURANCE_WAGE): + "between EGP 3,200 and EGP 19,300 from 1 January 2027".
- Employer On-Costs (texto + tabela): OAD 12.00% (12.50% from 1 Jan 2027); base legal + Executive Regulations Art. 57; totais 18.75% (19.25%), 11.00% (11.50%, 9.5% OAD), 29.75% (30.75%); remessa e piso/teto de 2027.
- §5.1 tabela de ramos: OAD 12% (12.5%) / 9% (9.5%); totais 18.75% (19.25%) / 11% (11.5%).
- §5.1.1 piso/teto: "revised periodically by ministerial decree" → regra do art. 53; coluna "Monthly Amount (2026 | from 1 Jan 2027)": 2,700 | 3,200 e 16,700 | 19,300.
- Tabela consolidada: OAD 12% (12.5%), 9% (9.5%), 21% (22%); piso/teto das 5 linhas (3,200)/(19,300); totais (19.25%)/(11.5%)/(30.75%); base legal: "Ministerial Decree…" → Regulamento arts. 53 e 57 + NOSI 30/11/2025.
- §5.2 passos de cálculo: piso/teto de 2027 no Step 2; × 12% (12.5%), × 9% (9.5%), totais; Steps 4 e 5.
- Arrears (3157), elementos intermediários (3545/3548), resumo (3882–3885), expatriados (4217/4218): valores de 2027 acrescentados.
- "Social Insurance — Rate and Ceiling Changes" (3916): o texto dizia que a mudança vale a partir da notificação do Ministro das Finanças (sem fonte); reescrito com a regra do art. 53 e do art. 19/art. 57, e com a nota "Worked examples in this guide use the 2026 parameters".

## Conferência
1. 56 edições, cada uma com o trecho antigo encontrado exatamente 1 vez (dry-run e gravação iguais).
2. Base × nova: mesmas partes do zip; só `word/document.xml` e `word/footer1.xml` mudaram; 5.561 parágrafos e 127 tabelas nos dois; 56 parágrafos diferentes = 56 da lista; XML válido.
3. 47 parágrafos com valores de 2026 ficaram como estão de propósito: são exemplos de cálculo (Example 1, 2, bônus, part-time, expatriado…), cobertos pela nota do §3916.
4. Contas: 12,5 + 1,5 + 3,25 + 1 + 1 = 19,25; 9,5 + 1 + 1 = 11,5; 19,25 + 11,5 = 30,75; OAD 12,5 + 9,5 = 22. Piso 2.700 × 1,15 = 3.105 → 3.200; teto 16.700 × 1,15 = 19.205 → 19.300.
5. Render no Word → PDF (178 p.): p. 21 (On-Costs), p. 41–42 (§5.1.1 e tabela consolidada) conferidas na imagem, sem quebra de layout.

## Não alterado (de propósito)
- Exemplos de cálculo com 2026 (47 parágrafos).
- Prazo de remessa "by the last day of the month following" e surcharge 1,5% (achado 3 da análise: art. 121(1) diz início do mês seguinte) — fora do pedido, vai para o hub.
- Faixa 60+ (sem ramo de velhice): inferência de que não muda (⚠️, confirmar com o Mohit).
- Matrix e Design (Mohit / produção).

## Pendências
- Subir para o Drive (`05 - Payroll Regulation Guide`) e atualizar o link no Monday: só com ordem do usuário.
- Origem do arquivo `v1_4` (capa interna "v1.1"): não identificada.

## Frentes que mexeram
| Data | Frente | O quê |
|---|---|---|
| 2026-10-25 | Suporte | CCG v1.5 gerado (56 parágrafos + rodapé), conferido; nada no Drive. |
