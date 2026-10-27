# Pesquisa NA: contribuição SSC (MSD) x base do PAYE (HRBS-13602)

- **Data da pesquisa:** 2026-10-08
- **Ticket:** HRBS-13602 (Baker Hughes Namibia), "SS Employee Share (WT 2551) not applied as pre-tax deduction before Payroll Tax (WT 2552 / PAYE) calculation"
- **Status:** rascunho, nada foi enviado. Ainda não está registrado no hub do país nem em `correcoes.md`.
- **Fontes usadas:** apenas primárias (Government Gazette via LAC, texto anotado da LAC, PDF da SSC, brochura da NamRA no portal ITAS). Os sites namra.org.na (conexão recusada) e namiblii.org (403) não abriram.

---

## Veredito por pergunta

| # | Pergunta | Veredito |
|---|---|---|
| 1 | A contribuição do empregado à SSC (MSD) é dedutível da renda tributável pelo Income Tax Act 24 of 1981? | **NÃO.** A s.17(1) só permite ao empregado deduzir: (n) fundo de pensão/provident como condição do emprego, (q) retirement annuity fund e (qA) apólice de educação, além de (w) seguro de vida do sócio-chave, que vale só para trade. O teto conjunto da s.17(2) é **N$150 000/ano** (anos de avaliação a partir de 2022-03-01). A SSC/MSD **não aparece** na s.17 e o texto do Act não menciona "Social Security" em nenhum lugar. O MSD Fund também não se enquadra como "pension fund" ou "provident fund". O nosso CCG está correto: a WT 2551 não é dedução antes do imposto. |
| 2 | Algum guia oficial da NamRA trata da SSC no cálculo do PAYE? | **Nenhum guia oficial trata do assunto explicitamente.** A brochura oficial da NamRA "Taxation of Individuals who earn a Salary" lista as "Allowable Deductions" como uma lista fechada de três itens (pensão/provident, retirement annuity e apólice de educação, com limite de N$150 000) e **não inclui a SSC**. Não consegui acessar outro guia de PAYE/employer da NamRA porque namra.org.na estava fora do ar. |
| 3 | Valores vigentes da SSC | Taxa de **0,9% para o empregado e 0,9% para o empregador** (GN 198/1995, reg. 8). Base mensal ("basic wage") de no mínimo **N$500** e no máximo **N$12 500** desde 2026 (GN 236/2026, GG 8975). Contribuição máxima de **N$112,50** de cada lado (cálculo: 0,9% × 12 500). **⚠️ Divergência sobre a data de início:** o Gazette diz "with effect from **1 March 2026**", mas fontes secundárias (PwC Tax Alert ago/2026, Sage) dizem que a própria SSC adiou a aplicação para **1 September 2026** por meio de um Public Notice de 2026-08-07. **Não localizei esse Public Notice no site da SSC.** Antes disso valia teto de N$11 000 e contribuição máxima de N$99 (a partir de 2025-03-01, GN 275/2024, GG 8461). |
| 4 | A contribuição do empregador à SSC é fringe benefit tributável para o empregado? | **Não encontrado em fonte clara.** O Act tributa "any benefit or advantage granted in respect of employment, as determined by the Minister" (definição de "gross income", par. (g), sujeito à s.16A). Não achei nenhuma determinação, guia ou nota da NamRA que inclua ou exclua expressamente a contribuição patronal à SSC. A brochura da NamRA cita como fringe benefits só a moradia e o carro. Não vou afirmar nada além disso. |

**Conclusão para o ticket:** o tratamento do sistema está correto. A WT 2551 (MSD EE) deve ser retida depois do cálculo do PAYE e não reduz a base da WT 2552. Não existe base legal para a dedução que o cliente pede.

---

## Tabela de valores SSC (MSD Fund) com vigência e fonte

| Item | Valor | Vigência | Fonte |
|---|---|---|---|
| Taxa do empregado | 0,9% | a partir de 1995-11-01 (sem alteração encontrada) | GN 198 de 1995-11-01, reg. 8(a), GG 1181. https://www.lac.org.na/laws/1995/1181.pdf |
| Taxa do empregador | 0,9% (igual à do empregado) | a partir de 1995-11-01 | GN 198/1995, reg. 8(b), GG 1181 (mesma URL) |
| Basic wage mín./máx. (histórico) | N$300 / N$9 000 | até 2025-02-28 | Citado no consolidado NamibLII (403, não verificado diretamente). ⚠️ instrumento exato não verificado |
| Basic wage mín./máx. | N$500 / N$11 000 | de 2025-03-01 até 2026-02-28 (ou 2026-08-31, ver divergência) | GN 275 de 2024, GG 8461 de 2024-10-01, reg. 1 "basic wage". https://www.lac.org.na/laws/2024/8461.pdf |
| Contribuição máxima EE / ER | N$99,00 / N$99,00 | idem | Calculado: 0,9% × 11 000 |
| Basic wage máx. (FY 2025/2026) | N$12 500 (mín. N$500) | **Gazette:** a partir de 2026-03-01. **SSC (secundário):** a partir de 2026-09-01 | GN 236 de 2026, GG 8975 de 2026-07-15. https://www.lac.org.na/laws/2026/8975.pdf. O adiamento consta no PwC Tax Alert Aug 2026 (https://www.pwc.com/na/en/assets/pdf/tax-alert-august-2026.pdf, ⚠️ secundário) |
| Contribuição máxima EE / ER | N$112,50 / N$112,50 | idem | Calculado: 0,9% × 12 500 |
| Contribuição mínima EE / ER | N$4,50 | a partir de 2025-03-01 | Calculado: 0,9% × 500 |
| Basic wage máx. (FY 2026/2027) | N$14 000 | a partir de 2027-03-01 | GN 236/2026, GG 8975 (tabela) |
| Basic wage máx. (FY 2027/2028) | N$15 000 | a partir de 2028-03-01 | GN 236/2026, GG 8975 (tabela) |
| Basic wage máx. (FY 2028/2029) | N$16 000 | a partir de 2029-03-01 | GN 236/2026, GG 8975 (tabela) |

Observações:
- A tabela do GG 8975 vem desalinhada no PDF: a coluna 3 ("Effective Date") começa uma linha acima. A leitura coerente com o caput ("with effect from 1 March 2026") é: 12 500 a partir de 2026-03-01, 14 000 a partir de 2027-03-01, 15 000 a partir de 2028-03-01 e 16 000 a partir de 2029-03-01. O cabeçalho do PDF também traz o erro tipográfico "15 July 2926".
- A reg. 8 original de 1995 calcula a contribuição sobre "remuneration". O teto atua pelo proviso da definição de "basic wage" na reg. 1. Não localizei o GN que trocou "remuneration" por "basic wage" na reg. 8. ⚠️ Verificar no consolidado.
- A entidade que emite o GN mudou: em 2024 era o Ministry of Labour, Industrial Relations and Employment Creation; em 2026 é o Ministry of Justice and Labour Relations.

---

## Citações literais

### Income Tax Act 24 of 1981 (texto anotado da LAC, atualizado até o Income Tax Amendment Act 4 of 2024, GG 8442)
Fonte: https://www.lac.org.na/laws/annoSTAT/Income%20Tax%20Act%2024%20of%201981.pdf

**s.17(1), caput:**
> "17. (1) For the purpose of determining the taxable income derived by any person from carrying on any trade within Namibia, there shall be allowed as deductions from the income of such person so derived -"

**Definição de "trade" (s.1):** inclui o emprego.
> "\"trade\" includes every profession, trade, business, employment, calling, occupation or venture, ..."

**s.17(1)(n)(i):**
> "(n) (i) subject to subsection (2), any sum contributed during the year of assessment by way of current contributions to any pension fund or provident fund by any person holding any office or employment where the making of such a contribution is a condition of the holding of such office or employment;"

**s.17(1)(q):**
> "(q) subject to subsection (2), so much of the total current contributions to any retirement annuity fund or funds made by any person as a member of such fund or funds during a year of assessment during which such person has carried on any trade;"

**s.17(1)(qA):**
> "(qA) subject to subsection (2), so much of the total current premiums paid during the year of assessment in question for an education policy taken out by the taxpayer to provide funds at a future date for the education or training of a child or step child of such taxpayer as contemplated in paragraph (ab) of section 16(1);"

**s.17(2), teto conjunto:**
> "(2) The aggregate of the amounts that may be deducted in terms of paragraphs (n), (q), (qA) and (w) of subsection (1) shall not, as from the year of assessment commencing on or after 1 March 2022 in any year of assessment exceed the sum of N$150 000."

**Busca no texto integral:** a expressão "Social Security" não aparece em nenhum ponto do Income Tax Act anotado. A única ocorrência próxima é "Social Pensions Act, 1973", que não tem relação com o tema.

**Definição de "gross income", par. (g), base da pergunta 4:**
> "(g) subject to the provisions of section 16A, the value during the year of assessment of any benefit or advantage granted in respect of employment, as determined by the Minister;"

### Social Security Act 34 of 1994 (PDF publicado pela SSC)
Fonte: https://www.ssc.org.na/downloads/documents/social-security-act-34-of-1994.pdf

**s.21(4), retenção pelo empregador:**
> "(4) An employer shall, subject to the regulations contemplated in subsection (2), deduct the contributions payable by his or her employee from such employee's remuneration and pay it, together with the contributions payable by him or her as employer, over to the Commission within the prescribed period."

**s.42:** a isenção é do fundo e da Comissão, não do empregado.
> "42. No tax on income shall be payable by the Commission or in respect of any fund established by this Act or scheme referred to in section 37(4)."

O Social Security Act não tem nenhuma regra que torne dedutível do imposto de renda a contribuição do empregado.

### GN 198 de 1995, General Regulations (GG 1181, 1995-11-01)
Fonte: https://www.lac.org.na/laws/1995/1181.pdf
> "8. The contributions payable in respect of the Maternity Leave, Sick Leave and Death Benefit Fund shall - (a) in the case of an employee, be equal to 0,9 per cent of his or her remuneration; (b) in the case of the employer of such employee, be equal to the contribution contemplated in paragraph (a); (c) in the case of a self-employed person, be equal to both contributions contemplated in paragraphs (a) and (b)."

### GN 275 de 2024 (GG 8461, 2024-10-01)
Fonte: https://www.lac.org.na/laws/2024/8461.pdf
> "... I have amended the regulations published under Government Notice No. 198 of 1 November 1995, as set out in the Schedule with effect from 1 March 2025."
> "\"Provided that, for the purpose of these regulations, an employee shall be deemed to have been paid a basic wage of not less than N$500 and not more than N$11 000 in any month, as the case may be; and\"."

Obs.: o índice do Gazette numera este aviso como "No. 285", mas o corpo do texto e o GN 236/2026 citam "275 of 1 October 2024".

### GN 236 de 2026 (GG 8975, 2026-07-15)
Fonte: https://www.lac.org.na/laws/2026/8975.pdf
> "Under section 47 of the Social Security Act, 1994 (Act No. 34 of 1994), on the recommendation of the Social Security Commission, I have amended the regulations published under Government Notice No. 198 of 1 November 1995 as set out in the Schedule, with effect from 1 March 2026."
> "\"Provided that, for the purpose of these regulations, an employee shall be deemed to have been paid a basic wage of not less than N$500 and not more than the maximum basic salary set out in Column 2 of the Table, in any month of each financial year as set out in Column 1 of that Table with effect from the date set out in Column 3 of that Table, as the case may be:"
> Tabela: 2025/2026 N$12,500; 2026/2027 N$14,000; 2027/2028 N$15,000; 2028/2029 N$16,000; datas efetivas 1 March 2026 / 1 March 2027 / 1 March 2028 / 1 March 2029.

### NamRA, brochura "Taxation of Individuals who earn a Salary" (taxas a partir de 2024-03-01)
Fonte: https://itas.namra.org.na/assets/documents/other-forms/Tax%20on%20Individuals%20Brochure.pdf
> "Allowable Deductions: 1. An amount contributed to an approved pension or provident fund as a condition of employment; 2. An amount contributed to a retirement annuity fund; and 3. The total premiums paid under a policy taken out for the education of a child. The total of the amounts that may be deducted for all the above 3 deductions is limited to N$150,000 as of 2023 tax year."

---

## Lacunas e pontos de atenção
- **Public Notice da SSC de 2026-08-07** (que adia o teto de 12 500 para 2026-09-01): não encontrei no site da SSC. A data de início em folha (março ou setembro de 2026) precisa ser confirmada. Não afeta o veredito do ticket, mas afeta o teto da WT 2551.
- **Income Tax Amendment Bill 2025:** segundo fontes secundárias, foi apresentado ao Parlamento em 2026 e ainda não foi publicado no Gazette. Pelo que foi noticiado, não mexe na s.17 nem prevê dedução da SSC. Não verifiquei em fonte primária. O texto da LAC está atualizado até o Act 4 of 2024.
- **Pergunta 4 (contribuição patronal como fringe benefit):** sem fonte oficial. Não foi incluída no rascunho de resposta.

---

## Rascunho de resposta HRBS-13602 (EN, não enviado)

> Hi Daniel Kelvin Balogun,
>
> Thank you for raising this. We reviewed the Namibian legislation and the current system behaviour (WT 2551 "SS Employee Share" calculated after, and not deducted from, the Payroll Tax base WT 2552 / PAYE) is correct.
>
> **Reasoning**
> 1. Under the Income Tax Act 24 of 1981, the only employee contributions deductible from taxable income are those listed in section 17(1): contributions to a pension or provident fund made as a condition of employment (s.17(1)(n)), retirement annuity fund contributions (s.17(1)(q)) and education policy premiums (s.17(1)(qA)), with an aggregate annual cap of N$150,000 (s.17(2), from the year of assessment starting 1 March 2022). Contributions to the Social Security Commission's Maternity Leave, Sick Leave and Death Benefit Fund are not included in this list, and the Act contains no other provision allowing them as a deduction.
> 2. NamRA's official guidance ("Taxation of Individuals who earn a Salary") lists these same three allowable deductions only.
> 3. The Social Security Act 34 of 1994 requires the employer to deduct the employee contribution from remuneration (s.21(4)). Its tax exemption (s.42) applies to the Commission and its funds, not to the employee's contribution.
>
> Therefore the employee SSC contribution is a post-tax deduction and PAYE must be calculated on remuneration before SSC. No configuration change is required.
>
> For reference, the SSC contribution is 0.9% employee + 0.9% employer (GN 198/1995, reg. 8), on a basic wage between N$500 and N$12,500 per month (GN 236/2026, Government Gazette 8975 of 15 July 2026), i.e. a maximum of N$112.50 each side (previously N$11,000 / N$99.00 under GN 275/2024).
>
> Sources:
> - Income Tax Act 24 of 1981, s.17(1)(n), (q), (qA) and s.17(2)
> - NamRA, Taxation of Individuals who earn a Salary: https://itas.namra.org.na/assets/documents/other-forms/Tax%20on%20Individuals%20Brochure.pdf
> - Social Security Act 34 of 1994, s.21(4) and s.42: https://www.ssc.org.na/downloads/documents/social-security-act-34-of-1994.pdf
> - Government Gazette 8975 (15 July 2026), GN 236: https://www.lac.org.na/laws/2026/8975.pdf
>
> Kind regards,

⚠️ Antes de enviar: confirmar a data de início do teto de N$12 500 (2026-03-01 pelo Gazette ou 2026-09-01 pelo aviso da SSC) e se o cálculo da WT 2551 no sistema já usa esse teto. Se a data não for confirmada, tirar o parágrafo "For reference" da resposta.
