# BE-WTC — aba "Wage Type Catalogue_Final_BA" da Suman (2026-11-03)

Ligado a [[Belgica]] e [[Research Pipeline/Belgium/2026-10-21-wtc-series-62-65-74/CONFERENCIA|CONFERENCIA 62/65/79]].

## Pedido (Suman Rai, DM Google Chat, 03/11 10:53–11:24)
"Just fill in Column P,Q,R,S,T and G against those element… where its blank, I need this today. Design submission deadline is tomorrow"; "Valid input is only either Yes or No, not both"; "Please dont change it".

## Planilha
- gsheet `BE-WTC-001-v1.3` (id 1FoWGN4t0mUIM6WgzlQID91rWP4W__MxkagSPteuv4H4), Drive `Country Folders/Belgium/03 - WTC`.
- Histórico: 23/10 13:27 Wallisson Gomes (versão com VC 1.3 = "Belgian legislation in force from 1 November 2026… BE-060 row 829"); 03/11 06:40–11:22 Suman (renomeou a aba para "_RA" e criou "_Final_BA", 728 códigos 62/65/79, sem coluna F).
- **Duas v1.3:** (A) nossa local = v1.2 + 355 códigos All Codes (este cérebro, 22/10); (B) este gsheet = v1.2 + legislação 1º/11 + BE-060, feita pelo Claude via claude.ai em 22/10, sem registro aqui. Unificar numa v1.4 depois da entrega da Suman.

## O que foi gravado (03/11, com ok do usuário, só na aba _Final_BA)
- 360 linhas com G/P/Q/R em branco ("those elements"):
  - G e P–R vazios (603 células): da aba _RA (mesmo código); os 112 códigos que só existem na A (65508, 65509, 65609, 65659 e contadores 79) vieram da v1.3 local (108 contadores = NA).
  - S/T (720 células), benchmark WTC de produção Espanha V4.3 e Singapura V4.2: Earning → "Yes" / "Include in YTD."; Intermediary → "No" / "Counter, not a payment; no YTD load."; Earning com G e Q = NA → "No" / "Not used in Belgian payroll; no YTD load."
- 39 células "Yes-No" → valor único (nenhuma WTC de produção usa Yes-No; Espanha separa em colunas):
  - Q/R = Yes: 62160–62162, 62305, 62920, 79401, 79450, 79452 (13,07% pessoal comum devido; patronal só na parte simples/nenhuma — limitação da coluna única).
  - Q/R = No: 62210–62218, 62877, 62878, 62880, 62882 (contribuições especiais no lugar das comuns: 33%/13,07% solidariedade, estudante, BE-053, Decava BE-054).
  - N = Yes: 62182 (indenizações de proteção).
- Conferência por export CSV: 1.362 células alteradas = 603 + 720 + 39; 0 fora do permitido; 0 divergência. Incidente: colagem vazou em 102 células (P447–450, G–K456–459, P456–469, H–K455, H–K549–563); restauradas com os valores originais e reconferidas.

## Fora do pedido (não mexido, não enviado)
- 120 células G preenchidas pela Suman divergem da _RA/v1.3 (série 65 parece deslocada; 79xxx com 250 onde a fonte diz NA).
- N e O vazios nos 112 códigos novos.

## Frentes que mexeram
- 2026-11-03 · Chat · preenchimento da _Final_BA (acima).

## 2026-11-04 · Chat · 2ª rodada (pedidos da Suman de 03–04/11, resposta enviada pelo usuário)
- Cabeçalhos: O "Tax - Periodic scale", P "Tax - Special rate", Q "Ordinary SS - Employee", R **nova** "Ordinary SS - Employer", S "Special SS Contribution" (antes "Subject to Pension"); YTD Load/Remarks deslocados de S/T para T/U (sem inserir coluna: reescrita N2:U729, porque o menu Inserir não abria).
- Valores: NA e vazio → No em N–Q (23 Earnings + 108 contadores); 65508/65509/65609/65659 N/O = Yes/Yes; 62811 = Yes/Yes/No/Yes/Yes/Yes e G 250 (valor fixo de estacionamento = salário); 62810 tudo No (reembolso de custo do empregador); ER e Special = EE, exceto duplo pecúlio 62160–62162 (ER No, Special No; ONSS 2026/3).
- Fontes: Anexo III 2026 nº 58; ONSS 2026/3 (contribuição especial, duplo pecúlio, taxa global, reembolso de custos); Belcotax 2025 ficha 281.10.
- Incidente: 1ª tentativa com a janela do Chrome minimizada e **filtro da Suman ativo (P = Yes)** → colagem deslocada (N–U em ~715 linhas, linhas 809–925, G316). Corrigido restaurando a versão das 11:56 (última da Suman) pelo histórico, tirando o filtro, recolando e **recolocando o filtro P = Yes** (119 de 807 linhas, igual a antes).
- Conferência por export CSV: N–U = calculado em 728 linhas (0 diferenças); A–M iguais ao original salvo G282 (62811 = 250); nada abaixo da linha 729.
- Pendências: pecúlio de saída 62305/62920/79401/79450/79452 numa linha só (parte simples EE+ER, dupla só EE sobre 6,80%) → ER "Yes" é aproximação; ideal separar em dois códigos. Cabeçalho U sem a formatação das demais. Fora do pedido (não mexido): 62645/62646 Category; 65509 G 252.

## 2026-11-04 · Chat · coluna "Special Rate Table (Annex III)" + comentários da CCG
- Coluna V nova na _Final_BA (com ok do usuário): 119 linhas Special = Yes classificadas (nr. 53 exceptional 65; nr. 58 arrears 28; nr. 53 holiday 8; nr. 62 notice 3; outro: winstpremie 7% 4; nr. 80 SWT 1; Open 10) e 609 "None (periodic scale)". Fonte: Anexo III 2026 nºs 53, 58, 62, 80 (conferidos no PDF oficial). Lista e erros achados em `rascunhos/2026-11-04-resposta-suman-wtc-be.md`.
- Filtro P = Yes liberado e recolocado (119 de 807). Export: V = calculado em 728 linhas; colunas A–U inalteradas; nada abaixo da 729.
- CCG BE v1.1 (Drive): respondidos com ok do usuário os 4 comentários da Suman de 04/11 (9:26, 9:44, 10:39, 10:43), postados às 13:44–13:45 e conferidos no fio.
