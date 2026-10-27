# HRBS-12110: revisão completa da Reporting Matrix do Congo (2026-10-09)

> Arquivo revisado: `raw/tickets/api/anexos/HRBS-12110/20260721-0936 - Reporting Matrix - Congo.xlsx` (anexo do ticket, baixado pela API).
> Referência: skill `payroll-compliance-congo`, `references/04-reports-spec.md` (CG-CNSS-001, CG-DGID-001, CG-DAS-001; FY2026).
> Complementa a nossa revisão de 2026-08-13 no ticket (aba "note" do Senegal, abas CNSS e DAS vazias, DGID "XML", ITS ~10×). Rascunho: não enviado.

## Veredito
**Não está pronta para o cliente.** Das 11 linhas da aba "List of Reports", as 3 estatutárias estão incompletas ou erradas, e várias abas vieram de modelos de outros países.

## 1. Relatórios estatutários (o que o Congo exige × o que a matriz traz)
| Relatório (skill) | Órgão / canal | Prazo | Na matriz | Problema |
|---|---|---|---|---|
| **CG-CNSS-001**: bordereau nominativo mensal (PVID, PF, AT-MP, **CAMU**, **TUS 5,475%**) | CNSS, e-déclaration (edeclaration.cnss.cg); upload XLSX/CSV ou formulário no portal | Antes do dia 15 de N+1 | Linha 11 "CG - CNSS"; aba **vazia** | Falta a aba inteira. CAMU (4,55% ER / 2,27% EE / 0,5% solidarité) e a parte CNSS da TUS (5,475%) não aparecem em nenhum lugar da matriz |
| **CG-DGID-001**: declaração mensal agregada de ITS + TUS (parte DGID 2,025%) | DGID, e-Taxe / SYSTAF; formulário online, **sem XML/XSD** | Até o dia 15 de N+1 | Linha 9; aba com exemplo | (a) A aba diz "Real submission to DGID is via télédéclaration (XML upload)" e, duas linhas acima, "no public XSD". A skill diz formulário online, sem XML. (b) O ITS de 279.300 XAF para 120 empregados é o valor anual de um único empregado, não o total mensal (≈ 2.793.000) |
| **CG-DAS-001**: declaração anual dos salários (DAS1 + DAS2 + **DAS3**, nova em 2026) | CNSS **e** DGID, no mesmo modelo ministerial | 31 de março do ano seguinte | Linha 10; aba **vazia** | Falta a aba. Não indica que vai aos dois órgãos nem a DAS3 (recap por número de partes, LF 2026 art. 116 H–I) |

## 2. Resíduos de outros países
| Aba | O que tem | De onde veio |
|---|---|---|
| note | État 1024, Retenues IR/TRIMF/CFCE, IPRES RG/RCC, CSS-IPRES | **Senegal** |
| Payslip | "Mercans Estonia", endereço em Tartu, moeda GHS | **Estônia / Gana** |
| Global Payment Report | Country Ghana, Currency GHS | **Gana** |
| Indemnity Accrual Register | Nacionalidades Algeria/Canada, company code 6145 | Outro cliente (⚠️ parece ter IDs reais de empregados: não circular) |

## 3. Outros pontos
- "Payslips Local Language" está com idioma **English**; o idioma oficial do Congo é o francês.
- Nenhuma linha estatutária informa prazo, canal (portal) ou formato. A skill tem esses três dados para cada relatório.
- Abas de relatórios de payroll (G2N, Variance, GL, Payment, OT, Field Bonus) são modelos genéricos; não são escopo de Compliance.

## 4. O que corrigiria a matriz (para o time de Implementação)
1. Apagar a aba "note" do Senegal e escrever uma nota do Congo com os 3 relatórios acima.
2. Preencher a aba CG-CNSS (com CAMU e TUS 5,475%) e a CG-DAS-001 (DAS1/DAS2/DAS3, CNSS + DGID, 31/03).
3. Na CG-DGID-001: trocar "XML upload" por formulário online e refazer o exemplo do ITS (total mensal dos 120).
4. Trocar os exemplos de payslip e de pagamento por exemplos do Congo (XAF, francês).

## Conhecimento a absorver
- Congo: 3 declarações estatutárias, todas por portal, sem XML: CNSS mensal (nominativa, inclui CAMU e TUS 5,475%), DGID mensal (agregada, ITS + TUS 2,025%) e DAS anual (CNSS + DGID, 31/03, DAS3 nova em 2026).
- Matrizes de relatório montadas a partir de modelos de outros países carregam resíduos (Senegal, Estônia, Gana). É o mesmo defeito que o check C42 (foreign-country leftovers) pega nos nossos artefatos; vale aplicar à matriz do cliente.
