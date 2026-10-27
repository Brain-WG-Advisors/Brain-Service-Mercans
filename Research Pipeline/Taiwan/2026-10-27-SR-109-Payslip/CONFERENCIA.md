# SR-109 Taiwan Payslip: spec v1.2 (CONFERENCIA)

> Tudo local. Nada foi para Drive, YouTrack, e-mail ou chat. Draft para o usuário revisar.
> Nenhum dado pessoal: o holerite de teste anexado ao ticket (dados reais) não foi lido nem copiado.

## Pedido
Mohit, 15/09/2026: "Spec Review only and fill the gaps in specs." Pontos herdados: overtime por tipo de dia (Lily, 28/11/2025) e versão em chinês (Brenet/Lisa, ago/2025). Análise de origem: `rascunhos/2026-10-23-shruti/SR-109-taiwan-payslip.md`.

## Arquivos
| Arquivo | md5 |
|---|---|
| Base: `raw/docs/drive-exports/2026-10-27/TW Payslip Specification.xlsx` (export de hoje, igual à de 23/10) | `1cbe1e44477b982032520e3d7c26efdc` |
| Final: `TW Payslip Specification_v1.2.xlsx` (esta pasta) | `d198bd28f8c0910e47572e42c47b0c1a` |
| `scripts/build_v12.py` | gera a v1.2 por cirurgia XML + zip (partes não alteradas byte a byte) |
| `scripts/compare_v12.py` → `comparacao-celula-a-celula.md` | conferência célula a célula + validação do pacote |
| `scripts/changes.json` | lista das 125 células escritas |
| `scripts/validate_workbook_v12.txt` | saída do `mercans-artifact-toolkit/validate_workbook.py` |
| `comentario.md` | rascunho do comentário (EN), não postado |

## Fontes (relidas por mim nesta sessão)
| # | Fonte | Arquivo | Uso |
|---|---|---|---|
| P1 | Labor Standards Act (勞動基準法), MOL | `raw/docs/oficiais/TW/2026-10-23-payslip-LSA-labor-standards-act-mol.html` | art. 23 (明細 com o pagamento; 工資清冊 5 anos), art. 24 (dia útil +1/3 até 2 h, +2/3 nas 2 h seguintes; 休息日 1⅓ até 2 h, 1⅔ depois), art. 32-1, art. 38, art. 39 (休假 trabalhado = dobro), art. 40, art. 79 (multa NT$20.000–1.000.000) |
| P2 | LSA Enforcement Rules (施行細則), MOL | `raw/docs/oficiais/TW/2026-10-23-payslip-LSA-enforcement-rules-mol.html` | art. 14-1: (1) 勞雇雙方議定之工資總額, (2) 工資各項目之給付金額, (3) deduções, (4) 實際發給之金額; §2 papel/eletrônico/acessível e imprimível |
| P3 | MOL 參考例 (anexo do ticket) | `raw/tickets/api/anexos/SR-109/20250807-0604 - 8. Pay slip勞動基準法第23條第1項-工資各項目計算方式明細-之參考例 (1).pdf` | modelos 1–3 (rótulos zh-TW, 倍率/時數, 約定薪資結構), notas 3–4 (休息日 >8 h 2⅔; 休假日 ≤8 h +1 dia, >8 h +1/3 e +2/3), nota 7 (modelo adaptável) |
| I1 | DD V3.3 | `raw/docs/drive-exports/2026-10-23/Taiwan Data Dictionary V3.3.xlsx` | `id_card_number` (ID Information, ordinal 8, rótulo 證件號碼); Country Fields sem endereço da entidade (só `$legal_entity_hr.post_code`), sem salário acordado, sem data de pagamento |
| I2 | WTC V2.8 | `raw/docs/drive-exports/2026-10-23/Taiwan WTC V2.8.xlsx` | PEs 62110/62111, 62120–62122, 62130–62132 (nomes com multiplicador); todos "Lump Sum", sem fórmula |
| I3 | Outras specs TW (export 2026-10-27) | Tax Report, SNHI, SI Join/Salary/Termination | usam `$hr.id_card_number`; SI Termination usa `$hr.passport_number` para não residentes |

## Decisões (o que entrou na v1.2)
| Item | Antes | Depois | Fonte |
|---|---|---|---|
| Agreed Total Wage (linha 23, M–U; exemplo F16/H16) | não existia | linha nova; mapeamento TO BE CONFIRMED BY MOHIT/BA (NEW DD FIELD proposto ou valor contratual); proposta: salário mensal contratado (base + adicionais fixos, antes de proporcionalização/ausência) | P2 art. 14-1(1); P3 modelo 2 |
| Payment Date (Q15) | vazio | TO BE CONFIRMED BY MOHIT/BA | P3 (發薪日期/入帳日期); DD sem campo |
| Employer Address (Q6) | vazio | TO BE CONFIRMED BY MOHIT/BA | DD só tem post code |
| National ID (Q12) | `$person.national_id` | `$hr.id_card_number`, opcional; fallback para estrangeiros TO BE CONFIRMED | I1, I3 |
| Total Gross / Total Deductions / Total ER (linhas 22, 30, 41) | sem linha | SUM das mesmas contas dos blocos | spec existente (Q18, Q28, Q39) |
| Overtime rate (linha 20) | — | multiplicador estático do nome do PE; exibição TO BE CONFIRMED | I2; P1 art. 24; P3 notas 3–4 |
| Overtime hours (linha 21) | — | TO BE CONFIRMED (PEs Lump Sum sem fórmula; se não houver horas, só valor) | I2 |
| Account currency / Account type (linhas 51–52) | só no exemplo | linhas novas, TO BE CONFIRMED | exemplo I63/K63 |
| Descrições | R/S vazias (TA/BA) | coluna nova **T "Field description - RA (v1.2)"**; R/S intocadas (são do TA/BA) | padrão da Tax Report Spec (coluna RA) |
| Idioma | — | coluna nova **U "Label zh-TW (proposed)"** só com rótulos tirados de P2/P3/DD; Report Matrix registra proposta bilíngue zh-TW + EN como decisão de produto TO BE CONFIRMED | P1 art. 23 e P2 art. 14-1 não fixam idioma; Lisa 08/08/2025 |
| Report Matrix | não existia | aba nova (layout da SNHI spec TW) | P1 arts. 23, 79; P2 art. 14-1 §2 |
| Version Control | vazia | linha 1.2 / 2026-10-27 / resumo / Draft / Wallisson Gomes | pedido |

Overtime por tipo de dia: faixas do WTC conferem com a fonte. Dia útil 1.33/1.67 = P1 art. 24 §1 (1)(2). Descanso 1.33/1.67 = P1 art. 24 §2; 2.67 (>8 h) = P3 nota 3 (a LSA, no texto lido, não traz o >8 h). Feriado 1 (≤8 h, +1 dia) e 1.33/1.67 (>8 h) = P3 nota 4 + P1 art. 39. Nada a mudar no mapeamento por faixa (62106:62999 cobre todos).

## TO BE CONFIRMED BY MOHIT/BA (na planilha)
1. Agreed Total Wage: variável/campo e definição (Q23, T23).
2. Payment Date: variável (Q15).
3. Employer Address: variável da entidade (Q6).
4. Overtime: exibir rate (Q20) e se o motor tem horas (Q21).
5. National ID: fallback para quem não tem ID card (T12).
6. Account currency / type (Q51, Q52).
7. Net Pay = Total Gross − Total Deductions para as contas de sistema (T37).
8. Report Matrix: encoding, file naming, currency (TWD), rounding, number format, idioma bilíngue.

## O que não consegui provar
- O sentido exato de "議定之工資總額" (salário contratado × total bruto acordado): P2 não define; a proposta é inferência a partir do modelo 2 do MOL e está marcada como tal.
- Se o motor guarda horas por PE de overtime.
- Variáveis core de endereço da entidade e data de pagamento (não estão no DD TW; o DD core não foi consultado).
- Rótulos zh-TW para campos sem rótulo em P2/P3/DD: deixados em branco na coluna U (o RA local preenche).
- `validate_workbook.py --artifact RSPEC` dá FAIL na base e na v1.2: o contrato é o "Spain 9-sheet" (não se aplica a esta spec de 3 abas), e os marcadores "TO BE CONFIRMED" são os pedidos de confirmação intencionais. Sem erros de fórmula.

## Conferência
- Célula a célula (valor + preenchimento, todas as abas): 125 diferenças, todas previstas e em `FFDDEBF7`; **nenhuma fora do escopo** (`comparacao-celula-a-celula.md`). Por aba: Version Control 5, Report Matrix 41 (aba nova), Spec 79 (só Q12 tinha valor antes; as outras 78 eram vazias).
- Pacote: 15 partes idênticas byte a byte; alteradas só `sheet1.xml`, `sheet2.xml`, `styles.xml`, `workbook.xml`, `workbook.xml.rels`, `[Content_Types].xml`; nova `sheet4.xml`. Todo XML bem formado; rels e content types íntegros; 183 cellXfs/9 fills coerentes; 142 merges sem sobreposição; abre no openpyxl. Desenhos, imagem, comentários e `person.xml` intactos.
- Destaque em `FFDDEBF7` (pedido). O comentário da Version Control diz "highlight changes in yellow": seguimos o padrão do cérebro; ajustar se o Mohit preferir.

## Achados fora do pedido (para o hub de Taiwan, não entram no ticket)
1. WTC V2.8 sem PE para: trabalho em 例假 / folga suspensa por emergência (dobro, P1 art. 40; também art. 24 §1(3)); horas de 補休 vencidas pagas em dinheiro (P1 art. 32-1; "屆期未補休折發工資" no P3).
2. PEs 62112–62119, 62123–62129, 62133–62139 continuam "Overtime" genérico; 62110 tem explicação "Overtime 1.34" × nome "1.33".
3. A faixa 65500:65859 inclui benefícios nocionais (ex.: 65508/65509, 65659): entram no Total Gross sem serem pagos em dinheiro.
4. Exemplo da spec: I34 `=SUM(I19:K21)` não soma as linhas de overtime do exemplo; "Personal Leave"/"Sick Leave" (B45/B46) no bloco de deduções sem PE correspondente no WTC (só 62109, earning). Não alterados.
5. Análise de 23/10 cita "art. 38 §4" para o registro de 特休 no 工資清冊: no texto lido é o **§5** (§4 é o pagamento dos dias não gozados). Corrigir no hub.
6. Teste do Jani (29/01/2026) foi numa entidade da Índia: retestar na entidade de Taiwan.
7. Opcional não aplicado: bloco de saldo de 特休/補休 (P3 備註; P1 art. 38 §5, art. 32-1).

## Histórico
| Data | Frente | O quê |
|---|---|---|
| 2026-10-27 | Suporte (construtor C) | v1.2 gerada da export de 27/10 (md5 1cbe1e44…); 125 células em azul-claro; Report Matrix nova; colunas RA e zh-TW; conferência célula a célula sem diferença fora do escopo; comentário EN rascunhado, nada postado |
