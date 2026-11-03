# CCG Espanha v1.8 — descendentes e excesso da indenização (2026-11-02)

> Hub: [[Espanha]] · Anterior: [[Research Pipeline/Spain/2026-10-29-CCG-v1.7-HRBS-16407/CONFERENCIA|v1.7]] · País ativo → regra 9: ticket ao Development

## Origem
E-mail da Lily, "Fwd: Spain Migration Progress" (02/11/2026 09:16 e 10:21): (1) o excesso da indenização é rateado nos 12 meses anteriores ao mês do desligamento? (2) com 16 descendentes no DD, os acima do 4º entram no mínimo? Resposta: sim aos dois. Pedido do usuário (janela Gmail): citar o CCG na resposta, montar a v1.8, recalcular o exemplo, subir no Drive e trocar o link no YouTrack e no monday.

## Base
- `base/Spain_Payroll_Configuration_Guide_2026_v1_7.docx` = docx da v1.7 no Drive (md5 8cee645a6eaa64e2469eefeb854cc58d, igual ao local e ao Drive em 02/11). Alterações rastreadas no padrão da v1.7 (autor "Claude", data 2026-11-02). Script: `edit_v18.py` (só `word/document.xml`; as outras partes copiadas sem alteração).

## Final
- `Spain_Payroll_Configuration_Guide_2026_v1_8.docx` · md5 fffe1a08762dba132b3aeec60b53cdc8 · abre no Word (147 páginas, 84 revisões; v1.7: 146 e 75).

## Antes → depois (texto com as alterações aceitas)
| Seção | Antes (v1.7) | Depois (v1.8) | Fonte |
|---|---|---|---|
| Tabela de versões | — | Linha 1.8, 02-Nov-26, Updated, Wallisson Gomes | — |
| 6.1.1, 4. Family Minimums | "…€4,500 (4th+) per child." | + "For the withholding rate, each descendant counts by half unless the employee is exclusively entitled to the whole minimum (Art. 84.2.º RIRPF; Art. 61.1.ª LIRPF)." | RIRPF art. 84.2.º (`raw/docs/oficiais/ES/2026-10-19-BOE-RIRPF-arts80-88.txt` l. 159); LIRPF art. 61.1.ª (`2026-10-19-BOE-LIRPF-Ley35-2006-consolidado.txt` l. 2363) |
| 7.1, tabela, Descendant Minimum | "Must be < 25 years old or disabled, & living with employee." | + "For withholding, counted by half unless the employee is exclusively entitled (Art. 84.2.º RIRPF)." | RIRPF art. 84.2.º |
| 9.1, Treatment of Excess | "generally excluded… typically, pure severance is excluded" | Excluída só até o valor obrigatório (se o contrato termina antes da conciliação: até o valor da demissão improcedente, salvo saídas de mútuo acordo em planos coletivos de baixas incentivadas; despedimento coletivo (ET 51) ou objetivo do ET 52.c por causas ETOP/força maior: isento até o limite obrigatório da improcedente — LGSS 147.2.c, 3.º e 4.º parágrafos); o excesso entra na base e é rateado nos 12 meses anteriores ao mês do desligamento, qualquer que seja o dia | LGSS art. 147.2.c (`2026-10-27-BOE-LGSS-RDLeg8-2015-consolidado.txt` l. 3071); RD 2064/1995 art. 23.2.B (`2026-10-27-BOE-RD2064-1995-consolidado.txt` l. 729) |
| 9.1, ETP-002, Social Security | Excluded (generally) | Included only for the part above the exempt amount of Art. 147.2.c LGSS (see Treatment of Excess; no €180,000 cap), prorated over the 12 months before the termination month | idem |
| 9.1, exemplo, Ex-Gratia Severance, SS base | €0.00 (Excluded) | €36,712.60 (Included, prorated: €3,059.38 a month, Dec 2024 to Nov 2025) | idem |
| 9.1, exemplo, Step 8 (novo) | — | Excesso €36,712.60 ÷ 12 = €3,059.38/mês, dez/2024–nov/2025; €63,287.40 legal segue excluído; salário mensal €5.833,33 acima da base máxima de 2025 (€4.909,50, BNR 01/2025) → base de contingências comuns de jan–nov/2025 não sobe; parte acima → solidariedade (LGSS 19 bis e DT 42.ª, desde 2025); dez/2024: "apply the 2024 maximum base" (teto de 2024 não lido na fonte, por isso sem número) | LGSS 147.2.c; RD 2064/1995 23.2.B; LGSS art. 19 bis (l. 1156) e DT 42.ª (l. 11818); `2026-10-27-TGSS-BNR-01-2025.txt` l. 70 |

A seção de inclusão/exclusão da base de SS ("Severance (Excess) | YES | … prorated over the last 12 months") já estava certa na v1.7; a v1.8 alinha as três passagens que a contradiziam.

## Conferência
- Contas: 36.712,60 ÷ 12 = 3.059,383 → 3.059,38; 70.000 ÷ 12 = 5.833,33 > 5.101,20 (base máxima usada no próprio exemplo). Colunas de IRPF do exemplo não mudam (a v1.8 só toca a SS).
- Diff do texto aceito (v1.7 → v1.8): só as 6 passagens acima + a linha de versão.
- XML bem formado; zip íntegro (testzip); abre no Word.
- Google Doc convertido ("Save as Google Docs"): 76 sugestões do Claude; textos novos presentes como sugestões; linha 1.8 da tabela de versões conferida na tela. A referência "6.1.1 and 7.1 … (6.1.1) … (7.1)" da linha 1.8 foi corrigida no Google Doc por Localizar/substituir (1 ocorrência cada) e no docx (rebuild).

## Correções depois da 1ª conferência (02/11, ok do usuário)
- 9.1 Treatment of Excess: acrescentado o último parágrafo da LGSS 147.2.c (contrato extinto antes da conciliação → isento até o valor improcedente, salvo baixas incentivadas coletivas). Lido no BOE consolidado, l. 3071–3075.
- Step 8: retirado "declared as supplementary settlements (L03)" — sem fonte primária lida (vinha do hub/spec Bases).
- Google Doc ajustado por Localizar/substituir (1 ocorrência cada; conferido na tela). No Google Doc, o trecho trocado do Treatment of Excess ficou como texto normal dentro da sugestão do Claude; o texto final está igual ao docx.
- ETP-002 (2ª revisão, ok do usuário): o excesso do IRPF (teto €180.000, LIRPF 7.e) e o da SS (só o valor obrigatório, LGSS 147.2.c, sem teto) podem divergir; a célula passou a dizer "only for the part above the compulsory amount … no €180,000 cap". O exemplo não muda (os dois excessos são €36.712,60).
- Google Doc: uma tecla Ctrl+H com o editor ainda carregando digitou "hh" no 1º parágrafo; removido e conferido (texto simples do v1.8 = v1.7, salvo a célula ETP-002). A célula ETP-002 e o trecho novo do Treatment of Excess ficaram como edição direta, não sugestão; o texto final é igual ao docx.
- Descendentes (3ª revisão, ok do usuário): a regra da folha é a do RIRPF art. 84.2.º ("se computarán por mitad, excepto cuando el contribuyente tenga derecho, de forma exclusiva…"), não só a LIRPF 61.1.ª (imposto anual). 6.1.1, 7.1 e linha 1.8 trocados; e-mail da Lily ajustado. Google Doc: Localizar/substituir aberto pelo menu Editar (sem atalho); "split equally" 0 ocorrências, "84.2.º RIRPF" 3; texto simples = v1.7 salvo as 3 células/linhas previstas.
- Conferência final (02/11, ok do usuário, depois de "é tão difícil assim…?"): cada frase alterada relida contra o artigo inteiro (LGSS 147 completo, RD 2064/1995 art. 23 completo, LIRPF 58 e 61, RIRPF 84, LGSS 19 bis e DT 42.ª, BNR 01/2025) + hub + correcoes. Resultado: faltava o 4.º parágrafo da LGSS 147.2.c (coletivo/objetivo ETOP) → acrescentado; ETP-002 passou a remeter ao valor isento do 147.2.c; Step 8 só com o teto de 2025 lido. Google Doc: busca conferida (textos novos 1 ocorrência cada, "84.2.º RIRPF" 3; textos antigos 0); texto simples = v1.7 salvo 3 linhas previstas; 1.ª linha íntegra. Word: 147 páginas, 84 revisões.
- Coerência com outros artefatos (fora do pedido, não alterados): WTC V4.6 trata o 58188 como "non SS subject", a spec ES-CRA-001 reporta 58184/58186/58188 como 0054/E e a spec ES-BASES-001 (H39) diz que o excesso não entra no 500. Pela LGSS 147.2.c e pelo manual CRA, o excesso é base (I). Já estão nas Pendências do [[Espanha]]; decisão de design + ticket ao Dev.

## Drive
- docx: `Spain > 05 - Payroll Regulation Guide/Spain_Payroll_Configuration_Guide_2026_v1_8.docx` (id 18zVlQ01hbvTZfULJWXRpWV-CCUzK09wL), md5 igual ao local (fffe1a08…, depois das correções).
- Google Doc: https://docs.google.com/document/d/1553taH1yi_q26_Zy9gBgzT_rZHqfO8--RioLIyfwtjU/edit

## Pendente
- Link no HRBS-16407 e no monday (item 9278601265) → janela Suporte (pedido enviado em 02/11).
- Ticket de alteração ao Development (regra 9) → janela Suporte.
- Fora do pedido (não alterado): o exemplo do 9.1 termina em 31/12/2025 mas usa a base máxima de 2026 (€5.101,20); ETP-001/002 citam CRA 0008/0009/0053, e o hub registra 0054 para indenização (SR-81).

## Frentes que mexeram
| Data | Frente | O quê |
|---|---|---|
| 2026-11-02 | gmail | v1.8 criada (6.1.1/7.1 divisão do mínimo; 9.1 excesso da indenização na base de SS + exemplo recalculado); docx + Google Doc no Drive; rascunho da Lily citando a v1.8 |
| 2026-11-02 | suporte | `ticket-dev.md` (ticket ao Development: v1.7 + v1.8, 4 itens; fontes relidas: RIRPF 84.2.º (item 3, depois da correção), LGSS 147.2.c, RD 2064/1995 23.2.B); md5 do docx local conferido (98da7eca…); link no monday e comentário no HRBS-16407 preparados, aguardando ok do usuário na janela Suporte |
| 2026-11-02 | suporte | monday (item 9278601265) → "Spain Payroll Configuration Guide 2026 v1.8" + link 1553taH1… (gravado com ok do usuário, conferido 20:27 UTC); HRBS-16407: draft com o link da v1.8 à Lily (455 car., IGUAL), não publicado; `ticket-dev.md` atualizado (RIRPF 84.2.º; LGSS 147.2.c com ET 51/52.c) |
