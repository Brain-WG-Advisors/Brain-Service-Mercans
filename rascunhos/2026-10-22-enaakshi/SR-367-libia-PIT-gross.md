# SR-367: Líbia, LY-TAX-PIT-001 (Monthly PIT Withholding Return): o "Gross Salary" inclui o Exempt Income Amount?

## Metadados
- **Ticket:** SR-367, LY-TAX-PIT-001-MonthlyPITWithholding-Spec. Estado In Review, fase *Final Review Phase - Business Analyst*. Research Analyst: Enaakshi Vats. Assignee: wgomes desde 22/10. Dev: Michael Mukosi John. BA: Lily Li.
- **Relatório:** `ly-tax-monthly-pit-withholding-return`, em **acceptance** no nível país Líbia ("LY Monthly Declared Payroll & PIT Withholding Return"), teste REF-04-363 (Michael, 15/10).
- **Spec vigente:** LY-TAX-PIT-001 v1.0. O Version Control só tem a 1.0 de 2026-07-20, apesar das mudanças de 15/09. Export de 22/10: `raw/docs/drive-exports/2026-10-22/LY-TAX-PIT-001-MonthlyPITWithholding-Spec-v1_0.xlsx`.
- **Fonte do ticket:** `raw/tickets/api/2026-10-22-for-evats/SR-367.md`. Anexos em `raw/tickets/api/anexos/SR-367/`.
- **Análise:** 2026-10-22, janela Suporte. Só leitura: nada foi postado nem alterado.

## O que foi pedido a nós
Lily, 20/10 10:00, com @evats: *"In LY monthly PIT report, does gross salary refer to taxable gross OR it also includes Exempt Income Amount as well? Currently, Gross Salary is mapped to taxable gross with Exempt Income Amount excluded. … Based on my testing, gross salary should included Exempt Income Amount. Pls confirm."*
O print (`image.png`) mostra a aba de spec com as linhas 18 (Gross Salary) e 19 (Exempt Income Amount, em amarelo) e as explicações da coluna M.

Só isto: o "Gross Salary" do relatório é o bruto tributável ou inclui a renda isenta?

## Histórico do ticket
| Data | Quem | O quê |
|---|---|---|
| 2026-07-20 | Enaakshi | Abre o SR com a spec v1_0 |
| 2026-09-14 | Lily | Pergunta se o Exempt Income Amount cobre só EOS e férias na rescisão, porque o WTC tem mais tipos isentos |
| 2026-09-15 | Enaakshi | "it should include all exempt incomes". Muda os textos (em amarelo), **move "Exempt income" para logo depois de "Gross"**, remove "Exempt income type" e ajusta os exemplos |
| 2026-09-16 | Lily | "Mapping done" |
| 2026-10-15 | Michael | Relatório desenvolvido e em acceptance; anexa template e amostra de teste |
| 2026-10-20 | Lily | Pergunta Gross × Exempt (esta) |

## O que nossos artefatos dizem
**Spec, aba "PIT Withholding Spec":**
| Linha | Campo | O que diz |
|---|---|---|
| 8 (header) | Total Gross Salaries | M8 "Sum of gross salaries across all employee rows"; T8 = SUM de "Gross Salary" |
| 18 | **Gross Salary** | M18 "Total monthly gross employment income (basic + allowances + overtime + bonuses + in-kind cash value) for Libya services." **T18 (BA) = 58008** (WTC: "Period Gross Salary Current", Intermediary, sem explicação no WTC) |
| 19 | **Exempt Income Amount** | F19 = C; G19 "Populated only when an exempt payment (like severance / accrued-leave payout) is made"; M19 "Statutorily exempt amounts paid in the month (end-of-service indemnity; accrued-leave payout on termination) — reported for transparency, excluded from the taxable base (Art. 55)"; T19 = "SUM of pay elements under the sheet 'Exempt Income'" |
| 21 | Social Unity Fund (1%) | M21 "= gross × 1%"; T21 = 2553 |
| 25 | **Taxable Income (Base)** | M25 "Monthly taxable base = **Gross − Exempt Amount** - Employee SS − Social Unity Fund − Personal Exemption, with statutory exclusions removed (Art. 55). Floored at 0." T25 = 58552 (Taxable Income PIT Base) |
| 29 | Net Salary | M29 "Gross − Employee SS − Social Unity Fund − PIT withheld − other deductions" |

- **A fórmula da linha 25 só fecha se o Gross incluir a renda isenta**: ela tira o Exempt Amount do Gross. Se o Gross já for o tributável (58008, segundo a Lily), a renda isenta sai duas vezes. O trecho "Gross − Exempt Amount -" usa hífen comum, ao contrário dos "−" do resto, o que sugere inserção posterior (provavelmente a mudança de 15/09). Isso é só um indício.
- **Aba "Exempt Income"** (lista do T19): 76 códigos, todos com *Subject to Tax = No* no LY WTC V3.0 (conferi 62180, 62305, 62504, 62505, 62540, 62550, 62570, 62640, 62800, 62810, 62820, 62900). Incluem severance/EOS, férias pagas, reembolsos de despesa, pensões, diárias, carro, mudança, passagem, estacionamento, "Donation recovery".
- **Textos que contradizem a linha 25:** M18 não menciona a renda isenta, M19 ainda lista só EOS e férias (contra o "all exempt incomes" de 15/09), Payroll Scope Summary C21 "reported as exempt income, excluded from the taxable base", File Structure B12 "Gross − employee SS − Social Unity Fund − personal exemption; statutory exclusions removed".
- **Aba Sample File:** N16/N17 = `MAX(G − I − J − M, 0)`. **Não subtrai a coluna H** (Exempt Amount). Os exemplos têm H = 0, então não testam o caso.

**Template do dev** (`20261015-1415 - ly-tax-monthly-pit-withholding-return_template.xlsx`): G = `Gross Salary`, H = `Exempt Income Amount`, N = `Taxable Income (Base)`, cada um vindo da sua coluna do relatório. O relatório não recalcula: só exibe o que o motor entrega (58008, soma da lista, 58552).

**Amostra do teste:** 3 empregados, todos com **Exempt Amount = 0**. A amostra não exercita a pergunta, e o teste em que a Lily se baseou não está no ticket.

**CCG LY-CCG-001 v1.0:** Step 1 "Sum all cash and in-kind employment earnings … except the specific statutory exclusions (reimbursed actual work expenses, disciplinary deductions, end-of-service pay, and accrued-leave payout on termination)" (Mod. 3.1); "Statutorily excluded items … are removed from the base entirely (Art. 55)" (Mod. 6). A CCG trata o bruto do G2N como bruto tributável. O relatório é outra coisa: é a lista do art. 60, e desde 15/09 traz a renda isenta numa coluna própria.

## Fonte primária
1. **Lei 7/2010 (Imposto de Renda), art. 55**. Texto árabe (`815-Law-7-2010-IncomeTax_AR.pdf`, p. 14–15) e tradução DCAF não oficial (`815-Law-7-2010-IncomeTax_EN.pdf`, p. 11–12):
   > "tax on work income and other income from any service or job … shall apply, including: a. … all payments, recurrent and non-recurrent, whether cash or in kind … The tax set out in this Article shall not apply to the following: 1. Contributions … to the retirement system … 2. Amounts received … for actual expenses incurred in performing their work. 3. Deductions … for disciplinary penalties … 4. Cash allowance for accumulated leaves at the end of service. 5. End of service remuneration."
   (AR: "ولا تسري الضريبة المنصوص عليها في هذه المادة على ما يلي: … 4. البدل النقدي عن الإجازات المتراكمة عند نهاية الخدمة. 5. مكافأة نهاية الخدمة.")
   → EOS e férias pagas na rescisão são **rendimento do trabalho sobre o qual o imposto não incide**. Não deixam de ser rendimento pago.
2. **Art. 57:** "Tax shall be assessed on the total amount of income subject to this tax … over the deduction limit." O imposto incide sobre a renda **sujeita**. O conceito de base tributável é separado do de rendimento recebido.
3. **Art. 60** (AR p. 16; EN p. 13): "The employers … shall submit a list of the names of those working for it, their domiciles, positions and **income received** to the Authority." (AR: "وما يتقاضونه من دخول"). A lista legal que o relatório representa pede **o rendimento recebido**, não o tributável.
4. **Formulário oficial:** `Tax-model-1-report.pdf` **não é o formulário da declaração mensal**. É o **Modelo nº 1 (Impostos), "إخطار بوجود ممول خاضع للضريبة"** (notificação da existência de contribuinte sujeito ao imposto), com base no art. 1 do regulamento executivo da Lei 7/2010. Tem 9 campos de identificação do contribuinte e **nenhum campo de salário, bruto ou isento**. Não há na pasta da Líbia formulário oficial da lista mensal do art. 60, e a spec o declara DERIVED (Report Matrix B13, B14; B21 "~70% confidence on FIELD LAYOUT"). Logo, **nenhum formulário oficial define o "Gross Salary"** nem tem linha própria para isentos.
   Arquivos: `G:\Drives compartilhados\Compliance Team\Country Folders\Libya\14 - Legislation\` (`Tax-model-1-report.pdf`, `815-Law-7-2010-IncomeTax_AR.pdf`, `815-Law-7-2010-IncomeTax_EN.pdf`).

## Veredito
**Confirmado (a leitura da Lily está certa): o Gross Salary do relatório deve incluir o Exempt Income Amount.**
- Não há definição legal do rótulo (sem formulário oficial). A resposta vem da **coerência interna da spec**: a linha 25 define Taxable Base = Gross − Exempt − SS − SUF − Personal Exemption, e desde 15/09 o Exempt Income Amount vem logo depois do Gross e cobre toda a renda isenta. A sequência Gross → (−) Exempt → (−) SS → (−) SUF → (−) PE → Base só fecha com Gross = tributável + isento.
- Está de acordo com a lei: o art. 60 pede o rendimento **recebido**, e o art. 55 trata EOS e férias pagas como rendimento do trabalho em que o imposto não incide.
- **O que a spec deve dizer:** Gross Salary = total do rendimento do trabalho pago no mês (tributável + isento); Exempt Income Amount = parte não tributável (lista da aba "Exempt Income"), já contida no Gross; Taxable Base = Gross − Exempt − SS − SUF − PE. O mapeamento (T18) é da BA: 58008 + soma da lista "Exempt Income", ou um acumulador equivalente.

## Mudança na spec
Aba **PIT Withholding Spec**:
| Célula | Antes | Depois |
|---|---|---|
| M18 | Total monthly gross employment income (basic + allowances + overtime + bonuses + in-kind cash value) for Libya services. | Total monthly gross employment income paid for Libya services: taxable earnings (basic + allowances + overtime + bonuses + in-kind cash value) **plus the exempt income reported in Exempt Income Amount**. Art. 60 list of income received. |
| M19 | Statutorily exempt amounts paid in the month (end-of-service indemnity; accrued-leave payout on termination) — reported for transparency, excluded from the taxable base (Art. 55). | Non-taxable amounts paid in the month: **all pay elements listed in the sheet "Exempt Income"** (e.g. end-of-service indemnity, accrued-leave payout on termination, reimbursed actual expenses — Art. 55). **Included in Gross Salary** and deducted from it to arrive at the taxable base. |
| G19 | Populated only when an exempt payment (like severance / accrued-leave payout) is made. | Populated only when an exempt payment (any pay element in the sheet "Exempt Income") is made. |
| M25 | Gross − Exempt Amount - Employee SS − … | Gross − Exempt Income Amount − Employee SS − Social Unity Fund − Personal Exemption (Art. 55, 57). Floored at 0. *(só uniformiza; o conteúdo não muda)* |
| M21 | Employee Social Unity Fund contribution = gross × 1%. … | Employee Social Unity Fund contribution = 1% of the Social Unity Fund base (see LY-TAX-SUF-001). … *(evita ler "gross" como o novo Gross com isentos; ver lacuna sobre a base do SUF)* |

Aba **Sample File**: N16 `=MAX(G16-I16-J16-M16,0)` → `=MAX(G16-H16-I16-J16-M16,0)`; N17 idem. Opcional: um 3º empregado com Exempt Amount > 0 para ilustrar.
Aba **Payroll Scope Summary**, C21: "Exempt from PIT (Art. 55) — reported as exempt income, excluded from the taxable base." → "Exempt from PIT (Art. 55): included in Gross Salary, reported in Exempt Income Amount and deducted from the taxable base."
Aba **File Structure**, B12: "Gross − employee SS − Social Unity Fund − personal exemption; statutory exclusions removed (Art. 55); floored at zero." → "Gross − Exempt Income Amount − employee SS − Social Unity Fund − personal exemption (Art. 55); floored at zero."
**Version Control**: linha 1.1 · 2026-10-22 · "SR-367: Gross Salary includes Exempt Income Amount; explanations (M18, M19, G19, M21, M25), Scope C21, File Structure B12 and Sample formula aligned" · wgomes. (A mudança de 15/09 também não foi versionada. Pode entrar como 1.1, e esta como 1.2, se o usuário preferir.)
**T18 (BA Mapping):** não é nossa coluna. A Lily ajusta.

## Achados fora do pedido
1. **"Official Source" errada** (Report Matrix B20): "Tax registration form 'Tax model 1' (طلب تسجيل ممول)". O documento é o Modelo 1, *notificação* de contribuinte (إخطار بوجود ممول خاضع للضريبة), e não serve de fonte para o layout mensal. Corrigir o título e deixar claro que não há formulário mensal oficial.
2. **Dedução do SUF atribuída ao art. 55** (M21 "Deducted from gross before PIT"; no SUF, Scope C13). O art. 55 não lista o SUF. A fonte é só a PwC (2026-05-31). ⚠️ sem fonte primária.
3. **Tradução DCAF do art. 58 errada:** "First 1200 LYD of income: 5%". O texto árabe diz 12.000 (= 1.000/mês). A spec está certa (1.000/mês); o risco é alguém citar a versão EN.
4. **Arredondamento na saída do dev:** Total PIT e Net saem com 2 casas (ex.: O14 = 12.188 e Q14 = 12.19; Q16 = 2105.19 contra O16 + P16 = 2105.188). A spec pede "Nearest 0.001 LYD" (P26–P29) e o formato é `#,##0.000`. Avisar a Lily/dev.
5. **Net Salary do dev desconta o selo de 0,5%** (R13 8471.18 = 8513.75 × 0,995). Bate com a CCG (Net = Gross − SS − SUF − tax − stamp duty − other), mas o M29 da spec não cita o selo de forma explícita ("other deductions", e diz que a base do selo é o Statutory Net). Esclarecer o M29 numa próxima versão.
6. **Lista "Exempt Income" (76 WTs):** inclui reembolsos (art. 55(2)), pensões (art. 33(12)), diárias, passagem, mudança, estacionamento e "Donation recovery". Com o Gross incluindo isentos, todos entram no "Gross Salary" do relatório. Bate com o "all exempt incomes" de 15/09, mas 62820 "Donation recovery" não parece rendimento: vale a Enaakshi/Lily conferirem. Não validei a classificação tributária de cada WT (fora do pedido).
7. **Version Control** sem registro da mudança de 15/09.

## Rascunho de resposta (EN)
> @lli Yes, Gross Salary should include the Exempt Income Amount. In the spec, Taxable Income (Base) = Gross − Exempt Income Amount − Employee SS − Social Unity Fund − Personal Exemption, so Gross must be the total employment income paid in the month (taxable + exempt), which is also what Art. 60 of Income Tax Law 7/2010 requires the employer to list ("income received"); the Art. 55 items (e.g. end-of-service indemnity, leave payout) are employment income on which the tax does not apply. Field explanations (Gross Salary, Exempt Income Amount) and the Sample File formula updated accordingly (v1.1).

(A última frase só entra depois de a spec ser alterada e aprovada. Sem a alteração, cortar.)

## O que precisa ser feito
| # | Ação | Quem | Urgência |
|---|---|---|---|
| 1 | Aprovar o veredito e o rascunho | Usuário | Alta: relatório em acceptance, BA esperando desde 20/10 |
| 2 | Spec v1.1 (M18, M19, G19, M21, M25; Sample N16:N17; Scope C21; File Structure B12; Version Control), células alteradas em azul claro `FFDDEBF7`, conferência célula a célula. Partir do export de 22/10, arquivar local e subir ao Drive só com ordem do usuário | Janela Suporte, com ok do usuário | Alta |
| 3 | Gravar o draftComment no SR-367 (não enviar) | Janela Suporte, com ok do usuário | Alta |
| 4 | Ajustar o mapeamento do Gross Salary (T18) para incluir a renda isenta e pedir ao dev um reteste com um empregado com pagamento isento (a amostra atual tem Exempt = 0) | Lily (BA) / Michael (dev) | Alta, depois da resposta |
| 5 | Achados 1–7 no hub da Líbia (inexistente: criar `paises/Libia.md`) | Janela geral | Média |
| 6 | Arredondamento a 3 casas (achado 4): avisar a Lily junto da resposta ou num comentário à parte, se o usuário quiser | Usuário decide | Média |

## Lacunas
- **Sem formulário oficial** da lista mensal do art. 60 nem print do portal: o rótulo "Gross Salary" não é verificável contra a autoridade. O veredito se apoia na lógica da própria spec e no art. 60 ("income received").
- **O que o WT 58008 soma:** sem explicação no WTC. Que ele é "taxable gross" vem da Lily (⚠️ não verificado no motor).
- O teste da Lily ("based on my testing") não está no ticket.
- **Base do SUF sobre renda isenta:** a Lei 20/1428 (2007) art. 3(1) fala em "total dos rendimentos". A spec SUF exclui os isentos sem fonte (ver SR-369, achado 2). O M21 proposto evita contaminar essa questão.
- Lei 7/2010: usei o texto árabe (eastlaws, não oficial) e a tradução DCAF (não oficial). Não li o regulamento executivo (اللائحة التنفيذية), que pode prescrever a forma da lista mensal: vale buscar.
