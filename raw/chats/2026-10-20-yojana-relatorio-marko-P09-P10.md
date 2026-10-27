# Chat "Mammoet defetcs - Oct 20" — Yojana, relatório do Marko P09–P10 (2026-10-20)

Lido pelo Claude in Chrome (chat) e pelo Google Docs (texto do documento via /mobilebasic).

## Conversa (resumo)
- 14:16 Yojana: está vendo com o Marko se ele quer fazer um sanity check da Montage. Manju: P09 e P10 fechados com validação pelas skills do Marko e do Imran, mais a nossa (Wallisson); "another check will definitely help". Manju passa os links (Final Deliverables e pasta Montage com os relatórios).
- 15:27 Yojana pede de novo o caminho; Manju repete os links. Depois, call (Yojana + Manju).
- ~16:00 Yojana compartilha o Google Doc **Mammoet_Montage_NL_P09-P10_2025_Forensic_Validation_Report_Mercans_v1_0_2026-10-20** (dono: Marko Taylor; id 1nweqBNu665ZfJijC0k8GKsW-fF7NYlF1JSH_wY8C8U0). Sem pergunta direta a nós.

## O documento (v1.0, "draft sample", preparado para Marko Taylor)
- Base: 12 relatórios "Final deliverables › Mammoet Montage › P09 e P10". **Hashes do inventário = P09 V12 e P10 V7** (os mesmos sets que validamos), não os arquivos de `x_Mammoet/Final Deliverables/Mammoet Montage BV` (customer set de set/2025, hashes diferentes).
- 92 testes, 176 resultados, 8.028 itens; 150 pass, 10 obs, 7 fail, 9 N/T.
- Opinião: QUALIFIED. 0 High, 1 Medium, 3 Low, 6 Observations; nenhum efeito em valor pago, imposto ou prêmio. Imposto final P09 10.341,48 e P10 9.860,00, exatos.
- Achados:
  - EM-01 (Medium, F-13): LnInGld = Ctrctln em todas as relações; pela regra dele, LnInGld deveria ser LnLbPh − WrdLn.
  - EL-01 (Low, G-13): o saldo de reserva no holerite P10 não é saldo acumulado (repete o P09 = 3 contribuições TSF do período).
  - EL-02 (Low, D-01): payment report sem payroll ID.
  - EL-03 (Low, B-08): GL sem descrição.
  - OB-01: TSF creditado em net wages payable, sem remessa ao fundo no set.
  - OB-02: conta debitora da SEPA é a mesma da Mammoet Nederland.
  - OB-03: base de prêmio acima do máximo do período/SV wage (método cumulativo).
  - OB-04: 58551 da G2N difere do holerite/declaração.
  - OB-05: reserva de vakantiegeld ≠ 8% (TSF; nenhuma para dois empregados staff).
  - OB-06: XML criado antes do fim do período.
