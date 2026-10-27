# Dinamarca — comentários da Ruchi no CCG V2.3.8 (Holiday Pay na rescisão) — 2026-10-22

Pedido: Manju (chat STG Denmark, 22/10 07:00) — assumir na ausência da Enaakshi (volta segunda). Ruchi 07:15 + 3 avisos do Drive.
Base já decidida: HRBS-15410 (Resolved 15/10) — `raw/tickets/api/2026-10-22/HRBS-15410.md`.
Material: `raw/chats/2026-10-22-mencoes-do-dia.md`. Nada postado.

## Fontes (lidas em 22/10)
- Ferieloven, LBK nr 152 af 20/02/2024 (gældende) — `raw/docs/oficiais/DK/2026-10-22-ferieloven-LBK-152-2024.pdf`. Única alteração posterior: LOV 715/2025, só § 44 (`...-LOV-715-2025-aendring-ferieloven.pdf`).
- Exposição de motivos: 2017/1 LSF 116 (Forslag til lov om ferie) — `raw/docs/oficiais/DK/2026-10-22-LSF-116-2017-18-forslag-lov-om-ferie.pdf`.

| Regra | Texto |
|---|---|
| § 15 stk. 3 | Férias **sem** pagamento (dias não acumulados): desconta 4,8% do salário mensal por dia. |
| § 16 stk. 1 | Mensalista: salário durante as férias + ferietillæg de 1% do salário. |
| § 16 stk. 4 | Quem se desliga recebe feriegodtgørelse (§ 19, 12,5%) pela férias paga acumulada **e não gozada**. |
| LSF 116, Til § 16 stk. 4 | "beregne feriegodtgørelsen ud fra lønnen i det eller de relevante ferieår og afregne en **forholdsmæssig andel** heraf i forhold til den optjente og afholdte ferie." |
| § 18 | 1% calculado como a feriegodtgørelse (§ 19); pago no início da férias correspondente ou em maio/agosto; pago não se pede de volta. |
| LSF 116, Til § 18 | No modelo "ao gozar": apurar o 1% acumulado e pagar "den andel, der svarer til den planlagte ferie". |
| § 19 stk. 4 | Não se calcula feriegodtgørelse/ferietillæg sobre feriegodtgørelse, **løn under ferie** ou ferietillæg. |

## [a] — base reduzida pelos dias pagos × 1% dos dias gozados
Pergunta: os dias que reduzem a base são os mesmos que recebem o 1% na rescisão?
Resposta: sim. São os dias de férias gozados com salário: o salário desses dias (løn under ferie) sai da base (§ 19 stk. 4), e são esses dias que dão direito ao 1% (§ 16 stk. 1; § 18). Na rescisão, paga-se o 1% só dos dias gozados ainda não suplementados (o já pago em maio/agosto não volta, § 18). Os dias não gozados vão a 12,5% (§ 16 stk. 4).
⚠️ Fora da resposta: o valor 4,8% por dia **pago** é convenção do CCG; a lei fixa 4,8% só para dia **sem** pagamento (§ 15 stk. 3). A lei não fixa o valor do løn under ferie por dia para mensalista.

> Yes, the same days: holiday taken with pay. Salary paid for those days is excluded from the base (Ferieloven § 19(4)). On termination, untaken days are settled at 12.5% (§ 16(4)), so the 1% is paid only for taken days not yet supplemented (HRBS-15410); a supplement already paid, e.g. in May/August, cannot be reclaimed (§ 18).

## Versões curtas (com as sugestões aplicadas no CCG)
- [b] > Agreed, suggested in the text: Step 7 drops the 1% accrual for the termination month (HRBS-15410; § 16(4)).
- [e] > Yojana is right: per § 16(4) and the bill's remarks (LSF 116), the 12.5% is settled as a proportional share for the untaken days. Example with 10 days taken suggested below the Version 2 table: DKK 24,804.49 gross to FerieKonto, plus the 1% for the taken days if not yet paid (DKK 2,275.64).

## [b] — Cenário C, passo 7 (1% acumulado no mês da saída)
Procede: o exemplo contradiz o HRBS-15410 e o § 16 stk. 4 (o salário do mês da saída vira 12,5% dos dias não gozados). Correção de texto do CCG — tratar depois (decisão do usuário: comentar × V2.3.9).

> Agreed. Per HRBS-15410 there is no new 1% accrual in the termination month, in line with Ferieloven § 16(4): untaken days are settled at 12.5%, and the 1% is paid only for taken days not yet supplemented. Step 7 should drop the 1% accrual.

## [e] — provisão bruta quando houve férias gozadas
Procede (Yojana tem razão): a lei manda pagar parte proporcional (LSF 116, Til § 16 stk. 4).

Exemplo (mesmos números do CCG, Versão 2: salário DKK 50.000, set/2025–mai/2026, 10 dias gozados; redução de 4,8%/dia conforme o próprio CCG):
| Passo | Cálculo | DKK |
|---|---|---|
| Salário no ano de férias | 9 × 50.000 | 450.000 |
| Menos salário das férias gozadas (§ 19 stk. 4) | 10 × 4,8% × 50.000 | −24.000 |
| Base | | 426.000 |
| 12,5% | 426.000 × 12,5% | 53.250 |
| Dias acumulados / não gozados | 9 × 2,08 = 18,72 / 18,72 − 10 = 8,72 | |
| Ao FerieKonto (bruto) | 53.250 × 8,72 / 18,72 | 24.804,49 |
| 1% dos 10 dias gozados, se ainda não pago | 426.000 × 1% × 10 / 18,72 | 2.275,64 |

> Yojana is right: the gross provision is prorated. Ferieloven § 16(4) gives 12.5% only for earned holiday not taken, and the bill's remarks (LSF 116, note to § 16(4)) say the employer calculates it on the holiday-year salary and settles a proportional share relative to the holiday earned and taken ("afregne en forholdsmæssig andel heraf i forhold til den optjente og afholdte ferie"). Example, same figures as Version 2 with 10 days taken. Salary paid for the 10 holiday days is taken out of the base (§ 19(4)); the CCG values it at 4.8% per day: base 9 × 50,000 − 10 × 4.8% × 50,000 = 426,000; 12.5% = 53,250; earned 18.72 days, untaken 8.72; gross to FerieKonto = 53,250 × 8.72 / 18.72 = DKK 24,804.49 (then AM-bidrag and A-tax as in the table). The 1% for the 10 taken days, if not yet paid: 426,000 × 1% × 10 / 18.72 = DKK 2,275.64.
