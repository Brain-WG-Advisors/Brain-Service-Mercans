# Noruega: fluxo das entregas ao governo (rascunho, 29/10/2026)

> Modelo do pedido (Manju, weekly 27/10, 10:41–11:30): para cada entrega, o que o **sistema** faz, o que o **cliente** faz e o que a **autoridade** faz. Hoje × como deveria ser × o que falta.
> Projeto: [[PLANO_fluxo_entregas_v0.2]] · Hub: [[Noruega]] · Pacote: `Norway/Henkel Norway - 2026-09/`.
> **Fontes:**
> - **S##** = `internal-certification/references/Norway/2026/sources.md` (lidas em 14/10);
> - **R1/R2/R3** = `raw/docs/oficiais/NO/2026-10-29-altinn3/skatteetaten_reetablering_{virksomheter,systemleverandor,regnskapsforer-revisor}.html` (baixadas em 29/10).

## Entrega 1: A-melding (mensal, até o dia 5; a-opplysningsforskriften § 2-1, S21)

| Quem | Como deveria ser (fonte oficial) | Como é hoje (evidência) | O que falta |
|---|---|---|---|
| **Sistema (HR Blizz)** | Envio pela API da Skatteetaten, "Fra 2026 er dette den eneste måten å sende inn a-melding fra system" (S05). Autenticação pelo Maskinporten com **systembruker**, "upersonlig bruker med fullmakt til å utføre definerte oppgaver på vegne av en virksomhet"; o login antigo pelo ID-porten "blir fjernet" (R2). O fornecedor registra o sistema no Altinn e define os tilgangspakker exigidos (R2). | O recibo de set/26 traz `"kildesystem":"HR Blizz"`, `altinnReferanse`, entrega em 2026-10-02T15:24 e `"mottakstatus":"mottatt"` sem `avvik` (`tilbakemelding (13).json`). | **Confirmar com o Dev:** o HR Blizz já usa systembruker/Maskinporten? Ou ainda usa Altinn II? |
| **Cliente (empregador)** | "Dersom du rapporterer gjennom et system (for eksempel lønnssystem) må du godkjenne tilgangspakkene som settes opp og gi systemet rettigheter til å levere på vegne av deg" (R1). | ⚠️ Não sabemos se a Henkel (ou cada cliente NO) já aprovou os tilgangspakker para o HR Blizz. | Confirmar por cliente NO: **até 17/11/2026**. |
| **Autoridade (Skatteetaten)** | Recebe, valida e devolve o tilbakemelding A03, com KID para pagamento (S02, S03). **Prazo crítico:** "17. november: A-melding" é a data em que a a-melding deixa de funcionar pelos papéis do Altinn II (R1, R2, R3). | Aceitou set/26 sem erro. | — |
| **BAU (Umesh)** | Sem passo manual, se o fluxo acima estiver completo. | ⚠️ Não perguntado: quem disparou o envio, se houve correção antes e se há terceiro. A certificação viu GL "CORRECTED" (C-01) e o sindicato sem fradrag (A-01, High). | Perguntas ao BAU ([[mensagens_BAU_v0.1]]). |

**Achado para o Marko (risco de "penalty/surprise", W27 13:08):**
- A a-melding sai dos papéis do Altinn II em **17/11/2026** (R1–R3).
- Se o HR Blizz ou os clientes NO ainda dependerem deles, a a-melding de outubro (prazo: 05/11) passa, mas a de novembro (prazo: 05/12) já não sairia pelo sistema.
- ⚠️ É um risco a confirmar com o Dev, não um defeito provado.

## Entrega 2: Pagamento de forskuddstrekk e AGA
- **Como deveria ser:** com o KID do A03 (S02). Forskuddstrekk no 1º dia útil depois do pagamento do salário; AGA a cada 2 meses, no dia 15 (skattebetalingsloven § 10-10, S13).
- **Como é hoje:** ⚠️ não visto. O pacote tem o bank file, mas não foi conferido se ele inclui o pagamento ao fisco.

## O que falta para fechar a Noruega
1. **Dev:** systembruker/Maskinporten em uso? Os tilgangspakker dos clientes NO estão aprovados antes de 17/11?
2. **BAU:** as 3 perguntas.
3. **Conferir o bank file** de set/26: pagamento de forskuddstrekk e AGA com KID.

## Bloco de prova
- **Teste:** os trechos de R1–R3 foram lidos direto do HTML baixado em 29/10 (busca por "17. november", "tilgangspakke", "Maskinporten"). O recibo JSON foi lido dentro do zip.
- **Confiança 85%:** as regras estão com fonte. Falta a resposta do Dev e do BAU para o "como é hoje", e a parte de "klientsystembruker" (fornecedor que atende vários clientes) não foi lida no texto original, só em resumo.
