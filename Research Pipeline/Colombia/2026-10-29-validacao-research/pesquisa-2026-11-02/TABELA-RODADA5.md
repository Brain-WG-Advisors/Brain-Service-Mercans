# Rodada 5 — pesquisa dos resíduos (02/11/2026)

Ligada a [[CONFERENCIA]], [[TABELA-CONSOLIDADA]] e [[Colombia]]. Detalhe: [[LOTE-A-RETENCAO]], [[LOTE-B-SEGURIDADE]], [[LOTE-C-PRESTACOES-NE]]. Research CO **não** está em produção (usuário, 29/10) → versão nova, sem ticket ao Development (os relatórios dos lotes dizem o contrário; está errado).

## Muda os finais
| ID | Artefato | Como está | Como fica | Fonte primária | Conf. | Reaberta por mim |
|---|---|---|---|---|---|---|
| A-1 | WTC Tax Credit A41, A65–A68, Coverage C16(4); CCG P661, T91, T103, T105, T117, T169, T175, T180, T202, P768; specs 004 D22/D23, 001 C39 | Tetos 790 e 1.340 UVT aplicados como 1/12 por mês | Tetos anuais, controlados pelo acumulado do ano; exemplos T105 (4.994.989,65 → 3.947.554,80) e T180 (1.945.004,60 → 1.763.832,00) recalculados, com a premissa escrita | CE S4 rad. 24047 (28/10/2021) anulou "es decir 420 UVT mensuales" do DUR 1.2.4.1.6 par. 3; Decreto 2231/2023 art. 9 ("1.340 UVT anuales"); ET 336 num. 3 | 90% | Sim (sentença e decreto) |
| A-2 (F-13) | WTC P120:P122, P321:P322 (e N se N = retenção); CCG T86R4C2, T150R3C2, P722; specs 001 C22, 006 A37, 004 A34/D21/D34, 005 A34/C22 | Cesantías de não residente: retenção de 20% (ET 408) | Sem retenção na fonte para ninguém; 20% fica como opção configurável conservadora | Ley 100 art. 135 par. 3 ("En ningún caso ... cesantía ... retención en la fuente"); DUR 1.2.4.1.11; DIAN Oficios 8899/2015 e 4358/2019 | 80% | Sim (os dois ofícios) |
| SIM-07 | Spec 004 A26/C26/A34; 005 A28/C28/A35 | Média da casilla 59 = 13.000.000 | 12.000.000 (6 meses do ano anterior à consignação, só salário, sem prima) | Instrutivo Form. 220 (Res. DIAN 22/2024), casilla 59, caso (ii); DIAN Concepto 1302/2019 | 88% | Sim (instrutivo) |
| S-07 | SIR l. 33 | "more than 430 validation rules" | Número exato do anexo §6 (519: 486 R, 31 N, 2 sem marcação; nómina 437) | Anexo NE v1.0 §6 pp. 182–232 | 90% | Não (contagem do agente, 2 métodos) |
| WTC-Y | WTC Y255–Y264 (+ skill 02-wtc.md); recomendado Y114–116, Y124–133, V1 | "Pacted" aponta AuxilioS (NIE141) | AuxilioNS (NIE142) com pacto, senão AuxilioS; Salary só elemento S | Anexo NE v1.0 pp. 32–39; CST 127/128 | 92% / 80% | Não |
| P-06 (ARL) | PILA-003 J131/K131/P131; Population Rules C17 | Tarifa ARL "000005220" (decimal implícito) | Decimal com ponto, como as demais | AT2 v30 (saída ARL campo 28: "Tarifa. En decimales", do campo 61) | 80% | Sim (AT2 l. 12373) |
| DD-21 | DD ID Information H7 (H8/H9); Mappers nova linha 98 | Banco obrigatório em todos os códigos menos 1, 10, 20, ZZZ | Lista positiva (42, 45, 46, 47, 98…); acrescentar 98 | Anexo NE v1.0 NIE064–068, tabelas 5.3.3.1/2 | 85% | Não |
| Res. 2708 | CCG T12R3, T35R3/R4, T34R3, T52R7, P416, P433 | Regras apoiadas só na Circular 101 revogada | Tirar "limited to objective causes"; base = lei (CST 161, 179 par. 3; Ley 2101 art. 3). Nenhum valor muda | Res. MinTrabajo 2708/2026 arts. 1, 5.4, 8, 10 (cópia cerlatam) | 90% | Não |

## Confirmado, não muda (só nota opcional)
D5 (parafiscais em incapacidade = No, 85%), A-14 (Ley 2381 art. 20 e C-264-26, 95%), D9 (férias compensadas fora da base, 90% — CSJ SL467-2019), NE-18 (75%, sem definição oficial), auxílios de carro (85%, CSJ SL5159-2018).

## Fica aberto
- Linha 346 do WTC (alimentação "non-remunerative" na coluna V): precisa de decisão sobre V.
- NE-18 só fecha com consulta formal à DIAN.
- Validador da DIAN da NE: fora do escopo (G7).
