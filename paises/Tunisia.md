---
tipo: pais
codigo: TN
etapa_research: concluida
etapa_research_data: 2026-11-02
etapa_design: aguardando
etapa_design_data:
etapa_producao: outro time (Henkel em produção)
etapa_suporte: "1 aberto(s): HRBS-16418"
etapa_suporte_data: 2026-11-02
ccg: "v1.0"
ccg_data:
wtc: "v1.0"
wtc_data:
dd: "v1.0"
dd_data:
report_specs: "7 specs (.gsheet)"
report_specs_data:
sir:
sir_data:
payslip: "TN_Compliance_Payslip_Generator (.gsheet)"
skill: "SKILL.md no Drive (19 - Skill File)"
tickets_abertos: 1
tickets_conferidos_em: 2026-11-02
atualizado_em: 2026-11-02
---
# Tunísia

> Painel: `paineis/paises.base` (properties acima: etapas = concluida | em andamento | aguardando; versão vigente = maior número, regra 8) · Hub do país. Índice: [[00-INDEX]] · Skill: `payroll-compliance-tunisia` (não instalada; há um SKILL.md no Drive) · Correções: [[correcoes]] · Fronteiras: [[fronteiras]]

Hub criado em 2026-11-02 pela janela Suporte (HRBS-16418). Etapas de research/design inferidas só dos arquivos no Drive; confirmar com o usuário.

## Situação
| Etapa | Status | Data | Observação |
|---|---|---|---|
| [[research-pipeline]] | ✅ | 2026-11-02 | Artefatos v1.0 no Drive (Country Folders/Tunisia), lidos em 02/11 |
| [[design]] | ⏳ | | Design tn_2026 citado no HRBS-16418 (Reg 259 TN Tax Advantage, Reg 260 faixas); não está no Drive de compliance |
| Produção (outro time) | — | | Henkel em produção (regra 9: mudança de artefato → ticket ao Development) |
| [[suporte]] | 🔄 | 2026-11-02 | HRBS-16418 |

## Artefatos entregues
| Artefato | Versão | Data | Arquivo/local | Observação |
|---|---|---|---|---|
| CCG | v1.0 | | Drive `05 - Payroll Regulation Guide/TN-CCG-001-v1.0.docx` | |
| WTC | v1.0 | | Drive `03 - WTC/TN-WTC-001-v1.0.xlsx` | Aba Tax Credit: mínimo de 45% só para seguro de vida |
| DD | v1.0 | | Drive `02- DD/TN-DD-001-v1.0.xlsx` | |
| Report Specs | 7 specs | | Drive `18 - Statutory Reports/` (CNSS-001 a 004, DGI-001 a 003) | |
| Payslip | — | | Drive `17 - Payslip/TN_Compliance_Payslip_Generator.gsheet` | |

## Valores-chave (com vigência)
| Item | Valor | A partir de | Até | Fonte |
|---|---|---|---|---|
| Imposto mínimo de pessoa física com isenções (Art. 12 bis Lei 89-114) | 45% do IRPP calculado sem as isenções | 2017-02-21 (60% antes) | — | Lei 2017-8, art. 2-6 (JORT 21/02/2017); não alterado pela LF2025 nem pela LF2026 (lidas em 02/11) |
| Dedução CEA (comptes épargne en actions) | até 100.000 TND/ano, sob reserva do Art. 12 bis | — | — | Código IRPP/IS art. 39-VIII (edição 2024) |
| Dedução seguro de vida | até 100.000 TND/ano, sob reserva do Art. 12 bis | — | — | Código IRPP/IS art. 39-I-2 (LF 2020-46 art. 16) |

## Decisões
- 2026-11-02: o mínimo de 45% do Art. 12 bis vale para as deduções concedidas "sous réserve" do 12 bis (seguro de vida 39-I-2, CEA 39-VIII, CEI 39 bis), não para as "nonobstant" (39-V, 39 ter); também na retenção mensal (art. 53-I). Fontes em `raw/docs/oficiais/TN/` (HRBS-16418).

## Suporte (tickets)
| Data | Ticket | Assunto | Resolução | Mudou artefato? |
|---|---|---|---|---|
| 2026-11-02 | HRBS-16418 (Henkel) | Cliente mandou o Art. 12 bis da Lei 89-114 (mínimo de 45%); rfusana mostrou que o design tn_2026 não aplica o piso (Reg 259 deduz 100% da 58891); asaber cobrou resposta (10 dias) | Publicado 02/11 por nós com ordem do usuário (4-205738, 573 car.): a regra vale para as deduções "sous réserve"; aplica-se na folha (art. 53-I); exemplo do ticket correto (45% × 9.550,000 = 4.297,500 > 3.250,000); nada extra do cliente. Texto: [[rascunhos/2026-10-28-youtrack-drafts/HRBS-16418|HRBS-16418]] | Não |
| 2026-11-03 | HRBS-16418 (Henkel) | Ahmed (asaber), no chat: entendeu que o piso se aplica, não como se aplica no exemplo do Romano | Publicado pelo usuário 03/11 12:00 UTC (4-206003, IGUAL ao draft; chat ao Ahmed enviado): passo a passo (3.250,000 com CEA; 45% × 9.550,000 = 4.297,500; vale o maior; retenção = anual ÷ nº de folhas, art. 53-I → 358,125 × 12 onde a folha concede o CEA). Faixas = LF2025 art. 36 (desde 01/01/2025; a edição 2024 do código ainda traz as antigas). Texto: [[rascunhos/2026-10-28-youtrack-drafts/HRBS-16418-passo-a-passo|passo a passo]] | Não |

## Pendências
- [ ] CCG v1.0 e WTC v1.0 citam o mínimo de 45% só para o seguro de vida; faltam CEA (39-VIII) e CEI (39 bis). País em produção → mudança só com ticket ao Development (regra 9).
- [ ] Confirmar com o usuário as etapas de research/design deste hub (criado a partir do Drive).
- [ ] Note Commune 3/2025 (jibaya.tn) não lida: site fora do ar em 02/11.
- [ ] Piso de 45% não está no design tn_2026 (achado do Romano, Reg 259/260; design não lido por nós). 03/11, chat ao Ahmed (enviado com ok do usuário): não está no sistema; nosso comentário só diz como deve funcionar; é alteração da regulation (Mohit), não da Configuration; regra estatutária → correção, não CR do cliente; custo a confirmar com o Mohit. País em produção → ticket ao Development (regra 9) quando o Mohit decidir.
- [ ] CEA na folha? Art. 39-VIII condiciona a dedução ao certificado de depósito "lors du dépôt de la déclaration annuelle" e a 5 anos sem saque; não li fonte que autorize o empregador a conceder na retenção (Reg 259 deduz 100% da 58891). Procurar Note Commune quando o jibaya.tn voltar (achado 03/11, fora do pedido do HRBS-16418).

## Fontes
- `raw/docs/oficiais/TN/2026-11-02-Loi-2017-8-avantages-fiscaux-JORT.pdf`
- `raw/docs/oficiais/TN/2026-11-02-Code-IRPP-IS-2024-IORT.pdf`
- `raw/docs/oficiais/TN/2026-11-02-LF2025-Loi-2024-48-ar.pdf`
- `raw/docs/oficiais/TN/2026-11-02-LF2026-Loi-2025-17-JORT148-ar.pdf`
