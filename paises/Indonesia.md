# Indonésia

> Hub do país. Índice: [[00-INDEX]] · Skill: `payroll-compliance-indonesia` · Fronteiras: [[fronteiras]]

## Situação
| Etapa | Status | Data | Observação |
|---|---|---|---|
| [[research-pipeline]] | ✅ | [data?] | skill compilada |
| [[design]] | ⏳ | | |
| Produção (outro time) | — | | |
| [[suporte]] | ⏳ | | |

## Ficha do país (da skill)
> Resumo do que mais importa para o serviço. Fonte: skill `payroll-compliance-indonesia`, lida em 2026-10-02. Valores exatos e tabelas: ler a skill. Se divergir, vale a skill.

- **Escopo:** ano fiscal 2026, empregadores do setor privado, IDR (moeda sem decimais). Fora: PNS, TNI/Polri, pejabat negara, bukan pegawai.
- **Órgãos:** DJP (imposto), BPJS Ketenagakerjaan (JHT/JP/JKK/JKM/JKP), BPJS Kesehatan, Kemnaker e governadores provinciais (salário mínimo).
- **Relatórios principais:** seis filings via Coretax, SIPP Online, e-Dabu e WLKP (PPh 21 mensal: pagamento até dia 15, declaração em 20 dias; BPJS Ketenagakerjaan até dia 15; WLKP anual). Layouts não confirmados.
- **Confiança da skill:** PASS WITH DISCLOSED GAPS. Motor de cálculo (PPh 21, PTKP, BPJS, hora extra, THR, severance e imposto) em 95-99%. Quatro áreas abaixo do piso: layouts dos relatórios (35-55%), multiplicador de severance por motivo de PHK (60%), valores de UMP 2026 (70%), tabelas TER (~93%, 12 de 125 taxas interpoladas).

**Armadilhas confirmadas** (correções marcadas na skill)
1. Aplicar TER sobre o bruto, nunca sobre o líquido após deduções (engine) → `01-ccg.md` §3
2. `penghasilan bruto` > bruto em caixa: JKK, JKM e BPJS Kesehatan do empregador são renda tributável imputada; JHT e JP não (engine) → PMK 168/2023 Pasal 5(3)
3. JKP não custa nada extra ao empregador (0,36% = 0,22% governo + 0,14% recomposto do JKK); JKM voltou a 0,30% (engine) → PP 6/2025 Pasal 11, `01-ccg.md` §4
4. Teto JP muda em março/2026 e limites de benefício em fevereiro: duas vigências na mesma circular (engine) → `01-ccg.md` §4.3
5. Quatro tetos distintos; JHT sem teto; só o Kesehatan tem piso (UMK/UMP) (engine) → `01-ccg.md` §4
6. Base da seguridade social é só `Upah pokok` + `tunjangan tetap` (engine) → PP 46/45/44/2015, Perpres 82/2018
7. PTKP congelado em 1º de janeiro (engine) → UU PPh Pasal 7(2); PMK 168/2023 Pasal 9(4)
8. Funcionária casada recebe só o PTKP próprio (TK/0), salvo certificado de nível kecamatan (engine) → PMK 168/2023 Pasal 9(2)-(3)
9. `Masa Pajak Terakhir` não é só dezembro: mês de saída também faz o true-up anual (engine) → PMK 168/2023 Pasal 1 no. 18
10. Sem método separado de bônus no TER: soma ao bruto do mês (engine) → PMK 168/2023
11. Hora extra: divisor 1/173 e piso de 75% da base (engine) → PP 35/2021 Pasal 32
12. Severance só é imposto final dentro da janela de 2 anos; ano 3 em diante usa Article 17 (engine) → PP 68/2009 Pasal 2(2), 6
13. Nunca cotar severance sem definir o motivo da PHK → `07-qa-report.md` O2
14. Limites de BIK em dois relógios (anual: presentes e esporte; mensal: moradia e vale-refeição) (engine) → PMK 66/2023
15. Pagamento do PPh 21 vence dia 15 (não 10); PKP arredondado para baixo a milhares; limites TER inclusivos (`gross <= upper`) (engine) → PMK 81/2024 Pasal 94(2)(c); PMK 168/2023 Pasal 8(4)

**O que mais dá errado** (do QA, por impacto monetário)
- TER sobre bruto; JKP como linha extra; JP em março; JHT sem teto; BIK dos BPJS na base tributária; PTKP congelado; PTKP da funcionária casada; Masa Pajak Terakhir; base SS estreita; piso do Kesehatan; piso de 75% de hora extra.

**Lacunas abertas / não confirmado** (candidatos a ticket ou nova pesquisa)
- O5: sem layout de campos para nenhum dos seis relatórios (Coretax migrou em jan/2025); não gerar arquivo; nunca citar número de box ou tag XML.
- O2: matriz de severance por motivo de PHK não construída (60%).
- O6/L4: valores de UMP/UMK/UMSP só ilustrativos (PP 49/2025 tornou o salário mínimo setorial obrigatório, chaveado por KBLI de 5 dígitos).
- O7: escopo BPJS para expatriados não resolvido. O3: férias de 12 dias não lidas no texto consolidado (85%). O1: JKM 0,30% é inferência jurídica corroborada.
- O4: ausência de M2M direto é falta de evidência (só intermediação PJAP). O10: retenção do holerite; O11: prazo do BPJS Kesehatan; O12: data do WLKP.
- Reverificar ao vivo: teto/limites JP (O8 arredondamento inconsistente: consumir o valor publicado), taxas BPJS Kesehatan, juros e multas fiscais, kurs KMK, feriados 2026 (80%).

**Valores-âncora**
| Item | Valor | A partir de | Fonte |
|---|---|---|---|
| Teto JP | Rp 11.086.300 (Rp 10.547.400 em jan-fev/2026) | 2026-03-01 | BPJS Ketenagakerjaan circular B/1226/022026 (2026-02-25) |
| Limites de benefício JP | Rp 411.400 / Rp 4.932.300 | 2026-02-01 | mesma circular |
| JKP | 0,36% (0,22% governo + 0,14% do JKK) | 2025-02-07 | PP 6/2025 Pasal 11 |
| Teto BPJS Kesehatan | Rp 12.000.000 (piso UMK/UMP) | vigente | Perpres 64/2020 |
| PTKP TK/0 | Rp 54.000.000 | 2026 | PMK 168/2023 Pasal 9(2)(a) |
| Prazo de pagamento PPh 21 | dia 15 do mês seguinte | 2025 | PMK 81/2024 Pasal 94(2)(c) |

## Artefatos entregues
| Artefato | Versão | Data | Arquivo/local | Observação |
|---|---|---|---|---|
| | | | | |

## Valores-chave (com vigência)
| Item | Valor | A partir de | Até | Fonte |
|---|---|---|---|---|
| | | | | |

## Decisões
- 

## Suporte (tickets)
| Data | Ticket | Assunto | Resolução | Mudou artefato? |
|---|---|---|---|---|
| | | | | |

## Pendências
- [ ]

## Correções ligadas
- _(links para entradas de [[correcoes]])_

## Fontes
- skill payroll-compliance-indonesia (lida em 2026-10-02)
