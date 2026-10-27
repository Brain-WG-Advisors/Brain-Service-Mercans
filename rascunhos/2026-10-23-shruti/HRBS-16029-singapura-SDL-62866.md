# HRBS-16029 — Singapura / GSK: SDL só sobre componentes CPF-able (pay element 62866)

> Análise só leitura, feita em 2026-10-23 pela janela Suporte (subagente). Nada foi postado, enviado ou alterado no Drive. Rascunho para o usuário decidir.

## Metadados
| Campo | Valor |
|---|---|
| Ticket | [HRBS-16029](https://youtrack.hrblizz.dev/issue/HRBS-16029) — "GSK Singapore - SDL Wage" |
| Estado | Pending on reporter · Question / Inquiry · Medium · Production · Live/BAU |
| Reporter | Hayat Harmy (nharmy) |
| Assignee | wgomes (era da Shruti/skamble até 22/10; reatribuído, ver [[2026-10-22-triagem-tickets-enaakshi-shruti]]) |
| Criado / atualizado | 2026-10-15 / 2026-10-22 |
| Fonte do ticket | `raw/tickets/api/2026-10-23-ex-skamble/HRBS-16029.md` |
| Artefato | Singapore Wage Type Catalogue **V4.2** (export de 2026-10-23, md5 `e381165b…f0358f`; aba Version control marca V4.2 como **"Under Review"**, 2026-09-11) |
| Hub | [[Singapura]] · correções: nada sobre SG/SDL/CPF em [[correcoes]] |

## O que foi pedido a nós
1. Pergunta original (15/10): se é correto o SDL só incidir sobre componentes CPF-able e se o 62866 (fixed earning, não CPF-able) deveria usar outro componente.
2. Pedido em aberto (16/10, Hayat): **"can you update 62866 component as CPF-able in the compliance WTC?"**
3. Respostas do Hayat às 6 perguntas da Shruti (21/10): entidade 03-085; pago pela folha, não BIK; "Above 4K"; vigência no mês da correção; sem retroativo (shortfall tratado manualmente); sem aviso ao cliente; Q6 (códigos relacionados): "Fixed earning should be considered as monthly wage".

O que falta da nossa parte: **decidir a mudança no WTC (62866 e, se for o caso, os relacionados), responder ao Hayat e abrir a mudança (WTC V4.3 + task de configuração).**

## Histórico do ticket
| Data (UTC) | Quem | O quê |
|---|---|---|
| 15/10 02:16 | Hayat | Abre: SDL só sobre CPF-able; 62866 é fixed earning não CPF-able; deveria contar como wage. |
| 16/10 10:53 | Shruti | SDL usa a mesma definição de "wages" do CPF; fixed earning em dinheiro é wage para CPF e SDL; recomenda pagar em componente CPF-able, não criar componente só para SDL, rever períodos passados. Ressalva: reembolso, verba rescisória ou pagamento a terceiro não é CPF. |
| 16/10 12:29 | Hayat | Pede para mudar 62866 para CPF-able no WTC. |
| 16/10 14:57 | Shruti | Identifica 62866 = Childbirth Allowance; WTC é country-level; faz 6 perguntas (uso, forma de pagamento/> $200, vigência, passado, aprovação do cliente, códigos 62867, 62868/62869, 62870, 62878). |
| 21/10 10:30 | Hayat | Responde (ver acima). |
| 22/10 | (interno) | Ticket reatribuído a wgomes. |

Leitura: a resposta da Shruti está correta no princípio (mesma definição de wages; ver Fonte primária). O ponto em aberto é **como** classificar 62866 no WTC (OW ou AW) e o que fazer com os relacionados.

## O que nosso WTC diz
Aba `Wage Type Catalogue`, colunas: M = Subject to Tax · N = Subject to CPF/ Other Social Security · Q = Ordinary Wage/ Additional Wage · R/S = IRAS XML/PDF group · T = Remarks. Todos: Category Earning, Calculation Lump Sum, Occurrence **Additional**.

| Linha | Código | Nome | Tax (M) | CPF (N) | OW/AW (Q) | IRAS (R/S) | Remark (T) |
|---|---|---|---|---|---|---|---|
| 685 | **62866** | Childbirth Allowance (non taxable) | No | **No** | NA | — | — |
| 686 | 62867 | Death Allowance (non taxable) | No | No | NA | — | — |
| 687 | 62868 | Gift Voucher (non taxable) | No | No | NA | — | "Exempt up o SGD 200" |
| 688 | 62869 | Gift Voucher (non taxable) | No | No | NA | — | — |
| 689 | 62870 | Other Non Taxable Payment | No | No | NA | — | — |
| 697 | 62878 | Child Care Subsidy | No | **No** | NA | — | **"CPF Payable as it is paid in the payroll."** (contradiz a coluna N) |

Comparáveis já existentes no mesmo WTC:
| Linha | Código | Nome | Tax | CPF | OW/AW | Observação |
|---|---|---|---|---|---|---|
| 465–466 | 62590 / 62591 | Birth and Marriage Allowance | Yes | **Yes** | **Additional Wages** | Mesmo evento (nascimento), versão em dinheiro tributável e CPF-able |
| 830 | 65816 | Parenthood Gift (Benefit) | Yes | No | NA | BIK, Appendix 8A, "Exempt up to SGD 200" |
| 771 | 62983 | Maternity Allowance | Yes | **No** | NA | Remark copia o texto do CPFB, que diz **YES** (ver Achados) |
| 515 / 625 | 62660 / 62780 | Personal Allowance 1 / Family allowance | Yes | Yes | **Ordinary Wages** | Recurring, Pro Rata: o padrão do WTC para allowance fixa mensal |
| 615 / 164 | 62770 / 62182 | Long Service Award (CPF / não CPF) | Yes | Yes / No | AW / NA | Par "CPF / não CPF" por regra própria do LSA |

Base do SDL no WTC: só as linhas 11 (`2534 SDL ER Contribution`, Regulation Output) e 75 (`58534 SDL Base`, Base, **sem fórmula** e sem coluna própria de SDL). A composição da base vem da engine; pela resposta da Shruti, ela soma os componentes com N = Yes. Não há coluna "Subject to SDL" no WTC.

Guia interno (`Singapore Payroll Regulation Guide 2024.txt`): lista "Gifts in kind (e.g., marriage or childbirth) (Ang bao / red packet are not covered as these are money)" em *Income not subject to CPF*; SDL "0.25% of monthly total wages", mín. 800 / máx. 4.500.

## Fonte primária
Todas baixadas em 2026-10-23 para `raw/docs/oficiais/SG/` (ver lista no fim da seção).

**1. Skills Development Levy Act 1979 (2020 Rev. Ed., versão corrente em 23/10/2026)** — sso.agc.gov.sg
- **s.2**, "wages": *"'wages' means the remuneration in money, including any bonus, due or granted to a person in respect of the person's employment but does not include such payments as the Minister may, by notification in the Gazette, specify."* [Act 4 of 2023 wef 15/06/2023]
- **s.3(1)**: *"every employer must, in respect of each of the employer's employees, pay a skills development levy of the greater of the following amounts: (a) … an amount calculated at the rate of 0.25% of the wages in any month of that employee …; (b) $2."*
- **s.3(2)**: *"the levy is not chargeable on the part of the wages of the employee in any month that exceeds $4,500 …"*
- s.2 "employee": inclui todo empregado com serviço total ou parcial em Singapura (exclui só empregado doméstico, jardineiro ou motorista de pessoa física). Não exige ser membro do CPF → **SDL vale para estrangeiros**.
- Vigência: 0,25%, piso $2, teto de base $4.500 → máximo $11,25/empregado/mês, a partir de 15/06/2023 (Act 4 of 2023), vigente em 23/10/2026.

**2. Central Provident Fund Act 1953 (2020 Rev. Ed., versão corrente em 23/10/2026)** — sso.agc.gov.sg
- **s.2**, "wages": *"'wages' means the remuneration in money, including any bonus, due or granted to a person in respect of the person's employment but does not include such payments as the Minister may, by notification in the Gazette, specify."* → **texto idêntico ao do SDL Act s.2.**
- **First Schedule para 5(e)**: *"'ordinary wages for the month' means the amount of remuneration due or granted wholly or exclusively in respect of employment during that month and payable before the due date for the payment of contribution for that month"*.
- **First Schedule para 5(d)(i)**: *"'additional wages' … means any remuneration other than ordinary wages"*.
- **First Schedule para 5(ea)(iv)**: Ordinary Wage Ceiling *"in respect of each month in the year 2026 and every subsequent year, is $8,000"* [S 599/2023]. **Para 5(da)**: "applicable amount" (base do teto anual de AW) = $102.000.

**3. CPF Board — "What constitutes wages for CPF contributions"** (cpf.gov.sg/employer/employer-obligations/what-constitutes-wages-for-cpf-contributions)
- *"Under the CPF Act, wages are defined as remuneration in money … Allowance — For example, meal allowance and transport allowance"* (incluir).
- *"Payments not to include as wages … Benefit in kind — Non-cash benefit or gift given to the employee. For example, a commemorative watch."*
- OW: *"They are given to an employee for their employment in that month, and They are payable by the 14th of the following month. For example, monthly salary."* AW: *"Wages which are not classified as Ordinary Wages will be Additional Wages for the month."*

**4. CPF Board — "Which allowances and payments attract CPF contributions?"** (PDF, *Last Updated on: 28 July 2025*; a versão de 28/10/2021 no caminho `/faq/` está desatualizada)
- *Festive allowance — "Cash gift (e.g. hongbao) given to employees during festive season" — **YES***
- *Gifts in kind — "Award in kind e.g. token gifts" — **NO***
- *Staff welfare benefits — "Gifts in kind to employees on their marriage or birth of their children" — **NO***
- *Maternity allowance — "Payment to female employees during confinement and in addition to monthly salaries" — **YES***
- *Holiday expenses — "Fixed payment to employees for vacation" — YES* · *Education allowance — "Contractual payment for education of employee's children" — YES*
- Não há entrada para morte/luto (death/bereavement) nem para childcare subsidy.

**5. CPF Board FAQ "Are CPF contributions payable on gift vouchers?"** (Last Updated 7 Jun 2024; lida via WebFetch, página em JavaScript, **sem cópia local**): *"CPF contributions are not payable on gift vouchers given to your employee if they are non-cash benefits, i.e. they are not legal tender or convertible into cash."*

**6. CPF Board — Skills Development Levy** (cpf.gov.sg/employer/employer-obligations/skills-development-levy)
- *"The levy payable for each employee is at 0.25% of the monthly total wages. The minimum payable is $2 for an employee earning less than $800 a month and the maximum is $11.25 for an employee earning more than $4,500 a month."*
- *"Add up the SDL calculated for each employee and then round the total amount down to the nearest dollar."*
- *"SDL is auto-computed for all Singapore Citizen and Singapore Permanent Resident employees. You'll need to input the SDL payable for foreign employees in CPF EZPay."*

**7. IRAS — "Gifts"** (iras.gov.sg/…/understanding-the-tax-treatment/gifts) — só para o achado de imposto
- *"Special occasions e.g. celebration of SG50, birthdays, weddings and births of child (cash/ non-cash)"*: *"Cash and non-cash gifts relating to festive and special occasions which do not exceed the exemption threshold of $200 are considered to be not substantial in value and are not taxable due to an administrative concession granted. If a gift exceeds the exemption threshold, the full value of the gift is taxable."* *"The threshold of $200 is applicable per occasion."* Gifts devem estar *"generally available to all staff"*.

**"Above 4K" do Hayat** (resposta à pergunta "Is any amount above $200?"): o valor do 62866 passa de $4.000.
- **SDL:** a base é limitada a $4.500/mês (s.3(2)). Se o restante da remuneração do empregado no mês já passa de $4.500, ele já paga o máximo de $11,25 e incluir o 62866 **não muda o SDL**. Só muda quando os outros wages ficam abaixo de $4.500. O impacto no SDL é pequeno (no máximo $11,25 por empregado/mês).
- **CPF:** é aqui que o valor pesa. Como OW, o 62866 entra no teto mensal de OW de **$8.000** (para 2026, para 5(ea)(iv)): com salário + mais de $4.000, boa parte pode ficar acima do teto e sem CPF. Como AW, entra no teto anual de AW (**$102.000 − OW sujeito a CPF no ano**, para 5(da)): em geral, todo o valor sofre CPF. Ou seja, **classificar como OW ou AW muda o valor do CPF**, não só a forma.

Fontes primárias baixadas (`C:\Users\instituto\Documents\brain-service\raw\docs\oficiais\SG\`):
- `2026-10-23-SDLA1979.html` (lei inteira; s.2) e `2026-10-23-SDLA1979-s3.html` (s.3)
- `2026-10-23-CPFA1953.html` (s.2) e `2026-10-23-CPFA1953-First-Schedule.html` (First Schedule para 5)
- `2026-10-23-CPFB-what-constitutes-wages.html`
- `2026-10-23-CPFB-which-allowances-and-payments-attract-CPF-v2025-07-28.pdf`
- `2026-10-23-CPFB-SDL-page.html`
- `2026-10-23-IRAS-gifts.html`

## Veredito
**Princípio (confirma a Shruti):** o SDL Act s.2 e o CPF Act s.2 definem "wages" com o mesmo texto. Logo, o teste "é wage?" é um só para CPF e para SDL. O que muda é a base: o SDL não separa OW e AW, tem base limitada a $4.500 e vale também para estrangeiros, sem CPF. Usar o flag de CPF do WTC para montar a base do SDL está certo **desde que** a engine use o flag do componente (e não o valor do CPF já calculado e limitado, nem a elegibilidade do empregado ao CPF). Ver Lacunas.

| Código | CPF | OW/AW | SDL | Fundamento | Força da prova |
|---|---|---|---|---|---|
| **62866 Childbirth Allowance** (paga em dinheiro pela folha) | **Yes** | **AW** | Yes (consequência) | Pagamento em dinheiro é "remuneration in money" (CPF Act s.2). Só presente **em espécie** por nascimento está fora (CPFB: "Gifts in kind … on their marriage or birth of their children — NO"). Pagamento único por evento não é "wholly or exclusively in respect of employment during that month" → AW (para 5(d)/(e)). Mesmo tratamento que o WTC já dá ao 62590/62591. | Alta |
| GSK: "fixed earning … monthly wage" | Yes | **OW** | Yes | Se o pagamento é fixo e mensal pelo trabalho do mês, é OW (para 5(e); CPFB: "monthly salary"). O 62866 é, por definição no WTC, um pagamento único (Additional, Lump Sum) por nascimento. Mudá-lo para OW no país inteiro classificaria errado o auxílio-nascimento verdadeiro de todos os clientes. Um ganho fixo mensal cabe num código recorrente de OW (o WTC já tem vários, ex.: linhas 515 e 625). Escolher o código é com a implementação, não conosco. | Alta (regra); o uso pela GSK é informação do Hayat |
| 62867 Death Allowance | manter **No** | NA | No | O guia interno lista "Death benefits" e "Donation on bereavements" como fora do CPF. A lista do CPFB (2025) **não tem entrada** sobre morte/luto. | ⚠️ sem fonte primária: manter e registrar lacuna |
| 62868 / 62869 Gift Voucher | manter **No** | NA | No | FAQ do CPFB: voucher que não é moeda corrente nem conversível em dinheiro não é wage. Se for conversível em dinheiro, é wage. | Alta (para voucher não conversível) |
| 62870 Other Non Taxable Payment | manter **No** | NA | No | Código genérico; o tratamento depende do que for pago. Não pode servir para pagamento em dinheiro que seja wage. | Não decidível sem uso; manter |
| **62878 Child Care Subsidy** | **Yes** se paga em dinheiro ao empregado; **No** se paga direto à creche (BIK) | AW | Yes / No | A própria Remark do WTC diz "CPF Payable as it is paid in the payroll", e a coluna N diz No. Em dinheiro é wage (s.2). Pago ao prestador é benefício em espécie (CPFB 2025: "Maternity subsidy — Payment from employer directly to service provider, e.g. hospital, clinic … — NO"; "Benefit in kind — Non-cash benefit … — not wages"). | Média: o CPFB não tem entrada específica; a conclusão vem da definição legal e da analogia com maternity subsidy |

## Mudança no WTC
Proposta para **V4.3** (aba `Wage Type Catalogue`; partir da export de 23/10; destacar em azul-claro `FFDDEBF7`; não sobrescrever o `.gsheet`):

| Linha | Código | Coluna | Antes | Depois |
|---|---|---|---|---|
| 685 | 62866 | N Subject to CPF | No | **Yes** |
| 685 | 62866 | Q OW/AW | NA | **Additional Wages** |
| 685 | 62866 | T Remarks | (vazio) | "Cash payment through payroll = wages (CPF Act s.2; SDL Act s.2) → CPF (AW) and SDL. Gifts in kind for childbirth are not wages (CPFB). Not taxable only up to SGD 200 per occasion and if available to all staff (IRAS concession); above that use 62590." |
| 697 | 62878 | N Subject to CPF | No | **Yes** *(decisão do usuário: incluir nesta versão?)* |
| 697 | 62878 | Q OW/AW | NA | **Additional Wages** *(idem)* |
| 697 | 62878 | T Remarks | "CPF Payable as it is paid in the payroll." | manter + "Subsidy paid directly to the childcare provider is a benefit in kind: not CPF." |
| Version control | — | nova linha | — | 4.3 · data · "62866 (and 62878) set as subject to CPF (Additional Wages) as per HRBS-16029; SDL follows CPF wages definition (SDL Act s.2)" · Released/Under Review · autor |

Ficam como estão: 62867, 62868, 62869, 62870, e as colunas M (Tax) e R/S do 62866 (ver Achados 1).

**Impacto no país (WTC country-level, vale para todos os clientes SG):**
- Todo cliente que paga 62866 (ou 62878) passa a ter CPF do empregado e do empregador sobre AW, dentro do teto anual de AW. Para o empregado, o líquido diminui.
- O SDL passa a incluir o valor (efeito máximo de $11,25/empregado/mês) para SC/SPR **e estrangeiros**.
- Não há efeito no imposto (coluna M não muda) nem no IR8A.
- O Hayat disse "no need to inform the client" para a GSK, mas isso não cobre os outros clientes. Para o 62866, a mudança corrige uma subcontribuição legal; ainda assim, alguém interno precisa listar os clientes e entidades que usam o código antes da produção. Isso não é nosso; ver [[fronteiras]].
- Vigência: competência a partir da folha em que a configuração entrar (pedido do Hayat). Sem retroativo pelo sistema: a GSK diz que o shortfall foi lançado manualmente.

## Achados fora do pedido
> Vão para Pendências do hub [[Singapura]], não para o ticket (salvo decisão do usuário).
1. **62866 "(non taxable)" com valor acima de 4K:** o IRAS só isenta presente por nascimento (em dinheiro ou espécie) até **$200 por ocasião** e desde que disponível a todo o pessoal. Acima disso, **o valor inteiro é tributável**. Com M = No e R/S vazios, um pagamento acima de 4K pelo 62866 **sai do IR8A**: subdeclaração. Isso é do cliente/implementação; vale avisar o usuário.
2. **62983 Maternity Allowance com CPF = No**, mas o CPFB (PDF de 2025) diz **YES** para "Payment to female employees during confinement and in addition to monthly salaries", e a Remark do próprio WTC copia esse texto. Mesmo tipo de erro do 62866; candidato a entrar na V4.3.
3. **Remark diz "CPF payable" e a coluna N diz No** também em 62844 (Personal Club Membership Reimbursement), 62854 (Overseas Holiday Trip), 62855 (Holiday Reimbursement) e 62859 (Reimbursements for health supplements…). Inconsistência interna a revisar. Holiday: o CPFB diz YES para "Fixed payment to employees for vacation" e para reembolso de despesas de férias, conforme o guia interno.
4. **WTC V4.2 está "Under Review"** (desde 11/09/2026). A V4.3 precisa partir dela ou esperar a liberação; confirmar com o Mohit/Ruchi.
5. **Guia interno (Payroll Regulation Guide 2024)** diz "Ordinary wages have a ceiling at SGD 6,800" e logo depois "SGD 8,000 from 2026": texto desatualizado e contraditório. O vigente é $8.000 (para 5(ea)(iv)).
6. A Remark do 62868 tem erro de digitação ("Exempt up o SGD 200"), e o 62869 está sem a Remark.

## Rascunho de resposta (EN)
> Para o comentário no YouTrack. Não postado. A linha entre colchetes é opcional (achado 1): o usuário decide.

Hi @nharmy,

Thank you for the details. Confirmed:

- The SDL Act and the CPF Act define "wages" in identical terms ("remuneration in money … due or granted … in respect of the person's employment", SDL Act 1979 s.2; CPF Act 1953 s.2). A childbirth allowance paid in cash through payroll is therefore wages for both CPF and SDL. Only gifts in kind on the birth of a child are excluded (CPF Board, *Which allowances and payments attract CPF contributions*, "Staff welfare benefits").
- 62866 is a one-off lump-sum payment, so it is classified as **Additional Wages** (CPF Act, First Schedule para 5(d)–(e)). A fixed earning paid for each month's employment is **Ordinary Wages** (para 5(e)) and belongs under a recurring OW allowance code, not 62866.
- SDL is 0.25% of the month's wages, capped at $4,500 of wages ($11.25 maximum, SDL Act s.3(2)). Where the employee's other wages already exceed $4,500, adding 62866 does not change the SDL.

Next step: we will release WTC V4.3 with 62866 as subject to CPF (Additional Wages), effective from the payroll period in which it is configured, and raise the configuration task. As the WTC is country-level, this applies to all Singapore clients using 62866.

[Note: 62866 is set as non-taxable. Under IRAS's gift concession, a cash gift for the birth of a child is not taxable only up to $200 per occasion; above that, the full amount is taxable and reportable in the IR8A.]

Regards,
Wallisson

## O que precisa ser feito
| # | O quê | Quem | Urgência |
|---|---|---|---|
| 1 | Decidir o escopo da V4.3: só 62866 (recomendado: sim) · 62878 (recomendado: sim) · 62983 (recomendado: sim, mas fora do pedido) · 62844/54/55/59 (revisar depois, à parte) | Usuário | Alta: a GSK está compensando à mão a cada folha |
| 2 | Confirmar com o Mohit/Ruchi se a V4.2 ("Under Review") já foi liberada e como a base 58534 (SDL Base) é montada (pelo flag de CPF do componente? para estrangeiros também? antes ou depois do teto de OW?) | Usuário → Mohit/Ruchi | Alta, antes da V4.3 |
| 3 | Montar a V4.3 a partir da export de 23/10: alterar só as células aprovadas, azul-claro `FFDDEBF7`, conferir célula a célula, copiar ao Drive como `Singapore Wage Type Catalogue V4.3.xlsx`. Pela regra de 19/10, arquivar primeiro no cérebro e só mandar ao Drive quando o usuário mandar. | Janela Suporte, com ok do usuário | Alta |
| 4 | Postar a resposta ao Hayat (rascunho acima) com ok do usuário | Usuário | Alta |
| 5 | Abrir a task de configuração (CT) para 62866 (e o que mais entrar) com a vigência e a lista de clientes/entidades afetados. A lista de clientes é com a implementação. | Usuário/Mohit (configuração: outro time, ver [[fronteiras]]) | Alta |
| 6 | Registrar no hub [[Singapura]] (Suporte, Pendências com os achados 1–6) e em `log.md` ao fechar | Janela Suporte, em "fecha a sessão" | Normal |

## Lacunas
- **Composição real da base do SDL na engine (58534):** o WTC não tem fórmula. Não verifiquei se a base usa o flag do componente (certo), o CPF OW/AW já limitado (aceitável, porque $8.000 > $4.500), ou a elegibilidade ao CPF (errado para estrangeiros; para 58563 CPF Eligibility Flag = 0 para não SC/SPR). A Shruti afirmou que o SDL é calculado para estrangeiros, mas isso ⚠️ não está provado nos arquivos.
- **Natureza do pagamento da GSK:** o Hayat diz "fixed earning", "monthly wage" e "Above 4K" para um código chamado *Childbirth Allowance*. Não sabemos se é um auxílio-nascimento recorrente ou outra verba lançada no 62866. Se for verba mensal, a classificação certa é OW, e o mapeamento do cliente fica fora do nosso escopo.
- **62867 Death Allowance:** sem fonte primária atual do CPFB para pagamento em dinheiro por morte/luto. O guia interno diz "não CPF"; ⚠️ sem fonte. Mantido como está.
- **62878 Child Care Subsidy:** o CPFB não tem entrada própria; a conclusão vem da definição legal e da analogia. Força média.
- **Quem usa 62866/62878 em outros clientes SG:** desconhecido (dado interno da implementação).
- **Gazette Notifications de exclusão de "wages"** (CPF Act s.2 / SDL Act s.2: "such payments as the Minister may … specify"): não consultadas. A lista do CPFB é a leitura administrativa delas.
- FAQ de gift vouchers do CPFB: lida por WebFetch (página em JavaScript); **sem cópia local**.
