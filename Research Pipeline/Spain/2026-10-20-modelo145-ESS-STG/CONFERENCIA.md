# CONFERÊNCIA — DD Espanha V5.1 (2º retorno da STG sobre o ESS do Modelo 145)

## Pedido
Chat STG (20/10, 11:41): a cliente pede que a tela do ESS siga o Modelo 145: listas com o texto oficial, NIF só na situação 2 e com o nome "cónyuge", discapacidade em 3 opções, textos do formulário, ordem do formulário e 10 filhos em vez de 16. Fonte: `raw/chats/2026-10-20-stg-spain-modelo145-feedback-cliente.md`. Análise: `rascunhos/2026-10-20-chat-STG-modelo145-feedback.md`.
O usuário delegou as decisões com base na fonte oficial (20/10).

## Entradas
- Base: `../2026-10-19-modelo145-x-DD/Spain_Data_Dictionary_V5.0.xlsx` (md5 9f83bb035ed615d5fe0131a8105d57ac), a mesma copiada ao Drive e importada como `Spain_Data_Dictionary_V5.0.gsheet` em 20/10 às 09:45. As exports `Downloads\Spain_Data_Dictionary_V5_0*.xlsx` são de 14/09 (outra linhagem) e não foram usadas.
- Fontes (`raw/docs/oficiais/ES/`): Modelo 145 (`2026-10-19-modelo145.pdf`), algoritmo AEAT 2026 (validações 4, 5, 8, 15, 17), `AEATRetenciones2026.xsd` (Descendiente maxOccurs=16; ordem Nacimiento, Adopcion, ComputadoEntero, Discapacidad; Ascendiente: Nacimiento, Convivencia, Discapacidad), desenho do 190 (pos. 167, códigos 0–3), LIRPF art. 58.1 e art. 60 (consolidada BOE).

## Decisões (com fonte)
| Ponto do cliente | Decisão | Fonte |
|---|---|---|
| Situação familiar com o texto completo | Textos do mapper "Family Situation Codes" trocados pelo texto oficial do 145 (ES) e tradução fiel (EN) | Modelo 145, seção 1 |
| NIF só na opção 2, nome "cónyuge" | Field Name "Spouse NIF", label "NIF del cónyuge", CM "If Family Situation = 2", descrição com a regra. Código interno `$hr.related_person_nif` mantido | 145 seção 1; algoritmo AEAT, validações 4 e 5 |
| Discapacidade em 3 opções, sem código | ESS mostra 3 opções (chaves 0, 1, 3) + a caixa de ajuda separada; a chave 2 não aparece e é derivada (1 + ajuda = 2) para o 190. Textos do mapper "Disability Codes" no texto do form | 145; 190 pos. 167; XSD `tipo_Discapacidad` |
| (decorrente) caixa de ajuda | Só permitida com 33%–65%; com ≥65% os +3.000 já valem | algoritmo AEAT, validações 8, 15, 17; LIRPF art. 60 |
| Textos do formulário | Texto oficial do 145 como ajuda do ESS: mobilidade (flag e data), rendimentos irregulares, vivenda, pensão compensatória, anualidades, cómputo por entero, ano de adoção (nota 1), convivência dos ascendentes; cabeçalhos de Descendants e Ascendants nas notas do 1º campo de cada sub-grupo | Modelo 145, seções 1–5 |
| Ordem: ano primeiro | Ordinais na ordem do form: filho n = nascimento, adoção, cómputo por entero, discapacidade, ajuda (1–80); ascendente n = nascimento, convivência, discapacidade, ajuda (1–8). Linhas físicas não mudaram. Mesmos ordinais na aba oculta "Filteration for SaaS" (só as linhas que existem lá) | XSD AEAT; Modelo 145 |
| 10 filhos em vez de 16 | **Mantido 16** no DD (vale para todos os clientes). A lei não tem limite e o serviço AEAT aceita até 16. O ESS pode mostrar blocos extras só quando usados | LIRPF art. 58.1; XSD maxOccurs=16 |
| ESS Read × Write | Não alterado; pergunta à Nihita | — |

## Conferência
- `dd_v50_para_v51.py`: edição por XML, partes não tocadas copiadas byte a byte; células alteradas em **laranja claro FFFCE4D6** (as adições da V5.0 continuam em amarelo FFFFF2CC).
- `conferencia_v50_v51.py` (todas as 9 abas, valor e formato de cada célula): Country Fields 158 células alteradas, Country Option Mappers 14, Filteration for SaaS 16, Version Control +1 linha (5.1); demais abas 0. **0 problemas**: toda célula alterada está em laranja; nenhuma célula mudou de formato ou cor sem mudar de valor. Mesclagens iguais (67/67, 60/60, 2/2); zip íntegro.
- Ordinais: Employee Information 13 campos (1–14, o 8 vago como antes), Descendants 80 únicos (1–80), Ascendants 8 únicos (1–8).
- Final: `Spain_Data_Dictionary_V5.1.xlsx`, md5 **7c9f595333c96c028ed1a4c043d28d30**. Copiado ao Drive em `Spain\02 - DD\` com md5 idêntico (20/10, ok do usuário); antes, conferido pelo Chrome que a V5.0.gsheet não teve edição depois da importação (modificada 09:45). O usuário importa.

## Achado fora do pedido
- A aba oculta "Filteration for SaaS" não tem os 71 campos incluídos na V5.0 (só vai até Child 4 e não tem os campos novos de Employee Information/Ascendants). Não corrigido: o uso dessa aba não está documentado. Pergunta para a Lily.

## Histórico por frente
| Data | Frente | O quê |
|---|---|---|
| 2026-10-20 | Geral (frente Chat ocupada) | V5.1 criada e conferida como acima; decisões delegadas pelo usuário, tomadas com a fonte oficial. Não copiada ao Drive. |
| 2026-10-20 | Geral | Nihita respondeu no chat STG: "yes ESS should be write". **V5.2** a partir da V5.1 (`dd_v51_para_v52.py`): ESS = Write nos 98 campos do grupo declarados no Modelo 145; ficam ESS = Read os 3 que não estão no form: Perceptor Situation (SITUPER, definido pelo pagador; Alg AEAT dados de entrada), Disability Degree (%) (o form pede só a faixa) e Child Count (Total) (resulta dos filhos informados). Child 1-16 Birth Year marcados Form 145 = Yes (estavam vazios; "Año de nacimiento" está na seção 2). Células em amarelo FFFFE699; VC linha 5.2. Conferência `conferencia_v51_v52.py`: 114 células alteradas na Country Fields, demais abas 0, **0 problemas**. md5 9740e641e46ca9f072de12d15f84679c. Copiado ao Drive `Spain\02 - DD\` com md5 idêntico (ok do usuário, 20/10). Observação: Disability Degree (%) e Child Count (Total) têm Form 145 = Yes no DD (herdado), embora não sejam casillas do 145; não alterado. |
| 2026-10-20 | Geral | **Decisão do usuário: consolidar tudo do dia na V5.1** (a V5.2 deixa de valer). Nihita perguntou se o empregado precisa informar o Disability Degree (%) e se o Child Count (Total) é automático. `dd_v51_consolidar.py` sobre a V5.1 parcial: ESS = Write nos 98 campos do 145; Birth Year Form 145 = Yes; coluna Form 145 vazia em Disability Degree (%) e Child Count (Total) (não são casillas do 145); descrição do Child Count (Total) + "Must equal the number of children entered (Child 1-16). Derive automatically if possible; otherwise HR fills it in MSS. Not a box of Form 145, so ESS = Read."; linha 5.1 do VC com a descrição completa. Tudo em laranja claro FFFCE4D6. Conferência contra a V5.0 (`conferencia_v50_v51.py`): Country Fields 275, Option Mappers 14, Filteration for SaaS 16, VC +1 linha; **0 problemas**. Contra a V5.2: só X51, X52 e G52 diferentes (as 2 correções). Final **V5.1 consolidada**, md5 **a2a230bacd66e88ad2fec2279dce21e2**, copiada ao Drive `Spain\02 - DD\` com md5 idêntico. Arquivos anteriores em `_substituidos/` (V5.1 parcial md5 7c9f5953…, V5.2 md5 9740e641…). No Drive ficaram as planilhas Google V5.0, V5.1 e V5.2 (importadas pelo usuário às 16:57, 17:00 e 17:05): o usuário reimporta a V5.1 e decide o destino da V5.2. |
