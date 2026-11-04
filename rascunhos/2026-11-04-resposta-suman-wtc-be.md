# Resposta à Suman Rai — WTC BE, aba _Final_BA (2026-11-04)

Ligado a [[Belgica]], [[Research Pipeline/Belgium/2026-11-03-wtc-final-ba-suman/CONFERENCIA|conferência de 03/11]]. Não enviado.

## Rascunho (DM Google Chat)
Hi Suman, answers below.
1. N and O: I'll fill the blank rows.
2. Social security: Belgium has one ordinary contribution (employee 13.07% plus employer) and the employee special contribution; the pension is inside the ordinary contribution (CCG 5.1). I'll rename Q to "Subject to Ordinary SS" and R to "Subject to Special SS".
3. ER/EE: agreed. Double holiday pay has the employee 13.07% but no employer contributions (CCG 3.1 and 4.2), so I'll split Ordinary SS into Employee and Employer.
4. Tax: both come from Annex III. I'll rename O to "Tax - Ordinary scale" and P to "Tax - Exceptional payments" (bonus, double holiday pay, arrears of a previous year, termination indemnity).
5. Arrears: 62101 is arrears for a previous calendar year, so it is taxed as an exceptional payment, not at the scale. Current-year arrears go with the monthly pay at the scale (CCG 4.4 and 9.2).
6. NA: I'll change all of them to Yes or No.
I'll let you know when it's done.

## Dados (export CSV da _Final_BA, 04/11)
- N/O vazios: 112 (códigos novos). NA: N 23, O 23, P/Q/R 131 (108 contadores Intermediary 79xxx; 23 Earnings com G = NA ou pensão).
- Pensões com G preenchido e flags NA: 62642 (285), 62644 (285), 62645 (387), 62646 (283), 62649 (285) → pesquisar antes de pôr Yes/No.
- Duplo/partida (62160–62162, 62305, 62920): Q/R = Yes desde 03/11 (eram "Yes-No" = empregado sim, empregador não); a divisão ER/EE resolve.
- R repete Q (390/207/131): rever R contra a base da contribuição especial (Lei 30/03/1994 art. 106) antes de afirmar valores.

## Versão 2 (após pesquisa, 04/11) — substitui o rascunho acima
Hi Suman, answers below, checked against the official sources.
1. N and O: I'll fill the blank rows. The counters are No; 65508, 65509, 65609 and 65659 are benefits taxed at the scale, so Yes/Yes.
2. Social security: Belgium has no separate pension contribution; the pension share sits inside the ordinary 13.07% and the employer rate (NSSO instructions 2026/3). I'll replace "Subject to Social Insurance" and "Subject to Pension" with "Ordinary SS - Employee", "Ordinary SS - Employer" and "Special SS Contribution".
3. ER/EE: agreed. Double holiday pay has only the employee 13.07% (on 85/92 of the legal amount), no employer contribution, and it does not count for the special contribution (NSSO 2026/3).
4. Tax: both columns come from Annex III. I'll rename O to "Tax - Periodic scale" and P to "Tax - Special rate" (exceptional pay, double holiday pay, arrears, notice pay).
5. Arrears: 62101 is arrears for a previous year. These are taxed separately (ITC 92 art. 171, 5°, b), withheld at the Annex III nr. 58 arrears rate instead of the monthly scale, and reported in 281.10 code 252. That's why it's Special Tax.
6. NA: all become No. These elements are either not paid through Belgian payroll or are pension deductions (codes 283, 285, 387), not earnings.
I'll let you know when it's done.

## Prova (conferida pessoalmente)
- Anexo III 2026 nº 58 (raw/docs/oficiais/BE/2026-10-25-Bijlage-III-KB-WIB-2026.pdf): "Voor achterstallige bezoldigingen van werknemers (onder meer … na het verstrijken van het belastbare tijdperk …)".
- ONSS 2026/3: specialsocialsecuritycontribution.html ("Aangezien het dubbel vakantiegeld geen loon is … komt het niet in aanmerking …"); doubleholiday_privatesector.html (sem retenção a partir do 3º dia da 4ª semana = 85/92); contributions.html (Pensioenen 7,50 / 8,86 dentro da taxa global).
- Agentes: art. 171, 5°, b WIB 92 (Fisconetplus); Belcotax 2025 fiche 281.10 (250/251/252/283/285/387); aviso 281.10 e Wikifin (pensões).

## Fora do pedido (hub [[Belgica]])
- Aba _Final_BA: 62645/62646 são Deduction (estão Earning); 65509 com G 252 (certo 250).
- CCG BE v1.0/v1.1: 13,07% sobre 100% do duplo pecúlio (certo 85/92) em exemplos; duplo pecúlio e CBA 90 somados à base da contribuição especial (Ex. 5 e bônus); 4.4/9.2 mandam atrasados para a tabela excepcional ×13,92 (certo: Anexo III nº 58, referência do ano anterior); 13,92 sem fonte oficial; pecúlio de saída: parte simples EE+ER, dupla só EE sobre 6,80%.
- Abertos: atrasado do ano corrente (sem regra expressa, 50%); estacionamento 62810/11 (65%); KB 27/09/2026 altera Anexo III desde 01/11/2026 (não lido).

## Versão 3 (após pesquisa do estacionamento, 04/11) — item 6 trocado
6. NA: all become No, except 62811. 62810 is the reimbursement of parking costs, which is an employer cost (no tax, no SS); 62811 is a fixed parking allowance, which is ordinary pay (Tax Yes at the scale, SS Yes). The others are not paid through Belgian payroll or are pension deductions (codes 283, 285, 387).
- Prova estacionamento: ONSS 2026/3 expensesreimbursement (conferido: forfait "parking 15,00 EUR/maand", "De sommen die het bedrag van de werkelijke kosten overschrijden, zijn loon"); imposto: art. 31 al. 2, 1° in fine WIB 92 via Ruling 2016.781 e 2026.0217 (Fisconetplus, via agente) e nota CRB 29/07/2024.
- Fora do pedido: CCG não trata estacionamento; "Commuting allowance, public transport … Exempt within limits" a rever (art. 38 §1, 9° a: transporte público totalmente isento); WTC 21810 afirma vaga no trabalho não tributável sem fonte.

## Coluna "Special rate table" (proposta, 04/11; não gravada)
Fonte: Anexo III 2026 (raw/docs/oficiais/BE/2026-10-25-Bijlage-III-KB-WIB-2026.pdf) — conferido por mim: nº 53 (colunas VAKANTIEGELD / ANDERE VERGOEDINGEN EN TOELAGEN), nº 58 (achterstallen), nº 62 ("volgens de regels van nrs. 58 tot 60"), nº 80 (SWT, "regels van deel 5 … op het totaalbedrag").
- nr. 58 - arrears (tax 252): 62101, 62135, 62141, 62171, 62209, 62301, 62361, 62401, 62411, 62421, 62431, 62441, 62451, 62461, 62741, 62761, 62781, 62861, 62971, 62981, 65221, 65401, 65511, 65601, 65651, 65661, 62883, 62884
- nr. 53 - holiday pay: 62160, 62161, 62162, 62305, 62920, 79401, 79450, 79452
- nr. 62 - notice pay: 62180, 62181, 62182
- nr. 53 - exceptional pay: 62143 (se anual), 62149, 62200–62208, 62213, 62214, 62219–62222, 62230–62249, 62563, 62591, 62730, 62771–62779, 62866, 62867, 62900, 62901, 62905, 62910, 62921–62925, 62930–62935
- Other - profit premium 7% levy (outside Annex III): 62210, 62215, 62216, 62217
- nr. 80 - SWT top-up: 62882
- Open: 62650/62652/62653 (fundo social: nº 78.1/79.2.2/70 conforme natureza), 62731/62732, 62501, 65501 (atrasado do ano corrente), 62880 (não concorrência), 65701/65711 (atrasado de complemento-maternidade)
- Erros da WTC achados (hub): texto dos atrasados manda tabela excepcional ×13,92 (certo nº 58); 62880 texto nº 53 × tax 308; winstpremie com Special Yes; 62882 tax 250; 62143 Special fixo; "Arrears" com tax 250; tax codes 65511/65661/65711/65601/65701 = 252 na v1.3 local × NA/250 na _Final_BA.
