---
tipo: pais
codigo: "CD"
etapa_research: "concluida"
etapa_research_data: 
etapa_design: "aguardando"
etapa_design_data: 
etapa_producao: 
etapa_suporte: "sem ticket no hub"
etapa_suporte_data: 
ccg: 
ccg_data: 
wtc: 
wtc_data: 
dd: 
dd_data: 
report_specs: 
report_specs_data: 
sir: 
sir_data: 
payslip: 
skill: "payroll-compliance-drcongo"
tickets_abertos: 
tickets_conferidos_em: 
atualizado_em: 2026-10-27
---
# RD Congo

> Hub do país. Índice: [[00-INDEX]] · Skill: `payroll-compliance-drcongo` · Fronteiras: [[fronteiras]]
> Atenção: não confundir com a República do Congo (Brazzaville), ver [[Congo]] (skill `payroll-compliance-congo`).

## Situação
| Etapa | Status | Data | Observação |
|---|---|---|---|
| [[research-pipeline]] | ✅ | [data?] | skill compilada |
| [[design]] | ⏳ | | |
| Produção (outro time) | — | | |
| [[suporte]] | ⏳ | | |

## Ficha do país (da skill)
> Resumo do que mais importa para o serviço. Fonte: skill `payroll-compliance-drcongo`, lida em 2026-10-02. Valores exatos e tabelas: ler a skill. Se divergir, vale a skill.

- **Escopo:** FY2026 (ano calendário), o primeiro ano do regime IRPP; setor privado; moeda CDF; idioma legal francês. Fora: servidores, militares, autônomos. Prestador de serviço não residente cai na retenção separada de 14% (arts. 142-144).
- **Órgãos:** DGI (IRPP, PEEEPE; portal i-impots.dgirdc.cd), CNSS (edeclaration.cnss.cd), INPP, ONEM, Inspection du Travail.
- **Relatórios principais:** RPT-CD-001 retenção mensal do IRPP; RPT-CD-002 PEEEPE mensal; RPT-CD-003 DMFP (CNSS mensal); RPT-CD-004 recapitulativo anual do empregador (status mudou em 2026); RPT-CD-005 declaração/pagamento único; RPT-CD-006 INPP; RPT-CD-007 ONEM (declaração até o dia 10); RPT-CD-008 recapitulativo anual do empregado (status incerto); RPT-CD-009 IRPP anual da pessoa física; RPT-CD-010 bulletin de paie.
- **Confiança da skill:** veredito SHIP WITH DOCUMENTED LIMITATIONS. Seção a seção em geral 93-99% (barème 98%, CNSS 98%, regime IPR→IRPP 97%). Seis itens abaixo do piso de 95% (ver Lacunas). Layouts de campo DERIVADOS (55-60%); formatos de identificador 50%. Caveat metodológico: a Loi n° 23/053 só existe como scan de imagem, lida por OCR com reconhecedor não francês (arts. 118, 150 e o segundo limb do 123 têm corroboração mais fraca).

**Armadilhas confirmadas** (esclarecimentos da skill; prevalecem sobre `references/`)
1. FY2026 é o primeiro ano do IRPP: IPR e IERE não existem mais (Loi 23/053 arts. 152-153); o site da DGI ainda mostra a página do IPR e o folheto de agosto/2025, válido só até 31/12/2025; usar o folheto de outubro/2025 → SKILL.md item 1
2. Nunca pegar barème de anexo de despesa tributária ou calculadora: o LF 2026 reimprime a escala antiga de dez faixas (524 160 / 1 428 000 / 2 700 000), pré-2020 → item 2
3. Duas bases paralelas: CNSS/INPP/ONEM seguem CdT art. 7 litera h (moradia, transporte, saúde e abono familiar excluídos por inteiro, sem teto); o IRPP inclui e imuniza com tetos (art. 69) → item 3
4. CNSS tem piso (SMIG) e NÃO tem teto; 13% ER + 5% EE = 18%; quem configura teto importou o do antigo INSS → item 4
5. Dois arredondamentos: base líquida para baixo ao milhar (art. 118); imposto arredondado ao 100 mais próximo (art. 150); o arredondamento antigo "ao 10" foi revogado → item 5
6. O teto de 30% do imposto é aplicado ANTES do alívio por dependentes (barème → teto → art. 123 → arredondamento) → item 6
7. Dependentes (art. 123): 2% por dependente, máx. 9, e nenhuma redução sobre a parte da renda acima da terceira faixa (43 200 000 anual / 3 600 000 mensal); cláusula nova → item 7
8. Dois testes de dependente na mesma folha: IRPP (art. 124-125, situação congelada em 1º de janeiro, teste de renda na 1ª faixa) × abono familiar do CdT art. 7 litera k; não compartilhar contador → item 8
9. O imposto mínimo mensal por empregado (2 000/2 500 CDF) acabou; achado negativo, 93% → item 9
10. PEEEPE (25%, ER): base reduzida pelas imunidades do art. 69, mas NÃO pela dedução CNSS do empregado; "personnel expatrié" não é definido em lei (65%) → item 10
11. ONEM é 0,5%, não 0,2% (AM de 05/08/2025); a ANAPI ainda publica 0,2% → item 11
12. Alíquotas INPP FY2026 a 70%: tabela rastreável é de 2006 (3% / 2% / 1% por porte); novo arrêté citado, não localizado → item 12
13. Rescisão passa a ser tributada pelo barème (art. 68.6); as taxas proporcionais antigas (10%/15%/20%) não têm sucessor; 70%; risco é retenção a maior → item 13
14. O payslip é duplicata destacável do livre de paie: 33 menções, francês, nomes em MAIÚSCULAS, 2ª via para a CNSS; registro informatizado exige autorização do Inspetor do Trabalho → item 14
15. Portal round-trip, não M2M; RDC não é CEMAC e CD não é CG; não validar conta RDC como IBAN CD/CG → item 15

**O que mais dá errado** (do QA)
- Usar uma base única para CNSS e IRPP: erra quase toda folha
- Barème obsoleto de calculadoras/anexos e teto de CNSS importado do INSS
- Ordem errada entre teto de 30% e alívio de dependentes
- Hora extra baseada em arrêtés de 1968 não publicados no JO, com 48 h, enquanto o CdT art. 119 (2016) fixa 45 h (pack usa 45 h, ~85%); sempre checar a CBA (CdT art. 291)

**Lacunas abertas / não confirmado** (candidatos a ticket ou nova pesquisa)
- INPP 2026 (70%); tributação de rescisão (70%); sobrevivência da declaração anual por empregado (55%); declaração unique ainda operante (65%); status do RPT-CD-008 (55%); base de referência dos 30% de moradia (75%)
- Layouts de todos os formulários (derivados); formatos de NIF, CNSS e NNI não estabelecidos
- Tabela anexa do Décret 25/22 (SMIG por categoria acima de manœuvre ordinaire); calendário de feriados de 2026 sai por communiqué anual
- Loi de finances rectificative 2026 (~11/08/2026): existe, dispositivo fiscal não obtido; risco baixo, não verificado
- Para fechar acima de 95%: cópia com texto da Loi 23/053, arrêté do art. 126, arrêté INPP 2026, um formulário oficial DGI/CNSS

**Valores-âncora**
| Item | Valor | A partir de | Fonte |
|---|---|---|---|
| IRPP barème | 3% / 15% / 30% / 40% nas faixas de 1 944 000 / 21 600 000 / 43 200 000 CDF anuais; teto de 30% do imposto sobre a renda tributável | 2026-01-01 | Loi n° 23/053 art. 118 |
| CNSS | 18% (ER 13% = 6,5% família + 5% pensão + 1,5% riscos; EE 5%); piso SMIG, sem teto | 2018 (Décret 18/041) | Loi 16/009; Décret n° 18/041 |
| SMIG | 21 500 × 26 = 559 000 CDF/mês | 2025 | Décret n° 25/22 |
| PEEEPE | 25% ER sobre pessoal expatriado | 2026-01-01 | Loi n° 23/053 arts. 145-149 |
| ONEM | 0,5% ER | 2025-08-05 | AM n° 30/CAB/MIN.ET/EAN/JDO/8/2025 |
| INPP (provisório, 70%) | privado 3% (1-50) / 2% (51-300) / 1% (>300) | 2006 | arrêté interministerial de 2006 |

## Artefatos entregues
| Artefato | Versão | Data | Arquivo/local | Observação |
|---|---|---|---|---|
| | | | | |

## Valores-chave (com vigência)
| Item | Valor | A partir de | Até | Fonte |
|---|---|---|---|---|
| | | | | |

## Decisões
- AAAA-MM-DD: decisão, por quê, quem decidiu

## Suporte (tickets)
| Data | Ticket | Assunto | Resolução | Mudou artefato? |
|---|---|---|---|---|
| | | | | |

## Pendências
- [ ]

## Correções ligadas
- _(links para entradas de [[correcoes]])_

## Fontes
- skill payroll-compliance-drcongo (lida em 2026-10-02)
