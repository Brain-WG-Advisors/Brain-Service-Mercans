# HRBS-16252 — Iêmen (Baker Hughes): base do Social Security (GCSS)

> Análise só leitura, 2026-10-22. Nada foi postado no YouTrack, nada foi alterado no Drive nem nos artefatos.

## Metadados
| Campo | Valor |
|---|---|
| Ticket | [HRBS-16252](https://youtrack.hrblizz.dev/issue/HRBS-16252) — "Baker Yemen – Confirmation required on SS base" |
| Cópia local | `raw/tickets/api/2026-10-22-for-evats/HRBS-16252.md` (gerada em 22/10 16:30) |
| Anexos | `raw/tickets/api/anexos/HRBS-16252/` (G2N Validation, Yemen BH Jan Results, image.png, image1.png). O "Book1.xlsx" citado na descrição **não** veio nos anexos. |
| País / cliente | Iêmen / Baker Yemen (REF-P203-923), Live/BAU, período jan/2026 em diante |
| Wage types | 2551 SS EE 6%, 2550 SS ER 9% |
| Reporter | Aasim Bagwan (abagwan) |
| Assignee | Enaakshi Vats (evats) no export; passou para wgomes em 22/10 (ver `rascunhos/2026-10-22-triagem-tickets-enaakshi-shruti.md`) |
| Urgência | Alta: trava a UAT da Mercans e o reprocessamento de janeiro antes dos prazos do GCSS e do Form 4 |
| Artefatos lidos | `raw/docs/drive-exports/2026-10-22/YE-CCG-001-v1_0.txt`, `YE-WTC-001-v1_0.xlsx`, `YE-DD-001-v1_0.xlsx`; comparação com `G:\...\Yemen\05 - Payroll Regulation Guide\Archived\YE-CCG-001-v1.0_AI.docx`, `02 - DD\Archived\YE-DD-001-v1.0_AI.xlsx` e `12 - Country Report Codes\Statutory Reports Spec\Archived\YE-SSF-001-...-Spec.xlsx` |

## O que foi pedido a nós
O Suman respondeu a)–f) em 22/10 11:26 e escreveu: **"@evats, please confirm on point a), d) and e)"**. Logo depois (11:35) o Aasim perguntou ao Suman se, no sistema atual, a base basic+housing+transport é **mensal** ou **fixada no salário de janeiro**, e anexou a posição do agente fiscal do cliente: a base é o salário de **janeiro de cada ano** (link para https://gcss-yemen.org/).

Pedido a nós (Compliance):
- **a)** Base só com o basic é aceitável? Se não, qual base?
- **d)** Admitidos, desligados e licença não remunerada com base travada: base cheia ou proporcional?
- **e)** Tirar o transporte da base já?
- Pergunta do Aasim, na parte que é de lei: a base é mensal ou o salário de janeiro? (Se o **sistema** calcula mês a mês é pergunta ao Suman; ele já respondeu em b) que não existe base fixa.)

b), c) e f) foram respondidos pelo Suman e não foram pedidos a nós; f) entra em "Achados fora do pedido" porque a lei prevê um adicional.

## Histórico do ticket
| Data (UTC) | Quem | O quê |
|---|---|---|
| 20/10 11:42 | Aasim | Abre o ticket. O cliente quer SS sobre o **basic de janeiro**, travado no ano. O sistema hoje recalcula todo mês sobre basic + housing + transport e exclui bônus. Diz que o CCG Step 2 aplica "fixed insured wage of contractual basic + housing, transport excluded", que o WTC marca o transporte como não sujeito a SS e que o DD tem o campo "SI Insured / Contractual Wage (monthly)". Totais de jan: sistema EE 540.892 / ER 811.335; guia (basic+housing fixo) 505.342 / 758.010; pedido do cliente (basic jan) 364.465 / 546.697; resultado real do cliente 426.152 / 639.227. |
| 20/10–21/10 | Ankit | Acusa o recebimento e atribui ao Suman. |
| 22/10 11:26 | Suman | a) o CCG cobre o pagamento real, não salário fixo, e inclui basic + outras allowances; o WTC inclui o transporte (print do CCG 5.2, image.png). b) o sistema não tem base fixa. c)/d) não se aplicam. e) o transporte entra, conforme a matriz do CCG e o WTC (print da matriz, image1.png). f) ER só 9%. Pede à @evats que confirme a), d) e e). |
| 22/10 11:35 | Aasim | Pergunta se o cálculo atual é mensal ou com base em janeiro; cita o GCSS ("January of each year"). |

Observação sobre o anexo G2N (`Issues_Log`, item 3): a diferença entre Mercans e cliente no SS foi registrada como "Client to confirm GCSS-registered wage". A base implícita do cliente para o empregado A (SS EE ÷ 6%) é **menor** que o basic de janeiro/2026 dele. Isso bate com o cliente estar usando o salário **registrado no GCSS** (de janeiro), não o salário real do mês. É inferência pelos números, não confirmação.

## O que nossos artefatos dizem

### Como se resolve a contradição Aasim × Suman
**Os dois citaram trechos que existem: nossos artefatos se contradizem por dentro.**

**YE-CCG-001 v1.0 (Google Doc, export de 22/10; o `.gdoc` mudou em 22/10 08:24 BRT = 11:24 UTC, 2 minutos antes do comentário do Suman):**
| Local (linha no .txt) | Texto literal | Leitura |
|---|---|---|
| Módulo 3, **Step 2** (l. 341) | "The social-insurance base ("covered earnings") is the basic salary plus all allowances, excluding bonuses and overtime (SSA SSPTW 2018; Social Insurance Law 1991). **In the reviewed payroll the base is applied as a fixed insured wage - the contractual basic plus housing - with transport, bonuses and overtime excluded.**" | Bate com o que o Aasim citou. |
| 5.2 "Are contributions based on actual or standard salary?" (l. 772) | "Contributions are based on actual covered earnings for the period — the insured wage: **in the reviewed payroll a stable contractual figure (basic plus housing) that excludes transport**, bonuses and overtime and does not move with the month's paid basic (retro and proration adjustments do not enter the SI base)." | É o trecho do print do Suman (image.png, grifado em amarelo). Ele leu só "actual covered earnings", mas o mesmo parágrafo diz "stable contractual figure" e "excludes transport". |
| 4.x matriz (l. ~584–600) e 5.1.1 (l. 693–694) | Transport allowance: In SI base = "Yes"; "Transport / representation / appearance allowances — Yes (as allowances) — Included in the SI base even though partly tax-exempt" | Bate com o Suman (image1.png). |
| 5.2 cálculo (l. 754) | "Assemble covered earnings = basic salary + all cash allowances for the period" | Base mensal. |
| 5.2 admissão/desligamento (l. 775–778) | "pro-rate covered earnings for the days worked using a 30-day month"; "Termination month: contributions run through the last month … pro-rated" | Proporcional nos dois casos. |
| Leave (l. 1260, 1272) | "an unpaid period produces no covered earnings and therefore no employee 6% or employer 9% contribution for those days" | — |
| 5.1 (l. 659, 669–681) | Um único esquema 6% + 9%; "work-injury add-on treated as an administrative caveat" | — |

**Origem das frases sobre "reviewed payroll":** elas **não existem** na versão gerada por IA arquivada (`Archived/YE-CCG-001-v1.0_AI.docx`). Lá, o Step 2 (l. 184) termina em "excludes bonuses and overtime", e o 5.2 (l. 301) diz "the real basic salary plus allowances paid … If actual covered earnings change, the base changes with them". Alguém acrescentou as frases ao Google Doc antes de 20/10, porque o ticket já as cita. O motivo provável é a revisão de uma folha real (a da Baker?). ⚠️ Autor e data não identificados: ver o histórico de versões do Doc.

**YE-WTC-001 v1.0 (export de 22/10):**
| Aba / linha | Código | Coluna Q "Subject to Social Insurance (GCSS, 6% EE / 9% ER)" | Explicação (col. F) |
|---|---|---|---|
| Wage Type Catalogue, l. 207–213 | 62510–62513, 62520–62523 (Car & Transportation / Transportation allowance e arrears/adjustment/advance) | **Yes** (R = Yes) | "The FULL allowance IS part of the GCSS covered base (SI base = basic + all allowances)." |
| Wage Type Catalogue, **l. 307** (adição YE, sem código) | "Transport Allowance (Yemen - tax-exempt up to YER 30,000/mo)" | **No** (R = No) | "…Excluded from the GCSS/SI covered base." Também diz que o excesso sobre 30.000 vai a 15% flat (Special Tax), o que contradiz a l. 210 (excesso na tabela de residente). |
| Wage Type Catalogue, l. 308 (adição YE) | Representation & Appearance Allowance | No | "Excluded from the GCSS/SI covered base", o que contradiz o CCG 5.1.1. |
| Wage Type Catalogue_Final, l. 196–202 | 62510–62523 | P "Subject to Social Insurance" = **Yes** | — |
| Global WTC Coverage, l. 311 | "(YE) Transport Allowance (Yemen …)" — Added | — | — |

O Aasim leu a l. 307 e o Suman as linhas globais/_Final. A aba _Final, que é a configurada, tem o transporte **dentro** da base.

**YE-DD-001 v1.0:** **não existe** campo "SI Insured / Contractual Wage" nem nada parecido. Procurei "insured", "contractual" e "wage" em todas as abas do export de 22/10 e na versão arquivada `_AI`. Os campos de SS são: GCSS Social-Security Number, Employer GCSS Registration Number, Social Security Exemption, Enrolment Status e GCSS Administering Zone. A afirmação do ticket não tem respaldo no DD (pode vir de outro documento ou da configuração do cliente; ⚠️ não localizado).

**YE-SSF-001 (spec do retorno do GCSS, versão arquivada .xlsx):** E-12 "Covered Earnings = Basic (E-09) + Allowances (E-10), pro-rated by Days Worked ÷ 30"; E-10 inclui o transporte. A base é mensal e proporcional.

## Fonte primária

**F1. Lei — Decreto Republicano com força de lei nº 26 de 1991 sobre Seguros Sociais (قرار جمهوري بالقانون رقم (26) لسنة 1991م بشأن التأمينات الاجتماعية)**, alterada pela Lei nº 16 de 2008. Publicada no Diário Oficial nº 7/2 de 1991. PDF publicado pelo próprio GCSS (Aden): `raw/docs/oficiais/YE/2026-10-22-lei-26-1991-seguros-sociais-gcss.pdf` (31 págs., digitalizado; página de origem `raw/docs/oficiais/YE/2026-10-22-gcss-pagina-lei-seguros-sociais.html`).
> Atenção: a lei do setor privado (GCSS) é a **nº 26/1991**, não a nº 25/1991 citada no pedido. As notas de rodapé da compilação mostram que a Lei 16/2008 mudou a definição de idade de aposentadoria (art. 2), o art. 51(1), o art. 57(1)(a), acrescentou o art. 64-bis e revogou o art. 76(4). **Os arts. 2 (الأجر), 14, 15, 27, 49 e 50 não têm nota de alteração.**

| Art. | Árabe (transcrição da página digitalizada) | Tradução |
|---|---|---|
| **2** — الأجر (p. 90) | "كل ما يحصل عليه المؤمن عليه من أجر أساسي مقابل عمله أو أي بدلات أخرى تضاف بقرارات من الوزير ولا تدخل في حساب الأجر الأساسي (الأجور الإضافية والمنح والمكافأة التشجيعية)." | "Salário: tudo o que o segurado recebe como salário básico pelo seu trabalho, ou quaisquer outras allowances acrescentadas por decisões do Ministro; não entram no cálculo do salário básico (horas extras, gratificações e bônus de incentivo)." |
| **14(1)** (p. 94) | "تحسب الإشتراكات التي يؤديها صاحب العمل وتلك التي تستقطع من أجور المؤمن عليهم على أساس ما يتقاضونه من الأجور في شهر يناير من كل سنة حتى ولو زادت أو نقصت أجورهم خلال العام." | "As contribuições pagas pelo empregador e as descontadas dos salários dos segurados são calculadas com base nos salários que eles recebem no **mês de janeiro de cada ano**, **mesmo que os salários aumentem ou diminuam durante o ano**." |
| **14(2)** | "بالنسبة للعاملين الذين يلتحقون بخدمة صاحب العمل بعد شهر يناير تحتسب الإشتراكات على أساس الأجر الكامل عن الشهر الذي التحقوا فيه بالخدمة حتى شهر يناير التالي." | "Para quem entra a serviço do empregador depois de janeiro, as contribuições são calculadas sobre o **salário integral do mês de admissão**, até o janeiro seguinte." |
| **14(3)** | "يسري حكم الفقرة (2) من هذه المادة على من يطبق عليهم هذا القانون لأول مرة." | "A regra do §2 vale para quem passa a ser coberto pela lei pela primeira vez." |
| **15(1)** | "تقدر الاشتراكات … على أساس أجر المؤمن عليه قبل استنزال أية استقطاعات كالضرائب والرسوم … وكذلك قبل استنزال الاستقطاعات الأخرى من الأجر بسبب الأجراءات أو الغرامات أو خصم ساعات التأخير أو أيام الغياب بدون أجر أو غير ذلك من الأسباب التي تدعو إلى تخفيض الأجر." | "As contribuições são apuradas sobre o salário do segurado **antes de qualquer desconto** (impostos, taxas, dívidas, parcelas…) e antes dos descontos por medidas disciplinares, multas, horas de atraso, **dias de ausência sem remuneração** ou qualquer outro motivo que reduza o salário." |
| **15(2)** | "لا تؤدى الاشتراكات عن الشهر الذي تنتهي فيه خدمة المؤمن عليه بغض النظر عن عدد الأيام التي اشتغلها فيه." | "**Não se pagam contribuições pelo mês em que termina o serviço** do segurado, independentemente de quantos dias ele trabalhou nesse mês." |
| **19** (p. 96) | "حصة صاحب العمل وحصة العامل في الإشتراكات واجبة الإستحقاق في اليوم الأول من الشهر التالي لشهر الإستحقاق وعلى صاحب العمل أن يؤديها إلى المؤسسة في خلال خمسة عشر يوماً من ذلك التاريخ." | "As contribuições vencem no 1º dia do mês seguinte e devem ser pagas ao GCSS em até 15 dias." |
| **27(1)(a), 27(2)** (p. 97) — Seguro de Acidente de Trabalho | "الإشتراكات الشهرية التي يلتزم أصحاب الأعمال بأدائها شهرياً للمؤسسة بواقع (4%) من أجور المؤمن عليهم العاملين لديه … لا يجوز تحميل العمال أي نصيب في هذا التأمين." | "Contribuições mensais do empregador ao GCSS de **4%** dos salários dos segurados … o trabalhador não pode arcar com nenhuma parte." |
| **49(1)(2)** (p. 102–103) — Velhice, invalidez e morte | "حصة صاحب العمل في الإشتراكات وتعادل (9%) من أجور المؤمن عليهم … حصة المؤمن عليهم التي تقتطع من أجورهم وتعادل (6%)" | "Parte do empregador: **9%** dos salários; parte do segurado, descontada do salário: **6%**." |
| **50(3)** (p. 103) | "يجوز للعامل أن يتحمل حصته وحصة صاحب العمل في حالة الإجازة بدون مرتب شريطة أن يدفعها في مواعيد استحقاقها وإلا اعتبرت إشتراكاته متوقفة خلال فترة الإجازة." | "Na **licença sem remuneração**, o trabalhador pode arcar com a sua parte e a do empregador, desde que pague nos vencimentos; caso contrário, as contribuições ficam **suspensas** durante a licença." |
| **6(1)** (p. 92) | "يطبق أحكام تأمين الشيخوخة والعجز والوفاة وإصابة العمل على أصحاب الأعمال الذين يستخدمون خمسة عمال فأكثر …" | "Os seguros de velhice/invalidez/morte **e de acidente de trabalho** aplicam-se aos empregadores com 5 ou mais trabalhadores…" |

**F2. Publicação oficial do GCSS — página "Seguro dos empregadores e seus trabalhadores" (التأمين الإلزامي لصاحب العمل)**, https://gcss-yemen.org/التأمين-الإلزامي-لصاحب-العمل/ → `raw/docs/oficiais/YE/2026-10-22-gcss-tamin-ilzami-saheb-alamal.html` (é a mesma fonte que o cliente citou):
- **الأجر الخاضع للإشتراك:** "1- الأجر الأساسي مضافاً إليه البدلات والعلاوات التي لها صفة الديمومة والثبات ولا يدخل في عنصر الأجر المكافآت التشجيعية والأجور الإضافية" → "Salário sujeito à contribuição: o básico **mais as allowances e adicionais de caráter permanente e estável**; bônus de incentivo e horas extras não entram."
- "2 – يجب ان لا يقل الحد الأدنى للأجور الخاضعة للاشتراكات عن الحد الأدنى لأجور العاملين في الجهاز الإداري للدولة" → "O salário de contribuição não pode ser inferior ao salário mínimo do funcionalismo público."
- "3 – تحسب الاشتراكات على اساس أجور العاملين في شهر يناير من كل عام، أو على اساس اجر الاشتراك في تاريخ الالتحاق لأول مرة إذا كان بعد شهر يناير، كما تحسب الاشتراكات على أساس أجر المؤمن عليهم قبل استنزال أية استقطاعات منه" → "As contribuições são calculadas sobre os salários de **janeiro de cada ano**, ou sobre o salário de contribuição na data da primeira admissão, se posterior a janeiro, e sempre antes de qualquer desconto."
- **نسب الإشتراك:** "(15) من إجمالي أجور المؤمن عليهم … ( 9% ) حصة صاحب العمل … (6%) حصة العامل" no seguro de velhice/invalidez/morte. **A página não menciona os 4% de acidente de trabalho.**
- **Documentos:** "صورة طبق الأصل من كشوفات المرتبات ( كما ترفق أيضا مع البيان المفصل للأجور في شهر يناير من كل عام )" → a folha é entregue também com o **demonstrativo detalhado dos salários de janeiro de cada ano**.
- **الاشتراكات في حالة الإجازات:** férias anuais pagas: contribuição devida "como se estivesse trabalhando"; licença sem remuneração: o trabalhador pode pagar a sua parte e a do empregador mediante **pedido escrito ao GCSS**, pago por meio do empregador; caso contrário, a contribuição fica suspensa.
- **توقيف العامل:** em suspensão com salário integral ou parcial, a contribuição incide sobre o **salário integral**.

**Fonte secundária (só apoio):** o CCG cita "SSA SSPTW 2018". Não consegui baixar (HTTP 403) e não usei. Arquivos baixados sem uso: `2026-10-22-gcss-home.html` (página inicial do GCSS, de onde saem os links) e `2026-10-22-gcss-qanun-altaminat.html` (**é uma página 404**, link errado; desconsiderar).

## Veredito por pergunta
| Item | O que a lei diz | Nossos artefatos | Veredito |
|---|---|---|---|
| **a) Base só com o basic?** | **Não.** A base é o "الأجر" (art. 2): básico + allowances; o GCSS (F2) especifica as allowances "de caráter permanente e estável". Ficam fora horas extras, gratificações e bônus de incentivo (art. 2). O ponto do cliente sobre **janeiro** está certo (art. 14(1)); o "só basic", não. Base correta: **salário de janeiro (basic + allowances fixas, como housing e transport) travado de jan a dez**. | CCG: basic + all allowances, mas mensal, e o Step 2 e o 5.2 dizem "fixed insured wage basic + housing, transport excluded". | **Divergente** (cliente: só basic). **Confirmado**: a base inclui allowances fixas. **Divergente** (nosso CCG e sistema: base mensal; a lei manda janeiro). Fonte: art. 2, 14(1); F2. |
| **Pergunta do Aasim (mensal × janeiro)** | **Janeiro de cada ano**, "mesmo que os salários aumentem ou diminuam durante o ano" (art. 14(1)); confirmado pelo GCSS (F2 item 3). | CCG 5.2: "monthly determination on actual covered earnings", "no year-end". O sistema calcula mês a mês (Suman, b). | **Divergente**: lei = base anual fixa de janeiro; sistema e CCG = mensal. |
| **c) Atualização da base** (não pedido a nós, mas é consequência) | Automática **a cada janeiro** (art. 14(1)), e não quando o cliente avisa o GCSS. | — | **Confirmado** pela lei: renova em janeiro. |
| **d) Admitidos** | Admitido depois de janeiro: base = **salário integral (الأجر الكامل) do mês de admissão**, até o janeiro seguinte (art. 14(2)). O texto não prevê proporcionalização. | CCG 5.2 e SSF E-12: proporcional (dias ÷ 30). | **Divergente**: base cheia do mês de admissão. ⚠️ Se a contribuição do próprio mês de admissão é cheia ou parcial: a lei não diz expressamente; a leitura de "الأجر الكامل" e do art. 18 (responsabilidade a partir da admissão) indica **cheia**. Confirmar no regulamento executivo (não localizado). |
| **d) Desligados** | **Sem contribuição no mês do desligamento**, qualquer que seja o número de dias trabalhados (art. 15(2)). | CCG: "pro-rated for a mid-month leaver". | **Divergente**: zero no mês da saída (nem cheia nem proporcional). |
| **d) Licença não remunerada** | Faltas/dias sem remuneração **não reduzem** a base (art. 15(1)). Licença sem remuneração formal: a contribuição fica **suspensa**, salvo se o empregado optar, por pedido escrito ao GCSS, por pagar 6% + 9% (art. 50(3); F2). Suspensão com salário: contribuição sobre o salário integral (F2). | CCG l. 1260/1272: a licença não remunerada "reduces or removes the covered earnings … no 6%/9% for those days". | **Divergente**: base cheia para ausências sem remuneração; suspensão (ou pagamento integral pelo empregado, se ele optar) na licença sem remuneração formal. |
| **e) Tirar o transporte?** | **Não.** O transporte pago como allowance mensal fixa é "بدل … له صفة الديمومة والثبات" (F2) → entra na base. O art. 2 só exclui horas extras, gratificações e bônus de incentivo. ⚠️ O art. 2 fala em allowances "acrescentadas por decisões do Ministro"; essa decisão ministerial (ou o regulamento executivo) **não foi localizada**. A inclusão se apoia na publicação do GCSS. | WTC l. 207–213 e _Final = Yes; CCG 5.1.1 e matriz = Yes; **WTC l. 307 (adição YE) = No; CCG Step 2 e 5.2 = "transport excluded"**. | **Confirmado** que entra (F2; art. 2 não o exclui), com a ressalva ⚠️ da decisão ministerial. Nossos artefatos se contradizem: corrigir a l. 307 do WTC e as frases do CCG. |
| **f) ER 9%, sem acidente de trabalho?** (não pedido a nós) | Art. 49: ER 9% / EE 6% (velhice, invalidez, morte). **Art. 27: seguro de acidente de trabalho, 4% só do empregador**, e o art. 6(1) o aplica a empregadores com 5+ trabalhadores. A página do GCSS (F2) só lista os 15%. | CCG: "work-injury add-on treated as an administrative caveat"; Suman: "only 9%". | **Divergente da letra da lei** (4% de acidente de trabalho previsto e não revogado na compilação). ⚠️ Se o GCSS cobra os 4% na prática: sem fonte. Os números do cliente mostram só 9%. |

## Achados fora do pedido
(Vão para o hub do país / correções, não para o ticket.)
1. **CCG, base mensal × janeiro:** os módulos 3 (Step 2) e 5 (5.1.1, 5.2, "Are year-end adjustments required?") descrevem base mensal sobre "actual covered earnings". A lei (art. 14) manda salário de janeiro travado no ano. Erro de conteúdo no CCG.
2. **CCG, frases de "reviewed payroll"** (Step 2, l. 341; 5.2, l. 772): misturam a prática de uma folha específica (basic + housing, sem transporte) com a regra legal e contradizem a matriz do próprio CCG. Não estão na versão de IA arquivada. Saber quem incluiu e quando.
3. **CCG, admissão/desligamento/licença** (l. 775–778, 1260, 1272): proporcionalização não prevista; o mês da saída é **isento** (art. 15(2)); ausências sem remuneração não reduzem a base (art. 15(1)); licença sem remuneração segue o art. 50(3).
4. **CCG/WTC/SSF, acidente de trabalho 4% (art. 27):** tratado como "caveat"; a lei prevê a alíquota. Confirmar a aplicação real com o GCSS/cliente (avisos mensais de cobrança, "قرارات الربط الشهرية").
5. **CCG, piso:** o CCG diz "No statutory floor located". O GCSS (F2) diz que o salário de contribuição não pode ser inferior ao salário mínimo do funcionalismo público.
6. **CCG, prazo de pagamento:** o CCG diz "confirm exact date with GCSS". O art. 19 diz: vence no dia 1 do mês seguinte, pagamento em até 15 dias. Multa de 3% ao mês (art. 20) e adicional de 5% por subdeclaração de salário ou data (art. 21).
7. **CCG, fonte:** cita "Social Insurance Law 1991" sem número e apoia a base em "SSA SSPTW 2018". O correto é **Lei nº 26/1991** (alterada pela Lei 16/2008), arts. 2, 14, 15, 27, 49, 50.
8. **WTC l. 307–308 (adições YE sem código):** transporte e representação = "Excluded from the GCSS/SI covered base", o que contradiz as linhas globais 62510–62523 e o CCG 5.1.1. A l. 307 ainda manda o excesso de transporte para 15% flat, contra a l. 210 (tabela de residente). Avaliar remover ou alinhar.
9. **YE-SSF-001 E-12:** "pro-rated by Days Worked ÷ 30" diverge do art. 14. O retorno mensal deveria levar o salário de contribuição anual (janeiro).
10. **DD:** falta um campo de **salário de contribuição GCSS (janeiro / admissão)** para guardar a base travada. O campo que o ticket cita não existe no YE-DD-001.

## Rascunho de resposta (EN)
> Para a @evats/wgomes revisar. **Não postar sem o ok do usuário.**

```
Hi @abagwan, @srai,

Under the Yemen Social Insurance Law No. 26 of 1991 (as amended by Law 16/2008), published by GCSS:

a) Basic-only is not acceptable. The contribution wage (Art. 2) is basic salary plus allowances; GCSS specifies "allowances of a permanent and stable nature" and excludes only overtime, grants and incentive bonuses. The January point is correct: Art. 14(1) — contributions are calculated on the wages received in January of each year, even if wages rise or fall during the year. So the base is the January wage (basic + fixed allowances such as housing and transport), locked January–December and reset each January.

d) Joiners after January: base = full wage of the joining month until the next January (Art. 14(2)) — no proration. Leavers: no contribution is due for the month in which service ends, regardless of days worked (Art. 15(2)). Unpaid absence deductions do not reduce the base (Art. 15(1)); during formal unpaid leave contributions are suspended unless the employee elects, in writing to GCSS, to pay both shares (Art. 50(3)).

e) No — transport, as a fixed monthly allowance, stays in the base.

On your question: the law requires the January-based annual base, not a monthly recalculation. Our YE-CCG-001 / YE-WTC-001 will be aligned accordingly.

Source: GCSS — Law 26/1991 Arts. 2, 14, 15, 50 (https://gcss-yemen.org/قانون-اللتأمينات/) and "Mandatory insurance" page (https://gcss-yemen.org/التأمين-الإلزامي-لصاحب-العمل/).
```

(f) fica fora da resposta porque não foi pedido a nós. Se o usuário quiser mencionar, uma linha: "Note: Art. 27 also provides a 4% employer work-injury contribution; please confirm with the client whether GCSS assesses it.")

## O que precisa ser feito
| # | Ação | Quem | Urgência |
|---|---|---|---|
| 1 | Revisar e aprovar o rascunho acima; postar como comentário (draft → ok do usuário) | Usuário (wgomes) → janela Suporte | **Hoje**: trava a UAT |
| 2 | Configuração: base SS **anual de janeiro** por empregado (basic + housing + transport de janeiro), travada no ano; admitidos com o salário integral do mês de admissão; **zero no mês da saída**; sem redução por faltas não remuneradas; licença sem remuneração = suspensão (ou opção do empregado). O Suman disse que hoje não existe base fixa (b): avaliar campo/intermediário (ex.: 58550 "Social Security Base") alimentado pelo valor de janeiro. Reprocessar janeiro/2026 (em janeiro, a base de janeiro coincide com o mês, então a diferença de jan vem da regra de transporte e dos números do cliente, não do travamento). | Suman / config Mercans | Alta, antes da UAT |
| 3 | Pedir ao cliente o **salário registrado no GCSS** (demonstrativo de janeiro entregue ao GCSS) para conciliar a diferença do Issues_Log #3. A base implícita do cliente é menor que o basic atual. | Aasim / cliente | Alta |
| 4 | Corrigir o **YE-CCG-001**: Step 2, 5.1.1, 5.2 (base de janeiro, admissão, saída, licença, piso, prazo) e o "work injury"; tirar as frases de "reviewed payroll"; citar a Lei 26/1991 | Compliance (pipeline / dono do artefato), com ok do usuário | Média (depois da resposta) |
| 5 | Corrigir o **YE-WTC-001**: l. 307–308 (transporte/representação "No" e tratamento de imposto) | Compliance | Média |
| 6 | **YE-DD-001**: avaliar campo "GCSS Contribution Wage (January / on joining)"; **YE-SSF-001** E-12 sem proporcionalização | Compliance | Média |
| 7 | Registrar no cérebro (fecha a sessão): `correcoes.md` (base mensal × janeiro; mês de saída; transporte contraditório no WTC) e criar o hub `paises/Iemen.md` | Janela Suporte / geral | Na sessão |
| 8 | Confirmar com o cliente se o GCSS cobra os **4% de acidente de trabalho** (art. 27) | Aasim / cliente | Baixa–média |

## Lacunas
- ⚠️ **Decisão ministerial / regulamento executivo** da Lei 26/1991 (lista de allowances do art. 2, art. 26 "a regulamentação organiza o cálculo das contribuições"): não localizados. A inclusão do transporte apoia-se na página oficial do GCSS ("allowances de caráter permanente e estável") e na ausência de exclusão no art. 2.
- ⚠️ **Mês de admissão:** se a contribuição desse mês é sobre o salário integral ou só sobre os dias. O art. 14(2) fala em "الأجر الكامل"; o regulamento não foi lido.
- ⚠️ **4% de acidente de trabalho:** previsto na lei (arts. 6, 27), não citado na página do GCSS; aplicação prática não confirmada.
- ⚠️ **Alterações posteriores a 2008** (ex.: em Sanaa × Aden): a compilação do GCSS-Aden só mostra a Lei 16/2008. Não verifiquei se a administração de Sanaa aplica algo diferente.
- ⚠️ **Allowance variável** (ex.: transporte que muda no ano): pela lei vale o valor de janeiro; a definição de "permanente e estável" para casos limite não foi localizada.
- **Origem do campo "SI Insured / Contractual Wage"** citado no ticket: não está no YE-DD-001 (export de 22/10 e versão _AI).
- **Autor/data das frases "reviewed payroll"** no CCG e mudança de 22/10 08:24 no Doc: ver o histórico de versões do Google Doc (não acessível pelo disco).
- "Book1.xlsx" (comparação do basic de janeiro) não está nos anexos baixados.
- A transcrição do árabe foi feita da imagem digitalizada (PDF sem camada de texto); conferir as citações no PDF antes de usar literalmente.
