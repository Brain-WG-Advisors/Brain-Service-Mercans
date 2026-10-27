---
tipo: pais
codigo: "GQ"
etapa_research: "concluida"
etapa_research_data: 
etapa_design: "aguardando"
etapa_design_data: 
etapa_producao: 
etapa_suporte: "sem ticket no hub"
etapa_suporte_data: 
ccg: v1.0
ccg_data: 
wtc: v1.0
wtc_data: 
dd: v3.0
dd_data: 
report_specs: 
report_specs_data: 
sir: v1.0
sir_data: 
payslip: 
skill: "payroll-compliance-equatorialguinea"
tickets_abertos: 
tickets_conferidos_em: 
versoes_fonte: "nome do arquivo no Drive (Country Folders/Eq. Guinea), lido em 2026-10-27; sem data de versão"
atualizado_em: 2026-10-27
---
# Guiné Equatorial

> Hub do país. Índice: [[00-INDEX]] · Skill: `payroll-compliance-equatorialguinea` · Fronteiras: [[fronteiras]]

## Situação
| Etapa | Status | Data | Observação |
|---|---|---|---|
| [[research-pipeline]] | ✅ | [data?] | skill compilada |
| [[design]] | ⏳ | | |
| Produção (outro time) | — | | |
| [[suporte]] | ⏳ | | |

## Ficha do país (da skill)
> Resumo do que mais importa para o serviço. Fonte: skill `payroll-compliance-equatorialguinea`, lida em 2026-10-02. Valores exatos e tabelas: ler a skill. Se divergir, vale a skill.

- **Escopo:** setor privado, moeda XAF, Novo Código Tributário Geral (Ley 1/2024, em vigor desde 2025-01-01). Idioma oficial espanhol (único build em espanhol entre os países CEMAC/XAF do Mercans). Fora: servidores e empregados do Estado.
- **Órgãos:** DGI (IRPF), INSESO (previdência), Fundo de Proteção do Trabalho (WPF). Os três arquivam em papel/manual, sem portal nem integração máquina a máquina (SIR = MANUAL_ONLY).
- **Relatórios principais:** GQ-DGI-001 imposto mensal sobre salários, formulário 0720 (autoliquidación, até o dia 15 do mês seguinte); GQ-DGI-002 reconciliação anual; GQ-INSESO-001 contribuição mensal; GQ-INSESO-002 Alta/Baja (ficha de afiliación); GQ-WPF-001 Fundo de Proteção.
- **Confiança da skill:** "utilizável para cálculo de folha, provisório para relatórios". O pacote não passou pelo Stage 9/10 formal do pipeline; o QA é compilado das notas de cada Report Spec. As 5 specs se autoavaliam abaixo de 95% (GQ-DGI-001 ~80%, GQ-DGI-002 ~70%, INSESO-001 ~75%, INSESO-002 ~78%, WPF-001 ~75%): taxas, base legal e prazos sólidos; layouts de campo DERIVADOS (sem imagem de formulário oficial). Não usa a nomenclatura TIER-B.

**Armadilhas confirmadas** (esclarecimentos da skill; prevalecem sobre `references/`)
1. O teto social do empregado é exatamente 5,0% por lei: INSESO 4,5% + WPF 0,5% (Lei do Trabalho art. 89.3) (engine) → SKILL.md item 1
2. Custo patronal de 22,5% (INSESO 21,5% + WPF 1%) é paralelo ao bruto, nunca descontado do líquido (engine) → item 2
3. O idioma oficial é espanhol, não francês; não herdar termos ou modelos de Gabão, Congo, Chade ou Costa do Marfim (engine) → item 3
4. Antigüedad (indenização por tempo de serviço) é isenta de imposto, para residentes e não residentes (Lei do Trabalho art. 112.6); não passar pela retenção do IRPF (engine) → item 4
5. Residente e não residente usam a mesma escala IRPF 0-25%; muda a base (residente: renda mundial do trabalho; não residente: só fonte GQ) (engine) → item 5
6. Honorários de prestador não residente têm retenção própria de 10%, fora da folha (Ley 1/2024) → item 6
7. Benefícios em espécie valem percentuais fixos do bruto: moradia 15%, veículo 10%, alimentação 15% (com teto), empregados domésticos 5%, água e luz 5% → item 7
8. Os dois bônus estatutários (2 × 15 dias) somam-se ao salário do mês para o imposto, sem retenção separada → item 8
9. Formulário 0720 vence nos primeiros 15 dias do mês seguinte, sem portal eletrônico → item 9
10. A ordem de cálculo importa: contribuições sociais saem do bruto ANTES de apurar a base do IRPF (Passo 4 do CCG); exemplo: 1.000.000 XAF/mês, residente, dá ≈ 115.833 de IRPF, líquido ≈ 834.167 → "What good answers look like"

**O que mais dá errado** (do QA)
- Tratar posições de campo das 5 specs como definitivas; é o principal alerta para quem construir a integração de arquivamento
- Inverter ou pular a ordem contribuições sociais → base do IRPF

**Lacunas abertas / não confirmado** (candidatos a ticket ou nova pesquisa)
- Layouts de campo do 0720 (por empregado), da declaração INSESO, da ficha de afiliación e do WPF; formato de importação e-Tax
- Se o WPF é linha de declaração própria ou vai junto da remessa ao INSESO
- Layout do formulário anual da reconciliação (sem imagem oficial)
- Formato/máscara do ID do empregado (sequência de 7 dígitos / "código patronal"): confirmar direto com o INSESO
- Observação resolvida (2026-10-05): o "26%" do QA é o total INSESO (21,5% ER + 4,5% EE) e o "1,5%" é o total do WPF (1% ER + 0,5% EE); não há taxa adicional (confirmado: skill `references/01-ccg.md` §5.1, tabela Employer/Employee/Total, e `07-qa-report.md`). Pendência: a mesma tabela do CCG lista também AT/MP 2% e saúde/maternidade 12% sem separar empregador/empregado e fora dos totais (ver relatório rev-AF)

**Valores-âncora**
| Item | Valor | A partir de | Fonte |
|---|---|---|---|
| INSESO | ER 21,5% / EE 4,5% (total 26%) | ⚠️ vigência? | Ley 4/1984 (INSESO); Ley 4/2021; PwC (revisado em nov/2025) (skill, 01-ccg §5.1) |
| Work Protection Fund | ER 1% / EE 0,5% (total 1,5%) | ⚠️ vigência? | Ley 4/2021; Lei do Trabalho art. 89.3 (skill, 01-ccg §5.1) |
| IRPF sobre salários | escala progressiva 0-25%, autoliquidación (form. 0720) | 2025-01-01 | Ley 1/2024 |
| Prazo do 0720 | até o dia 15 do mês seguinte | 2025-01-01 | Ley 1/2024 (via skill) |
| Retenção de prestador não residente | 10% | 2025-01-01 | Ley 1/2024 |
| Benefício em espécie (moradia) | 15% do bruto | 2025-01-01 | Código Tributário (via skill) |

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
- skill payroll-compliance-equatorialguinea (lida em 2026-10-02)
