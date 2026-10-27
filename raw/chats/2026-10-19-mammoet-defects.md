# Google Chat — "Mammoet Defects - Oct 19" (meeting chat) — 2026-10-19 18:08 → ~22:50

Lido via Claude in Chrome. Nomes de empregados omitidos (regra 3). Participantes: Suresh Jalihal, Yojana Bonagir ("Yoyo"), Imran Sayyad, Manju Shetija, Wallisson.

- 18:08 Suresh: P10 ainda aberto (anexo "Mammoet NL — P10 2025 Validation Report.docx"): AOW sem crédito (2 empregados €40,85/período abaixo da tabela; 1 com €43,15 não retido); mês de início AOW (1 ~€318 sub-retido, 1 €146,71 sobre-retido, 1 special-rate com taxa sub-AOW); transition payment €1.085,39 sem imposto (€433,07) e fora do special-rate wage do XML; licença parental não paga ~€1.249 sobre-retido em 5; XML: 47 conflitos de tipo de contrato × payslips, 26 registros de licença não paga sem código "O", 7 registros de correção com prêmio ≠ base × taxa; sem bloco de correção P09; return P10 completo datado 2026.
- 18:16 Suresh: @Wallisson checar se esses achados ainda precisam ser corrigidos. 18:19 Wallisson: checking.
- 18:21 Yojana: "Client Findings - G2N-Mammoet_P9-P13_Claimed-Issue-Log_Mercans_v1_0_2026-09-16 (1).xlsx".
- 18:25–18:52 Imran: Forensic_Audit_Exception_Register _3, _4 (versão curta só com variâncias), _5 ("4 Variances").
- 18:44 Wallisson: Corrections_Log v1.3 + CORRECTED_v1.3.zip ("P10 updated"). 19:26–19:30: Corrections_Log v1.4 + CORRECTED_v1.4.zip.
- 20:04 Wallisson: "Any news guys!?" 20:15 Yojana: "am working on p10 final set". **20:38 Wallisson: "ok, waiting..."**
- 20:57 / 21:04 Manju: Mammoet_NL_P10_2025_Forensic_Validation_Report_Mercans_v1.0_2026-10-20.docx.
- 21:04 Wallisson: o relatório não cobre o nosso set (nenhum dos 6 hashes bate com v1.1–v1.4 nem com o court set; população diferente: 689 IKVs, 9 blocos de correção, TotTeBet €986.104 com +€319.041, 1.537 payslips incl. 856 retro, SEPA €2.296.214,36 × v1.4: 694 IKVs, TotTeBet €1.316.751 com −€50.323, 701 payslips, SEPA €2.292.974,64). Testes do relatório rodados na v1.4: nenhum defeito. Pede confirmação de quais arquivos P10 foram usados e acordo sobre o set final.
- 21:07 Wallisson: o SEPA deles é do run P10 de 27-10-2025 (o nosso v1.4 parte do run regular de 25-09). Diferença €38.717 no valor devido (deles TotGen €1.305.145 com correções P01–P09 dentro do return P10; nosso TotGen €1.266.428 com P09 em return próprio). Pedidos: (1) os 6 arquivos do set 27-10 para testar a tese "o return de 27-10 copiou valores de P11"; (2) decisão sobre qual run P10 é a referência.
- 21:17 Wallisson: @Manju pode ajudar? 21:26–21:27 Manju: report _2; "I didn't get the question"; "It is V5 for P10 which is considered". 21:34 Wallisson: entendeu; "You're running something in parallel"; "I've given to AI V5".
- 21:52 Yojana: pasta Drive "Skillfiles" (drive.google.com/drive/folders/1T351Hd5aWVj1cLwKzssD45HNnUQvdN7N) + yoyo-nl-payroll-forensic-suite_v3.1.skill.
- 21:54 Manju: @Wallisson "take up Montage entity and validate against the skill files provided by Yoyo … and regenerate the final output"; "once you regenerate do one final validation with Marko's skill file"; "Can you join the call once to discuss?"
- ~22:00 Manju: "@Wallisson there?"; "We will pick up P11 once we resume after few hours. Can you please take up Montage as its a smaller entity and do the above"; "This will help to conclude on one entity".
- ~22:45 Wallisson: "should I start with P09?" / "did not get it".
