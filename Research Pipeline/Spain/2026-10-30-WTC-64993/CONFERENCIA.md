# WTC Espanha — 64993 Contractual Extra Pay (proposta V4.9) — 2026-10-30

> Hub: [[Espanha]] · Correções: [[correcoes]] · Ticket: HRBS-16407 (STG) · Espanha ativa → regra 9 (ticket ao Development via Lily). **Proposta; nada gravado no Drive, ticket ou monday.**

## Base
- WTC vigente: **V4.8** (Google Sheet 1RWOFryO4nK7sdq3WQ19-bSNxdtnmdQqddv15xhZuyZQ, mesma planilha da V4.7, renomeada em 30/10 10:07; Version Control 4.8 = "29-Oct-26, Added formula for 62520", Lily Li). Lida no Chrome (gviz, 30/10).
- Export local mais recente: `Downloads\Spain Wage Type Catalogue V4.7.xlsx` (23/10). A V4.8 não foi exportada.

## Antes (V4.8)
| Código | Nome | Categoria | Formula |
|---|---|---|---|
| 64993 | Contractual Extra Pay | Notional | `$62100.amount` |
| 64556 | Prorated Extras (provisão) | Notional | `58214 × (64440 ÷ 6) ÷ 63957 × 63956` (2 extras; ÷ 4 com 58209 = 1; dias SS 63953/63952 quando 58239 > 7) |

## Problema
1. `$62100.amount` dá zero quando o cliente não lança o 62100 e informa o salário por 64430/64440 (Vaishnavi, call 30/10, `raw/reunioes/2026-10-30-STG-spain-extras-seguro-call.txt` l. 33–39).
2. A paga extra fica fixa no salário-base, contra o CCG ("The composition must be configurable per pay group; it cannot be hard-coded to base salary", seção "Composition of the Gratificación Extraordinaria", export da v1.6 de 29/10, par. 179–180; ET art. 31).
3. Provisão (64556/58140, sobre 64440) e paga (64993, sobre 62100) usam bases diferentes: o que entra na base de SS mês a mês não é o que se paga em junho/dezembro.
4. Já apontado por nós em 16/09 (`raw/reunioes/2026-09-16-spain-regulation-connect.txt` l. 177 e l. 198): "64993 cannot be hardcoded to basic salary"; regra: **64993 × nº de extras = 58140 × 12**; "we cannot use just monthly salary" (64440 pode trazer o rateio das extras, ex.: 62147 "Pro-rated Extra Payment", que é "Part of 64440").

## Depois (proposta V4.9)
| Código | Formula proposta | Por quê |
|---|---|---|
| 64993 | `58140 × 12 ÷ nº de extras` (nº = 2; 3 quando 58209 = 1) | mesma base da provisão; não depende do 62100; regra de 16/09 |
| 64993 (entidade) | override quando o convênio define outra composição (ex.: STG: `62100 + 62182`) | CCG: configurável por pay group (ET art. 31) |

## A confirmar com a Lily antes do ticket
- O 58140 do mês do pagamento tem os fatores de dias (63956/63957, 58214); para admitido/desligado ou mês incompleto, `58140 × 12 ÷ n` não é a soma das provisões do período de devengo. Pode ser preciso usar a soma do 58140 no período (campos "Extra Pay Month (Accrual Month)", HRBS-10563).
- Para quem recebe as extras rateadas no mês (62147 dentro do 64440), conferir que 64440 ÷ 6 não inclui o próprio rateio (16/09: "64440 already carries the prorated extras… would inflate").

## Conferência
- 64993 e 64556 lidos na V4.8 (30/10). Regra de 16/09 e problema 1 relidos nas transcrições (linhas citadas).
- Conta (2 extras, mês cheio, 58214 = 1): 58140 = 64440 ÷ 6 → 64993 = 64440 ÷ 6 × 12 ÷ 2 = 64440. Exemplo STG (EE do HRBS-16407): 2.400,31 ÷ 6 = 400,05 → 400,05 × 12 ÷ 2 = 2.400,30 (arredondamento de 0,01).

## Frentes que mexeram
| Data | Frente | O quê |
|---|---|---|
| 2026-10-30 | chat | proposta e rascunho do ticket ao Dev (`ticket-dev.md`); pedido da janela geral |
| 2026-11-02 | chat | **Proposta suspensa:** Lily (chat STG 02/11 3:37) diz que o 64993 está descontinuado para o annual gross (que já usa 58140×12÷nº extras); antiguidade da STG via 64556 por entidade (HRBS-16407, 02/11 10:15). Ticket ao Dev não deve ser aberto sem reconfirmar se algum cálculo ainda usa o 64993. |
