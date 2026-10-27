# Estado — Frente 5: Certificação (Internal Certification – Reports)

> Escrito **só pela janela "Certificação - Mercans"**. Criado em 2026-10-15 a partir de `internal-certification/PLANO_DE_ACAO_VALIDACOES.md` (§2, 14/10), do painel `Acompanhamento_Internal_Certification.xlsx` (14/10) e das sessões de 07–14/10 (Claude Desktop, VS Code e janela geral). Reescrever a cada "fecha a sessão" desta janela.

**Objetivo:** validar os statutory reports que o HRBLIZZ produz em 12 países, com o pacote real enviado pela Primary SBC (report + recibo, G2N, contracheques, GL, banco, master). Validamos e reportamos; achados vão para implementation/dev.
**Pasta:** `C:\Users\instituto\Documents\internal-certification` · Método: [[analise-reports]].

## Pacotes

| Pacote | País | Período | Pass / Finding / Not tested | Recibo prova aceite? | Situação | Próximo passo |
|---|---|---|---|---|---|---|
| Henkel Norway AS | [[Noruega]] | set/26 | 34 / 9 / 4 | Sim (A-melding GODKJENT) | ✅ Fechado · Audit Report 16/10 | Cobrar Umesh (C-01): GL "CORRECTED", carro, OTP, sindicato |
| Sherwin-Williams Denmark A/S | [[Dinamarca]] | set/26 | 18 / 5 / 2 | Sim (Afstemning SKAT) | ✅ Fechado · Audit Report 16/10 | Arquivo eIndkomst efetivamente enviado (C-02) |
| KGS Fire & Security Danmark ApS | [[Dinamarca]] | set/26 | 15 / 5 / 4 | Sim | ✅ Fechado (banco = Out of scope) · Audit Report 16/10 | Tipo do seguro-saúde; master (C-03) |
| Quest Software B.V. | [[Holanda]] | set/26 | 60 / 9 / 5 | Não | ⏳ Falta recibo Digipoort | Audit Report v1.1 emitido 14/10; v1.2 (correção Whk) + relatório interno v1.0 em 16/10, a mostrar à Manju; cobrança C-15 em rascunho (item 2 corrigido) |
| Sherwin Williams (Valspar B.V.) | [[Holanda]] | set/26 | 48 / 18 / 5 | Não (recibo é de outro LH) | ⏳ Falta recibo | C-16 em rascunho |
| Excerpta Medica B.V. | [[Holanda]] | set/26 | 60 / 5 / 5 | Não | ⏳ Falta recibo | C-14 em rascunho |
| One Identity Sweden AB (559400-9267) | [[Suecia]] | set/26 | 19 / 6 / 6 | Não (Kvittens é da Quest Software AB) | ✅ Validado · Audit Report 16/10 (qualified) | C-04: Kvittens, master, banco |
| Mastercard (Rep. office) | Cazaquistão | out/26 | 21 / 7 / 4 (v1.1) | Sim (200.00 3T/26 aceito KGD 25/09) | ✅ Validado · Audit Report 19/10 (qualified) | 200.00 recebido 19/10; ИПН ok (faixa 15%); F-06 High: folha "outubro" declarada como 3º mês do 3T; GL não existe (1C ZUP). C-18 em rascunho (confirmar o mês) |
| Altium | [[Ucrania]] | ago/26 | 33 / 13 / 12 | Sim para J0500111 (DPS 21/09, 0 erros); falta 1-PV | ✅ Validado · Audit Report 16/10 (qualified) | XML desempacotado; recibo do 1-PV (C-10) |
| Altium | [[Ucrania]] | set/26 | 9 / 4 / 7 | Não | 🔄 Audit Report INTERIM 19/10 (sem opinião sobre o report) | C-17 em rascunho: report de set + DPS, contracheques/GL/banco, 1-PV mensal e recibos, julho; reemitir como final |
| McDermott UK | [[Reino-Unido]] | set/26 | 50 / 4 / 17 | ⚠️ Ver nota 1 | ✅ Validado · Audit Report 16/10 (aceite HMRC: IRmarks conferem) | Workbook v1.1: NT-01/A02 → Pass, novos RF-02 (FPS após payday), MD-01, MD-02; master 69 = FPS 69 |
| A confirmar | Azerbaijão | set/26 | — | — | ⏸️ Pulado (zip AES, senha no e-mail) | Decisão D-01 do usuário |
| — | [[Finlandia]], [[Estonia]] | — | — | — | ⏳ Sem arquivos | C-11: cobrar Marju (2ª vez) |
| — | [[Irlanda]] | — | — | — | ⏳ Sem SBC | C-13: definir com Manju/Marko |
| — | Rússia | — | — | — | ⏳ Sem contato | C-12: Olga apresentada pela Sadaf (09/10); pedido em rascunho no Gmail desde 09/10, envio não confirmado |

**Notas**
1. **UK — divergência no painel:** o painel diz "Falta recibo", mas os ACKs do HMRC (FPS e EPS de set/26, recebidos 29/09) foram colados pelo Srikanth no Chat em 09/10 e arquivados em `United Kingdom/McDermott UK - 2026-09/01 Received/HMRC_acknowledgements_FPS_EPS_202609 (from Chat).txt`; os IRmarks batem com os arquivos validados. Atualizar o painel e o workbook UK (recibo → Pass) na próxima sessão desta frente.
2. **Ucrânia ago/26:** recibo da DPS do J0500111 (aceito 21/09/2026) já está no pacote; o que falta é o recibo do 1-PV.

## Ações para implementation (painel, aba Ações)
- A-01 NO: contribuição sindical fora da base do trekk e sem fradrag na A-melding (High).
- A-02 DK: seguro-saúde do empregador não tributado na KGS (High).
- A-03 DK: indenização no campo 0069 pelo líquido (Medium).
- A-04 SE: payout de férias acumuladas na tabela mensal (High) — aguarda decisão D-02.
- A-05 DK: base do Store Bededag / ferietillæg — aguarda decisão D-03.
- A-06: templates de contracheque (NO/DK/SE/KZ).
- A-07: pedir sempre o arquivo como enviado + recibo da autoridade.

## Esperando o usuário
- Aprovar as cobranças em rascunho (`followups.md` de cada pacote): C-01 a C-05, C-14 a C-16.
- Decisões D-01 (abrir zip AZ), D-02 (SE, SFL 11:17), D-03 (DK, Store Bededag).
- Regra (16/10): só validar e emitir Audit Report dos pacotes completos; não revisar workbooks depois de validado. KZ, UA set/26, AZ ficam fora até chegar o report principal.

## Onde ficou cada coisa
- Sessão VS Code (07–14/10, `8ae80473…`): validações NO/DK/SE/KZ, painel, Holanda completa + Audit Report.
- Sessão Claude Desktop (08–09/10): coleta inicial no Chat/Gmail, validações UK/UA, 8 cobranças em rascunho (7 Chat + 1 Gmail Olga).
- Janela geral do cérebro (14/10): kit v2, plano de ação, coleta KZ/AZ/DK/NO, correção da ponte do Chrome (`internal-certification/_chrome_fix/`).
