# HRBS-16234 — Filipinas / McDermott: Maternity Benefit (SSS) e Salary Differential (RA 11210)

> Análise só leitura. Nada foi postado no YouTrack, enviado ou alterado no Drive. País: [[Filipinas]]. Ver também [[correcoes]] (nenhuma entrada sobre Filipinas até hoje).

## Metadados
| Campo | Valor |
|---|---|
| Ticket | HRBS-16234 (Question / Inquiry, Medium; descrição diz "High") — https://youtrack.hrblizz.dev/issue/HRBS-16234 |
| Cliente / entidade | McDermott PH (Wave 2), Legal Entity Phase = Implementation; go-live 2027-01-01 |
| Reporter / assignee | Khoi Pham (kpham) / Enaakshi Vats (evats), Compliance Support |
| Material lido | ticket (`raw/tickets/api/2026-10-22-for-evats/HRBS-16234.md`); anexos `image.png` (snip do cliente) e `image1.png` (print do WTC V2.9 filtrado: 79406 e 79452); WTC exportado hoje `raw/docs/drive-exports/2026-10-22/Philippine Wage Type Catalogue_V2.9.xlsx` (md5 `7801a8fe211049f3e600d6db2bda419c`); hub [[Filipinas]]; `correcoes.md`; pasta do país no Drive (`G:\...\Country Folders\Philippines`) |
| Data da análise | 2026-10-22 |
| Skill carregada | `mercans-compliance-workflow` (a `payroll-compliance-philippines` citada no hub está em `~/.claude/skills/.trash/`; usada só como pista, nada citado dela como fonte) |

## O que foi pedido a nós
Último comentário útil: Vaishnavi (Config) às 2026-10-20 09:48 — "Please assign to regulation team". Ninguém da Compliance respondeu ainda. Pedidos (ações 1–5 da descrição):
1. Revisar a configuração de **Maternity Benefit** e **Salary Differential**: Taxable, SSS base, PhilHealth base, HDMF base, balde 13th month/De Minimis, classificação no 2316.
2. Confirmar o tratamento estatutário em SSS / PhilHealth / HDMF, com referência regulatória.
3. Se a configuração estiver errada: flags corretas e impacto em 1601-C, SSS R3, PhilHealth RF-1, remessa HDMF e mapeamento 2316/Alphalist.
4. Dizer se SIT/parallel run foi afetado e se precisa re-run.
5. Texto que o Khoi possa repassar à McDermott.

Posição do cliente: os dois itens são não tributáveis, ficam fora das bases de SSS, PhilHealth e HDMF e vão como compensação não tributável/isenta no 2316. O snip (image.png) cobre só imposto e 2316, como o próprio Khoi anotou.

## Histórico do ticket
| Data (UTC) | Quem | O quê |
|---|---|---|
| 2026-10-20 04:43 | Khoi Pham | Abre o ticket com as ações 1–5 e anexa 2 imagens |
| 2026-10-20 04:44 | Khoi Pham | cc Vaishnavi Mane |
| 2026-10-20 08:58 / 09:03 | Lavanya Balamurugan (Support) | Recebimento; encaminha ao time de Configuração |
| 2026-10-20 09:48 | Vaishnavi Mane (Config) | "Please assign to regulation team" → assignee Enaakshi |

## O que nosso WTC diz
Fonte: aba `Wage Type Catalogue` do V2.9 exportado (linhas 384 e 392). Bate com o print do cliente (image1.png).

| Coluna WTC | 79406 "Maternity Leave" (linha 384) | 79452 "SSS Salary Differential (Maternity leave Benefit)" (linha 392) |
|---|---|---|
| E Category / G Calc / J Occurrence | Employee Earnings / Lumpsum / Additional | igual |
| O Subject to Tax – Non MWE | **No** | **No** |
| P Subject to Tax – MWE | **No** | **No** |
| S De-minimis Benefit | (vazio) | (vazio) |
| T Subject to FBT | No | No |
| U Subject to SSS | **Yes** | **Yes** |
| V Subject to HDMF | **Yes** | **Yes** |
| W Subject to PhilHealth | **Yes** | **Yes** |
| X BIR2316 Non-MWE / AA BIR2316 MWE | **37** / **37** | **37** / **37** |
| Y Alphalist Non-MWE / Z Alphalist MWE | 7e-1 / 7n | 7e-1 / 7n |
| AB Payslip Display | **NA** | **NA** |
| D Explanation / F Formula | vazios | vazios |

Mais estrutura que importa:
- **Não há coluna "13th month" no WTC.** O 13º (62200–62209) é lumpsum de input, sem fórmula de base. O "balde" do 13th month / De Minimis é o 58102 (13 Month Pay Pre-tax Deduction, mapeado no item 34 do 2316) mais a coluna S. Nenhum dos dois WTs está nesse balde.
- As bases 58521 (HDMF), 58551 (SSS) e 58554 (PhilHealth) são "pro rata" e somam os WTs com flag Yes. Logo, o flag Yes em U/V/W põe o valor na base.
- Aba `58552 Explanation`: a base tributável exclui `79406` (fator 0) e a série `7945x` (fator 0, cobre 79452). Coerente com O/P = No.
- Legenda do WTC: a combinação "Taxable No, SSS/HDMF/PhilHealth Yes" corresponde à categoria **2 "Recurring Earnings – MWW"**. Não há categoria "não tributável e fora de tudo" além da 8 ("not subject to anything").
- 2316: a numeração do WTC segue o **BIR Form 2316 September 2021 (ENCS)**. Nesse leiaute, item 34 = 13th Month Pay and Other Benefits, 35 = De Minimis, 36 = SSS/GSIS/PHIC/Pag-IBIG contributions, **37 = "Salaries and Other Forms of Compensation"** (bloco Non-Taxable/Exempt), 38 = Total Non-Taxable, 39 = Basic Salary (tributável). Conferido na cópia do formulário (ver Fonte primária, item 9).

## Fonte primária
Cópias novas salvas em `raw/docs/oficiais/PH/` (todas com prefixo 2026-10-22).

| # | Fonte | Trecho (literal) | Cópia local | Situação |
|---|---|---|---|---|
| 1 | **RA 11210** (105-Day Expanded Maternity Leave Law), Sec. 5(c), que altera a Sec. 14-A do SS Act | "Employers from the private sector shall be responsible for payment of the salary differential between the actual cash benefits received from the SSS by the covered female workers and their average weekly or regular wages" | `2026-10-22-RA-11210-texto_lawphil.html` | ⚠️ Texto do LawPhil (repositório). A RMC 105-2019 (item 3) cita o mesmo trecho. Não baixado do Official Gazette |
| 2 | **IRR do RA 11210** (CSC/DOLE/SSS, 1º/maio/2019): Rule II Sec. 1(j); Rule III Sec. 2; Rule VI Secs. 3–5 | Rule III Sec. 2: "Employed female workers shall receive full pay which consists of (i) SSS maternity benefit computed based on their average daily salary credit and (ii) salary differential to be paid by the employer". Rule II 1(j) "Full pay" = "actual remuneration or earnings … including allowances provided for under existing company policy or collective bargaining agreement". Rule VI Sec. 4: o SSS reembolsa "only to the extent of one hundred percent (100%) of her average daily salary credit". **O IRR não trata de imposto, contribuições nem 13º** (busca no texto completo) | `2026-10-22-RA-11210-IRR-2019_lawphil.html` | ⚠️ LawPhil |
| 3 | **BIR RMC No. 105-2019** (3/set/2019), "Clarifies the Proper Tax Treatment of Maternity Leave Benefits Under RA 11210" | Classifica o salary differential como "benefit" sob o SS Act e conclui: "since the provisions of Section 2.78.1(B)(1)(e) under RR No. 2-98 do not provide any qualification in granting tax exemption on payments of benefits under the SSS law, the salary differential is exempt from income and withholding taxes." Transcreve a RR 2-98 Sec. 2.78.1(B)(1)(e): "Payments of benefits made under the Social Security System Act of 1954, as amended" | `2026-10-22-BIR-RMC-105-2019-salary-differential-RA11210_mirror-GrantThornton.pdf` | ⚠️ Cópia digitalizada do documento assinado, espelhada pela Grant Thornton. O CDN do BIR devolveu 403 e a lista de RMCs do site não carregou no Chrome |
| 4 | **NIRC Sec. 32(B)(6)(e)** | "Benefits received from or enjoyed under the Social Security System in accordance with the provisions of Republic Act No. 8282." (exclusão da renda bruta) | `2026-10-22-NIRC-RA-8424-texto-original_lawphil.html` | ⚠️ Texto original do RA 8424 (LawPhil). A alínea (e) não foi alterada pelo TRAIN, mas isso não foi conferido na versão consolidada do BIR |
| 5 | **RA 11199** (SS Act 2018), Sec. 8(f), Secs. 18–19 e Sec. 14-A | 8(f) "Compensation – All actual remuneration for employment, including the mandated cost-of-living allowance, as well as the cash value of any remuneration paid in any medium other than cash…". Sec. 18: contribuição do empregado "corresponding to his salary, wage, compensation or earnings during the month". Sec. 14-A(e): o SSS reembolsa ao empregador o benefício adiantado | `2026-10-22-SSS-RA-11199-SS-Act-2018-booklet_copia-Drive.pdf` (booklet oficial do SSS, mar/2019, cópia do Drive) | OK. O booklet traz a 14-A antes do RA 11210 (60/78 dias) |
| 6 | **SSS – página "Maternity Benefit"** | Define o salary differential como "the amount borne by the employer relative to the difference between the actual cash benefits received from the SSS and the regular wage". **Não diz se o benefício ou o differential entram na MSC** | `2026-10-22-SSS-pagina-maternity-benefit.html` | OK (oficial). A SSS Circular 2019-009 não foi achada no site do SSS ⚠️ |
| 7 | **PhilHealth Circular 2020-0005 (Revision 1)**, IV.F, V.B, V.D | IV.F "Monthly Basic Salary (MBS) – the fixed basic rate of an employee which shall not include sales commission, overtime pay, allowances, thirteenth month pay, bonuses or other gratuity payments. Further to this, those deductions to the employee's pay occasioned by his/her under time, tardiness, leave(s) without pay, absences, or other similar circumstances shall also be excluded in this computation." V.B: premium "computed straight based on the monthly basic salary". **V.D "The employers shall ensure that the premium contribution of women who are on maternity leave shall be regularly remitted to PhilHealth pursuant to the Department Advisory No. 01 s. 2019 of the DOLE"** | `2026-10-22-PhilHealth-PC-2020-0005-Rev1_copia-Drive.pdf` (cópia "Master Copy" do Drive, digitalizada; lida página a página) | OK. A Advisory 2026-0042 sobre a persistência da taxa não foi relida aqui |
| 8 | **HDMF: RA 9679 Sec. 4(b) e Sec. 7; Circular 460 §C** | RA 9679 4(b): "Compensation – basic monthly salary plus mandated cost of living allowance." Circ. 460 §C: "Fund Salary" = "the basic salary and other allowances … the remuneration or earnings … which is payable by an employer to an employee … for work done or to be done, or for services rendered or to be rendered"; teto MFS **₱10.000** | `2026-10-22-HDMF-RA-9679-texto_lawphil.html`; `2026-10-22-HDMF-Circular-460-MFS-2024_copia-Drive.pdf` | RA ⚠️ LawPhil; Circ. 460 OK (cópia do Drive). **O IRR do RA 9679 não foi obtido** ⚠️. Nenhuma norma do HDMF sobre licença-maternidade foi encontrada ⚠️ |
| 9 | **BIR Form 2316 Sept 2021 (ENCS)** e Jan 2018 (ENCS) | Sept 2021: item 37 "Salaries and Other Forms of Compensation" no bloco Non-Taxable/Exempt (no Jan 2018 é o item 35) | `2026-10-22-BIR-Form-2316-Sep2021-ENCS_mirror.pdf` | ⚠️ Espelho (CDN do BIR = 403). **Nenhuma instrução do BIR diz em que linha do 2316 vai o benefício de maternidade.** O item 37 é a leitura natural |
| 10 | **DOLE-BWC Handbook on Workers' Statutory Monetary Benefits (2023)**: cap. 8 (Maternity Leave), cap. 13 item H, cap. PhilHealth | 13th month, item H: "The salary differential shall be included as part of the basic salary for purposes of computation of the 13th-month pay of the rank-and-file employee" (nota hh → DA 01-2019). PhilHealth: "premium contribution of women who are on maternity leave shall be regularly remitted to PhilHealth pursuant to DOLE Department Advisory No. 1, Series of 2019" | `2026-10-22-DOLE-BWC-Handbook-Statutory-Monetary-Benefits-2023_copia-Drive.pdf` | OK (oficial DOLE-BWC) |
| 11 | **DOLE Department Advisory No. 01 s. 2019** (9/jul/2019), cálculo do salary differential | Segundo fontes **secundárias**, a fórmula é: full pay do período − parte do empregado em SSS/PhilHealth/Pag-IBIG "covering the maternity period" − benefício SSS = differential | — | ⚠️ **Não obtido.** dole.gov.ph fica atrás de desafio Cloudflare (não contornado). Só a regra do 13º e a da PhilHealth estão confirmadas, via Handbook (10) e PC 2020-0005 (7) |
| — | DOLE DA 001-A-19 (4/nov/2019), que repassa a RMC 105-2019 | Só por fonte secundária (digest.ph) | — | ⚠️ não obtido |

## Veredito por elemento
Legenda: **Correto** = o WTC bate com a fonte; **Divergente** = o WTC contraria a fonte; **⚠️ Não confirmado** = sem fonte primária específica.

### Maternity Benefit do SSS (WT 79406)
| Tratamento | Regra | Fonte | WTC hoje | Veredito |
|---|---|---|---|---|
| Imposto (withholding / IR) | Isento: benefício recebido do SSS | NIRC 32(B)(6)(e); RR 2-98 2.78.1(B)(1)(e) (transcrita na RMC 105-2019) | O = No, P = No; fora de 58552 | **Correto** |
| 2316 / Alphalist | Compensação não tributável/isenta: item 37 do 2316 Sept 2021 ("Salaries and Other Forms of Compensation"); fora do item 34 (balde de ₱90.000) e do 35 (de minimis) | Formulário 2316 Sept 2021 (leiaute). Nenhuma instrução específica do BIR ⚠️ | X/AA = 37; Y/Z = 7e-1 / 7n | **Correto** no 2316. Alphalist 7e-1/7n ⚠️ não conferido contra o leiaute oficial do 1604-C |
| SSS | Não é "actual remuneration for employment": é benefício pago pelo SSS (o empregador adianta e é reembolsado em 100% do ADSC) | RA 11199 Sec. 8(f) + Sec. 14-A(e); IRR RA 11210 Rule VI Sec. 4 | U = **Yes** | **Divergente** (pela letra da lei; nenhuma circular do SSS diz isso de forma expressa ⚠️) |
| PhilHealth | O prêmio incide sobre o **MBS** (taxa básica fixa, contratual), não reduzido por licença, e **continua sendo remetido durante a licença-maternidade**. O benefício do SSS não é MBS | PC 2020-0005 IV.F, V.B, V.D; Handbook DOLE | W = **Yes** | **Divergente no flag.** O resultado certo é o prêmio sobre o MBS integral na licença, não sobre o valor do benefício (ver nota abaixo) |
| HDMF | Base = "basic monthly salary plus mandated COLA" / remuneração "payable by an employer … for work done". O benefício do SSS não é pago pelo empregador como salário | RA 9679 Sec. 4(b); Circ. 460 §C | V = **Yes** | **Divergente** (pela definição; nenhuma norma do HDMF sobre maternidade ⚠️). Impacto pequeno: teto MFS de ₱10.000 |
| 13th month | Fica fora: o 13º é 1/12 do "basic salary" pago pelo empregador; o benefício do SSS não é salário pago pelo empregador | PD 851 / Handbook (definição de basic salary). A exclusão expressa do benefício SSS só aparece em fontes secundárias ⚠️ | O WTC não tem coluna de base do 13º; não está no balde 58102/item 34 | **Correto** quanto ao balde. A base do 13º é de config e não está no WTC |

### Salary Differential pago pelo empregador (WT 79452)
| Tratamento | Regra | Fonte | WTC hoje | Veredito |
|---|---|---|---|---|
| Imposto | **Isento** de IR e withholding: o BIR o trata como benefício sob o SS Act | **BIR RMC 105-2019** (+ RR 2-98 2.78.1(B)(1)(e)) | O = No, P = No; série 7945x fora de 58552 | **Correto** |
| 2316 / Alphalist | Não tributável/isento → item 37. Não vai no item 34: é isento por natureza, fora do teto de ₱90.000 | RMC 105-2019 + leiaute do 2316 Sept 2021 ⚠️ (sem instrução de linha) | X/AA = 37; Y/Z = 7e-1 / 7n | **Correto** no 2316. Alphalist ⚠️ |
| SSS | Pago pelo empregador, mas o IRR (Rule III Sec. 2) e o BIR (RMC 105-2019) o tratam como **componente do benefício de maternidade**, não como remuneração por serviço. **Nenhuma norma do SSS trata da MSC sobre o differential** | RA 11199 Sec. 8(f); IRR RA 11210 Rule III Sec. 2; RMC 105-2019 (tributário, por analogia) | U = **Yes** | **⚠️ Não confirmado.** Inclina para a exclusão (fonte da classificação como benefício). Falta norma do SSS |
| PhilHealth | Mesma regra do 79406: o prêmio é sobre o MBS e continua na licença. O differential não é a "fixed basic rate" | PC 2020-0005 IV.F, V.B, V.D | W = **Yes** | **Divergente no flag** (com a mesma ressalva de resultado do 79406) |
| HDMF | Pago pelo empregador durante a licença, sem trabalho prestado. A Circ. 460 fala em remuneração "for work done… or services rendered". Nenhuma norma do HDMF sobre o differential | RA 9679 Sec. 4(b); Circ. 460 §C | V = **Yes** | **⚠️ Não confirmado.** Impacto limitado pelo teto de ₱10.000 |
| 13th month | **Entra** na base do 13º (como basic salary) | **Handbook DOLE-BWC 2023, cap. 13, item H** (nota → DA 01-2019) | O WTC não tem coluna de base do 13º; não está no balde 58102/item 34 | **Correto** quanto ao balde. ⚠️ A config do cálculo do 13º (fora do WTC) precisa incluir o 79452 e excluir o 79406 |

**Nota sobre PhilHealth (vale para os dois WTs).** A posição do cliente ("excluir da base") está certa quanto ao WT, mas não basta: se o mês de licença zerar o básico (por exemplo, via 62109 "Unpaid LOA – Basic salary", que no WTC tem PhilHealth = **Yes**) e os WTs de maternidade saírem da base, o prêmio do mês cai ou zera. Isso contraria a PC 2020-0005 IV.F (o MBS não é reduzido por licença) e a V.D (o prêmio de quem está em licença-maternidade continua sendo remetido). O resultado correto é **prêmio sobre o MBS contratual integral durante a licença**. Como o engine chega a isso (base 58554 vinda do salário contratual ou ajuste no 62109) é decisão de Config/BA, não nossa.

**Nota sobre SSS/HDMF durante a licença.** Fontes secundárias atribuem ao DA 01-2019 a dedução, no cálculo do differential, da parte do empregado em SSS/PhilHealth/Pag-IBIG "covering the maternity period". Isso sugere que o DOLE supõe contribuições continuando na licença. Sem o texto oficial do DA (⚠️), não dá para afirmar a base de SSS/HDMF no mês de licença. Só a da PhilHealth está provada.

## Impacto em relatórios
Se os flags U/V/W de 79406/79452 mudarem, o impacto cai só sobre os meses em que esses WTs forem pagos:

| Relatório | Impacto |
|---|---|
| **BIR 1601-C** (mensal) | **Nenhum** no imposto: os flags O/P já estão em No e o 58552 já exclui os dois. A linha de "other non-taxable compensation" do 1601-C não foi conferida contra o leiaute ⚠️ |
| **BIR 2316 / 1604-C Alphalist** | **Nenhum.** Item 37 está correto. Alphalist 7e-1/7n ⚠️ não conferido. Os itens 34 (₱90.000) e 35 (de minimis) não são afetados |
| **SSS R3 / e-CL** | Muda a faixa de MSC (e o EC/MPF) do mês de licença. Com o benefício fora da base (Divergente), a contribuição do mês cai para a faixa da remuneração realmente paga. Para o differential, depende da confirmação ⚠️ |
| **PhilHealth RF-1** | O prêmio do mês de licença deve ser o do MBS integral (até o teto de ₱100.000). Tirar os WTs da base sem garantir o MBS sub-remete |
| **HDMF (MCRF / remessa)** | Só muda quando o restante da base HDMF do mês fica abaixo de ₱10.000 (MFS). Acima disso, a contribuição fica em ₱200 por lado de qualquer forma |
| **SIT / parallel run** (ação 4) | Pela análise, só dá para afirmar o seguinte: (a) imposto, 1601-C e 2316 **não foram afetados** pelos flags atuais; (b) em qualquer período de SIT/parallel com 79406 ou 79452 pagos, as bases 58551 (SSS), 58554 (PhilHealth) e 58521 (HDMF) **incluíram esses valores**; (c) se houve ou não esses WTs nos dados de SIT e se é preciso re-run, **não dá para saber daqui**: depende dos outputs, que não temos. A entidade está em Implementation (go-live 2027-01-01), então não deve haver remessa de produção afetada ⚠️ (a confirmar com a Implementação) |

## Achados fora do pedido
(Vão para Pendências do hub [[Filipinas]], não para o ticket.)
1. **Versão do WTC:** o arquivo se chama V2.9, mas o Version Control traz duas linhas "Version 3.0" (2026-01-26, remapeamento da série 6296%; 2026-10-08, flag 58237 "Stop Phil Health Employer Contribution"). O Drive tem ainda `Wage Type Catalogue_Philippines_v3 (1).gsheet`. A linhagem (V2.9 × v3) precisa ser esclarecida antes de qualquer nova versão (regra 8 e memória "Base = linhagem do Drive").
2. **62109 "Unpaid LOA – Basic salary" com PhilHealth = Yes:** se for negativo, reduz a base PhilHealth em licença sem remuneração e falta, o que contraria a PC 2020-0005 IV.F.
3. **Licenças pagas inconsistentes na PhilHealth:** Vacation/Sick/Emergency/Solo Parent/VAWC/Special Leave for Women/Long Service estão com PhilHealth = **No**; Paternity (79407), Maternity (79406) e Differential (79452) estão com **Yes**. Para PhilHealth (base MBS), nenhuma licença paga deveria mexer na base. A divergência mostra que o desenho da base 58554 precisa de revisão.
4. **Payslip Display = NA** em 79406 e 79452, dois pagamentos ao empregado. O holerite não mostraria a maternidade.
5. **Colunas D (explicação) vazias** nos dois WTs: não há definição de que 79406 = benefício SSS adiantado (reembolsável) e 79452 = differential do empregador.
6. **Skill `payroll-compliance-philippines` está na lixeira** (`~/.claude/skills/.trash/...`), mas o hub a cita como fonte da ficha do país.
7. Há sobreposição com o pedido 13th month: o WTC não tem onde dizer quais WTs entram na base do 13º. A regra do DOLE (o differential entra) precisa estar na config do cálculo do 13º.

## Rascunho de resposta (EN)
> Para o Khoi repassar. Não postado. Apresentar ao usuário antes de gravar como draftComment.

Hi @kpham,

**Income tax / BIR 2316** — Both elements are exempt from income tax and withholding tax on compensation:
- SSS maternity benefit: NIRC Sec. 32(B)(6)(e) ("Benefits received from or enjoyed under the Social Security System") and RR 2-98 Sec. 2.78.1(B)(1)(e).
- Employer-paid salary differential (RA 11210 Sec. 5(c)): BIR RMC No. 105-2019 (3 Sep 2019) classifies the differential as a benefit under the SSS law and concludes it "is exempt from income and withholding taxes".

In the PH WTC, 79406 (Maternity Leave) and 79452 (SSS Salary Differential) are already set to Subject to Tax = No (Non-MWE and MWE) and excluded from Period Taxable Income (58552). Both map to BIR 2316 item 37, "Salaries and Other Forms of Compensation", under Non-Taxable/Exempt Compensation (Form 2316, Sept 2021 ENCS). Neither falls in the ₱90,000 13th-month/other-benefits bucket (item 34) or in de minimis (item 35). The tax and 2316 configuration matches the client's reference.

**PhilHealth** — The premium is computed on the Monthly Basic Salary, "the fixed basic rate of an employee", which excludes allowances and is not reduced by "leave(s) without pay, absences, or other similar circumstances" (PhilHealth Circular 2020-0005 Rev. 1, Sec. IV.F and V.B). Sec. V.D adds: "the premium contribution of women who are on maternity leave shall be regularly remitted to PhilHealth". The SSS maternity benefit and the salary differential are therefore not part of the PhilHealth base. The premium for the leave months remains due on the employee's full contractual Monthly Basic Salary. The WTC currently has Subject to PhilHealth = Yes on both 79406 and 79452.

**SSS** — SSS contributions are based on "compensation", defined as "all actual remuneration for employment" (RA 11199 Sec. 8(f)). The SSS maternity benefit is an SSS benefit that the employer advances and the SSS reimburses (RA 11199 Sec. 14-A; RA 11210 IRR Rule VI Sec. 4), so it is not remuneration for employment. For the salary differential, we found no SSS issuance on its inclusion in the Monthly Salary Credit. The RA 11210 IRR (Rule III Sec. 2) defines the female worker's "full pay" as the SSS maternity benefit plus the salary differential, and BIR RMC 105-2019 treats the differential as part of the SSS maternity benefit. The WTC currently has Subject to SSS = Yes on both.

**HDMF (Pag-IBIG)** — The contribution base is "basic monthly salary plus mandated cost of living allowance" (RA 9679 Sec. 4(b)). Pag-IBIG Circular No. 460 defines Fund Salary as remuneration payable by the employer "for work done… or for services rendered", capped at ₱10,000. The SSS maternity benefit is not remuneration paid by the employer. For the salary differential, we found no HDMF issuance addressing it. The WTC currently has Subject to HDMF = Yes on both.

**13th month pay** — The salary differential is included as part of basic salary for the 13th-month computation (DOLE-BWC Handbook on Workers' Statutory Monetary Benefits 2023, Ch. 13 item H, citing DOLE Department Advisory No. 01 s. 2019).

**SIT / parallel run** — Tax, 1601-C and 2316 results are not affected. In any SIT/parallel-run period where 79406 or 79452 was paid, those amounts were included in the SSS (58551), PhilHealth (58554) and HDMF (58521) bases.

Kind regards,

> Notas para quem revisar (não vão no comentário): (1) a frase sobre SIT só vale como está, porque não vimos os outputs; (2) SSS/HDMF do differential ficam sem veredito no texto, por falta de norma do SSS/HDMF. Se o usuário quiser fechar o ponto, é preciso obter o DA 01-2019 oficial e/ou a SSS Circ. 2019-009; (3) o texto não prescreve mudança de flag, por disciplina de escopo. A Config tira a conclusão.

## O que precisa ser feito
| # | O quê | Quem | Urgência |
|---|---|---|---|
| 1 | Aprovar/ajustar o rascunho acima e decidir se vai como draftComment no HRBS-16234 | Usuário → janela Suporte | Antes de 2026-12 (go-live 2027-01-01) |
| 2 | Obter o texto oficial do **DOLE DA 01-2019** (dole.gov.ph bloqueia automação; abrir manualmente no navegador) e, se possível, a **SSS Circular 2019-009**, para fechar SSS/HDMF do differential | Usuário (download manual) → Compliance | Alta: define o veredito em aberto |
| 3 | Correção do WTC (nova versão a partir da maior da linhagem, ver achado 1): U/V/W de 79406 → No; W de 79452 → No; U/V de 79452 conforme o item 2; preencher a coluna D; rever o Payslip Display | Pipeline/Design do WTC (Mohit, último a versionar) com ok do usuário | Antes do go-live |
| 4 | Garantir que a base PhilHealth do mês de licença = MBS contratual integral (62109 e base 58554) | Config/BA (fora do nosso escopo; a resposta informa a regra) | Antes do go-live |
| 5 | Verificar se houve 79406/79452 nos dados de SIT/parallel run da McDermott e, se houve, decidir sobre re-run de SSS/PhilHealth/HDMF | Implementação/Config (Khoi/Vaishnavi) | Antes do go-live |
| 6 | Garantir que o cálculo do 13º inclua 79452 e exclua 79406 | Config (fora do WTC) | Antes de dez/2027 (1º 13º em produção), mas testar no SIT |
| 7 | Registrar no hub (Pendências: achados 1–7) e, depois do ticket, no Suporte do hub | Janela Suporte, com ok do usuário | Ao fechar a sessão |

## Lacunas
- ⚠️ **DOLE DA 01-2019** (texto oficial) não obtido: a fórmula com dedução das contribuições do empregado é só de fonte secundária.
- ⚠️ **SSS Circular 2019-009** não obtida. Nenhuma norma do SSS diz se o differential entra na MSC.
- ⚠️ **Norma do HDMF** sobre licença-maternidade/differential não encontrada. O IRR do RA 9679 não foi obtido.
- ⚠️ **RMC 105-2019**: só a cópia espelhada (Grant Thornton) da versão assinada. O site do BIR não serviu o PDF.
- ⚠️ RA 11210, IRR, RA 9679 e NIRC lidos pelo LawPhil (repositório), não pelo Official Gazette/BIR.
- ⚠️ Linha do 2316 para o benefício de maternidade: nenhuma instrução do BIR; item 37 é inferência pelo leiaute. A versão vigente do 2316 (Sept 2021) foi conferida só por espelho.
- ⚠️ Colunas da Alphalist (7e-1, 7n) e a linha do 1601-C não foram conferidas contra o leiaute oficial.
- ⚠️ Exclusão do benefício SSS da base do 13º: sem fonte primária expressa (só pela definição de basic salary).
- Sem acesso aos outputs de SIT/parallel run nem à config da entidade McDermott (base 58554, uso do 62109 na licença).
- Linhagem do WTC (V2.9 com linhas "3.0" × `v3 (1).gsheet`) não resolvida; a análise usou o V2.9 exportado hoje, o mesmo do print do cliente.
