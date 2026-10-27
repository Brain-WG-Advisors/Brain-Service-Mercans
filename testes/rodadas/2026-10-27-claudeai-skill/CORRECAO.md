# Correção da rodada 3: claude.ai + skill brain-service (2026-10-27)

- Gabarito e critérios: [[testes/exatidao]] (seção "Gabarito" + "Revisão do gabarito (2026-10-27, depois da fonte primária)").
- Respostas: T-001-r1 … T-030-r1 nesta pasta (uma passada, claude.ai org Mercans, Opus 5.5 esforço Alto, skill brain-service v2 + skills Mercans, pesquisa de conectores desligada, web/memória/conversas anteriores no padrão da conta).
- Critério literal do gabarito, sem reinterpretar. T-001 e T-003 anuladas (não contam). T-024 corrigida pelo gabarito reescrito (✅ = isenção por mês até o mês do 25º aniversário inclusive + `$person.birth_date`).
- Colunas: **Erro conh.** = repetiu o erro conhecido do gabarito; **Conf./fonte** = a resposta declarou confiança e/ou fonte; **Cérebro** = disse que usou a skill brain-service ou citou hub/correções/pacote ("indireto" = fala em "snapshot", "reference pack", "recorded decisions" sem nomear).

## Resultado por pergunta

| # | Nota | Erro conh. | Justificativa (trecho) | Conf./fonte | Cérebro |
|---|---|---|---|---|---|
| T-001 | anulada | não (gabarito antigo) | "58184, 58186 and 58188, all under CRA concept 0054, type E" + 62983 0054/E; diz que 58197/58198 ficam só no BASES; aponta o conflito com o Manual CRA de 01/07/2026 (prorrata 12 meses, excesso = I) como decisão de design pendente | sim (~70%, Table 84/SR-81) | sim, indireto ("my snapshot") |
| T-002 | ✅ | não | "TRL = *Tipo de Relación Laboral*"; diz que "Tipo de Riesgo Laboral" foi o erro corrigido na SR-80 | sim (SR-80, schema TGSS) | sim, indireto ("reference pack"); cita o achado B55/L55 do hub |
| T-003 | anulada | — | 79432 = L.27; 79429/79430 = **B.01** com campo 394 = "1", porque a Orden HAC/1431/2025 restringiu B.03 desde 2025 (segue a revisão do gabarito); avisa que o WTC V4.4 ainda mapeia B.03 | sim (95% L.27 / 85% B.01, Diseños lógicos 2025) | não visível |
| T-004 | ✅ | não | "pad it on the right with zeros up to 7 digits … `3123` → `3123000`"; DD continua com 4 dígitos | sim (HRBS-13757, T90) | não visível |
| T-005 | ✅ | não | 1.989,30 / 1.649,70 / 1.435,20 / 1.424,40 €/mês e 47,48 €/dia; "Orden PJC/297/2026 … art. 3", desde 01/01/2026 | sim | não |
| T-006 | ✅ | não | "No, 65815 should not be mapped to Modelo 296 … Flexible Remuneration – Non-Taxable SS Subject"; removido na V3.4, publicado na WTC V3.5, sem mudança até a V4.7 | sim (~90%) | sim ("brain's correction log", "Spain hub") |
| T-007 | ✅ | não | 50% (até 3) / 60% (3–5) / 70% (5–8) / 100% (> 8); Lei 1105-XIV art. 17(1) | sim | não |
| T-008 | ✅ | não | "the 12 calendar months immediately preceding the month in which the incapacity began"; Res. 1266 p. 25 | sim | não |
| T-009 | ✅ | não | "**Yes.**"; Res. CMU 1170, seção II item 2: isenção só para seguro médico e de pensão | sim | não |
| T-010 | ✅ | não | "4DF income code 157, Mercans wage type 62942 … PIT: No. Military levy: No. ESV: No."; PKU p. 177.8 | sim | indireto ("two artifact defects are recorded") |
| T-011 | ✅ | não | "These values are not fixed. They depend on which DPS body each legal entity files with"; SPR_STI.XML; C_STI_ORIG = C_REG × 100 + C_RAJ | sim (наказ 729, SPR_STI 06.03.2026) | não |
| T-012 | ✅ | não | "J0510611 (version 11)"; "took legal effect on 17 July 2026" (DPS aplica desde 01/08) | sim (Ordem MF 243/2026) | não |
| T-013 | ❌ | sim (parcial: ARL) | "only the ARL (occupational) incapacity is exempt … Exempt, up to the legal minimum" (art. 206 num. 1, par. 1); doença comum e licenças tributáveis, com Oficio 027408/2019 | sim (Oficios 023438/2015, 36846/2015, 901191/2020) | não; cita a skill payroll-compliance-colombia (`02-wtc.md`) como desatualizada |
| T-014 | ✅ | não | "Salud: 4% of the IBC, deducted from the employee"; "FondoPension: not due" | sim | indireto ("our reference") |
| T-015 | ✅ | não | host "`https://depot.dpae-edi.urssaf.fr`" (URSSAF, não net-entreprises); "Format 120 flat file (TXT)" e "`FR_DUE_Upload` XML" | sim (SIR França, guia URSSAF NAT/5492) | não (skill França) |
| T-016 | ⚠️ | não | cita "v1.1 (one YTM step)" e 58121/58122/58123, mas propõe IUSC mensal em 4 passos (a–d) + flag e recomenda trocar o step YTM por `retro_`; não afirma "3 passos + 1 step YTM" como o design | sim (validou em Python; "not production-ready") | indireto ("decisions recorded as of 2026-10-27") |
| T-017 | ✅ | não | "exempt up to **30% of base monthly salary**" (CGI 45-13°); CNPS: "Any excess is included in the base" | sim (com ressalva da fonte CNPS) | não (CCG/artefatos do Chade) |
| T-018 | ❌ | sim | "don't use the default single Differential regulation. Use the RPN-driven **Threshold → Base → Amount triplet**"; trata a Irlanda como exceção à regra | sim ("couldn't open CT-A-192") | indireto ("recorded IE design decisions") |
| T-019 | ✅ | não | "75,000 XOF per month … Retirement: 3,375,000 XOF per month"; Communiqué CNPS jan/2023 + Décret 2022-986 | sim | não |
| T-020 | ✅ | não | "Whk total = 1.45 % (WGA 0.91 % + ZW-flex 0.54 %)" | sim (UWV/Cijferbijlage; diz que o Handboek não imprime a taxa) | não (skill NL) |
| T-021 | ✅ | não | "withhold **1,000 XAF per month**"; Loi 34-2013 art. 14 reescrito pela Loi 48-2014 art. 8 | sim | não |
| T-022 | ✅ | não | "Employee deductions: Global 21100–21900. Employer contributions: Global 23640–23673 … 59 codes" | sim (conferiu 54 + 5 no Global WTC Coverage da França) | sim ("brain correction log and the Gabon hub") |
| T-023 | ✅ | não | "**5% employee and 3% employer**" | sim (GB pack `01-ccg.md` §8.2, `05-data-dictionary.md` §6.2) | não (skill GB) |
| T-024 | ✅ | não | isenção "by **month**, up to and including the month in which the employee turns 25" (Szja 29/F (3), NAV nº 73) + "`$person.birth_date`"; rejeita end_date e `$employee.years_worked` | sim (alta na regra, média na sintaxe) | sim ("superseded by the 2026-10-27 correction") |
| T-025 | ✅ | não | "each period's deduction is the lesser of the remaining annual maximum and the normal rate … never … 'annual maximum ÷ 12'" | sim (T4127) | indireto ("reference pack") |
| T-026 | ✅ | não | "**52560** holds the TZPB rate"; "Don't use **52980**" | sim (~85%) | sim ("brain snapshot", "corrections log and the Bulgaria hub") |
| T-027 | ✅ | não | GPM313 afetados "must be corrected too"; GPM312 = "newly completed declaration … not a delta" | sim (Aprašas VA-121; seminário VMI) | não |
| T-028 | ⚠️ | não | "Yes, it applies"; "The employee"; base: cita "total monthly salary" (Circular MF 14/2021) mas conclui que a base operativa é "basic disbursements only" (FAQ ETA v4 Q110) | sim | indireto (WTC EG-8003 "left over from before the 22 Oct 2026 correction") |
| T-029 | ✅ | não | "**19.88%** … from Q1 2018"; "about 25.00%"; (19,88 × 0,0427) + 4,27 = 5,12% | sim (instruções ONSS via WTC v1.3/CCG) | não |
| T-030 | ✅ | não | 50%/100% do prêmio; 15% mensal "not cumulative"; teto anual TRY 312.066 "cumulative"; "lower of the 15% amount and the remaining annual headroom" | sim (GİB Yayın 597) | não |

## Nota

**24/28 ✅ · 2 ⚠️ (T-016, T-028) · 2 ❌ (T-013, T-018)** (T-001 e T-003 anuladas).

Erro conhecido repetido: T-018 (inteiro) e T-013 (parcial, só ARL). As duas anuladas seguem a revisão do gabarito (T-001 cita o conflito com o Manual CRA; T-003 responde B.01 pela Orden HAC/1431/2025).

## Comparação

| Rodada | Configuração | Nota sobre 28 | ⚠️ | ❌ |
|---|---|---|---|---|
| 1 | claude.ai sem skill brain-service | 20/28 | 5: T-010, T-016, T-017, T-018, T-024 | 3: T-006, T-022, T-026 |
| 2 | Claude Code + cérebro (livro aberto) | 28/28 | 0 | 0 |
| **3** | **claude.ai + skill brain-service** | **24/28** | **2: T-016, T-028** | **2: T-013, T-018** |

- **Melhorou vs. rodada 1:** as 3 ❌ por falta de material interno (T-006, T-022, T-026) e três ⚠️ (T-010, T-017, T-024) viraram ✅. O pacote do cérebro supriu o WTC (65815), o Global WTC (21100–21900 / 23640–23673), o KB Bulgária (52560), o WT 62942, a base CNPS do Chade e a regra do mês + `$person.birth_date` da Hungria.
- **Piorou vs. rodada 1:** T-013 (✅ → ❌) e T-018 (⚠️ → ❌). T-028 (✅ → ⚠️).
- **Igual:** T-016 (⚠️).
- **Vs. rodada 2:** 4 abaixo. As 4 que falham aqui foram ✅ no Claude Code.

## O que ainda falha e causa provável

| # | Nota | O que errou | Causa provável |
|---|---|---|---|
| T-018 | ❌ | Recomenda o triplet Threshold/Base/Amount para a Irlanda | **Pacote ambíguo.** O `Irlanda.md` do pacote traz ao mesmo tempo "decompor … era específico do RPN; usar uma reg `Differential`" e "Padrão de design IE: … triplet; regs Paid", e o `design.md` diz "decomposição … que era específica do RPN (IE)". O modelo leu "específico do RPN" como "certo para a Irlanda". Conferir na fonte (T-2026-07-02, DevKB) se a correção vale para a Irlanda ou só para os outros países. Se valer para a Irlanda, reescrever a linha do hub (tirar "triplet" do padrão IE). Se não valer, o gabarito da T-018 está errado. |
| T-013 | ❌ | Diz que a incapacidade ARL é isenta até o mínimo legal (art. 206 num. 1 + par. 1) | **Leu errado / sobrepôs a correção.** A correção (linha 91, DIAN Oficio 27408) está no pacote (`correcoes.md` e `Colombia.md`), mas o modelo pesquisou na web e deu mais peso aos Oficios 023438/2015 e 36846/2015 para a ARL. A skill payroll-compliance-colombia ainda marca licenças como isentas (pendência "Levar à skill" aberta no hub), o que reforça a dúvida. Ação: levar a correção à skill do país e deixar explícito no hub que a ARL também é tributável (ou rever o gabarito na fonte, já que o ET 206 num. 1 cita acidente de trabalho). |
| T-016 | ⚠️ | Conhece o v1.1 (58121/58122/58123, 1 step YTM), mas propõe 4 passos e trocar o YTM por `retro_` | **Fora da skill / comportamento do modelo.** O dado está no pacote (`Chile.md` linhas 108 e 134), mas a pergunta "how should … be structured" levou a um redesenho, o mesmo padrão registrado em `design.md` ("redesign completo proposto onde bastava fix pontual"). A skill brain-service não manda responder pelo design registrado antes de propor outro. |
| T-028 | ⚠️ | Conclui que a base é só a remuneração básica (FAQ ETA v4 Q110), não o salário mensal total | **Fonte nova fora do pacote.** O pacote/correção dá "salário mensal total"; a resposta cita a Circular MF 14/2021 (total) e uma FAQ da ETA de mar/2026 (básico) e escolhe a FAQ. Vale conferir a FAQ ETA v4 Q110 antes de manter o gabarito. A resposta também acha a linha EG-8003 do WTC ainda com o texto antigo (achado fora do pedido para o hub do [[Egito]]). |

## Observações

- 2 das 4 falhas (T-018 e T-028) podem ser problema de gabarito ou de pacote, não do modelo: decidir na fonte antes de agir.
- Pesquisa em conversas anteriores e memória continuaram ativas: as respostas podem ter lido as rodadas 1 e 2 (ex.: T-002 cita "spotted in today's accuracy test"; T-024 cita a correção de 2026-10-27). Medição não é cega.
- Achados fora do pedido trazidos pelas respostas: WTC ES V4.4 com 79429/79430 ainda em B.03 (T-003); skill CO `02-wtc.md` com licenças isentas (T-013); TFE-001 do Chade com transporte na base (T-017); CCG Canadá Example D com PM = 6 para admissão em julho (T-025); WTC EG-8003 com texto antigo (T-028); skill NL §4.3 / QA U1 com linha deslocada (T-020).
