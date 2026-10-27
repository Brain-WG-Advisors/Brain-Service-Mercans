# Google Chat — DM Marko Taylor + "Mammoet defetcs - Oct 20" — 2026-10-21

Lido via Claude in Chrome em 2026-10-21. IDs de empregado mantidos só como PersNr (sem nomes; regra 3).

## DM Marko Taylor
- 20/10 22:11 Wallisson: "Hi Marko, please review. Final deliverables updated, 6 files per period" + links P09 (V14), P10 (V9), P11 (V7), P12, P13.
- 21/10 04:14 Marko: só um link, sem texto — Google Doc 12NysdKVHiG8f4lRept_QnN5ZyGzoPhAxSdUaJC_vYVo
  "Mammoet_Montage_NL_P09-P13_2025_Forensic_Validation_Report_Mercans_v3_0_2026-10-21" (v3.0, "draft sample", Draft for review).

## Relatório v3.0 (resumo do conteúdo)
- Base: Final deliverables › Mammoet Montage P09–P13 (30 arquivos, hashes no §2.2).
- Opinião: **QUALIFIED** — 5 erros (2 High, 3 Medium, 0 Low) + 8 Observations. 92 testes, 449 resultados, 20.542 itens; 99,35% itens OK (99,80% só erros).
- Ties: payslip ↔ G2N 441 valores 0 dif.; GL 698 valores 0 dif.; 31 pagamentos €104.048,05 0 dif.; imposto final P09 €11.125,74, P10 €9.969,01, P11 €20.604,05, P12 €11.503,70, P13 €13.142,46 "all exact".
- **EH-01 (High, net pay)** — P12: 10000723 sem TSF holiday pay (65802) e com 65803/65804; 10,725% × €3.756,57 = €402,89; P13 só acrescenta €17,48 → falta €385,41; saldo da reserva cai de €4.200,97 (P11) a €0,00 em P12. Ação: lançar €385,41 em P12 (com LH/prêmios), corrigir a declaração P12, remeter ao fundo.
- **EH-02 (High, net pay)** — P12: TSF holiday pay lançado para 10000726 (P06–P09 retro: €111,09) e 10000736 (€90,55), que não participam do TSF; sem taxa consistente; P13 não estorna. Ação: estornar e corrigir P06–P09 na próxima declaração; confirmar arranjo de vakantiegeld.
- **EM-01 (Medium, filing)** — LnInGld = Ctrctln em vez de LnLbPh − WrdLn em todas as relações P09–P13 (ex.: 10000723 P12 €4.720,69 vs €4.471,57; P13 €5.416,54 vs €5.167,53). Ação: corrigir mapeamento e declarar correções.
- **EM-02 (Medium, filing)** — 10000727: método de premieloon inconsistente (P02–P04 e P09 por período; P10, P12, P13 cumulativo, P12 €6.631,80 e P13 €6.211,19 acima do teto €5.835,69); total do ano correto. Ação: um método só; corrigir P02–P11 e estornar catch-up P12–P13.
- **EM-03 (Medium, net pay)** — P12 TSF holiday pay de 10000727/730/735 sobre salário antes do aumento CAO (€3.067,20 em vez de €3.206,30); P13 ajusta P05–P11 mas não P12: €13,48 + €14,06 + €12,89 = €40,43.
- Observations: OB-01 TSF €16.136,25 creditado em 21501800 sem remessa ao fundo no set; OB-02 conta debitora compartilhada com Mammoet Nederland; OB-03 SEPA P13 criado 18/12 19:52 UTC para execução no mesmo dia; OB-04 remittance P11/P12 com mês calendário; OB-05 teto de premieloon reduzido por licença não remunerada (10000726, €4.085,10); OB-06 58551 da G2N ≠ holerite; OB-07 reserva de vakantiegeld ≠ 8% (726/736 sem reserva); OB-08 declarações criadas no último dia do período.
- Conclusão (§6): "correct in net pay, payment and the wage tax filed"; abertos = TSF do retro P12, LnInGld, método de premieloon, 8 observações.

## Chat "Mammoet defetcs - Oct 20" (de 20/10 21:08 a 21/10)
- 20/10 21:08 Wallisson → Manju: "please review. Final deliverables updated, 6 files per period" (P09 V14, P10 V9, P11 V7 + 2 links).
- 21:13 Manju: "We need to change P12 and P13 after validating it basis Marko's skill file. Else there will be multiple observations". 21:16 "Otherwise folder looks fine".
- (mensagem apagada pelo autor)
- 22:33 Wallisson: "Done. P12 and P13 were validated with Marko's skill and corrected (V2), on the same basis as P09–P11. Both returns are rebuilt on the corrected chain: TSF indicator and holiday fields, travel allowance, contract wage and wage in cash, and the correction blocks with their saldi. […] Net pay and tax/premiums per employee are unchanged. […] P12 goes from €24,046 to €23,399 (−€647) and P13 from €20,239 to €20,257 (+€18). Each set has a Corrections Log, and the response note is updated to v1.1 for P09–P13."
- 21/10 01:16 Manju: "Have you send the files to Marko?" — 01:34 Wallisson: "Yes"; 01:35 encaminhou a mensagem ao Marko.
- 01:36 Manju: "Any feedback received?" — 02:30 Wallisson: "No response yet".
- (~10:xx) Yojana → Manju: "can u pls correct the names for the p11 and p12 for NL pls" / "Shared drives/x_Mammoet/Mammoet defetcs 2026/Final deliverables/Mammoet_Nederland/P11 P12/P11 P12 V1" / "also correct the generatio dates if any". Manju: "Sure Yoyo".
- Manju → @Wallisson: "have you got the feedback on Montage" (sem resposta nossa no momento da leitura).
