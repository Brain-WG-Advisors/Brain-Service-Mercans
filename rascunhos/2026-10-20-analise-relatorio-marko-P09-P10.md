# Análise — relatório do Marko (P09–P10 Montage) enviado pela Yojana — 2026-10-20

Fonte: [[2026-10-20-yojana-relatorio-marko-P09-P10]] (raw/chats). Conferido por esta janela nos arquivos do Drive e no Handboek 2025.

## Base é a mesma
Os 12 hashes SHA-256 do inventário do Marko = P09 V12 (`Montage/P09/V2/Mammoet_Montage_P09_2025_V12_20261020`) e P10 V7 (`Montage/P10/V1/Mammoet_Montage_P10_V7`), conferidos um a um. Ele chama de "Final deliverables", mas são os sets V12/V7.

## Achado por achado
| Ref | Marko | Conferência | Conclusão |
|---|---|---|---|
| EM-01 | LnInGld deveria ser LnLbPh − WrdLn | Handboek 2025 §11.2.9: loon LB/PH = kolom 3 + 4 + 5 − 7; §11.2.6: kolom 7 = pensão do empregado e PAWW. P09 V12, PersNr …726: LnInGld 7.772,73 = 62100 6.739,58 + 62145 1.033,15; LnLbPh 7.926,32 = 7.772,73 + WrdLn 594,21 − pensão 434,78 − PAWW 5,84. …736: 5.494,34 + 842,28 = 6.336,62 = LnInGld; LnLbPh 6.486,69 fecha igual. Nosso F-13 passou 6/6. | **Não se sustenta.** A fórmula dele omite a kolom 7. LnInGld = Ctrctln porque o salário em dinheiro do período é base + abono recorrente. |
| EL-02 | Payment report sem payroll ID | O payment report emitido (Final Deliverables P09/P10) tem o mesmo layout (Organization, Country, Currency, Pay period, Number of employees); o modelo do HR Blizz não tem payroll ID. | Formato do sistema, não defeito do V12/V7; colocar o ID quebraria o gate de formato. Melhoria, no máximo. |
| EL-03 | GL sem descrição | Igual ao nosso (obs nos relatórios P09–P11). | Mesmo achado. |
| OB-06 | XML criado antes do fim do período | Igual ao nosso FND-03/S-01 (DatTdAanm). | Mesmo achado. |
| EL-01 | Saldo de reserva do holerite P10 não acumula | Não conferido. Com TSF, a contribuição vai ao fundo a cada período (§29.15), então "saldo" = contribuição do período pode ser o desenho. | É sobre rótulo, não erro de valor. Conferir antes de aceitar. |
| OB-01 | Remessa ao TSF não está no set | Fora do set (escopo da Manju). | Coerente com o nosso escopo. |
| OB-02 | Conta debitora compartilhada com a Nederland | O SEPA é o arquivo original, igual ao do customer set (hash 6c3fba9a). Extrato fora do escopo. | Configuração do cliente, não da folha. |
| OB-03 | Base de prêmio acima do teto do período | Ele mesmo diz que é consistente com o método cumulativo. | Observação. |
| OB-04 | 58551 da G2N ≠ holerite | Campo nocional interno; XML = holerite. | Observação interna. |
| OB-05 | Vakantiegeld ≠ 8% | TSF: vakantiegeld via fundo (§29.15). Dois empregados sem reserva: não conferido. | Pendente de checagem nossa antes de responder. |

## Rascunho (EN, para colar — não enviado)
Hi Yojana, thanks for sharing Marko's report. It's based on the same P09 V12 and P10 V7 files we validated (hashes match), and the amounts tie the same way (P09 €10,341.48, P10 €9,860.00).

One point to review before it goes further: EM-01 (LnInGld) doesn't hold. Handboek Loonheffingen 2025 §11.2.9 defines the wage for LB/PH as column 3 (wage in cash) + 4 + 5 − 7, and column 7 includes the employee pension premium and PAWW (§11.2.6). So the check is LnLbPh = LnInGld + WrdLn − pension − PAWW, not LnInGld = LnLbPh − WrdLn. For example, in P09 for 10000726: 7,772.73 + 594.21 − 434.78 − 5.84 = 7,926.32 = LnLbPh. Our P09 test on this identity passed for all 6 income relations.

EL-02: the payment report follows the issued HR Blizz layout, which has no payroll-ID field. The empty GL descriptions and the XML creation date match observations already in our reports.
