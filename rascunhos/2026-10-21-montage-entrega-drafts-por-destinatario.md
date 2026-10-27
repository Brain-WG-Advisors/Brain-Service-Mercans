# Montage P09–P13 — drafts por destinatário (2026-10-21)

Nada enviado. Ordem de uso de cima para baixo. Base: [[2026-10-21-pedido-automation-V3-P12-P13]], [[2026-10-21-yojana-manju-p9p13]], conferência em `internal-certification/Netherlands/Mammoet Montage - P12-2025/2026-10-21-V3/CONFERENCIA.md`.

| # | Para | Onde | Quando | Para quê |
|---|---|---|---|---|
| 1 | Yojana | DM Google Chat | Agora | Saber se ela criou a pasta "P9 to P13" e qual versão vale |
| 2 | Manju | DM Google Chat | Agora | Responder "What about our P9 to P11" |
| 3 | Marko | DM Google Chat | Depois do ok da Yojana/Manju e da V3 no Drive | Mandar a V3 para revalidação e confirmar o EM-01 |
| 4 | Manju | chat "Mammoet defetcs - Oct 20" | Junto com o nº 3 | Avisar que foi entregue e o que mudou em valores |
| 5 | AUTOMATION | chat claude.ai | Quando quiser | Registro do que foi feito fora dele (memória: registrar no AUTOMATION) |

---

## 1. Yojana — DM (agora)
> Hi Yojana, did you create the "P9 to P13" folder in Final deliverables › Mammoet Montage today (forensic audit v1.0 and corrected sets P09–P13)? We have P12 and P13 V3 ready on top of our final deliverables, with Marko's v3.0 findings corrected. Should the Montage deliverables follow your set or ours?

**Por quê:** a pasta nova corrige os arquivos originais e não trata o TSF (EH-01, EH-02, EM-03 do Marko); a nossa V3 corrige o que o Marko apontou. Não substituir P12/P13 no Drive antes dessa resposta.

## 2. Manju — DM (agora)
> P9 to P11 don't need new files: Marko's v3.0 has no finding that changes them, and the 10000727 premium-base fix for those periods is in the P13 V3 return as correction blocks. The only open point from the other folder is the BSN masking in the payment reports, which I can apply to P09–P13 if we keep our set. I'm checking with Yojana now.

**Por quê:** ela perguntou "What about our P9 to P11". Conferido no Drive: nossos P09–P11 já têm o código de tabela 014/015 e não têm o AWf-herzien indevido; só falta o BSN mascarado.

## 3. Marko — DM (depois do ok e da V3 no Drive)
> Hi Marko, P12 and P13 are updated for your v3.0 report (V3, 6 files per period plus a Corrections Log), with the response note v1.2: [link P12] [link P13] [link nota]
> EH-01, EH-02, EM-02 and EM-03 are corrected (EM-03 also in the P13 own period, same defect). EM-01 is kept: Handboek 2025 §11.2.9 defines the LB/PH wage as columns 3 + 4 + 5 − 7, so LnInGld + WrdLn − LnLbPh equals the pension and PAWW in all 30 relations (section 4 of the note). Could you confirm you're fine with EM-01 on that basis, and rerun your validation on the V3 files?
> Limits are in section 6: no XSD available, so the returns were checked against the Gegevensspecificaties 2025.

**Por quê:** Manju (11:20) "After changes you need to send it back to Marko"; (11:23) a dúvida do EM-01 vai para ele no chat ou em nota.

## 4. Manju — chat "Mammoet defetcs - Oct 20" (junto com o nº 3)
> Manju, P12 and P13 V3 are in Final deliverables and sent to Marko for revalidation. Amounts change: net pay P12 −€107.14 and P13 −€30.53; TSF payment +€270.70. EM-01 is kept with the Handboek basis, and I've asked Marko to confirm.

**Por quê:** a V3 muda o que foi pago e declarado; ela precisa saber antes de qualquer conversa com o cliente.

## 5. AUTOMATION — chat claude.ai (PT)
> REGISTRO — V3 P12/P13 baixado e conferido fora deste chat (21/10). Hashes dos 2 zips, da nota v1.2, dos 12 arquivos e dos 2 Corrections Logs iguais aos informados. Conferência independente: G2N V2→V3 só nos empregados esperados (P12 −107,14; P13 −30,53), SEPA = CtrlSum, GL débito = crédito e Net Wages = SEPA, TotGen 23.513/20.296, identidade do EM-01 mantida, VCR do EM-02 no XML do P13. Achada no Drive a pasta "P9 to P13" (forensic audit v1.0 sobre os sets recebidos); aguardando a Yojana/Manju para saber qual versão seguir. Drive ainda não atualizado.

---

## O que eu faço depois (não é mensagem)
- Se a nossa versão valer: copiar a V3 para `Final deliverables › Mammoet Montage › P12/` e `P13/` (substitui os 12 arquivos da V2) e a nota v1.2; conferir os hashes no Drive; pôr os links no nº 3.
- Se decidirem mascarar o BSN: pedir ao AUTOMATION nos Payment Reports de P09–P13 antes de subir.
