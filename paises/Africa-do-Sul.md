# África do Sul

> Hub do país. Índice: [[00-INDEX]] · Skill: `payroll-compliance-southafrica` · Fronteiras: [[fronteiras]]

## Situação
| Etapa | Status | Data | Observação |
|---|---|---|---|
| [[research-pipeline]] | ✅ | [data?] | skill compilada (ano de avaliação 2027) |
| [[design]] | ⏳ | | |
| Produção (outro time) | — | | |
| [[suporte]] | ⏳ | | |

## Ficha do país (da skill)
> Resumo do que mais importa para o serviço. Fonte: skill `payroll-compliance-southafrica`, lida em 2026-10-02. Valores exatos e tabelas: ler a skill. Se divergir, vale a skill.

- **Escopo:** ano de avaliação (YoA) 2027 = 2026-03-01 a 2027-02-28 (o ano leva o nome do ano em que termina); setor privado; moeda ZAR. Fora: servidores, ministros, parlamentares, conselheiros municipais, líderes tradicionais, contratados independentes genuínos (exceto onde o Fourth Schedule os puxa).
- **Órgãos:** SARS (PAYE, SDL, coleta de UIF, ETI), UIF Commissioner, Compensation Fund (COIDA; RMA/FEM para classes 13, 4 e 5), Department of Employment and Labour (BCEA, NMW, sectoral determinations SD 1 e SD 9).
- **Relatórios principais:** EMP201 (mensal); EMP501 (intermediário + anual); IRP5/IT3(a) e arquivo de importação BRS; ITREG; UI-19 (mensal, UIF) e arquivo eletrônico E031; Return of Earnings W.As.8 / CF-2A (anual, Compensation Fund). DEL não tem declaração periódica (fiscalização).
- **Confiança da skill:** PASS WITH NOTES, agregado ~96%, zero defeitos críticos. 01-ccg 97%, 02-wtc 96%, 03-sir 96%, 04-reports 95%, 05-dd 96%, 06-payslip 93% (única abaixo do piso). Layouts de relatório NÃO são derivados (CF-2A gazetado; EMP501/IRP5 publicados campo a campo). Não usa a nomenclatura TIER-B; os itens abertos são U-1 a U-10 e os defeitos de fonte D-1 a D-8.

**Armadilhas confirmadas** (esclarecimentos da skill; vários são engine)
1. Não existe um "bruto" único: sete bases (remuneration, balance of remuneration, UICA, SDL, COIDA, BCEA s.6(3), acumulador s.11F código 4582); nunca reaproveitar uma pela outra → SKILL.md item 1
2. Comissão tem PAYE e SDL mas NÃO UIF (UICA s.1; UI-19 código 2; UIF eletrônico 05) → item 2
3. SDL é 1% do balance of remuneration, não do bruto; a página do SARS e o FAQ do Budget 2026 estão errados → item 3
4. Base de 27,5% da s.11F é o código 4582, não 3699; teto = R430.000 ÷ 12 = R35.833,33/mês, rodando mensalmente → item 4
5. São QUATRO deduções do para 2(4), com o código 4042 (remuneração devolvida/clawback, novo no YoA 2026); erro administrativo é recuperado pelo BCEA s.34(5)(a) e não vai ao 4042 → item 5
6. Auxílio-viagem com três percentuais na mesma folha: 80% na base do PAYE (20% se uso de negócio ≥80%), mas o campo 8300 do UIF leva 100%; código 3702 só é 80/20 se a taxa do empregador exceder R4,95/km → item 6
7. Idade testada no fim do ano e aplicada desde o início (rebate secundário/terciário vale o ano todo) → item 7
8. Ordem fixa: alíquotas → rebates s.6 → crédito médico s.6A (nunca gera restituição); s.6B no PAYE mensal só para 65+ → item 8
9. Percentual de tax directive incide ANTES das deduções do para 2(4), sobre a remuneration → item 9
10. ETI é só abatimento da remessa de PAYE do empregador, teto de 75% do código 3699 a partir do YoA 2027 (BRS V25.3.0 rejeita; sem citação legal, U-2), desqualificação por empregado/mês; o FAQ do SARS que diz "todo o claim desqualificado" não tem base → item 10
11. COIDA nunca é desconto do empregado (s.86); o CF-2A traz dois tetos lado a lado: R633.168 (ganhos reais) e R668.000 (provisórios) por pessoa → item 11
12. Acima do limiar de ganhos do BCEA (R269.600,90 a.a. desde 2026-05-01) não há hora extra, prêmio de domingo nem adicional noturno estatutários, mas a obrigação de payslip (s.33) permanece → item 12
13. 4141 = UIF e 4142 = SDL (o BRS inverte na descrição do 4149); trocar inverte os totais do EMP501 → item 13
14. Seis códigos IRP5 costumam ser trocados: 3817 pensão ER, 3825 provident ER, 3828 retirement annuity ER, 3813 serviços médicos, 3802/3816 carro sem/com leasing operacional, 3808 dívida paga; bolsas = matriz de oito códigos → item 14
15. Folha NÃO está nos canais M2M do SARS; PAYE via eFiling ou e@syFile Employer; exceção: TRN (ITREG em lote) → item 15
16. Separador decimal: imprimir `R9 934,58`, gravar `9934.58` nos arquivos SARS/UIF; valores de renda são truncados, não arredondados (exceto 4101, 4102, 4115, 4141, 4142, 4149, 4116, 4118, 4120, 6030, 7002, 7003, 7004, 7008) → item 16

**O que mais dá errado** (do QA)
- Seis erros de atribuição de código IRP5 (cada um gera arquivo de reconciliação rejeitado ou empregado tributado errado)
- Seis dos oito defeitos de fonte são conflitos entre duas fontes oficiais; hierarquia: gazette > Act > guia externo SARS > BRS > página web SARS (não tratar o FAQ Budget 2026 como autoridade)
- Taxa oficial de juros (8,00% desde 2026-06-01; o Budget 2026 Tax Guide, 7,75%, está desatualizado)
- Códigos do UI-19 em papel × arquivo eletrônico não coincidem (D-5): manter uma enumeração interna e mapear duas vezes

**Lacunas abertas / não confirmado** (candidatos a ticket ou nova pesquisa)
- U-1 prêmio por tempo de serviço (R16.000): redução ou tudo-ou-nada; U-2 base legal do teto de 75% do ETI; U-3 janela de correção COIDA (30 ou 60 dias); U-4 janela do ROE COIDA (31/mar × 1/abr); U-5 janela anual do EMP501 (não estatutária); U-6 prazo exato de entrega do IRP5/IT3(a)
- U-7 código UIF 19 "Parental Leave" × decisão Van Wyk ([2025] ZACC 20): licença vs benefício UIF não alinhados; U-8 se o s.28 do BCEA exclui quem trabalha <24 h/mês (~70%); U-9 método semanal do crédito médico (÷4 ou ×12÷52); U-10 payslip em sectoral determinations (~65%)
- O Income Tax Act em si nunca foi recuperado: Fourth e Seventh Schedule citados via guias do SARS
- Live-data (nunca fixar): taxa oficial de juros, tarifas COIDA por subclasse, taxas de sectoral determination/conselhos de negociação, versão do BRS, build do e@syFile

**Valores-âncora**
| Item | Valor | A partir de | Fonte |
|---|---|---|---|
| Teto de remuneração UIF | R17.712/mês (R212.544 a.a.), máx. R177,12 por lado | YoA 2027 (2026-03-01) | UICA; UIF ceiling (via skill) |
| SDL | 1% do balance of remuneration, sem teto | YoA 2027 | SDL Act 9 de 1999; SDL-GEN-01-G01 §6 |
| Teto s.11F | 27,5% limitado a R430.000/ano (R35.833,33/mês) | YoA 2027 | Income Tax Act s.11F |
| Limiar de ganhos BCEA | R269.600,90 a.a. | 2026-05-01 | BCEA 75 de 1997 (portaria) |
| Taxa oficial de juros | 8,00% (repo + 100 bps; vigora no 1º dia do mês seguinte à mudança do repo) | 2026-06-01 | SARS (via skill); revalidar |
| Tetos COIDA CF-2A | R633.168 (reais) / R668.000 (provisórios) por pessoa | YoA 2027 | CF-2A gazetado |

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
- skill payroll-compliance-southafrica (lida em 2026-10-02)
