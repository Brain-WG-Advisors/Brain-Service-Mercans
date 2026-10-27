# HRBS-15790 — Egito: Social Insurance a partir de 01/01/2027 (piso, teto, alíquotas)

> Análise só leitura, 2026-10-23 (janela Suporte). **Nada foi postado, enviado ou alterado** (YouTrack, e-mail, Drive, hubs, correcoes.md, log.md). O rascunho de resposta abaixo espera o ok do usuário.

## Metadados
| Campo | Valor |
|---|---|
| Ticket | [HRBS-15790](https://youtrack.hrblizz.dev/issue/HRBS-15790): "Egypt Social Insurance Regulation Changes – Effective January 2027" |
| Tipo / estado / prioridade | Service Request / In Progress / Medium |
| Reporter | Mustafa Mohamed Youssef (myoussef) |
| Assignee | Wallisson (wgomes), Compliance Support |
| Escopo | "All Egypt entities", Production, Live/BAU |
| Criado / atualizado | 2026-10-09 11:51 UTC / 2026-10-22 20:21 UTC |
| Cópia local | `raw/tickets/api/2026-10-23-ex-skamble/HRBS-15790.md` |
| Skills consultadas | `payroll-compliance-egypt` (versão na lixeira, só como pista: `~/.claude/skills/.trash/1791418175888-24024-B4Plfx/payroll-compliance-egypt/references/01-ccg.md` §4.3; `07-qa-report.md` item 01) |
| `correcoes.md` | Lida. A entrada de 22/10 sobre o Egito trata do Fundo dos Mártires e não toca neste assunto. |

## O que foi pedido a nós
O Mustafa avisa sobre a mudança e pede que, **depois de fechar a folha de dezembro/2026**, a configuração seja atualizada e testada **antes das folhas de janeiro/2027** (alguns clientes rodam a partir de **08/01/2027**). Valores informados:

| Item | Antes (segundo ele) | A partir de 01/01/2027 |
|---|---|---|
| Piso mensal | EGP 2.700 | EGP 3.200 |
| Teto mensal | EGP 16.700 | EGP 19.300 |
| Empregado | 11% | 11,5% |
| Empregador | 18,25% → corrigido em 21/10 para **18,75%** | 19,25% |

Ninguém perguntou nada específico; o pedido implícito é **confirmar os valores e acionar a configuração** (task de desenvolvimento).

## Histórico do ticket
- 2026-10-09: Mustafa abre o ticket com os quatro números (empregador "19.25% instead of 18.25%").
- 2026-10-21: Mustafa corrige: "Employer contribution: 19.25% instead of **18.75%**."
- Nenhum comentário de Compliance até 23/10. Sem anexos.
- Campos SLA: First Reply 2026-10-12 07:51 UTC, Resolution Time 2026-10-14 15:51 UTC (os dois prazos já passaram).

## O que nossos artefatos dizem
Todos lidos do Drive (`G:\Drives compartilhados\Compliance Team\Country Folders\Egypt\`), só leitura.

**CCG**: `05 - Payroll Regulation Guide\EG-CCG-001-v1_4-statutory-leave-country-standard.docx` (md5 `507fea21…`; o cabeçalho interno diz "EG-CCG-001 v1.1 / QA Patched — 2026-05-27"). O `EG-CCG-001-v1.1.docx` (md5 `4f397aaa…`) tem o mesmo texto nestes trechos.
- §3.1 (Employer On-Costs): "For 2026, the employer's total SS rate is 18.75% of the capped contribution wage". Tabela: OAD 12,00% (Art. 19) · Work Injury 1,50% (Art. 46) · Sickness 3,25% (Art. 70) · Unemployment 1,00% (Art. 86) · Gratuity 1,00% (Art. 36) · **Total Employer 18.75%** · **Total Employee 11.00% (9% OAD + 1% Sickness + 1% Gratuity)** · Combined 29.75%.
- §5.1.1: "The contribution wage is subject to a statutory floor and ceiling that are revised periodically by ministerial decree: … Minimum contribution wage (floor) EGP 2,700 · Maximum contribution wage (ceiling) EGP 16,700" (coluna "2026 Monthly Amount").
- §5.1 (resumo): base legal "Law 148/2019, Arts. 1, 19, 36, 46, 70, 86, 115; Ministerial Decree setting contribution wage floor and ceiling for 2026."
- §2.2: "Contribution wage (INSURANCE_WAGE) | EGP 16,700 | Must be between EGP 2,700 and EGP 16,700 for 2026".
- **Não menciona** o degrau de alíquota de 2027 (art. 19, último parágrafo) nem a regra de reajuste do piso/teto (Regulamento art. 53).

**Design**: `07 - Design\Egypt_Formulas_with_Explanations.md` (md5 `8f65252f…`; fonte declarada: `CT-A-628.md`, "EG 2026 Specifications"), **Regulation 23 — EG Social Security**:
- "Establishes a contribution-wage floor of EGP 32,400/year and ceiling of EGP 200,400/year (2026 SS wage band)" (= 2.700 × 12 e 16.700 × 12).
- "If the employee is under 60 … a base rate of 10% employee / 14.75% employer applies."
- "… if the employee is NOT flagged under 58201 … an additional layer of 1% employee / 4% employer … bringing the total to 11% employee / 18.75% employer".
- "If the employee is 60 or over … a flat 1% employee / 4.75% employer rate applies instead".
- A Regulation 205 (EG Comprehensive Social Security, UHI) cobre o 1%/4% quando o empregado tem o flag 58201.

**WTC**:
- `03 - WTC\EG-WTC-001-v1.0.xlsx`: as descrições trazem os valores fixos, por exemplo F154: "NOSI contribution wage = MIN(MAX(gross cash pay, EGP 2,700), EGP 16,700) per Arts. 19, 115, SIL 148/2019" (o mesmo texto em F155 e F177–F191). Não traz alíquotas.
- `03 - WTC\EG_WTC_and_Taxability_Matrix.xlsx`, E6: "Reg 23 (EG Social Security) — 6 of the 8 active band assertions key off this: LESS($58210;60) selects the under-60 rate/ceiling schedule". Não traz valores.

**DD**: `02- DD\EG-DD-001-v1.0.xlsx`
- F15/V39: "Full EE 11% and ER 18.75% SS contributions apply". F42: "This is the base amount on which both ER (18.75%) and EE (11%) contributions are calculated". J42: "EGP 2,700–16,700 (2026)". V40/V42: piso e teto de 2026 fixos na regra.
- V62/V63 (Training Fund): "0.25% of minimum insurable wage (EGP 2,700/month)" e "0.25% × (minimum insurable wage EGP 2,700 × 12 months)".

**Alert 2026**: `raw/docs/drive-exports/2026-10-23/Egypt 2026 Payroll Compliance Alert.txt` (export do Google Doc em `09 - Alerts\2025 Year end changes\`)
- §2.1: "Minimum Insurable Wage (SI_MIN): EGP 2,700 per month. Maximum Insurable Wage (SI_MAX): EGP 16,700 per month." (marcados como "Already Completed")
- §2.3.1: "Employee Share: 11% … Employer Share: 18.75% of the Insurable Wage". As fontes citadas são secundárias (PwC, Ramco, Mercans alert). Não fala de 2027.

**Resposta à pergunta 18,25% × 18,75%:** em todos os artefatos o valor patronal de 2026 é **18,75%**, e é isso que a lei dá para o setor privado (ver a soma abaixo). O "18,25%" do texto original do ticket estava errado, e o próprio Mustafa corrigiu em 21/10.

**Outros arquivos:** `EG New Draft Regulations.xlsx` (export de 23/10) só tem a reg. 9818072 (EG Post Termination Flat Tax) e não toca no seguro social. O PDF do Drive "Egypt 2019 regulation stating 15% increase in contribution base.pdf" é **o mesmo arquivo** (md5 `33effc18…`) que `raw/docs/oficiais/EG/2026-10-22-decreto-pm-2437-2021-regulamento-lei-148-gazette.pdf`, ou seja, o Regulamento Executivo de 2021, não de 2019.

## Fonte primária

### F1. Lei 148/2019, art. 19, último parágrafo: alíquota sobe 1 ponto a cada 7 anos
Arquivo: `raw/docs/oficiais/EG/2026-10-22-lei-148-2019-seguro-social-nosi.pdf` (edição oficial da NOSI, p. 25/155). Lido na imagem da página.
> "وتزاد نسبة الاشتراكات كل سبع سنوات اعتبارًا من تاريخ العمل بهذا القانون بنسبة (1٪)، وتقسم مناصفة بين صاحب العمل والمؤمن عليه، على ألا تتجاوز إجمالي نسبة الاشتراكات (26٪)."
>
> *Tradução:* "A alíquota das contribuições é aumentada a cada sete anos, a partir da data de vigência desta lei, em 1%, dividido igualmente entre o empregador e o segurado, sem que a alíquota total das contribuições ultrapasse 26%."

No mesmo artigo, 19(1): empregador "(12 ٪) من أجور المؤمن عليهم العاملين لديه شهريًا" (12% dos salários dos segurados que trabalham para ele, por mês) e empregado "(9٪) من أجره شهريًا" (9% do próprio salário, por mês).

### F2. Lei 148/2019, Sétimo artigo de promulgação: vigência em 01/01/2020
Mesmo PDF, p. 7/155:
> "يُنشر هذا القانون في الجريدة الرسمية، ويُعمل به اعتبارًا من 2020/1/1، فيما عدا المواد (111 و112 و113 و114) فيعمل بها من اليوم التالي لتاريخ نشره."
>
> *Tradução:* "Esta lei será publicada no Diário Oficial e vigora a partir de 01/01/2020, exceto os artigos 111, 112, 113 e 114, que vigoram a partir do dia seguinte ao da publicação."

Conta: 01/01/2020 + 7 anos = **01/01/2027**, o primeiro degrau.

### F3. Regulamento Executivo (Decreto do PM 2437/2021, Gazette nº 38 bis (ب), 28/09/2021), art. 57, último parágrafo
Arquivo: `raw/docs/oficiais/EG/2026-10-22-decreto-pm-2437-2021-regulamento-lei-148-gazette.pdf`, p. 48 da Gazette. Lido na imagem.
> "وتزاد جميع نسب الاشتراكات السابقة كل سبع سنوات اعتبارا من 2020/1/1 بنسبة (1٪)، وتقسم هذه الزيادة بالنسبة لفئات المؤمن عليهم المشار إليهم بالمادة (3) من هذه اللائحة مناصفة بين صاحب العمل والمؤمن عليه …"
>
> *Tradução:* "Todas as alíquotas de contribuição acima [as do seguro de velhice, invalidez e morte: 12% empregador / 9% empregado; 21% empregadores e expatriados; 9% + 12% trabalho irregular] são aumentadas a cada sete anos a partir de 01/01/2020 em 1%, e esse aumento é dividido igualmente entre empregador e segurado para as categorias do art. 3 deste regulamento [empregados]…"

Resultado: o degrau cai no ramo de **velhice, invalidez e morte**, que passa de 12% / 9% para **12,5% / 9,5%**.

### F4. Regulamento Executivo, art. 53: piso e teto
Mesmo PDF, p. 46 da Gazette. Lido na imagem.
> "يتحدد الحد الأدنى لأجر الاشتراك … اعتبارًا من 2020/1/1 بواقع 1000 جنيه شهريًا ويتحدد حده الأقصى بواقع 7000 جنيه شهريًا. ويتم زيادة الحدين الأدنى والأقصى بواقع (15٪) في أول يناير من كل عام منسوبة إليه في شهر ديسمبر السابق لمدة سبع سنوات ثم يتم زيادة هذين الحدين بنسبة التضخم، ويراعى جبر الحدين الأدنى والأقصى الشهري إلى أقرب مائة جنيه."
>
> *Tradução:* "O piso do salário de contribuição … a partir de 01/01/2020 é de EGP 1.000 por mês e o teto de EGP 7.000 por mês. O piso e o teto são aumentados em 15% em 1º de janeiro de cada ano, sobre o valor de dezembro anterior, por sete anos; depois disso, são aumentados pela taxa de inflação. O piso e o teto mensais são arredondados para cima, para a centena de libras mais próxima."

Conta refeita (×1,15 e arredondamento para cima até a centena, script em python):

| Vigência | Piso | Teto | Conferência |
|---|---|---|---|
| 2025-01-01 | 2.300 | 14.500 | NOSI (F5) cita como "de" |
| 2026-01-01 | 2.700 | 16.700 | **bate** com o anúncio da NOSI (F5) |
| **2027-01-01** | **3.200** (2.700 × 1,15 = 3.105 → 3.200) | **19.300** (16.700 × 1,15 = 19.205 → 19.300) | 7º e último aumento de 15% (2021–2027); a partir de 2028 o reajuste passa a ser pela inflação |

Anual, como a Reg. 23 usa: **38.400 / 231.600** (antes 32.400 / 200.400).

### F5. NOSI, notícia oficial de 30/11/2025 (valores de 2026)
Arquivo: `raw/docs/oficiais/EG/2026-10-23-nosi-noticia-2025-11-30-piso-teto-2026.html` (baixado em 23/10 de https://www.nosi.gov.eg/ar/News/Pages/2025-11-30.aspx; md5 `e0bc5e4705748da19173fa42332a5586`).
> "أعلنت الهيئة القومية للتأمين الاجتماعي عن رفع الحدين الأدنى والأقصى لأجر الاشتراك التأميني اعتبارًا من 1 يناير 2026، وذلك تنفيذًا لأحكام قانون التأمينات الاجتماعية والمعاشات رقم 148 لسنة 2019 ولائحته التنفيذية … الحد الأدنى لأجر الاشتراك التأميني سيرتفع من 2300 جنيه إلى 2700 جنيه، بينما يرتفع الحد الأقصى من 14500 جنيه إلى 16700 جنيه."
>
> *Tradução:* "A NOSI anunciou o aumento do piso e do teto do salário de contribuição a partir de 1º de janeiro de 2026, em cumprimento da Lei 148/2019 e do seu regulamento executivo … o piso sobe de EGP 2.300 para 2.700 e o teto de 14.500 para 16.700."

**Não há anúncio da NOSI para 2027** até 23/10/2026. O de 2026 saiu em 30/11/2025, então o de 2027 deve sair por volta do fim de novembro de 2026.

### F6. Soma das alíquotas do setor privado (2026 → 2027)
Lei 148/2019, lida no PDF da NOSI. A categoria é a do art. 2, "أولاً" item 3: empregados do setor privado regidos pela Lei do Trabalho.

| Ramo | Artigo (página do PDF NOSI) | Empregado 2026 → 2027 | Empregador 2026 → 2027 |
|---|---|---|---|
| Velhice, invalidez e morte | 19(1) (p. 25) + F1/F3 | 9% → **9,5%** | 12% → **12,5%** |
| Sistema de Recompensa (نظام المكافأة) | 36 (p. 40) | 1% | 1% |
| Acidente de trabalho, tratamento (só para quem não está no UHI) | 46(1) (p. 45) | — | 1% |
| Acidente de trabalho, benefícios em dinheiro (pode subir até 1% conforme o risco da atividade) | 46(2) (p. 45) | — | 0,5% |
| Doença (3,25% para os itens 3–5 do art. 2 "أولاً") | 70 (p. 55) | 1% | 3,25% |
| Desemprego ("بواقع (1٪) من أجور المؤمن عليهم لديه شهريًا") | 86 (p. 61) | — | 1% |
| **Total** | | **11% → 11,5%** | **18,75% → 19,25%** |

Leis de alteração da Lei 148/2019 conferidas nas imagens da Gazette: **Lei 25/2020** (altera os arts. 1(6), 35 e 111), **Lei 18/2023** (altera os arts. 35 e 111, art. 12 da lei) e **Lei 8/2024** (altera o art. 112). **Nenhuma muda o art. 19.** A Lei 11/2026 (art. 111, parcelas do Tesouro, segundo a imprensa) não tem texto oficial obtido (⚠️; ver Lacunas).

Apoio secundário (não é fonte): PwC Tax Summaries Egypt "Other taxes" (revisada em 17/08/2026) traz 2027 = 3.200 / 19.300 e "increased by 15% on 1 January of each year for a period of seven years, starting from 1 January 2021"; continua com 11% / 18,75% e não menciona o degrau de alíquota. A skill antiga (pista) já dizia "The first step therefore falls due on 1 January 2027".

## Veredito por número
| Número do Mustafa | Veredito | Prova |
|---|---|---|
| Piso EGP 3.200 a partir de 01/01/2027 | ✅ **Confirmado pela regra**; anúncio da NOSI de 2027 ainda não publicado | Reg. art. 53 (F4) + conta (2.700 × 1,15 = 3.105 → 3.200); o método reproduz o valor oficial de 2026 (F5) |
| Teto EGP 19.300 a partir de 01/01/2027 | ✅ **Confirmado pela regra**; mesma ressalva | F4 + conta (16.700 × 1,15 = 19.205 → 19.300) |
| "Antes" 2.700 / 16.700 | ✅ Confirmado (vigentes desde 01/01/2026) | NOSI 30/11/2025 (F5) |
| Empregado 11,5% (antes 11%) | ✅ **Confirmado** | Lei 148/2019 art. 19, último parágrafo (F1), vigência 01/01/2020 (F2); Reg. art. 57 (F3): +0,5 ponto no ramo de velhice (9% → 9,5%) |
| Empregador 19,25% | ✅ **Confirmado** | Mesmas fontes: +0,5 ponto (12% → 12,5%); soma em F6 |
| Empregador "antes" 18,25% (texto de 09/10) | ❌ **Divergente**; corrigido pelo próprio Mustafa | Hoje vale 18,75% (F6; CCG, DD, Design, Alert 2026) |
| Empregador "antes" 18,75% (correção de 21/10) | ✅ Confirmado | F6 |

Resumo: os quatro números de 2027 estão certos. Piso e teto saem do regulamento por conta; a alíquota está escrita na própria lei. O único "sem publicação" é o anúncio anual da NOSI de 2027, que não muda a regra mas deve ser conferido quando sair.

## Achados fora do pedido
(Para o hub [[Egito]] / Pendências, não para o ticket.)
1. **CCG §5.1.1 e §5.1 citam a base legal errada do piso e do teto:** "revised periodically by ministerial decree" / "Ministerial Decree setting contribution wage floor and ceiling for 2026". Na verdade é a fórmula do art. 53 do Regulamento Executivo (Decreto do PM 2437/2021): +15% ao ano por 7 anos, depois inflação, arredondando para cima até a centena.
2. **O CCG não menciona o degrau de alíquota** do art. 19 (+1 ponto a cada 7 anos, próximos em 2027 e 2034, total do ramo de velhice limitado a 26%).
3. **CCG §1.2/§3.1, prazo do recolhimento:** diz "by the last day of the month following" e "monthly surcharge of 1.5%". A Lei 148/2019 art. 121(1) (p. 79) diz "في أول الشهر التالي لشهر الاستحقاق" (no início do mês seguinte ao da competência). O cálculo do adicional por atraso (média de T-bills + 2%, com 15 dias de tolerância) vem da skill antiga e não foi conferido pessoalmente (⚠️).
4. **Os valores de 2026 estão gravados em muitas células do WTC e do DD:** WTC F154–F155 e F177–F191; DD F15, F42, J42, V39, V40, V42, V62, V63. Precisam de versão 2027 (ou de texto neutro, sem o valor).
5. **Training Fund (DD V62/V63, Alert §4.1):** a base é o piso do seguro, que passa a ser 3.200. Na leitura mensal do Alert, 3.200 × 0,25% = 8 → mínimo de EGP 10 (sem efeito). Na leitura anual do DD, 38.400 × 0,25% = 96 → máximo de EGP 30. As duas leituras já são a lacuna §4.4 do hub; em 2027 elas dão resultados diferentes (10 × 30 por empregado).
6. **Atividade de risco:** art. 46(2) permite 0,5% → até 1%. Em 2027 o empregador de atividade perigosa pode chegar a **19,75%**. Coincidência a evitar: hoje, 19,25% já pode ser o valor de quem tem risco máximo; o 19,25% de 2027 é o padrão.
7. **Diretores e gerentes do registro comercial (Alert §2.3.2: 21% sobre o teto):** o art. 57 do Regulamento aumenta "todas" as alíquotas do ramo de velhice, inclusive os 21% dos empregadores e equiparados. Em 2027 seria 22% sobre 19.300 (⚠️ inferência; o regulamento não diz como dividir para essa categoria). O Alert registra que essa lógica não existe no produto.
8. **A Reg. 23 do Design usa piso e teto anuais** (32.400 / 200.400, com rule group "…normalize_reconcile"). A NOSI e a skill tratam o teto como **mensal, sem acumulado anual**. Vale conferir se o motor reconcilia no ano (o que mudaria o resultado com salário variável). Não afirmo erro: é ponto para confirmar com o Mohit.
9. **Nome × conteúdo do CCG:** o arquivo `EG-CCG-001-v1_4-statutory-leave-country-standard.docx` diz internamente "v1.1, QA Patched 2026-05-27".
10. **Pendência do hub resolvida:** "Ler o art. 53 do Regulamento 2437/2021 (bdl excluídos ≤ 30%)". Lido pessoalmente (p. 46 da Gazette): "وفى جميع الأحوال يجب ألا يجاوز مجموع البدلات المستبعدة من أجر الاشتراك (30٪) من أجر اشتراك المؤمن عليه" (em todos os casos, o total dos adicionais excluídos do salário de contribuição não pode passar de 30% do salário de contribuição do segurado). ✅
11. **Arquivo mal nomeado no Drive:** "Egypt 2019 regulation stating 15% increase…" é o Regulamento de **2021** (Decreto PM 2437/2021), não de 2019.

## Rascunho de resposta (EN)
> Hi Mustafa,
>
> Thanks for raising this. We have checked it against the law and confirm all four changes from 1 January 2027:
>
> - Contribution wage floor/ceiling: EGP 3,200 / 19,300 per month (from 2,700 / 16,700). The Executive Regulations (PM Decree 2437/2021, Art. 53) raise both limits by 15% every 1 January for seven years (2021–2027), rounded up to the nearest EGP 100: 2,700 × 1.15 → 3,200 and 16,700 × 1.15 → 19,300. NOSI has not published its 2027 notice yet; we will check it when it comes out.
> - Rates: employee 11% → 11.5%, employer 18.75% → 19.25%. Law 148/2019, Art. 19 (last paragraph) adds 1% to the old-age, disability and death contribution every seven years from 1 January 2020, split equally between employer and employee (Executive Regulations, Art. 57): 9% → 9.5% and 12% → 12.5%. The other branches do not change.
>
> We will raise the configuration task so the change is in place and tested before the first January 2027 payrolls (8 January).
>
> Best regards,

(Antes de postar: trocar "We will raise the configuration task" pelo ID da task, se ela já existir; conferir se o usuário quer citar a NOSI.)

## O que precisa ser feito
| # | O quê | Quem | Prazo |
|---|---|---|---|
| 1 | **Development task** (padrão CT-4585/CT-4600 e do rascunho CI/CNPS de 21/10): Project CT · Type Development task · País EG · Assignee **Mohit Jain (mjain)** · Epic **Regulation Update** · anexos: Lei 148/2019 p. 25 + Regulamento p. 46/48. Conteúdo: **Reg. 23 EG Social Security** (CT-A-628): faixa **under-60 base** EE 10% → **10,5%**, ER 14,75% → **15,25%**; floor 32.400 → **38.400**/ano, ceiling 200.400 → **231.600**/ano (todas as faixas); camada 1%/4% (não-58201) **sem mudança**; faixa 60+ (1% / 4,75%) **sem mudança** (⚠️ inferência: a faixa não inclui o ramo de velhice; confirmar com o Mohit a composição); Reg. 205 (UHI) sem mudança. Vigência: períodos a partir de 01/01/2027, **sem afetar dezembro/2026**. Summary sugerido: "EG_NOSI floor/ceiling and OAD rate step_EGP 3,200/19,300, EE 11.5%/ER 19.25%_1 January 2027". | Usuário cria (rascunho pela API como no CI); Mohit configura | Criar já; configurar e testar até ~**15/12/2026**; produção antes de **08/01/2027** |
| 2 | Testes (Alert 2026 §9 como modelo): salário < 3.200 (base 3.200; EE 368,00; ER 616,00); salário > 19.300 (EE 2.219,50; ER 3.715,25); empregado com 60+; empregado UHI (58201); folha de dezembro/2026 rodada depois da mudança ainda com 2.700 / 16.700 / 11% / 18,75% | Mohit / QA; nós conferimos | Antes de 08/01/2027 |
| 3 | **CCG**: nova versão com a tabela de 2027 (OAD 12,5% / 9,5%; total 19,25% / 11,5%; 30,75%), piso e teto de 2027, regra do art. 53 e degrau do art. 19 (achados 1 e 2); exemplos de cálculo (16.700 × 11% = 1.837) e o prazo do art. 121 (achado 3) | Pipeline/Compliance (nós) | Antes de 01/01/2027 |
| 4 | **DD** e **WTC**: atualizar as células com os valores de 2026 (achado 4) e o Training Fund (achado 5) | Nós | Antes de 01/01/2027 |
| 5 | **Design** (`Egypt_Formulas_with_Explanations.md`, Reg. 23): valores de 2027 | Nós | Junto com a task |
| 6 | **Alert de virada 2026→2027** (pasta `09 - Alerts`), como o "Egypt 2026 Payroll Compliance Alert" | Nós | Novembro/2026 |
| 7 | Conferir o anúncio da NOSI de 2027 (fim de novembro) e baixá-lo para `raw/docs/oficiais/EG/` | Nós | ~30/11/2026 |
| 8 | Resposta ao Mustafa no ticket (rascunho acima), com o ID da task | Usuário aprova; janela Suporte grava o draft | Assim que a task existir |
| 9 | Registrar no hub [[Egito]] (Valores-chave com vigência; o piso/teto de 2026 ganha data de fim 2026-12-31) e linha em `log.md` | Janela Suporte, com ok | Ao fechar |

## Lacunas
- **Anúncio da NOSI para 2027:** ainda não publicado. Os valores 3.200 / 19.300 vêm da regra do art. 53 e da conta, não de um ato publicado para 2027.
- **Lei 11/2026:** só imprensa (Gazette de 07/06/2026, art. 111); texto oficial não obtido. Não há indício de que altere o art. 19 ou o regulamento, mas não está provado. Outras alterações ao **Regulamento** 2437/2021 depois de 2021 não foram procuradas a fundo.
- **Faixa 60+ da Reg. 23 (1% / 4,75%):** a composição não está documentada no Design. A conclusão "não muda" é inferência (a faixa não inclui o ramo de velhice).
- **Categoria de empregadores/diretores (21%):** a divisão do +1% não está no regulamento para essa categoria (achado 7).
- **CT-A-628:** não lido diretamente (só a síntese do Design). IDs reais das regs. 23/205 (prefixo 938…/981…) a conferir na task.
- **Teto mensal × anual no motor** (achado 8): a confirmar com o Mohit.
- **Regulamento art. 59 (معاش إضافي, 10% sobre a parte acima do teto, até 100% do teto):** não analisado; fora do pedido, mas vale conferir se se aplica a alguém no produto.
