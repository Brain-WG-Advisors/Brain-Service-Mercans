# Filipinas

> Hub do país. Índice: [[00-INDEX]] · Skill: `payroll-compliance-philippines` · Fronteiras: [[fronteiras]]

## Situação
| Etapa | Status | Data | Observação |
|---|---|---|---|
| [[research-pipeline]] | ✅ | [data?] | skill compilada |
| [[design]] | ⏳ | | |
| Produção (outro time) | — | | |
| [[suporte]] | ⏳ | | |

## Ficha do país (da skill)
> Resumo do que mais importa para o serviço. Fonte: skill `payroll-compliance-philippines`, lida em 2026-10-02. Valores exatos e tabelas: ler a skill. Se divergir, vale a skill.

- **Escopo:** ano de folha 2026, setor privado, PHP. Salário mínimo verificado só para NCR (Wage Order NCR-27); não há salário mínimo nacional (13+ RTWPBs). Fora: GSIS/governo, militares, autônomos/voluntários/OFW, kasambahay, diretores não empregados e contratados independentes.
- **Órgãos:** BIR (withholding), SSS, PhilHealth, Pag-IBIG/HDMF, DOLE, NWPC/RTWPB. Quatro autoridades independentes, quatro bases, sem declaração consolidada.
- **Relatórios principais:** BIR 1601-C (mensal), 1604-C + alphalist (anual), 2316, 1603-Q (FBT), SSS e-CL (mensal), PhilHealth RF-1, Pag-IBIG MCRF, relatório DOLE do 13º, AERW (até 31 de janeiro), RKS Form 5. Prazos mensais dependem de atributo do empregador (PEN, letra do nome, grupo industrial).
- **Confiança da skill:** maioria 95-99%; cinco itens abaixo do piso (FBT por benefício U4; P-2 emissão de holerite ~70%; P-3 normas setoriais ~60%; U9 data de e-pagamento eFPS ~60%; layouts de arquivo de máquina 40-55%). Nenhum altera o cálculo mensal, exceto U4 (recusado, não chutado).

**Armadilhas confirmadas** (correções marcadas na skill)
1. Três contribuições com três bases diferentes, nenhuma é o bruto: SSS (remuneração real total), PhilHealth (Monthly Basic Salary), Pag-IBIG (Fund Salary) (engine) → `01-ccg.md` Part I
2. PhilHealth não reduz por falta, atraso, undertime ou licença sem remuneração (PC 2020-0005 §IV.F) (engine) → `01-ccg.md` Part I Step 3
3. SSS é tabela por faixas de MSC (passo ₱500), não percentual; SS regular até MSC ₱20.000 e MPF acima até ₱35.000; EC só do empregador (engine) → `01-ccg.md` Part I Step 2
4. Isenção de Minimum Wage Earner é status (flag MWE), não limiar da tabela (engine) → `01-ccg.md` Part I Step 7
5. Tabelas periódicas Annex "E" não são a anual dividida; nunca derivar uma de outra; PDF oficial traz erro de impressão (correto ₱6.034,30) (engine) → `01-ccg.md` Part I Step 8
6. Compensação regular x suplementar define a faixa da tabela; exige flag R/S por wage type (engine) → RR 2-98 s.2.79(B)(3); Form 2316
7. Cumulative Average Method obrigatório em casos definidos e, uma vez usado, vale até o fim do ano (engine) → `01-ccg.md` Part I Step 8
8. FBT depende do cargo (gerencial/supervisor: empregador paga 35% sobre valor ÷ 65%, Form 1603-Q; rank-and-file: compensação suplementar); nunca desconto no holerite (engine) → `01-ccg.md` Part I Step 9
9. Dois eixos de cargo diferentes (tributário x padrões trabalhistas); não derivar um do outro (engine) → `01-ccg.md` Part VIII
10. Só contribuições obrigatórias e dues sindicais são pré-imposto; Pag-IBIG voluntário acima de ₱200 e MP2 são pós-imposto; parte do empregador nunca é dedução (engine) → RR 2-98 s.2.78.1(B)(12); RA 11199 s.19(a)
11. Prazos mensais por atributo do empregador (PhilHealth: último dígito do PEN; Pag-IBIG: letra do nome; BIR eFPS: grupo industrial; SSS: último dia do mês seguinte) → `03-sir.md`
12. Jurisdição de portal, não M2M; sem certificado ou assinatura digital; sites do Pag-IBIG (reCAPTCHA) e DOLE (Cloudflare) bloqueiam coleta automática → `03-sir.md`
13. Não há lei de conteúdo de holerite para o setor privado geral; vale o registro de folha (Omnibus Rules Book III, Rule X, Sec. 6, 3 anos de retenção, no local de trabalho) → `06-payslip.md`
14. Cronogramas legais de SSS e PhilHealth terminam em 2025; valores 2026 são persistência administrativa; reajuste NCR-27 em 20/jan/2027 (₱755 para ₱780) (engine) → `01-ccg.md` Part V
15. Nunca fixar: taxa legal BSP (juros BIR = dobro), proclamação presidencial de feriados (eleição: 200% x 130%), wage orders regionais, taxa do SSS Salary Loan → `01-ccg.md` Part V

**O que mais dá errado** (do QA)
- Risco estrutural: persistência 2026 das taxas de SSS e PhilHealth deve ser dita ao cliente (confirmada por SSS Circular 2024-006 não revogada e PhilHealth Advisory 2026-0042, mas sem instrumento 2026 novo).
- Itens ao vivo a diarizar: eBIRForms v7.9.5 (RMC 020-2026), teto de OT-meal de minimis de ₱188,75 para ₱195,00 com NCR-27.

**Lacunas abertas / não confirmado** (candidatos a ticket ou nova pesquisa)
- U4: RR 3-98 s.2.33(B) (valoração por benefício do FBT) não obtido e deliberadamente não declarado.
- U3: tratamento no SSS de bônus discricionário não equivalente a 13º (~75%). U2: Pag-IBIG MFS/taxas 2026 só corroboradas (~95%).
- U6: se há Tax Software Provider certificado para 1601-C/1604-C/2316. U9: data do e-pagamento eFPS (~60%; pagar até dia 10 por segurança).
- U7/U8: layout `.DAT` do alphalist (~55%) e do e-CL do SSS (~50%). U10: e-CL mensal x lista trimestral do RA 11199 s.19.
- P-2: dever de entregar holerite e assinatura eletrônica (~70%; emitir holerite e guardar folha assinada). P-3: D.O. 150-16 e D.O. 174-17 (segurança privada, terceirização) não lidas.
- DD-3 a DD-6: máscaras de identificadores e Alien Employment Permit. Layout do portal AERW (~45%); LA 08 s.2026 não recuperado.

**Valores-âncora**
| Item | Valor | A partir de | Fonte |
|---|---|---|---|
| PhilHealth | 5,00% do MBS (2,5% / 2,5%), piso ₱10.000, teto ₱100.000 | 2026 (persistência do passo 2025) | RA 11223 s.10; PC 2020-0005 (Rev. 1); PhilHealth Advisory 2026-0042 |
| SSS: máximo empregado / empregador | ₱1.750 (SS ₱1.000 + MPF ₱750) / ₱3.530 (₱2.000 + ₱1.500 + EC ₱30) | 2026 (persistência do passo 2025) | RA 11199 s.4(a)(9); SSS Circular 2024-006 |
| Pag-IBIG | MFS ₱10.000; 1%/2% e 2%/2%; máx. ₱200 por lado | 2026 | HDMF Circular 460 (via DBM CL 2024-2); ⚠️ não first-party |
| FBT | 35% sobre valor ÷ 65% (÷ 75% para não residente estrangeiro) | vigente | NIRC s.33 (RA 10963); RR 11-2018 |
| Salário mínimo NCR não agrícola | ₱755/dia (₱780 em 2027-01-20) | 2026 | Wage Order NCR-27 |
| Prazo AERW | até 31 de janeiro do ano seguinte | anual | DOLE Labor Advisory 09 s.2022 |

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
- skill payroll-compliance-philippines (lida em 2026-10-02)
