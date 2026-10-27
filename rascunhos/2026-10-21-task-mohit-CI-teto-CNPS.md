# Task para o Mohit — CI: teto CNPS PF/AM/AT-MP (CT-A-620 reg. 4061)

> Rascunho de 2026-10-21. **Não criado no YouTrack.** Pedido do Mohit no e-mail "Ceiling for Ivory coast" (19/10 10:57): *"Kindly raise a development task for the required changes, along with an explanation of what needs updating."*

## O que foi resolvido (cérebro)
- HRBS-14996, parecer de 22/09: dissemos que 70.000 XOF/mês era o teto de PF/AM/AT-MP e que 75.000 era só o SMIG (fonte: CLEISS, secundária e desatualizada).
- 15–16/10: a fonte primária mostra **75.000 XOF/mês desde 2023-01-01** (piso de todos os ramos e teto de PF/AM/AT-MP); teto da aposentadoria 3.375.000. Ver [[correcoes]] (2026-10-15) e [[Costa-do-Marfim]] (Valores-chave).
- Fontes: communiqué CNPS "Nouveau plafond des cotisations sociales de la CNPS" (11/01/2023, Décret 2022-986), `raw/docs/oficiais/CI/2026-10-15-CNPS-communique-nouveau-plafond-2023.pdf` (CRC32 conferido com o site); Loi 99-477 art. 23.
- Reflexo no produto: CT-A-620 reg. 4061 usa 840.000/ano (= 70.000 × 12); o certo é 900.000 (= 75.000 × 12). A reg. 4031 (aposentadoria: piso 900.000 / teto 40.500.000) já está certa.
- E-mails: nossa resposta de 16/10 17:06 (explicação da mudança) e de 19/10 08:17 (o que muda); Siva pediu ao Mohit "update and confirm" (19/10 08:37); Mohit pediu a task (19/10 10:57).

## Conferência de 21/10 (lida pessoalmente nas fontes primárias)
- Communiqué CNPS (PDF local, mesmo arquivo do site): "à compter du 1er janvier 2023 … plancher … (toutes branches confondues) est fixé à 75 000 FCFA … plafond de la branche retraite … 3 375 000 FCFA … plafond des autres branches (Assurance Maternité, Prestations Familiales et AT/MP) est fixé à 75 000 FCFA". ✅
- CT-A-620 (PDF original, `Downloads/CT-A-620.zip` → result.pdf): reg. 4061 "CI CNPS (Family Benefits, Maternity, Injury) Base", faixa `LTE($58216;1)`: Floor 840000.00 / Ceiling 840000.00; faixa `EQUALS($58216;2)`: 450000.00 / 450000.00. Reg. 4031 (Pension Base): 900000.00 / 40500000.00. ✅
- "Por ano": a spec não indica a unidade, mas 840.000 é exatamente o valor anual da própria CNPS antes de 2023 (página "Employeur" e guia de 2021: "840 000 F par an … 70 000 FCFA par mois"), e a reg. 4031 segue a mesma escala (75.000 × 12; 3.375.000 × 12). ✅
- Detalhe que o e-mail de 19/10 não disse: na reg. 4061 o **piso** também é 840.000 e também muda para 900.000 (piso = 75.000 em todos os ramos). Entra na task.

## Texto da task (inglês)

Campos no padrão de CT-4585 e CT-4600 (mudanças estatutárias abertas pela Enaakshi para o Mohit):
**Project:** CT · **Type:** Development task · **País:** CI · **Assignee:** Mohit Jain (mjain) · **Epic:** Regulation Update · **Prioridade:** Normal · **Sprint:** Year 2026 - Q4 (conferir) · **Acceptance criteria:** NA · **Anexo:** communiqué CNPS (PDF)

**Summary:** CI_CNPS ceiling for Family Benefits, Maternity and AT/MP_XOF 75,000_1 January 2023

**Description:**

> **What needs updating**
>
> In CT-A-620 (CI: Specifications), regulation **4061 – CNPS (Family Benefits, Maternity, Injury) Base**, band `LTE(58216;1)` (non-apprentice):
>
> | Field | Current | New |
> |---|---|---|
> | Floor Amount | 840,000.00 | 900,000.00 |
> | Ceiling Amount | 840,000.00 | 900,000.00 |
>
> 900,000 = XOF 75,000/month × 12, following the same annual logic already used in reg. 4031 (pension: 900,000 / 40,500,000).
>
> **Effective date:** 1 January 2023.
>
> **No change** to reg. 4031 (pension floor/ceiling), to the rates (PF 5%, AM 0.75%, AT/MP per employer class) or to the apprentice band `EQUALS(58216;2)`.
>
> **Why**
>
> The XOF 70,000 ceiling (840,000/year) dates from before 2023, when the SMIG was XOF 60,000. Decree n° 2022-986 of 21/12/2022 raised the SMIG to XOF 75,000, and from 1 January 2023 the CNPS set the monthly floor for all branches at XOF 75,000, the ceiling for Family Benefits, Maternity and Work Injury at XOF 75,000 and the pension ceiling at XOF 3,375,000.
>
> **Sources**
> - CNPS communiqué "Nouveau plafond des cotisations sociales de la CNPS" (published 11/01/2023): https://www.cnps.ci/wp-content/uploads/2023/01/NOUVEAU-PLAFOND-DES-COTISATIONS-SOCIALES-DE-LA-CNPS.pdf (attached)
> - Law n° 99-477 (Code de Prévoyance Sociale), art. 23
>
> **Related:** HRBS-14996 (Baker Hughes, Côte d'Ivoire); email thread "Ceiling for Ivory coast" (15–19/10/2026).

Anexo: `raw/docs/oficiais/CI/2026-10-15-CNPS-communique-nouveau-plafond-2023.pdf`.

## Rascunho no YouTrack (21/10)
- Draft privado `2-126271` criado pela API (`users/me/drafts`), com o communiqué anexado: https://youtrack.hrblizz.dev/newIssue?draftId=2-126271. A issue **não foi criada**: o usuário revisa e clica em Create.
- Campos em vermelho (provavelmente obrigatórios): Start date, Due Date, Original estimation. Quem preenche é o usuário.
- Mohit perguntou na thread (21/10): "the only change is … Contribution base Ceiling update to 75000 from 70000 right." Resposta conferida: sim, só a reg. 4061; Floor e Ceiling estão os dois em 840.000/ano e os dois vão para 900.000.

- 21/10: Original estimation e Estimation = 2d (como no CT-4600; CT-4585 tem 1d), gravados pela API a pedido do usuário. Start date 21/11/2026 e Due Date 30/11/2026 já aparecem no draft; não foram gravados por esta janela.

- 21/10, reconferência: artigo CT-A-620 **atual** (API; atualizado por mjain em 2026-10-09) ainda tem a reg. 9384061 com 840000.00/840000.00 (`LTE($58216;1)`) e 450000/450000 (aprendiz); 840.000 e 70.000 não aparecem em nenhuma outra reg.; a reg. 9384024 (pensão cumulativa) já usa 75.000 e 3.375.000 mensais × períodos ativos (63955). URL do communiqué no ar (200, 148.483 bytes, Last-Modified 11/01/2023). SMIG: nenhum decreto posterior ao 2022-986 até out/2026 (⚠️ só fontes secundárias: africapaierh.com). Descrição do draft reescrita: "só uma regulação muda", motivo de piso e teto mudarem juntos, aprendiz "fora do pedido" (em vez de "sem mudança"), art. 23 descrito pelo que diz, origem do 70.000 = guia CNPS 2021.

- 21/10: a pergunta do Mohit veio pelo Google Chat (espaço Product Compliance Team; antes, às 9:26, "Do we need to updating any ceiling in Ivory Coast?" e o usuário respondeu que estava criando a task). Decisão do usuário: confirmar e apontar para a task. Rascunho digitado na thread da mensagem, **NÃO enviado**: "Yes, that's right. Only reg. 9384061 CI CNPS (Family Benefits, Maternity, Injury) Base changes: from 70,000 to 75,000/month, effective 1 Jan 2023. The details are in the task: CT-XXXX" (trocar CT-XXXX pelo ID).

- 21/10, a pedido do usuário: descrição do draft encurtada para só o teto (70.000 → 75.000/mês; reg. 9384061 Ceiling 840.000 → 900.000), com link do CCG v1.3 (Google Doc 1RDDBCD4eX7uwteYmedM4lmrX-vYa9lNwjmoUZ3Ouid0, Módulo 5). CCG v1.3 (Downloads, md5 ee7131e5…) conferido: já usa 75.000 em tudo, sem 70.000/840.000; não precisa de alteração. O Floor da reg. 4061 (também 840.000) saiu da task por decisão do usuário.

## Depois de criar
- Responder ao Mohit na thread com o ID da task (rascunho pela janela Gmail).
- Registrar no hub [[Costa-do-Marfim]] (Suporte) e em [[log]].
