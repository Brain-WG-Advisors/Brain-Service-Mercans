# HRBS-16015: Iraque, Baker Hughes, horas extras (OT) na base do Social Security

> Análise só leitura, 2026-10-22, janela Suporte (subagente). Nada foi postado, enviado ou gravado no Drive. Sem dados pessoais: os dois empregados citados no ticket viram "empregado A" (entidade 6465) e "empregado B" (entidade 0621).

## Metadados
| Item | Valor |
|---|---|
| Ticket | HRBS-16015 "BH IRAQ SS OT query" (Question / Inquiry, Medium, Production) |
| Estado | Pending on reporter (atualizado em 2026-10-21 05:48 UTC) |
| Cliente / entidades | Baker Hughes Iraq: REF-03-147 e REF-03-148 "Best Solutions Trading and Services for Oil and Gas Equipment" (6465 e 0621) |
| Reporter | Aasim Bagwan (BH) |
| Assignee | Enaakshi Vats (@evats), Compliance Support |
| Quem pediu algo a nós | Suman Rai (2026-10-21 05:47): "@evats, confirm the understanding and advise" |
| Material lido | ticket (`raw/tickets/api/2026-10-22-for-evats/HRBS-16015.md`); 2 imagens (`raw/tickets/api/anexos/HRBS-16015/`); `IQ-CCG-001-v1.0.txt` e `IQ-WTC-001-v1.1.xlsx` (export de 2026-10-22); Design `G:\...\Iraq\07 - Design\iq.json` (md5 18dacf26…, data 2026-08-24); leis em `G:\...\Iraq\14 - Legislation\pdfs\` |
| Skill | `mercans-compliance-workflow` carregada antes de redigir. Não há hub `paises/Iraque.md` nem entrada de Iraque em `correcoes.md` |

## O que foi pedido a nós
- **Pergunta do reporter (14/10):** o SS de abril não considerou a OT lançada com datas de fevereiro e março; o SS ficou proporcional só aos inputs com data do mês corrente (additional) mais os recorrentes.
- **Resposta do Suman (21/10):** "as per Statutory, OT is not included for SS", com print.
- **Pedido para a Enaakshi:** confirmar esse entendimento e orientar. Ou seja, a pergunta para nós é: **a OT entra na base do SS no Iraque?** E, por consequência, o que responder sobre a OT com data de meses anteriores.

## Histórico do ticket
| Data (UTC) | Quem | O quê |
|---|---|---|
| 2026-10-14 13:28 | Aasim (BH) | Abre o ticket: OT de fev/mar lançada em abril não entrou no SS; SS proporcional só ao input do mês corrente + recorrentes. Cita 1 empregado por entidade |
| 2026-10-15 | Ankit (Support) | Acknowledgement |
| 2026-10-19 / 20 / 21 | Ankit / Aasim | "É de Compliance?" → "yes it does" → atribuído a Compliance |
| 2026-10-21 05:44 | Suman | "as per Statutory, OT is not included for SS" + print (`image1.png`) |
| 2026-10-21 05:47 | Suman | "@evats, confirm the understanding and advise" |

**O que a imagem do Suman mostra:** as duas imagens (`image.png` e `image1.png`, iguais, uma com um traço amarelo por cima) são um **print do nosso próprio CCG** (IQ-CCG-001 v1.0, Módulo 2, §2.1 Federal Iraq, "Contribution base, floor and ceiling"), com destaque amarelo em: *"Excluded from the base: variable, hours-based pay (overtime, shift/night premium); genuine expense reimbursements…"*. Não é texto de lei nem de site oficial: o "as per Statutory" do Suman é o nosso CCG. O print reproduz fielmente o CCG; o problema é se o CCG está certo (ver Fonte primária: no Federal, **não está**).

## O que nossos artefatos dizem

### CCG IQ-CCG-001 v1.0 (export de 2026-10-22)
- **§2.1 Federal Iraq, Base** (citação literal): *"Base: the actual wage, allowances and benefits of the contribution month — basic salary; fixed and recurring allowances (housing, transport, meal, mobile, etc.); recurring salary supplements; leave pay; bonuses; and benefits in kind (…) — clamped to the floor and 5x ceiling (wage and allowances of every kind, not basic pay alone; Art. 15(First)/(Second), Art. 1(11)). Excluded from the base: variable, hours-based pay (overtime, shift/night premium); genuine expense reimbursements (relocation, travel, per diem); exempt items (…); salary advances; and contractor payments."*
  - A exclusão de OT **não tem artigo citado**. Os artigos citados na mesma frase (Art. 1(11) e Art. 15) dizem o contrário ("of every kind").
- **§2.1 Base period:** *"The contribution wage is the actual wage and allowances (al-ajr wa-l-mukhassasat) the worker receives in the contribution month, clamped to the floor and the 5x minimum-wage ceiling (Law 18/2023, Art. 15(First)) (…) Law 18/2023 does not fix the Federal contribution wage annually."*
- **§2.1 Floor / Ceiling:** *"Floor: the minimum wage (IQD 350,000)."* / *"Ceiling: 5× the minimum wage = IQD 1,750,000/month."* (comentário [e] no CCG: "this is monthly").
- **§2.2 KRI, Base:** *"Basic salary plus fixed allowances (Law 39/1971). Irregular, non-recurring amounts - overtime and one-off or discretionary bonuses - are excluded."* + *"Base period (registration) - fixed for the year (…) set on the January wage of that year"*; floor IQD 450,000; sem teto.
- **§6.2 Overtime (Federal):** OT a ≥150% (dia) e 200% (noite, descanso, feriado), Labour Law Art. 71(4). Confere com o texto da lei.

### WTC IQ-WTC-001 v1.1 (aba "Wage Type Catalogue"; colunas "Subject to SS — Federal" / "Subject to SS — KRI")
| Linhas | Wage types | Ocorrência | Tax Fed / KRI | **SS Fed / KRI** |
|---|---|---|---|---|
| R68–R97 | 62110–62139 "Overtime" (30 códigos) | Additional | Yes / Yes | **No / No** |
| R7–R23, R38–R41 | 21110–21127, 21210–21213 "Overtime deduction" (21113 é Advance: tudo No) | Additional | Yes / Yes | **No / No** |
| R108–R113 | 62150–62155 "Premium pay (i.e. Shift premium)" | Recurring | Yes / Yes | **No / No** |
| R126–R155 | 62200–62229 Bonus | Additional | Yes / Yes | Yes / No |

A coluna "Wage Type Explanation" e a "Formula" das linhas de OT estão vazias: nenhuma justificativa ou fonte para o "No".

### Design (`07 - Design/iq.json`, regra "IQ Social Security Base", ordinal 21, Federal)
- Exclui da base, por padrão de conta: `6211%`, `6212%`, `6213%` (OT 62110–62139) e `6215%` (shift premium); inclui o resto de `62%%%`.
- `taxRuleGroup: "retro_simple_tax"` em todas as regras de SS (Federal e KRI).
- KRI ("KRI- Social Security Base - Registered Wage"): base = só as contas 64551/64552 (salário registrado), sem nenhum input variável.
- Ou seja, o sistema faz exatamente o que o CCG/WTC mandam: **OT nunca entra no SS, em nenhum período**.

## Fonte primária

### 1. Iraque federal: Lei 18/2023 (Retirement and Social Security Law for Workers)
Fonte: texto da Base de Legislação Iraquiana do Conselho Superior da Magistratura (`iraqld.e-sjc-services.iq/legislations/showlegislation?lawbookid=49822`), impresso em 27/05/2026, arquivos `..._Ar.pdf` (md5 b2f9914f…) e `..._En.pdf` (md5 27339ce9…) no Drive. Publicação: Al-Waqa'i al-Iraqiyya nº 4734, de 2023-08-28; vigência 90 dias após a publicação (Art. 109), ou seja, a partir de 2023-11-26 (a base registra "26-11-2023").

| Artigo | Árabe (texto oficial; hamzas normalizadas, a extração do PDF as perde) | Tradução |
|---|---|---|
| **Art. 1, Décimo primeiro (definição de salário)** | «حادي عشر: الأجر: كل ما يتقاضاه المضمون من مبالغ نقدية وعينية ومخصصات بكل أنواعها لقاء عمله» | "Salário: tudo o que o segurado recebe em valores em dinheiro e em espécie e em adicionais **de todos os tipos**, em contrapartida do seu trabalho." |
| **Art. 14, Segundo (a)** (parte do empregado) | «(5%) خمسة من المئة يستقطع من مجموع ما يتقاضاه المضمون من أجور ومخصصات» | "5% descontados do **total** do que o segurado recebe em salários e adicionais." |
| **Art. 14, Segundo (b)(1)** (parte do empregador) | «(12%) اثنا عشر من المئة من مجموع ما يتقاضاه العامل من الأجور والمخصصات» | "12% do **total** do que o trabalhador recebe em salários e adicionais." |
| **Art. 14, Segundo (c)** (Estado) | «تساهم الدولة بنسبة (8%) ثمانية من المئة مما يتقاضاه العامل من أجور ومخصصات (…) وكذلك العامل الأجنبي في العراق إذ يتحمل صاحب العمل نسبة مساهمة الدولة» | "O Estado contribui com 8% do que o trabalhador recebe em salários e adicionais (…) exceto o trabalhador estrangeiro, cujo empregador arca com a parte do Estado." |
| **Art. 15, Primeiro (piso e teto)** | «تحسب اشتراكات الضمان الاجتماعي على أساس نسبة محددة من الأجر والمخصصات، ولا يجوز أن يقل الأجر المعتمد في تحديد نسبة الاشتراك في جميع الأحوال عن الحد الأدنى للأجور المقررة في مهنة المضمون أو الحد الأدنى العام للأجور أيهما أعلى، على أن لا يتجاوز الأجر المعتمد في تحديد نسبة الاشتراك عن (5) خمسة أضعاف الحد الأدنى للأجور» | "As contribuições são calculadas sobre o salário e os adicionais; o salário de contribuição não pode ser inferior ao salário mínimo da profissão ou ao mínimo geral, o que for maior, nem superior a 5 vezes o salário mínimo." |
| **Art. 15, Terceiro (b)** (salário não mensal) | «تستحق اشتراكات المضمون بأجر غير شهري على أساس مجموع ما يتقاضاه فعليا من أجور خلال شهر كامل» | "Para salário não mensal, a contribuição é sobre o total efetivamente recebido durante o mês completo." |
| **Art. 16** (base mensal) | «تعد الاشتراكات المستحقة عن الشهر (…) واجبة الأداء خلال الشهر التالي ويلتزم أصحاب العمل (…) باستقطاع مبلغ الاشتراك المتوجب على المضمون من أجره شهرياً» | "As contribuições devidas do mês são pagas no mês seguinte; o empregador desconta a parte do segurado do salário mensalmente." |
| Art. 15, Quarto | «تحدد طريقة احتساب الأجور والاشتراك (…) بتعليمات يصدرها الوزير» | O método de cálculo para casos especiais (por produção, temporários, mais de um empregador etc.) sai por instruções do Ministro. |
| Art. 108 | Revoga a Lei 39/1971; regulamentos e instruções dela ficam em vigor até substituídos, e "qualquer disposição que contrarie esta lei é nula". | — |

**Leitura:** a Lei 18/2023 não tem lista de exclusões da base. A definição é "de todos os tipos" e a contribuição incide sobre o "total" recebido. OT é valor em dinheiro recebido em troca de trabalho, então **entra na base**, limitada ao teto mensal de 5× o salário mínimo.

**Apoio na lei trabalhista federal (Labour Law nº 37/2015, Art. 1(14), versão inglesa no Drive, `Labour Law 2015_Eng.pdf`, md5 74796f9b…):** *"Wage: Any amount or benefit due to the worker in return for any work performed, plus all allowances and wages due for the overtime."* A lei trabalhista inclui expressamente a OT no conceito de salário. ⚠️ É tradução (o CCG aponta beoe.gov.pk / ILO NATLEX); o texto árabe oficial não foi conferido (ver Lacunas).

**Secundárias (só apoio):** Deloitte Middle East, "Social Security Law no.18 of 2023": a base passa a ser o salário básico, em dinheiro ou em espécie, "along with all allowances", em vez da regra antiga dos adicionais fixos. Nenhuma fonte encontrada (primária ou secundária) exclui OT no regime federal.

**Piso, teto, periodicidade (Federal):**
- Base **mensal**: Art. 15, Terceiro (b) ("durante um mês completo") e Art. 16 (contribuições "do mês", desconto mensal).
- Piso: o maior entre o salário mínimo da profissão e o mínimo geral (Art. 15, Primeiro). CCG: IQD 350.000. ⚠️ sem fonte primária local para o valor (decisão do Conselho de Ministros não está na pasta).
- Teto: 5× o salário mínimo (Art. 15, Primeiro). CCG: IQD 1.750.000/mês, derivado do mínimo de 350.000 (mesma ressalva).

### 2. Região do Curdistão (KRI): Lei 39/1971 como aplicada na KRG
Fonte: `The-Pension-and-Social-Security-Law-for-Workers-as-Amended-Kurdistan_EN.pdf` (md5 fbad1fe3…), tradução inglesa.
- **Art. 1, "Wage"** (redação dada pela Lei 155/1971): *"All of which comes under the meaning of a fixed wage in the Labour law when it has been established by transactions or customs to be paid permanently."* → só o salário **fixo e permanente**. OT, por ser variável, fica fora.
- **Art. 26(b):** *"Subscriptions paid during one Gregorian year shall be based on wages paid in January of that year."* → base fixada no salário de janeiro, sem variação mensal.
- **Art. 26(a):** piso no salário mínimo (da profissão ou geral). Não há teto no texto.
- Coordenação federal × KRI: Lei 18/2023, Art. 4, Segundo (filiais "em cada governadoria que não pertença a uma região") e Art. 39, Quinto (coordenação com a Direção-Geral de Trabalho e Seguridade Social da Região do Curdistão na transferência de segurados).
- ⚠️ O PDF não traz o texto da Emenda KRG nº 4/2012 (a que o CCG cita). A exclusão de OT na KRI está sustentada pelo Art. 1 e pelo Art. 26(b) da Lei 39/1971, mas a emenda não foi conferida.

### 3. Federal ou KRI: onde estão as entidades?
- O ticket e os artefatos **não dizem** a região das REF-03-147/148. O nome "Best Solutions Trading and Services for Oil and Gas Equipment" não aparece em nenhum lugar do cérebro.
- Indício (inferência, não prova): o reporter diz que o SS foi "prorated (…) to input in current month's date". No Design, a base KRI é só o salário registrado (64551/64552) e não reage a inputs. Uma base que varia com inputs do mês é a regra Federal (ordinal 21). As duas entidades **parecem estar configuradas como Federal**. Confirmar o flag de região (conta 58219: 1 = Federal, 2 = KRI) na entidade.

## Veredito
| Regime | OT entra na base do SS? | Nossos artefatos | Veredito |
|---|---|---|---|
| **Federal Iraq** (Lei 18/2023) | **Sim**: Art. 1(11) "de todos os tipos" + Art. 14 Segundo e Art. 15 Primeiro "total de salários e adicionais", até 5× o salário mínimo; Labour Law 37/2015 Art. 1(14) inclui OT no salário | CCG §2.1, WTC (SS Federal = No) e Design (exclui 6211–6213%) **excluem** | **Divergente**: o "as per Statutory, OT is not included" do Suman não se sustenta para o Federal. A frase vem do nosso CCG, que não tem fonte para essa exclusão |
| **KRI** (Lei 39/1971) | **Não**: só salário fixo/permanente (Art. 1), base do salário de janeiro (Art. 26(b)) | CCG §2.2, WTC (SS KRI = No), Design (só salário registrado) | **Confirmado** (com a ressalva da Emenda 4/2012 não conferida) |

**Item 4: a data do input (fev/mar pago em abril) perde relevância?**
- **No sistema, como está hoje: sim.** OT está fora da base em qualquer período (Design exclui 6211–6213%). Com ou sem data retroativa, a OT nunca gera SS. O que o reporter chama de "prorated only to input in current month's date" é efeito de outros inputs (additional/recurring que entram na base), não da OT. As regras de SS estão em `retro_simple_tax`, o que indica que inputs datados em meses anteriores são calculados no período de origem (retro). ⚠️ É leitura do nome do grupo no Design; a semântica do motor não tem fonte documental aqui.
- **Pela lei (Federal): não perde.** Se a OT entra na base, é preciso decidir em que mês a OT de fev/mar conta:
  - (a) no mês em que é recebida (abril). A lei fala em "o que o segurado recebe" (يتقاضاه) e o Art. 15, Terceiro (b) em "o efetivamente recebido durante o mês"; ou
  - (b) retroativamente em fev/mar, cada mês com o seu teto.
  A lei não trata expressamente de pagamentos atrasados ("arrears"): ⚠️ sem fonte. Na prática, se o salário mensal do empregado (sem OT) já atinge o teto de IQD 1.750.000, a OT não muda o SS em nenhuma das duas leituras. O efeito só aparece para quem está abaixo do teto. Não há dados de pagamento no ticket para conferir os empregados A e B.

## Achados fora do pedido
(Não vão para o ticket. Candidatos a hub/`correcoes.md`, com o ok do usuário.)
1. **CCG §2.1 × WTC: "leave pay".** O CCG põe "leave pay" na base Federal, mas no WTC 62300/62302 "Annual leave pay" e 62305 "Annual leave payout" estão com SS Federal = **No**. O Design inclui 6230% na base (padrão `62%%%`), alinhado ao CCG e desalinhado do WTC.
2. **WTC × Design:** 62140–62149 "Salary addition" e 62108 "Historic Pay" estão SS Federal = **No** no WTC, mas entram na base no Design (não estão na lista de exclusões).
3. **Shift premium (62150–62155) e 6215% no Design:** mesma exclusão sem fonte que a OT. A Lei 18/2023 não exclui adicionais "de todos os tipos". Deve ser revisto junto com a OT.
4. **CCG, contradições internas sobre a base Federal:**
   - Step-by-step: "Consider the **registered** social security contribution base".
   - §3.4: "the registered SS wage continues for the calendar year (changed only at the next January…)".
   - As duas frases contradizem o próprio §2.1 ("Law 18/2023 does not fix the Federal contribution wage annually").
5. **CCG §2.2 × §2.1, mês de saída:** o §2.2 diz que "Federal Iraq (…) the PSSO requires the full month for both joiner and leaver". O §2.1 e a Lei 18/2023, Art. 15, Terceiro (a), dizem que no mês de saída a contribuição é só sobre a parte do mês ("جزء الشهر الذي تنتهي فيه الخدمة").
6. **CCG, vigência:** "in force in Federal Iraq since December 2023". Pela Lei 18/2023, Art. 109, com publicação em 2023-08-28, a vigência é a partir de 2023-11-26.
7. **Design, piso e teto:** a regra "IQ Social Security Base" usa `floorAmount: 4200000` e `ceilingAmount: 21000000` (= 350.000 × 12 e 1.750.000 × 12, valores anuais), mas o CCG diz que o teto é mensal (comentário [e]). Conferir se o motor anualiza ("retro_simple_tax") ou se aplica o valor anual a um mês (o que tornaria o teto inócuo). ⚠️ não verificado.
8. **Alíquota de 25% do setor de petróleo** (Lei 18/2023, Art. 14, Segundo (b)(2)): vale para empregadores privados/mistos "cujos lucros resultam da venda de petróleo… produzido no Iraque e exportado". O CCG deixa o setor "oil/prime" fora do escopo. Para uma entidade de "Trading and Services for Oil and Gas Equipment", provavelmente não se aplica (é serviço, não venda de petróleo), mas não foi confirmado.
9. **CCG, fontes da Lei 18/2023:** a lista de fontes cita "primary text via the Iraqi Official Gazette" e corrobora com WTW/Al-Tamimi/SSA [secondary]. O texto oficial (iraqld) já está no Drive e deveria ser a fonte citada.

## Rascunho de resposta (EN)
> Para a Enaakshi revisar antes de qualquer post. Pressupõe que as entidades são Federal (confirmar o flag de região). O parágrafo entre colchetes depende da decisão sobre o mês de atribuição (ver "O que precisa ser feito"). Não postar.

```
@srai @abagwan

Federal Iraq: overtime is part of the social security base. Law No. 18 of 2023 defines the wage as "all monetary and in-kind payments and allowances of all kinds received by the insured person in return for their work" (Art. 1, Eleventh), and contributions are calculated on the total wages and allowances received (Art. 14, Second; Art. 15, First), capped at 5x the minimum wage (IQD 1,750,000/month). Labour Law No. 37 of 2015, Art. 1(14), also includes overtime pay in the wage. The current exclusion of overtime (WT 62110–62139) from the Federal SS base will be corrected in the CCG, WTC and configuration.

Kurdistan Region: overtime remains excluded. Law No. 39 of 1971 limits the wage to the fixed wage paid permanently (Art. 1), and contributions are based on the January wage of the year (Art. 26(b)).

[Overtime for February/March paid in April: <decisão pendente: contributed in the month it is paid (April), within that month's ceiling / recalculated in February/March>.]

Please confirm whether REF-03-147 and REF-03-148 are registered under Federal Iraq or the Kurdistan Region.
```

## O que precisa ser feito
| # | Ação | Quem | Urgência |
|---|---|---|---|
| 1 | Decidir se responde no ticket como "Divergente" (OT entra no Federal) e escolher a atribuição da OT atrasada (mês de recebimento × retro) | Usuário / Enaakshi (dona do ticket e do CCG) | **Alta**: o ticket espera Compliance desde 21/10 e o Suman já disse ao cliente o contrário |
| 2 | Confirmar a região (flag 58219) das entidades REF-03-147/148 | Suman / Implementação (BH) | Alta: muda a resposta |
| 3 | Corrigir o CCG §2.1 (tirar OT e shift premium de "Excluded", com fonte Art. 1(11) / Art. 14 / Art. 15) e os achados 4–6 | Compliance (Enaakshi), nova versão do CCG | Média, depois do ok |
| 4 | WTC: SS Federal = Yes para 62110–62139, 21110–21127/21210–21213 (exceto o Advance 21113) e 62150–62155; rever 62300/62302/62305, 62108 e 62140–62149 (achados 1–2) | Compliance, nova versão do WTC | Média |
| 5 | Design: tirar 6211–6213% (e 6215%) das exclusões da "IQ Social Security Base"; conferir piso/teto anuais (achado 7) | Design (nosso) → produção é outro time | Média, depois da 4 |
| 6 | Avaliar o recálculo de SS dos meses de 2026 já processados das entidades Federal com OT (impacto só abaixo do teto) | Outro time (produção/cliente), ver `fronteiras.md`; nós só informamos a regra | Depende da 1 |
| 7 | Registrar a decisão no hub do país (criar `paises/Iraque.md`, que não existe) e, se confirmada, a entrada em `correcoes.md` | Janela Suporte / geral, com ok do usuário | Ao fechar o ticket |

## Lacunas
- **Região das entidades:** não identificada em nenhuma fonte; a inferência "Federal" vem do comportamento descrito pelo reporter.
- **Instruções ministeriais** (Lei 18/2023, Art. 15, Quarto) sobre o método de cálculo de salários: nenhuma encontrada. Também não se sabe se alguma instrução da Lei 39/1971 mantida pelo Art. 108 trata de OT. Não há prática publicada da Daman/PSSO excluindo OT. ⚠️ Sem fonte em contrário; também sem confirmação oficial positiva específica para OT além da definição legal.
- **Labour Law 37/2015, Art. 1(14):** só a tradução inglesa foi lida; o texto árabe oficial não foi conferido.
- **KRI:** o texto da Emenda KRG nº 4/2012 não está na pasta; o PDF "Kurdistan" é a Lei 39/1971 consolidada em inglês.
- **Salário mínimo IQD 350.000 (Federal) e 450.000 (KRI):** sem fonte primária na pasta (decisão do Conselho de Ministros / decreto KRG de 03/08/2025).
- **Atribuição de OT atrasada** (mês recebido × mês trabalhado): a lei não trata expressamente. ⚠️ sem fonte.
- **Semântica do `retro_simple_tax`** e dos piso/teto anuais no Design: inferidas, não documentadas.
- **Dados de pagamento** dos empregados A e B (abril, OT de fev/mar, se estavam acima do teto): não disponíveis; impacto real não quantificado.
- Nenhuma fonte oficial nova foi baixada (`raw/docs/oficiais/IQ/` não foi criada): todas as primárias usadas já estavam no Drive.
