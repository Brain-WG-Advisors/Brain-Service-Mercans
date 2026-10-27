# Auditoria — Wage Fund Classification (UA-1PV-001, mensal), linhas 401–578

Arquivo auditado: `M_Wage_Fund_Classification.txt`. A última linha preenchida é a 578. Não há linhas de rodapé, totais ou notas depois dela.
Fontes usadas:
- `SRC_instrucao5_2004_red2023.txt` (Instrução nº 5, red. 17.01.2023), referida abaixo como "Instr.";
- `SRC_rozyasnennia_trimestral.txt` (Роз’яснення 1-ПВ квартальна, secção IV);
- `SRC_rozyasnennia_mensal.txt`;
- `WTC_Wage_Type_Catalogue.txt` (V4.3).

Comparação mecânica (script) de A/B/C/D com o WTC V4.3: B↔B, C↔D (Category), D↔P (4DF). A coluna H foi conferida em todas as linhas: a fórmula `=IFERROR(VLOOKUP(A{r}, Sheet1!$A:$B, 2, FALSE), "")` está correta e aponta para a própria linha.

Mapa das linhas do formulário usado na análise (Роз’яснення trimestral, secção IV):
- 5020 = fundo básico (2.1);
- 5030 = fundo adicional (2.2);
- 5060 = pagamentos de incentivo e compensação (2.3);
- 5070 = **só ajuda material, subitem 2.3.3**;
- 5080 = benefícios sociais individuais (2.3.4);
- 5090 = tempo não trabalhado (2.2.12 + 2.3.1).

## (a) ERROS

| Linha | Célula | Atual | Correto | Citação da fonte | Por quê |
|---|---|---|---|---|---|
| 436–445 (65770–65779 "Recognition Award benefit") | F | `5070 (subset of 5060)` | `5060` (sem sub-linha) | Роз’яснення trim. IV.8: "Показник щодо матеріальної допомоги містить дані про суми нарахованої матеріальної допомоги, передбаченої підпунктом 2.3.3 пункту 2.3 глави 2 Інструкції". Instr. 2.3.2: "Винагороди та заохочення, що здійснюються раз на рік або мають одноразовий характер… одноразові заохочення, не пов’язані з конкретними результатами праці" | O bucket (INCENTIVE) e a razão (2.3.2) estão certos. Mas 5070 é exclusivamente ajuda material (2.3.3), e prêmio único não é ajuda material. A própria spec trimestral (Q_UA_1PV_002_Spec, X13) diz: "one-off bonuses (INCENTIVE, p. 2.3.2) have no sub-row and sit in 5060 only". A fórmula V14 da spec ("bucket='INCENTIVE' AND report_row='5070…'") carrega esses prêmios para 5070 indevidamente. |
| 446 (65800 Non-targeted material assistance) | C | `Earning` | `Benefit` | WTC D514 = "Benefit" | A categoria diverge do WTC V4.3. |
| 447 (65801 Gift/prize in-kind) | E / F / G | `BASIC` / `5020 / 1020,1070` / "2.1.7 -- pay in goods/in-kind valued in cash." | `INCENTIVE` / `5060` / 2.3.2 | Instr. 2.1.7: "Вартість продукції, виданої працівникам при натуральній формі оплати праці". Instr. 2.3.2: "одноразові заохочення, не пов’язані з конкретними результатами праці (наприклад, до ювілейних та пам'ятних дат, як у грошовій, так і натуральній формі)" | O 2.1.7 trata do salário pago em espécie (em substituição ao salário em dinheiro, art. 23 da Lei), não de presente ou prêmio. O WTC (AC515) descreve o código como "One-off payment not linked to work performed in a period", e o V515 como "one-off gift". Presente ou prêmio em espécie é incentivo único (2.3.2): vai para o 5060, não para o fundo básico 5020. |
| 418 (65630 Employer-paid voluntary medical insurance) | E / F / G | `SOCIAL_IND` / `5080 (subset of 5060)` / "2.3.4 -- employee-facing value… DISTINCT from 3.5" | `EXCLUDED` / Not in FOP / 3.5 | Instr. 2.3.4: "витрати в розмірі страхових внесків підприємств (**крім випадків, зазначених у п. 3.5**)…". Instr. 3.5: "Внески підприємств згідно з договорами добровільного медичного та пенсійного страхування працівників і членів їхніх сімей." | O próprio 2.3.4 remete o seguro médico voluntário ao 3.5. A distinção "valor para o empregado × prêmio pago à seguradora" não existe na Instrução. O WTC (B486/V486) descreve o código como "employer-paid insurance premiums", ou seja, é o prêmio. |
| 451 (65805) | B | `Benefit Earning` | `Medical Insurance (BIK)` | WTC B519 = "Medical Insurance (BIK)" (V519: "Renamed 2026-08-12… employer pays insurer directly") | Nome desatualizado em relação ao V4.3. |
| 451 (65805) | E / F / G | `SOCIAL_IND` / 5080 / "2.3.4-analogous" | `EXCLUDED` / 3.5 | Instr. 3.5 (citada acima). WTC V519: "Non-monetary form (employer pays insurer directly)" | É seguro médico voluntário pago pelo empregador, excluído pelo 3.5. |
| 453 (65807) | B | `Benefit Earning` | `Representation Expenses - Financial (BIK)` | WTC B521 | Nome divergente do V4.3. |
| 455 (65809) | B | `Benefit Earning` | `Family Insurance (BIK)` | WTC B523 | Nome divergente do V4.3. |
| 456 (65810) | B | `Benefit Earning` | `Additional Benefit` | WTC B524 = "Additional Benefit " | Nome divergente do V4.3. |
| 461 (65815) | B | `Benefit Earning` | `One-time payment due to martial law` | WTC B529 | Nome divergente do V4.3. |
| 451–505 (G comum) | G | "…the generic English name means individual instances were not reviewed one-by-one" | Retirar ou ajustar a afirmação | WTC B519/B521/B523/B524/B529 (nomes específicos acima) | No V4.3, 65805, 65807, 65809, 65810 e 65815 têm nome específico, e 65805 é seguro médico (3.5). A premissa "nome genérico" é falsa para essas linhas. A contagem "53 instances share 4DF=126" foi conferida e está certa. |
| 516 (79411 Bereavement Leave Payout) | E / F / G | `EXCLUDED` / Not in FOP / "3.31 -- one-off personal/family-circumstance assistance… excluded" | Dentro do FOP, pagamento por tempo não trabalhado: `UNWORKED` (5030/5090) se previsto em convenção coletiva (2.2.12), ou `UNWORKED_OTHER` (5060/5090) se não previsto em lei (2.3.1) | Instr. 3.31: "**Матеріальна допомога** разового характеру, що надається підприємством окремим працівникам у зв’язку із сімейними обставинами…". Instr. 2.2.12: "оплата додаткових відпусток (понад тривалість, передбачену законодавством), наданих відповідно до колективного договору". Instr. 2.3.1: "Нарахування за невідпрацьований час, не передбачені чинним законодавством". WTC AC584: "Paid absence compensated at average earnings." | O código é pagamento de dias de licença pela média salarial (WTC), não ajuda material. O 3.31 exclui ajuda material, não pagamento de licença. Pela Instrução, pagamento de tempo não trabalhado entra no FOP (2.2.12 ou 2.3.1); Роз’яснення trim. IV.10 manda os dois para a linha 5090. |
| 555–556 (79450, 79452) | G | "2.2.12 -- vacation pay ("Holiday Allowance" here uses the British-English sense…)" | Texto sem a referência a "Holiday Allowance" | WTC B623 = "Vacation Cashout Leave Payout"; B624 = "Vacation Cashout Leave Payout Adjustment" | A razão explica um nome ("Holiday Allowance") que não é o do código no V4.3 (sobra de versão antiga). Bucket e linha (2.2.12, compensação por férias não gozadas) estão corretos. |
| 576–578 (79497, 79498, 79499 "Other Leave Payout") | A / B / C / D | Códigos listados | Retirar, ou criar os códigos no WTC | WTC V4.3: a última linha da série é A643 = "79496.0" e não há 79497–79499. M_Sheet1 também termina a série em A643 = 79496. | Os códigos não existem no WTC V4.3. Por isso a coluna H (VLOOKUP no Sheet1) retorna "". Também não confere com o A1 da aba ("575 relevant wage types (…V3_7)"), que cita a V3.7 em vez da V4.3. A linha 1 está fora do meu intervalo, fica só como registro. |

## (b) Não determinável pela fonte

- **401–402 (65522/65523 Car Fuel Benefit, SOCIAL_IND 5080, 2.3.4).**
  - O 2.3.4 cobre "вартість проїзних квитків… та відшкодування… вартості проїзду транспортом загального користування" e "суми компенсації вартості виданого працівникам палива". O 3.22, ao contrário, exclui "Компенсації працівникам за використання для потреб виробництва… особистого транспорту".
  - O enquadramento depende de o combustível ser para uso pessoal (2.3.4) ou para uso no trabalho (3.22).
  - A razão G descreve a regra como "personal transport/car benefit (… notional car-benefit value)", mas a Instrução não menciona "car benefit".
- **429–434 (65700/65710 Maternity allowance (benefit) 1/2 e arrears/adjustments, EXCLUDED, 3.2).** O resultado EXCLUDED está correto em qualquer leitura. O WTC (AC497) diz que o código é "categorised as a Benefit, i.e. an employer payment rather than a state one". Se for complemento pago pela empresa, a base é o 3.4 ("Соціальні допомоги та виплати за рахунок коштів підприємства… на народження дитини"), não o 3.2 (fundos do Estado). Não dá para decidir sem a definição do cliente.
- **446 (65800 Non-targeted material assistance, MAT_ASSIST 5070, 2.3.3).**
  - O 2.3.3 só vale para ajuda "систематичний характер, надана всім або більшості працівників".
  - O WTC V514 descreve o código como "one-off/non-systematic". Ajuda única por circunstância familiar ou tratamento é excluída (3.31).
  - A Instrução não trata a ajuda única "não direcionada" a uma pessoa, e o Роз’яснення IV.8 só exclui a ajuda "разового характеру, необхідність отримання якої виникла раптово… за умови подання заяви".
  - Depende do uso real. O erro de categoria (C) já está registrado acima.
- **452 (65806 Representation Expenses, EXCLUDED, "1.3") × 453 (65807 Representation Expenses - Financial, SOCIAL_IND 5080).** A Instrução não menciona despesas de representação. O 1.3 é a definição geral do FOP. As duas linhas são o mesmo tipo de pagamento (WTC V521: "Paired with 65806") e foram classificadas de formas opostas. É uma inconsistência interna, mas a fonte não decide qual tratamento é o certo.
- **455 (65809 Family Insurance (BIK)).** Se for seguro médico ou de pensão da família, vale o 3.5 ("…медичного та пенсійного страхування працівників і членів їхніх сімей") e o código sai do FOP. Se for outro seguro voluntário pessoal, vale o 2.3.4 (5080). O WTC não diz o ramo.
- **456–505 exceto 461 (65810–65859, "Additional Benefit" e placeholders "Benefit Earning", 4DF 126, SOCIAL_IND 5080).** São placeholders sem conteúdo definido. O 4DF 126 é um sinal fiscal, não um critério da Instrução (1.1: "Інструкція не застосовується для визначення складових фонду оплати праці як бази… для нарахування внесків"). A classificação depende de como cada slot for configurado.
- **461 (65815 One-time payment due to martial law, SOCIAL_IND 5080).** O 2.3.4 trata de benefícios sociais (alimentação, seguro, moradia etc.). Pagamento único pode ser 2.3.2 (5060), 3.31 ou 3.33 (excluídos), conforme a finalidade. A Instrução não decide sem a definição do pagamento.
- **507 (79402 Emergency Leave Payout) e 509 (79404 Hajj Leave Payout), UNWORKED 2.2.12.** São licenças fora da lei. Pela Instrução, ficam no 2.2.12 se previstas em convenção coletiva, ou no 2.3.1 (UNWORKED_OTHER, 5060) se não estão previstas em lei. Divergência adicional: o WTC (AC575/AC577) as descreve como "Cash payment of an individual nature (p.2.3.4…)".
- **510 (79405 Marriage Leave Payout, EXCLUDED, 3.31).** O WTC (AC578) descreve o código como "One-off payment not linked to work performed", o que é compatível com o 3.31 se for ajuda única. Se for pagamento dos dias de licença, vale o mesmo raciocínio do 79411 (2.2.12/2.3.1, dentro do FOP). O nome "Leave Payout" sugere a segunda leitura.
- **512 (79407 Paternity Leave Payout, UNWORKED 2.2.12, "Law 'On Leave' art. 19-1… paid by the employer").** Os arquivos fornecidos não trazem a Lei "Про відпустки". Não foi possível confirmar se o art. 19-1 prevê licença paga.
- **521–554, 559–575 (79416, 79418–79449, 79480–79496 "Other Leave Payout", UNWORKED 2.2.12).** São slots genéricos. A G já prevê a reclassificação. Se a licença não for legal nem de convenção coletiva, a base passa a ser o 2.3.1 (UNWORKED_OTHER).

Observação sem classificação como erro: o WTC (AC de vários benefícios 126) diz "The payment is outside the wage fund". Essa frase se refere à base de ESV e de cálculo de média (Poryadok 100/1266), não à Instrução nº 5 (1.1). Não contradiz, por si só, o enquadramento em 2.3.4.

## (c) Contagem

- Linhas verificadas: **178** (401–578). Não há rodapé.
- Linhas com erro: **24** (418, 436–445, 446, 447, 451, 453, 455, 456, 461, 516, 555, 556, 576–578).
- Linhas só "não determinável": **61** (401–402, 429–434, 452, 457–505 exceto 461, 507, 509, 510, 512). As 446, 453, 455, 456 e 461 também têm ponto não determinável, mas já contam como erro. As 521–575 estão confirmadas com ressalva (ver lista).
- Linhas confirmadas: **93**.
  - Código, nome, categoria e 4DF batem com o WTC V4.3.
  - Bucket, linha e razão estão sustentados pela Instrução.
  - Grupos: per diem 3.15; telefone e refeição 2.3.4; ginástica 2.3.4 ("абонементів у групи здоров'я"); educação 3.10/3.24; serviços médicos 3.30; seguro de vida 2.3.4; doença 3.2/3.3; maternidade 3.2; férias não gozadas, estudo e doador 2.2.12; viagem a serviço 2.1.6; mobilização; unpaid leave 2.3.1; slots "Other Leave Payout" 2.2.12.
