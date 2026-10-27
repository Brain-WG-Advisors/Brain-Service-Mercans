# Análise — relatório v3.0 do Marko (Montage P09–P13) × o que dissemos no chat — 2026-10-21

Fonte: [[2026-10-21-marko-relatorio-v3-e-mammoet-defects]] (raw/chats). Anterior: [[2026-10-20-analise-relatorio-marko-P09-P10]].

## 1. Base é a nossa entrega final
Os 12 hashes de P12 e P13 no §2.2 do Marko = os nossos V2 (`internal-certification/Netherlands/Mammoet Montage - P12-2025/2026-10-20-V2` e `- P13-2025/...`), conferidos um a um (SHA-256, 16 primeiros). O relatório avalia exatamente o que entregamos em 20/10 22:11.

## 2. Achado por achado
| Ref | Marko | Conferência nossa | Leitura |
|---|---|---|---|
| EH-01 (High) | 10000723 sem 65802 TSF holiday pay em P12; faltam €385,41 | G2N P12 V2: 65802 = 0,00, 65803 = 418,67, 65804 = 263,65. G2N **idêntica ao intake** (mesmo hash c8b72ff4…) → vem do cálculo original da folha, não da nossa correção. | Procede como fato. É cálculo de folha (muda pagamento ao fundo, LH e prêmios): exige recálculo no sistema, não correção de arquivo. |
| EH-02 (High) | TSF holiday pay para 10000726 (€111,09) e 10000736 (€90,55), que não participam do TSF | G2N P12: 65802 = 111,09 e 90,55; 65803/65804 = 0. Também original do sistema. | Procede como fato; mesma natureza do EH-01. |
| EM-03 (Medium) | TSF P12 de 727/730/735 sobre salário pré-aumento CAO; €40,43 | Não refeito (precisa da taxa e da base CAO). | Mesma natureza (retro CAO no P12). Conferir antes de aceitar o valor. |
| EM-01 (Medium) | LnInGld = Ctrctln em vez de LnLbPh − WrdLn | É o **mesmo ponto do v1.0**. Nossa correção (Corrections Logs P12/P13, "decision 24–29 basis") pôs LnInGld = Ctrctln de propósito. Ex.: 10000723 P12: 4.720,69 + 1.106,73 − 5.578,30 = 249,12 = kolom 7 (pensão + PAWW). Handboek 2025 §11.2.9 (loon LB/PH = kolom 3 + 4 + 5 − 7) e §11.2.6. | Mantemos a posição do v1.0: a fórmula dele omite a kolom 7. O v3.0 não responde ao argumento da nota v1.1 (não se sabe se ele leu). |
| EM-02 (Medium) | Método de premieloon inconsistente para 10000727 (período × cumulativo); total do ano correto | Não refeito. No v1.0 era OB-03 ("consistente com o método cumulativo"); agora virou erro. | Conferir P01–P13 do 727 antes de responder. Se for, é parametrização do sistema. |
| OB-01…08 | TSF não remetido; conta da Nederland; SEPA P13 19:52 UTC; remittance mês calendário P11/P12; teto reduzido 726; 58551; reserva ≠ 8%; XML no último dia | OB-01/02/06/07/08 já estavam no v1.0 e na nota. Novos: OB-03, OB-04, OB-05. | Observações (evidência fora do set). |

## 3. O que dissemos × o que o relatório mostra
- 20/10 22:33 dissemos: "P12 and P13 were validated with Marko's skill and corrected (V2) … Net pay and tax/premiums per employee are unchanged."
  - **Coerente** com o relatório: ele confirma net pay, pagamentos e imposto final "all exact"; a correção nas declarações (cadeia de correções, BIC, datas, ID, GL) não aparece como defeito.
  - **Ponto fraco**: a frase "validated with Marko's skill" fica exposta, porque o v3.0 traz 2 High + 3 Medium. Os High/EM-03 estão na G2N original (que não mexemos, por regra: pagamento não muda) e o EM-02 era observação no v1.0; a skill dele evoluiu ou a nossa execução não pegou esses testes (G-13/G-14/H-05/F-08). Não está provado qual dos dois.
  - "contract wage and wage in cash" foram reconstruídos → é exatamente o EM-01 que ele mantém.
- 21/10 02:30 dissemos à Manju "No response yet": correto na hora; o relatório chegou às 04:14.
- Manju perguntou de novo ("have you got the feedback on Montage") — **sem resposta nossa**.

## 4. Decisões que são do usuário
1. Responder à Manju agora com o resumo e o link (recomendado: ela conduz a Montage com você, Yojana pediu os dois fechando).
2. EH-01/EH-02/EM-03: são recálculo de folha (dinheiro ao fundo, LH, prêmios) — fora do que corrigimos em arquivo. Recomendado: tratar como achado para a folha/cliente, não refazer XML.
3. EM-01: manter a contestação (já está na nota v1.1) ou alinhar com o Marko numa conversa curta.

## 5. Rascunho à Manju (EN, para colar — não enviado)
Hi Manju, yes — Marko sent his report at 4:14 AM: https://docs.google.com/document/d/12NysdKVHiG8f4lRept_QnN5ZyGzoPhAxSdUaJC_vYVo/edit
It covers the final deliverables P09–P13 (same files, hashes match). Net pay, payments and final wage tax tie for all five periods. Open items: 2 High, 3 Medium, 8 Observations.
- EH-01, EH-02 and EM-03 are TSF holiday-pay amounts in the P12 CLA retro run (one employee without it, two non-participants with it, three without the true-up). They come from the original P12 register, so fixing them means a payroll recalculation, not a file correction.
- EM-01 (LnInGld) is the same point as in his v1.0, already answered in our note (Handboek 2025 §11.2.9: column 3 + 4 + 5 − 7).
- EM-02 is the premium-wage method for one employee (10000727); I'm checking it.
I'll come back with the proposal per item.

## 6. Atualização 21/10 (depois do envio ao Marko)
- Manju no chat: "Wallisson this is after you sent the note also for our points" / "EM-01 is still coming" → o v3.0 já é a resposta do Marko à nota v1.1, e ele manteve o EM-01.
- Handboek 2025 (local `raw/docs/oficiais/NL/2026-10-20-handboek-loonheffingen-2025-okt-lh0221t53fd.pdf`), lido nesta data: §11.2.3 (p. 219), kolom 3 = "al het loon in geld"; §11.2.6 (p. 221), kolom 7 = pensioenpremie inhouden + PAWW; §11.2.9 (p. 222), kolom 14 = kolom 3 + 4 + 5 − 7. A posição sobre o EM-01 se mantém.
- Yojana × Manju sobre a NL P11 off-cycle: é da Nederland, não é conosco.

## 7. Rascunho à Manju (EN, para colar — não enviado)
Hi Manju, I went through Marko's v3.0. Two decisions are needed before we generate new files:
1. EH-01, EH-02 and EM-03 (TSF holiday pay in the P12 CLA retro) change amounts: P12 register, payslips, GL, the TSF payment and the P12/P13 returns. Until now the rule was that no paid or declared amount changes. Do we correct them in the deliverables, or report them as payroll items for a correction run?
2. EM-01: Handboek Loonheffingen 2025 §11.2.3 puts all cash wage in column 3, and §11.2.9 defines the LB/PH wage as columns 3 + 4 + 5 − 7, with column 7 holding the employee pension premium and PAWW (§11.2.6). Marko's LnLbPh − WrdLn takes column 7 out of the cash wage. Example, 10000723 P12: 4,720.69 + 1,106.73 − 5,578.30 = 249.12 (pension + PAWW). Do we keep it with this basis, or does Marko want it aligned to his rule anyway?
Meanwhile I'm checking EM-02 (premium-wage method, 10000727) and the EM-03 amounts.

## 8. Resposta do AUTOMATION ao pedido de análise (21/10)
| Achado | Veredito AUTOMATION | Prova / conferência |
|---|---|---|
| EH-01 | Procede | Taxa 723 = 10,725% sobre 62100 em P01–P11 e P13; P12 = 0,00; faltam 385,41; saldo corrigido 4.586,38 (P12) e 5.181,56 (P13). Taxas por empregado: 727 9,688%, 730 10,108%, 735 9,268%, 726/736 8,4% até P05. Artigo da CAO não está na pasta. |
| EH-02 | Procede | IndDeelnTijdspf N desde P06; 65802 de P06 estornado no P07; retro do P12 aplicou TSF sobre o aumento CAO em P06–P09 (726: 37,74 + 3 × 24,45 = 111,09; 736: 30,76 + 3 × 19,93 = 90,55). Causa provável, sem dado mestre. |
| EM-03 | Procede | 65802 P12 = taxa × 3.067,20 com 62100 = 3.206,30; faltam 13,48 / 14,06 / 12,89 = 40,43; P13 corrigiu P07–P11, não o P12. |
| EM-02 | "Depende" | Mistura de métodos; base anual 75.053,63 = SV acumulado < teto 75.863,97. Ficou em aberto se o Handboek exige um só método. **Conferido aqui:** Handboek 2025 cap. 6 (p. 90) — para os prêmios werknemersverzekeringen e Zvw "geldt de systematiek van het voortschrijdend cumulatief rekenen (VCR)"; p. 93 — "niet het maximumpremieloon per maand leidend, maar het cumulatieve maximumpremieloon". VCR é a regra → **EM-02 procede** por período (P02–P05 e P09–P12 abaixo do teto acumulado; ex. P02: SV acum. 11.784,77 > teto acum. 11.671,38, base acum. declarada 11.297,07); o total do ano está certo. |
| EM-01 | Não procede | 30/30 relações: LnInGld + WrdLn − LnLbPh = pensão + PAWW, diferença 0,00. Opção B = editar LnInGld em 173 registros (P09 62, P10 13, P11 12, P12 48, P13 38), sem mudar TotTeBet/saldos, mas contraria §11.2.9. |
| OB-03/04/05 | Ficam só na nota | OB-04 P12: falta conferir o texto da remessa no original …070856. OB-05: falta conferir dias SV no holerite. |

Impacto: EH-01/EM-03/EH-02 = recálculo da folha (G2N, holerites, GL, SEPA/payment report, declaração P12 + bloco P12 no P13, TSF líquido +224,20). Alternativa menor: lançar como retro do P12 num novo run do P13 (só o P13 muda). EM-02 = recálculo de prêmios patronais e bases (P10–P13 ou P02–P13). EM-01 opção B = só XML.
