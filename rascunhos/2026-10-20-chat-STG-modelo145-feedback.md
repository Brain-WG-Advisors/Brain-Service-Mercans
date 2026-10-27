# Chat STG Spain — 2º retorno do cliente sobre o ESS do Modelo 145 (análise + rascunho, não enviado)

> Janela geral, 2026-10-20 (a frente Chat estava ocupada). Fonte: `raw/chats/2026-10-20-stg-spain-modelo145-feedback-cliente.md`.
> Base: Modelo 145 oficial (`raw/docs/oficiais/ES/2026-10-19-modelo145.pdf`), DD V5.0 (`Research Pipeline/Spain/2026-10-19-modelo145-x-DD/`), matriz do 145.

## Análise ponto a ponto
| # | Pedido do cliente | O que o 145 diz | DD V5.0 hoje | Posição |
|---|---|---|---|---|
| 1 | Situação familiar: lista com 1/2/3 | três casillas com texto longo | mapper "Family Situation Codes" 1/2/3 já tem o texto completo EN/ES | ✅ Concordar. Usar o texto do mapper na lista. |
| 2 | NIF só se escolher 2; nome "Spouse", não "Related Person" | "NIF del cónyuge (si ha marcado la casilla 2…)" | CM "If family situation requires related person identification"; label local "NIF Cónyuge/Pareja" | ✅ Concordar. Ajustar a condição para "= 2" e o nome para Spouse NIF / NIF del cónyuge ("Pareja" não está no form). |
| 3 / 9 | Discapacidade: lista de 3 opções com texto; sem "código" | grau ≥33% e <65% / ≥65% + casilla separada "ayuda de terceras personas o movilidad reducida" | mapper "Disability Codes" com 4 valores (0, 1, 2 = 33–65% com ajuda, 3 = ≥65%) **e** flag separada de ajuda: a ajuda aparece duas vezes | ✅ Concordar. No ESS: Sem / ≥33% e <65% / ≥65% + a caixa de ajuda separada, como no form. O código do 190 pode ser derivado (⚠️ conferir regra no desenho do 190 antes de afirmar). |
| 4 | Data da mobilidade: texto do form | texto citado pelo cliente (idêntico ao PDF) | campo existe (#14) sem o texto oficial | ✅ Concordar. Texto oficial como ajuda do campo. |
| 5 | Rendimentos irregulares: texto do form | texto citado pelo cliente (idêntico ao PDF) | campo existe (#13) | ✅ Concordar. Texto oficial como ajuda. |
| 6 | Descendentes e ascendentes: texto do cabeçalho | descendentes: "Datos de los hijos… 8.000 euros"; ascendentes: "Datos de los ascendientes mayores de 65 años… durante, al menos, la mitad del año… 8.000 euros" | sem texto | ✅ Concordar. Os dois textos como ajuda dos sub-grupos. |
| 7 | 10 filhos bastam (eles têm no máximo 4) | sem limite; "adjunte otro ejemplar" a partir do 5º | 16 (teto do serviço AEAT, XSD maxOccurs=16) | ⚖️ Não é exigência legal. O DD é do país (todos os clientes); sugestão: manter 16 no DD e o ESS mostrar novos blocos só quando preenchidos. **Decisão do usuário.** |
| 8 | Ordem: ano primeiro, depois discapacidade | ordem do form: ano de nascimento, ano de adoção, cómputo por entero, discapacidade, ajuda | ordinais: Disability 1, Ajuda 2, Cómputo 3, Ano 4, Adoção 17–20 | ✅ Concordar. Exige renumerar ordinais existentes (em 19/10 o usuário escolheu "só acrescentar"). **Decisão do usuário.** |
| 10 | "Tax card" fácil e com o texto do form | — | — | Apresentação no ESS é da implementação (Nihita/Lily); o nosso lado é o DD: rótulos, opções, ordem e textos oficiais. |
| — | (pendente de 19/10) ESS Read × Write | o form é do empregado | MSS Write / ESS Read | O retorno confirma que o empregado preenche → ESS Write. Pedir confirmação à Nihita. |

## Entrega (feita em 20/10, decisões delegadas pelo usuário)
DD **V5.1** pronto e conferido: `Research Pipeline/Spain/2026-10-20-modelo145-ESS-STG/` (CONFERENCIA.md, md5 7c9f5953…8d30). Não está no Drive.

## Rascunho para o chat (EN) — versão objetiva, colocada como rascunho no chat STG (não enviada)
Hi Nihita, I checked STG's comments against the official Modelo 145 and updated the DD to v5.1 (Drive > Spain > 02 - DD, changes in light orange, internal codes unchanged):

1. Family Situation: the 3 options now have the official form text. "Related Person NIF" is now "Spouse NIF", required only for option 2.
2. Disability: 3 options as on the form (none / 33% to below 65% / 65% or more) plus the assistance/reduced mobility box, valid only for 33%-65%. Code 2 should not be shown to employees; payroll derives it for Modelo 190.
3. Official form wording added as help text to the form fields and to the Descendants/Ascendants headers.
4. Child and ascendant fields now follow the form order.
5. We keep 16 children: the law has no limit, the AEAT service accepts 16, and the DD serves all clients. Can the ESS show extra child blocks only when needed? Then STG would normally see up to 4.

Question: since employees fill this in, should the group be ESS = Write? Today it is Read.
