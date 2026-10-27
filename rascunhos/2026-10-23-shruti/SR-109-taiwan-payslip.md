# SR-109: TW, Pay slip (工資各項目計算方式明細)

> Análise só leitura, 2026-10-23 (janela Suporte). Nada foi postado, enviado nem gravado no Drive.
> O holerite de teste anexado traz nome e dados de uma pessoa: não foram copiados aqui.

## Metadados
| Campo | Valor |
|---|---|
| Ticket | SR-109, "TW - Pay slip" (https://youtrack.hrblizz.dev/issue/SR-109) |
| Estado / fase | In Review / Specification Phase - Research Analyst |
| Assignee | Wallisson (wgomes), vindo da Manju → Shruti |
| BA / RA / Dev | Mohit Jain / Manju Shetija / Katrin Rudi (configuração: Shaik Jani Sharif; mapeamento: Lily Li) |
| Reporter | Lisa Quan, criado em 2025-08-07 |
| Report code | `taiwan-payslip` (configurado em nível país em 2026-01-29) |
| Spec analisada | `raw/docs/drive-exports/2026-10-23/TW Payslip Specification.xlsx` (Version Control **vazia**) |
| Template | `raw/docs/drive-exports/2026-10-23/SR-109-payslip-template-Compliance_payslip_generator.xlsx` (aba "Taiwan Payslip") |
| Anexos | `raw/tickets/api/anexos/SR-109/`: PDF oficial do MOL (參考例), 3 prints do Jani, holerite de teste (PDF) e HTML |

## O que foi pedido a nós
Mohit, 15/09/2026: "Spec Review only and fill the gaps in specs. Assign back to me once done for Testing and Development." Revisar a spec contra a fonte oficial e preencher as lacunas.
Pontos em aberto herdados: overtime por tipo de dia (Lily, nov/2025) e versão em chinês (Brenet/Lisa, ago/2025).

## Histórico do ticket
- 2025-08-07 Brenet pede à Lisa conferir os campos obrigatórios e, se preciso, uma segunda versão em chinês. Anexo: PDF do MOL.
- 2025-08-08 Lisa: "For Chinese version, yes it is needed"; pergunta qual é a prática para versão local.
- 2025-11-25 Lily nota que a spec tinha "TH/Thailand" no título (Brenet confirma que é TW).
- 2025-11-28 Lily: mapeamento feito, exceto overtime, porque os PEs de overtime do WTC não distinguem dia útil / descanso / feriado.
- 2025-12-01 WTC V2.3 "Rename 62xxx overtime pay elements" (Lily). 2025-12-02 Lily: "TW payslip mapping is done".
- 2025-12-02/03 Jani pergunta se os wage codes saem um por linha e só com valor; Mohit: "All wage types to come individually only when there is a value."
- 2026-01-29 Jani: configuração concluída, testada "in my India entity", código `taiwan-payslip`.
- 2026-09-15 Mohit: atribuído para revisão de spec.

## Fonte primária
Cópias em `C:\Users\instituto\Documents\brain-service\raw\docs\oficiais\TW\` (e anexo do ticket).

| # | Fonte | Arquivo local | O que prova |
|---|---|---|---|
| P1 | Labor Standards Act (勞動基準法), texto do MOL (laws.mol.gov.tw, alterado em 2024-07-31; dados até 30/09/2026) | `2026-10-23-payslip-LSA-labor-standards-act-mol.html` | art. 23: salário pago ao menos 2× por mês salvo acordo/mensal antecipado, **"並應提供工資各項目計算方式明細"**; folha de salários guardada 5 anos. art. 24: overtime em dia útil +1/3 (2 primeiras horas) e +2/3 (2 seguintes); trabalho no dia de descanso (休息日) "另再加給" 1⅓ até 2h e 1⅔ depois. art. 32-1: horas de compensação não gozadas no prazo viram salário. art. 38 §4: dias de 特休 e o valor pago pelos não gozados vão na folha de salários, com aviso escrito anual. art. 39: feriado trabalhado com acordo = salário em dobro. art. 40: suspensão de folga por emergência = salário em dobro. art. 79: multa de NT$20.000 a 1.000.000 por violar os arts. 22–25 e 32, 34–41 |
| P2 | Enforcement Rules da LSA (勞動基準法施行細則), MOL | `2026-10-23-payslip-LSA-enforcement-rules-mol.html` | art. 14-1: o 明細 deve conter (1) 勞雇雙方議定之工資總額, (2) 工資各項目之給付金額, (3) valores deduzidos por lei ou acordo, (4) 實際發給之金額; pode ser em papel, eletrônico ou outro meio que o trabalhador possa acessar e imprimir a qualquer momento |
| P3 | MOL, "勞動基準法第23條第1項「工資各項目計算方式明細」之參考例" (anexo do ticket, 2025-08-07) | `raw/tickets/api/anexos/SR-109/20250807-0604 - 8. Pay slip勞動基準法第23條第1項-工資各項目計算方式明細-之參考例 (1).pdf` | 3 modelos. Modelo 3: overtime por tipo de dia com multiplicador e horas (dia útil 1⅓, 1⅔; feriado ≤8h 1, >8h 1⅓ e 1⅔; descanso ≤8h 1⅓ e 1⅔, >8h 2⅔), valor-hora = salário ÷ 240, descontos de ausência, tabela de 特休 e de 補休. Nota 7: "本參考例之內容均可依實際情形，自行增刪" (modelo adaptável) |

Fontes internas (secundárias): WTC V2.8 (V2.3 renomeou os PEs de overtime), DD V3.3.

## Estado da spec
A aba `Spec` tem 2 blocos: o exemplo (colunas B–J, cópia da aba "Taiwan Payslip" do template) e a tabela de mapeamento (colunas M–S, linhas 5–50). As colunas R/S (descrições TA/BA) estão **vazias** em todas as linhas. Não há aba Report Matrix. A Version Control não tem nenhuma linha.

### Mapeamento atual (colunas M–Q)
| Seção | Campo | Mapeamento | Situação |
|---|---|---|---|
| Company | Employer Name | `$legal_entity.name` | ok |
| Company | Employer Address | — | **lacuna** |
| Company | Country | `$legal_entity.country` | ok |
| Company | Period | "Period begin - Period end" (DD/MM/YYYY) | ok (sem variável explícita) |
| Employee | Name / ID / Position / Email / Hire date | `$employee_name`, `$employee.reference_code`, `$employee.position`, `$person.primary_email`, `$employee.hire_date` | ok |
| Employee | National ID | `$person.national_id` | conflito interno: o DD TW guarda o ID em `$hr.id_card_number` (usado no SI e no Tax Report) |
| Employee | Payment Date | — | **lacuna** |
| Employee | Payment Method | `$employee.payment_method` | ok |
| Earnings | Conta + nome / valor | `62100:62103 + 62106:62999 + 65500:65859 + 79401:79450`, uma linha por PE com valor | cobre os PEs de overtime 62110–62139 e o pagamento de férias não gozadas (79401) |
| Deductions | Conta + nome / valor | `21100:21999 + 25500:25899 + 2551 + 2555 + 2554 + 2558 + 2517 + 2557 + 2552 + 2572 + 2582 + 2592 + 2593 + 2594` | ok contra o WTC (LI, EI, NHI, SNHI, pensão voluntária, EWF, impostos) |
| Net | Net Pay | `2610 + 1310 + 26100 + 26102 + 26105` | não verificável pelo WTC (contas de sistema) |
| ER | Conta + nome / valor | `2550 + 2565 + 2560 + 2566 + 2564 + 2568 + 2537 + 2538 + 23550:23900` | ok contra o WTC (LI, EI, OAI, 積欠工資墊償, NHI, SNHI, pensão nova/antiga) |
| Bank | Bank name / SWIFT / Beneficiary / Acc. Number | `$primary_employee_bank_account.*` | ok; o exemplo também tem Account currency e Type sem mapeamento |
| Totais | Total Gross / Total Deductions / Total ER | aparecem no exemplo, **sem linha de mapeamento** | lacuna |

### Conferência contra a fonte oficial (P2 art. 14-1)
| Item obrigatório | Na spec? | Observação |
|---|---|---|
| (1) 勞雇雙方議定之工資總額 (salário total acordado) | **Não** | Nenhum campo de salário contratado; o template genérico tinha "Basic Salary / Daily / Hourly" (Extra Information), retirado na versão TW |
| (2) 工資各項目之給付金額 (valor de cada item) | Sim | Uma linha por PE com valor (Mohit, 03/12/2025) |
| (3) Deduções legais ou acordadas | Sim | Bloco Deductions |
| (4) 實際發給之金額 (líquido pago) | Sim | Net Pay |
| Meio que o trabalhador acessa e imprime | Sim | PDF |

Conflitos com a fonte: só o item (1) ausente. O resto (data de pagamento, endereço, totais) é lacuna de spec, não exigência literal da lei.

## Proposta de preenchimento
> **Proposta**, não aplicada. ⚠️ = depende de variável/PE a confirmar pelo BA.

| Linha | Campo | Antes | Depois (proposto) | Fonte |
|---|---|---|---|---|
| VC | Version Control | vazia | 1.0 (Lily, 02/12/2025, mapeamento); 1.1 (Jani, 29/01/2026, configuração); 1.2 (revisão de spec, data da entrega) | padrão da planilha |
| novo | Report Matrix | não existe | Report Name "Taiwan Payslip"; Code `taiwan-payslip`; Frequency `Payroll Run`; Format PDF; Language: rótulos bilíngues zh-TW + EN (ver Status); Rounding: NT$ sem decimais ⚠️ confirmar regra de arredondamento do produto | P2 art. 14-1 §2 |
| novo | Agreed total wage (議定工資總額) | não existe | Linha no cabeçalho ou "Extra Information": salário mensal contratado (base + adicionais fixos) do salary card ⚠️ variável a indicar pelo BA | P2 art. 14-1(1); P3 modelo 2 ("約定薪資結構") |
| Company | Employer Address | vazio | Endereço da entidade (`$legal_entity` address) ⚠️ variável a indicar | boa prática (não exigido literalmente) |
| Employee | Payment Date | vazio | Data de pagamento do payrun, DD/MM/YYYY ⚠️ variável a indicar | P3 modelos 2 e 3 ("發薪日期", "入帳日期") |
| Employee | National ID | `$person.national_id` | `$hr.id_card_number` (mesmo campo do SI e do Tax Report) **ou** retirar: não é item exigido pela P2 art. 14-1 | DD V3.3 Country Fields |
| Earnings | Overtime 62110, 62111, 62120–62122, 62130–62132 | só valor | Mostrar Rate (multiplicador do nome do PE) e Unit (horas) quando houver ⚠️ depende de o motor guardar as horas | P3 modelo 3 (recomendado, não obrigatório: nota 7) |
| Earnings | Total Gross | sem linha | `SUM` das contas de Earnings | P2 art. 14-1(2); P3 "合計(A)" |
| Deductions | Total Deductions | sem linha | `SUM` das contas de Deductions | P2 art. 14-1(3) |
| ER | Total Employer Contributions | sem linha | `SUM` das contas de ER | template |
| Bank | Account currency / Type | sem linha | `$primary_employee_bank_account.currency` / tipo ⚠️ | template |
| Exemplo | "Personal Leave", "Sick Leave" no bloco Deductions | rótulos no exemplo | Alinhar com o WTC: só existe 62109 "Unpaid LOA - Basic salary" (Earning, sai em Earnings). Tirar os rótulos ou pedir PEs ao BA | WTC V2.8 |
| Opcional | Saldo de 特休 / 補休 | não existe | Bloco opcional com dias de 特休 do ano e horas de compensação, se o cliente usar o holerite como aviso do art. 38 §4 | P1 art. 38 §4, art. 32-1; P3 "備註" |
| Descrições | Colunas R/S | vazias | Preencher uma frase por linha (o que é, de onde vem, quando aparece: "only when value ≠ 0") | Mohit, 03/12/2025 |

## Status dos pontos do ticket
| Ponto | Status |
|---|---|
| Overtime por tipo de dia (Lily, 28/11/2025) | **Resolvido no WTC**: V2.3 (01/12/2025) renomeou 62110/62111 (Work Day 1.33/1.67), 62120–62122 (Rest Day 1.33/1.67/2.67), 62130–62132 (Public Holiday 1/1.33/1.67). Os multiplicadores conferem com P1 art. 24 (dia útil e 休息日) e com o modelo 3 do MOL (P3; o 2⅔ acima de 8h no 休息日 e o 1/1⅓/1⅔ do feriado vêm do modelo e das notas 3 e 4). A faixa de contas da spec (62106:62999) já inclui esses PEs. Nada a mudar na spec além do Rate/Unit sugerido |
| Versão em chinês (Brenet/Lisa, ago/2025) | **Não é exigência legal**: P1 art. 23 e P2 art. 14-1 não fixam idioma (texto lido). A Lisa (cliente/RA local) disse que é necessária. Proposta: rótulos bilíngues zh-TW + EN numa versão só (evita duas configurações), com os rótulos do modelo do MOL (應發項目, 應扣項目, 實發金額…). Decisão de produto, não de compliance |
| PEs um por linha, só com valor (Jani/Mohit, dez/2025) | Compatível com P2 art. 14-1(2) ("工資各項目之給付金額") |
| Teste (Jani, 29/01/2026) | Feito numa entidade da Índia: os nomes dos PEs saíram do catálogo de outro país (ex.: 2558 aparece como "NSSF Tier 2 EE"), endereço e país da Índia, data de pagamento 23/12/2025 para o período de mar/2024. **Não valida o holerite de Taiwan**: refazer na REF-LE-02-826 "Taiwan Testing" (entidade do SR-108) |

## Veredito
**Quase pronta, mas não para devolver como está.** Falta: (1) o item (1) da P2 art. 14-1 (salário total acordado); (2) preencher Payment Date, Employer Address e as linhas de totais; (3) corrigir o campo do ID (ou retirá-lo); (4) preencher Version Control, Report Matrix e descrições; (5) decidir o idioma (bilíngue). O mapeamento por faixas de contas e o overtime por tipo de dia estão corretos.

## Achados fora do pedido
1. WTC V2.8 não tem PE para: trabalho em 例假 ou folga suspensa por emergência (dobro, P1 art. 40); horas de compensação vencidas pagas em dinheiro (P1 art. 32-1; aparece no modelo do MOL como "屆期未補休折發工資"); trabalho no feriado acima de 8h pelo art. 39 está coberto (62131/62132). Vai para o hub.
2. Os PEs 62112–62119, 62123–62129 e 62133–62139 continuam "Overtime" genérico: se forem usados, o holerite não mostra o tipo de dia.
3. A faixa 65500:65859 inclui benefícios nocionais (ex.: 65508/65509 "Car Benefit (Notional)", 65659 "Meal Benefit (Notional)"): entram no Total Gross do holerite sem serem pagos em dinheiro. Confirmar com o BA se devem aparecer em bloco separado.
4. O holerite de teste mostra dados reais de uma pessoa num anexo de ticket (fora do nosso controle; só registro).

## Rascunho de comentário (EN)
> @mjain Spec review done; changes highlighted in the spec (v1.2).
> 1. Overtime by day type is covered: WTC V2.3 split 62110/62111, 62120–62122 and 62130–62132, and the rates match LSA art. 24 and the MOL reference payslip. Proposed to also show rate and hours on these lines.
> 2. Added the "agreed total wage" line (LSA Enforcement Rules art. 14-1 item 1, the only mandatory item missing), Payment Date, Employer Address and the three total rows.
> 3. National ID now points to the TW field `$hr.id_card_number` (or can be dropped; it is not a mandatory item).
> 4. Chinese version: the law does not set a language; proposed one bilingual zh-TW/EN layout.
> The test was run on an India entity, so TW wage type names were not checked; please retest on REF-LE-02-826.

## O que precisa ser feito
1. Usuário revisa e aprova o texto (nada postado).
2. Aplicar a proposta numa cópia da spec (destaque `FFDDEBF7`, v1.2), depois do ok.
3. BA indica as variáveis: salário acordado, data de pagamento, endereço, moeda/tipo da conta, horas de overtime.
4. Decisão de produto sobre o layout bilíngue (Mohit/Brenet; a Lisa já pediu).
5. Retestar na entidade de Taiwan.
6. Registrar os achados 1–3 no hub de Taiwan.

## Lacunas
- ⚠️ O que exatamente a fiscalização aceita como "議定之工資總額" (salário base contratado ou total bruto acordado): P2 não define; os modelos do MOL mostram a estrutura acordada (modelo 2) ou o total a pagar (modelo 1). Proposta conservadora: salário mensal contratado.
- ⚠️ Se o motor guarda horas e multiplicador para os PEs de overtime (para Rate/Unit).
- ⚠️ Regra de arredondamento do NT$ no holerite: não verificada.
- A LSA e o Enforcement Rules foram lidos no site do MOL (laws.mol.gov.tw); law.moj.gov.tw recusa conexão daqui.
