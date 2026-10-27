---
tipo: pais
codigo: "ES"
etapa_research: "concluida"
etapa_research_data: 2026-09-17
etapa_design: "em andamento"
etapa_design_data: 2026-09-29
etapa_producao: "outro time (Dev/deploy = Drew/Brenet)"
etapa_suporte: "4 aberto(s): CT-4321, HRBS-14528, HRBS-16407, SR-79"
etapa_suporte_data: 2026-10-27
ccg: "v1.6"
ccg_data: 2026-09-17
wtc: "v4.7"
wtc_data: 2026-10-23
dd: "v5.1"
dd_data: 2026-10-20
report_specs: "ES-BASES-001 v2.5; ES-AFI-001 v2.0; ES-AFI-OUT-001 v1.4; ES-CRA-001 v2.3; SEPE CERTIFICA v1.1; M111 v4; ES-M190-001 v3.3; M296 v2.3; SEPE LLAMAMIENTO, ES-CERT-001, ES-FINIQ-001 sem versão"
report_specs_data: 
sir: 
sir_data: 
payslip: 
skill: "payroll-compliance-spain"
tickets_abertos: 4
tickets_conferidos_em: 2026-10-27
atualizado_em: 2026-10-27
---
# Espanha

> Hub do país. Índice: [[00-INDEX]] · Skill: `payroll-compliance-spain`

Espanha é o país mais ativo do serviço (chat: mercans-compliance). Contexto: Research (CCG/WTC/DD) entregue em 2026; o grosso do trabalho atual é Design/Report Specs (SR-xx, com Lily Li como BA e Drew/Brenet como Dev) e Suporte. Datas de tickets são aproximadas (±1 dia). Detalhe estatutário geral: ver a skill, não copiado aqui. Serviços: [[research-pipeline]] · [[design]] · [[suporte]] · [[fronteiras]].

## Situação
| Etapa | Status | Data | Observação |
|---|---|---|---|
| [[research-pipeline]] | ✅ | CCG v1.6 em 2026-09-17 | CCG v1.0 (jan/2026) → v1.1 (HRBS-10121) → v1.2 (HRBS-10272) → v1.3 → v1.6 (17/09, tracked insertions). WTC e DD em evolução contínua por tickets (ver Artefatos). Pesquisa ainda pedida em tickets (HRBS-14528 SILTRA, HRBS-13757 payslip). |
| [[design]] | 🔄 | atualizado 2026-09-29 | Regulation Design v2 (CT-A-507) em produção desde jun/2026 com redesign de ~40% (reteste pendente). Specs: SR-79 em produção (~17/09); SR-144 em produção (~08/09); SR-83 deploy ~15/09 (portal ainda com erro); SR-81/82/85/342/365 em Final Review; SR-80 Open (Dev); SR-432 em Product Mapping (BA). |
| Produção (outro time) | — | | Dev/deploy = Drew/Brenet; ver [[fronteiras]]. |
| [[suporte]] | 🔄 | 2026-10-27 | API 27/10: abertos: CT-4321 Ready for Design, HRBS-14528 Open, HRBS-16407 Open, SR-79 In Review; 14 fechado(s): HRBS-10121, HRBS-10272, HRBS-10563, HRBS-12839, HRBS-13757, SR-144, SR-342, SR-365, SR-432, SR-80, SR-81, SR-82, SR-83, SR-85. Antes (2026-09-28): HRBS-10563, HRBS-12839, HRBS-13757, HRBS-14528 abertos. SLA de HRBS-10563 estourado, de HRBS-12839 em violação. |

## Ficha do país (da skill)
> Resumo do que mais importa para o serviço. Fonte: skill `payroll-compliance-spain`, lida em 2026-10-02. Valores exatos e tabelas: ler a skill. Se divergir, vale a skill.

- **Escopo:** ano fiscal 2026, setor privado, Régimen General da Seguridad Social, EUR. Fora: territórios forais (tributação), RETA/autónomos, regimes especiais, funcionários públicos, IRNR e art. 93 LIRPF (Beckham), bonificaciones/reducciones (só tarifas cheias).
- **Órgãos:** TGSS, AEAT, SEPE, Ministerio de Trabajo y Economía Social.
- **Relatórios principais:** RNT/RLC (mensal), Modelo 111 (mensal/trimestral), Modelo 190 (anual), CRA, Contrat@, Certific@2, Delt@, eventos de afiliação (altas/bajas), Modelos 216/296, recibo individual de salarios.
- **Confiança da skill:** build do zero; veredito PASS WITH NOTES, 0 defeitos críticos, 8 itens abertos (Q1–Q8), 4 abaixo de 95%. Abaixo do piso: RNT/RLC e CRA layouts (~55–60%), Modelo 190 layout/subclaves (~65%), prazo do certificado de empresa (~70%), Modelos 216/296 (~50%). Seções estatutárias do CCG em 93–98%.

**Armadilhas confirmadas** (SKILL.md "Design clarifications" e `07-qa-report.md` §4)
1. Dois motores sobre o mesmo bruto (SS mensal com teto e prorrata das pagas; IRPF projeção anual com tipo único); base IRPF reduz SS, base SS nunca reduz IRPF (engine) → `01-ccg.md`
2. Pagas extraordinárias: prorrata na base de cotização, tributadas no pagamento (engine) → `01-ccg.md`
3. Horas extras fora da base de contingencias comunes, dentro da base AT/EP (que também serve a desempleo/FOGASA/FP); um único campo "base SS" não representa a Espanha (engine) → `01-ccg.md`
4. MEI incide sobre a base CC, não AT/EP (engine) → `01-ccg.md`
5. Quota de solidariedade: art. 19 bis imprime as taxas de 2045 (5,5/6/7%); 2026 = 1,15/1,25/1,46% (DT 42.ª); base é a remuneração sem teto (engine) → `01-ccg.md` §2.3
6. Base mínima = 1.424,40 (diário arredondado 47,48 × 30), não 1.424,50 (engine) → `01-ccg.md`
7. Km: 0,26 (Orden HFP/792/2023); o texto do RIRPF art. 9.A.2.b) ainda diz 0,19 (engine) → `01-ccg.md` §8
8. SMI integral está sujeito a retenção de IRPF em 2026 (piso do art. 81 ainda 15.876) (engine) → `01-ccg.md`
9. Retenção IRPF usa escala nacional única, sem variação por comunidade; forais fora; Ceuta/Melilla com redução de 60% (engine) → `01-ccg.md`
10. Tarifa AT/EP atribuída pela TGSS por CNAE-2025 (LGSS DA 61.ª); ocupação pode sobrepor; empregador não escolhe (engine) → `01-ccg.md` §2.4
11. Prazo de baja passou de 3 para 6 dias corridos em 2026-08-01 (RD 643/2026); reporte do CNO de toda a força de trabalho até 2027-02-01 → `04-reports-spec.md`
12. Modelo 111 de julho (grandes empresas): agosto inteiro + 20 dias de setembro → `04-reports-spec.md` ES-RPT-002
13. Todos os valores de 2026 repousam em prorrogação orçamentária; RDL 16/2025 e RDL 2/2026 foram revogados, nunca citar como vigentes (cadeia: RDL 3/2026 → Orden PJC/297/2026) → `07-qa-report.md` U1
14. Anexo do recibo: "II. DEDUCCIONES" (corrección de errores BOE-A-2014-11988); templates antigos trazem "I." → `06-payslip.md`

**O que mais dá errado** (do QA)
- Tarifa AT/EP: reverificar as taxas por CNAE contra BOE antes de calcular prêmio real (Q1, 93%).
- Percentuais de IT 60% (dias 4–20)/75%: cadeia de citação, RD 53/1980 não lido (Q2, 88%).
- Incerteza jurídica viva: sem Ley de Presupuestos 2026 (U1); SMI × retenção (U2); Directiva de transparência salarial 2023/970 não transposta (U3); semana de 37,5h rejeitada, ET art. 34.1 segue 40h (U4); formato do reporte CNO da RD 643/2026 não especificado (U5).
- Sempre pedir o convenio colectivo para estrutura salarial, antiguidade, pagas, horas extras, jornada < 40h, complemento de IT.

**Lacunas abertas / não confirmado** (candidatos a ticket ou nova pesquisa)
- Layouts de campo RNT/RLC e CRA (Q3, maior lacuna do pack); Modelo 190 registro/subclaves (Q4); prazo do certificado de empresa (Q7); Modelos 216/296 e Beckham não pesquisados (Q8).
- Limite de elegibilidade RED Directo (<25 vs 15 trabalhadores) (Q5); Contrat@ em lote (Q1/Q6, 60%); Modelo 111 caixas 13–27 derivadas (~70%).
- Algoritmos de validação de NIF/NIE/NAF/CCC/IBAN tratados como conhecimento comum, não lei citada.

**Valores-âncora**
| Item | Valor | A partir de | Fonte |
|---|---|---|---|
| Tope máximo de cotização | 5.101,20 €/mês | 2026 | Orden PJC/297/2026 |
| Contingencias comunes | 28,30 % | 2026 | Orden PJC/297/2026 |
| MEI | 0,90 % (0,75 ER / 0,15 EE) | 2026 | Orden PJC/297/2026 art. 16 |
| Solidariedade | 1,15 / 1,25 / 1,46 % (acima de 5.101,20 / 5.611,32 / 7.651,80) | 2026 | LGSS DT 42.ª; Orden art. 17 |
| SMI | 1.221,00 €/mês (17.094/ano) | 2026 | RD 126/2026 |
| Base mínima | 1.424,40 €/mês | 2026 | Orden PJC/297/2026 |

## Artefatos entregues
| Artefato | Versão | Data | Arquivo/local | Observação |
|---|---|---|---|---|
| CCG (Spain Payroll Configuration Guide 2026) | v1.6 (vigente: maior versão) | 2026-09-17 | `Spain_Payroll_Configuration_Guide_2026_v1_6.docx` | Tracked insertions (autor "Claude"). Observação: tickets citam só "2026" (CT-4321) e chat de 12/08 citava V1.3; prevaleceu o chat mais recente. Versões anteriores: v1.1 (HRBS-10121), v1.2 (HRBS-10272), v1.3 (queries da Lily). (chat: mercans-compliance, chat: design-dev-kb) |
| WTC (Spain Wage Type Catalogue) | **V4.7** (vigente: maior versão) | 2026-10-23 | Drive, planilha da Lily (id `1RWOFryO4nK7sdq3WQ19-bSNxdtnmdQqddv15xhZuyZQ`); export em `Downloads\Spain Wage Type Catalogue V4.7.xlsx` | VC 4.7 "Add flag 58223" (Lily Li, Approved). 58223 = Employee Disability Flag (Flag, Lump Sum, Recurring), fórmula `IF(GREATER($hr.disability_code;0);1;0)`. A Lily indicou configurar o flag na entidade (HRBS-16407, seguro-saúde não tributável). A V4.6 (25/09, cópia em Downloads) não tem o 58223. |
| WTC — histórico | V4.4 (vigente até a V4.6/V4.7; regra de 2026-10-05) | ~2026-08-13 | Drive (arquivo da Lily) | V4.4 (SR-83, 79429/79430→B.03; 79432→L.27). Observação: chat de 12/08 cita WTC V3.10 como vigente e design-dev-kb cita V3.9 final; HRBS-10563 editou V3.9 In Progress. Os tickets SR-83/SR-342 já falam V4.2 (~23/07) e V4.4, o que conflita com V3.10 em 12/08. Resolvido em 2026-10-05: vale a maior versão (V4.4). Marco: V3.4 (07/05) / V3.5 tirou 65815 do 296 (SR-85). |
| DD (Spain Data Dictionary) | **V5.1** (vigente; Draft) | 2026-10-20 | Drive [[Research Pipeline/Spain/2026-10-20-modelo145-ESS-STG/Spain_Data_Dictionary_V5.1.xlsx\|Spain_Data_Dictionary_V5.1.xlsx]] (consolidada; md5 a2a230bacd66e88ad2fec2279dce21e2 = cópia em `Research Pipeline/Spain/2026-10-20-modelo145-ESS-STG/`); usuário reimporta na planilha V5.1. Decisão do usuário: tudo do dia numa versão só; a V5.2 (ESS Write, 17:05) não vale mais | ESS = Write nos 98 campos do 145 (confirmado pela Nihita); SITUPER, Disability Degree (%) e Child Count (Total) ficam ESS = Read e sem marca Form 145 (não são casillas do form); Child Count (Total) deve bater com os filhos informados (automático se possível, senão RH no MSS). 2º retorno da STG sobre o ESS do 145: textos oficiais do 145 como ajuda; mappers Family Situation e Disability no texto do form; Spouse NIF só na situação 2 (AEAT val. 4-5); discapacidade em 3 opções + caixa de ajuda (chave 2 derivada para o 190 pos. 167; ajuda só 33-65%, AEAT val. 8/15/17, LIRPF art. 60); ordinais de Descendants/Ascendants na ordem do form/XSD; 16 filhos mantidos (LIRPF 58.1; XSD maxOccurs=16). 305 células em laranja claro FFFCE4D6; códigos internos inalterados. |
| DD (Spain Data Dictionary) — histórico | V5.0 (substituída pela V5.1 em 2026-10-20; Draft) | 2026-10-19 | Drive [[Research Pipeline/Spain/2026-10-19-modelo145-x-DD/Spain_Data_Dictionary_V5.0.xlsx\|Spain_Data_Dictionary_V5.0.xlsx]] (md5 9f83bb035ed615d5fe0131a8105d57ac = cópia em `Research Pipeline/Spain/2026-10-19-modelo145-x-DD/`); usuário importa na planilha ativa | Modelo 145 × DD (caso STG Spain, ESS "Employee Tax Relief Declaration"): +71 linhas em amarelo claro FFFFF2CC, nenhuma linha da V4.9 alterada. Employee Information #10-14 (pensão compensatória, anualidades por alimentos, empréstimo de vivenda, irregular art. 18.2 não aplicado, Relocation Date da mobilidade); Descendants #17-20 (ano de adoção dos filhos 1-4) + #21-80 (Child 5-16, 5 campos cada; teto 16 = XSD AEAT); Ascendants #7-8 (convivência). Critério: só entra campo que a fonte oficial prova ser insumo da retenção ou do Modelo 190. Matriz e fontes: [[Espanha]] pasta da entrega + `raw/docs/oficiais/ES/2026-10-19-*`. |
| DD (Spain Data Dictionary) — histórico | V4.9 (substituída pela V5.0 em 2026-10-19; Draft, SR-432; `Spain_Data_Dictionary_V4.9.xlsx` no Drive, 15/10; a importar na planilha ativa e renomear de V4.0 para V4.9) | 2026-10-15 | Drive | 15/10: VC reorganizado — as 10 entregas registradas como "4" (03/09 a 15/10) viraram 4.0 a 4.9, uma por entrega, data real e descrição curta (SR-82 4.0; SR-79 4.1; AFI-OUT 4.2; SR-83 4.3; AFI-OUT 4.4; Art. 83.3.e 4.5; revisão AFI 4.6; SR-432 4.7/4.8/4.9). 4.9 = campo `$legal_entity_hr.social_security_principal_ccc` (ID Information linha 16; AFI campo 400). Comparado célula a célula com a export de 14/10: nada excluído. A numeração antiga citada abaixo (4.1 SITUPER, 4.5) não corresponde à nova. Histórico: VC 4.6 em 2026-09-23, com remoção de 58 campos AFI em 2026-09-28 e arquivo V4.0 Draft em 2026-09-29 (histórico); renumeração do VC se perdeu no export; todas as linhas B24–B31 leem 4.0. V4.1 (SITUPER, 18/09, Approved) e V4.5 (data não registrada) também citados. Tickets antigos: v3.9 (SR-80/SR-365), v3.12 (SR-79, ~10/09). Anteriores: v3.7 (design v2). |
| ES-BASES-001 Fichero de Bases Spec (SR-79) | v2.5 (vigente: maior versão; arquivo único consolidado em produção ~2026-09-17) | 2026-09-17 | arquivo linkado na descrição do SR-79 | Observação: histórico: SR-79 cita v2.1 → v2.3 → v2.4 → consolidado (08/09); HRBS-13757 cita v2.5 (~01/09). |
| ES-AFI-001 TrabajadoresTramos Spec (SR-80, inbound) | v2.0 (Audit Closure Memo) | ~2026-07 | Drive | Observação: DD v3.9 alinhado. Ticket Open com Lily (14/09). |
| ES-AFI-OUT-001 AFI Outbound (SR-432) | VC 1.4 (vigente: maior versão; arquivo `ES_AFI_OUT_001_v1.0.xlsx`) | 2026-09-29 | Drive | Observação: ticket SR-432 (28/09) cita VC 1.2; chat registra 1.1 (21/09), 1.2 (23/09), 1.3 (25/09, validação A3, escopo 12/7/58), 1.4 (29/09). |
| ES-CRA-001 CRA Spec (SR-81) | V2.3 (vigente: maior versão) | ~2026-08 | Drive | Observação: v2.2 em jun/2026 (Dev, 548 WTs). |
| SEPE LLAMAMIENTO Spec (SR-144) | sem versão | produção ~2026-09-08 | Drive | Orientado a evento (só gera com `sepe_callback_start_date`). |
| SEPE CERTIFICA Spec (SR-145) | v1.1 | ~2026-09-01 | Drive | CodProfesion com padding a 7 dígitos (HRBS-13757). |
| M111 Spec (SR-82) | v4 | 2026-09-02 | Drive | Tabela de campos reconstruída contra dr111e16v18.xls. |
| ES-M190-001 Modelo 190 Spec (SR-83) | v3.3 (vigente: maior versão; "cópia do Compliance", citada em 10/09) | 2026-09-16 | Drive | Histórico: v2.7 (21/07); edições posteriores sem número até 15/09. Deploy ~15/09. |
| M296 Spec (SR-85) | V2.3 (vigente: maior versão; Dev ~ago) | 2026-09-04 | Drive | Histórico: v2.1 em ~mai. |
| ES-CERT-001 Certificado de Retenciones (SR-342) | sem versão | aceite ~2026-09-10 | Drive | Formato verificado contra 5 certificados reais da AEAT (HRBS-13757). |
| ES-FINIQ-001 Finiquito Spec (SR-365) | sem versão | ~2026-08-07 | Drive | Aceite do Dev ~06/08; validação de Gulnaaz pendente. |
| Runbooks AEAT ES-AEAT-INT-OUT-001 / IN-001 | v1.3 | até 2026-07-31 | Drive | Presentación directa por HTTP POST JSON (chat: mercans-compliance). |
| Regulation Design v2 (CT-A-507) | v2 | 2026-06 | Drive/KB | ~90+ passos, ordinais 5–621; substituiu v1 (19 PDFs CT-A-485..505). |
| KB SPAIN - Regulation Specifications (CT-A-485) | atualizada 2026-09-14 | 2026-09-14 | KB Compliance | Espelho de configuração do CCG/WTC (Mohit/Lily). Sub-artigo BCCC Taxability Matrix: 2026-09-07. |

## Valores-chave (com vigência)
Só o que foi decidido/discutido em ticket ou chat. Valores estatutários gerais: skill `payroll-compliance-spain`.

| Item | Valor | A partir de | Até | Fonte |
|---|---|---|---|---|
| Tope máximo de cotização mensal | EUR 5.101,20 (diário 170,04, grupos 8–11) | 2026-01-01 | | Orden PJC/297/2026 (BOE-A-2026-7296) citada em HRBS-10563; confirmado: skill 01-ccg.md §2.2 (arts. 2–3, "from 1 January 2026") |
| Bases mínimas mensais G1 / G2 / G3 / G4-7 | 1.929,00 / 1.599,60 / 1.391,70 / ~1.424,50 (provisório) | 2026 (⚠️ vigência?) | 2026-10-08 (substituída: valores do CT-A-485 divergem da Orden; ver [[correcoes]]) | CT-A-485 (⚠️ sem fonte); chat: design-dev-kb cita CCG. Associação grupo-valor confirmada no PDF de CT-A-485 (leitura pdftotext -layout, 2026-10-05) |
| Bases mínimas mensais G1 / G2 / G3 / G4-7 | 1.989,30 / 1.649,70 / 1.435,20 / 1.424,40 (G8-11: 47,48/dia) | 2026-01-01 | | Orden PJC/297/2026 arts. 2-3 (verbatim), via skill `payroll-compliance-spain` 01-ccg.md §2.2, conferida em 2026-10-08. 1.424,40 = 47,48 × 30 (não 1.424,50 = SMI + 1/6) |
| Bases mínimas part-time por hora G1 / G2 / G3 / G4-11 | 11,98 / 9,94 / 8,65 / 8,58 | 2026 (CCG v1.3) | 11,62 / 9,64 / 8,38 / 8,32 (CCG v1.0) | Orden PJC/297/2026 (chat: design-dev-kb) |
| MEI 2026 | 0,90% (ER 0,75% + EE 0,15%) | 2026 | | Orden PJC/297/2026 (chat: mercans-compliance) |
| Contingências comuns EE / ER | 4,7% / 23,6% | 2026-01-01 | | CT-A-485; CCG; confirmado: Orden PJC/297/2026 art. 4.a) (skill 01-ccg.md §2.3) |
| Desemprego indefinido / temporário (EE/ER) | 1,55/5,5 e 1,6/6,7 | 2026-01-01 | | CT-A-485; CCG; confirmado: Orden art. 33.2.a).1.º e 2.º (skill 01-ccg.md §2.3) |
| FOGASA ER / Formação profissional EE/ER | 0,2% / 0,1% e 0,6% | 2026-01-01 | | CT-A-485; confirmado: Orden art. 33.2.b) e c) (skill 01-ccg.md §2.3) |
| Quota de solidariedade | 0,19/0,96; 0,21/1,04; 0,24/1,22 (excesso 0–10%, 10–50%, >50%); base codes 497/498/499 só no 1º tramo do Bases | 2026-01-01 | | CT-A-492 / CCG; SR-79; taxas confirmadas: Orden art. 17 / LGSS DT 42.ª (skill 01-ccg.md §2.3) |
| Base de cotização em nascimento/cuidado | BCCC do M-2 | 2026 | | Orden PJC/297/2026 (HRBS-10563) |
| Base diária durante IT/risco/nascimento | base do mês anterior ÷ 30 (grupo mensal); ÷ dias reais do mês anterior (grupo diário) | 2026 | | Orden PJC/297/2026 (HRBS-10563) |
| Tempo parcial, base reguladora | soma dos últimos 3 meses ÷ dias do período | ⚠️ vigência? | | RDL 11/2024 (HRBS-10563) |
| BCCC e BCCP durante licença | continuam as duas (nunca zero com trabalhador de alta); worked-days entram nas duas; piso/teto sobre a base mensal | 2026 | | Orden PJC/297/2026 Art. 6.1, 6.3, 6.5 (HRBS-10563) |
| Novas IT (aborto, menstruação incapacitante, interrupção da gravidez) | 60% BR dias 1–20; 75% do dia 21 | ⚠️ vigência? | | LO 1/2023; arts. 169.1.a e 173 LGSS (HRBS-10563) |
| Acidente de trabalho | dia 1 = 100% salário pelo empregador; dia 2+ = 75% da BR (BCCP mês anterior ÷ 30) | 2026 | | Art. 173.1 LGSS (HRBS-10563); confirmado: skill 01-ccg.md (tabela de IT, art. 173.1) |
| Risco na gravidez/lactação | 100% BR, INSS/mútua desde o dia 1 | ⚠️ vigência? | | Arts. 186–187 LGSS (HRBS-10563) |
| Licença parental | 2 de 8 semanas pagas a 100% pela SS | nascimentos a partir de 2024-08-02 | | RDL 9/2025 (HRBS-10563) |
| Prazo de baja AFI | 6 dias corridos | 2026-08-01 | 3 dias | RD 643/2026 (chat: mercans-compliance) |
| Settlement types do Bases em escopo | L00, L02 (corrente); L03, L13, L90–L93, V03, V90 (retro); C02/C03/C90/C91 fora | ⚠️ vigência? | | Manual TGSS SLD Especificaciones Técnicas (ago/2025) (SR-79) |
| ReferenciaExterna do Bases | 8 caracteres: últimos 4 do CCC + MMyy | ⚠️ vigência? | `'BAS'+MMyyyy` (9 caracteres, nunca válido) | Bases.xsd v2.0.2 / spec (SR-79) |
| Código de horas no Bases | "01" (minLength 2, maxLength 3) | mar/2024 | | "SLD: Fichero de Bases – Manual de Usuario" v2.0.2 (SR-79) |
| Severance no CRA | 58184/58186/58188, 0054/E; 62983 também 0054/E | ⚠️ vigência? | 58197 0054/I e 58198 0054/E (errado, abr/2026) | ES-CRA-001 Table 84 (SR-81, HRBS-10563) |
| Severance no Bases | 58197 → base code 701 (nunca 500/601), L03 nos 12 meses anteriores; 58198 não reportado | ⚠️ vigência? | | spec ES-BASES-001 (SR-79); acúmulo L03: RD 2064/1995 Art. 16.2.b/c |
| M190, riscos gravidez/lactação (79429/79430) | Clave B / subclave B.03 | Ejercicio 2025 | B.01 | AEAT Diseños Lógicos 190 / FAQ AEAT (SR-83) |
| M190, licença parental paga (79432) | Clave L / L.27 (isenta) | Ejercicio 2025 | Clave B (21/07) | AEAT Diseños Lógicos 190 (SR-83) |
| M190, subsídios de IT com empregado ativo (79417–79424) | Clave A (pago delegado); B só quando INSS paga direto | ⚠️ vigência? | clave B/pago directo | HRBS-10563 |
| M190, série 6298 (62983 / demais) | Clave L/L05 (despido isento, Art. 7.e LIRPF) / L/L01 | ⚠️ vigência? | clave A subject to withholding | HRBS-10563 |
| M190, Family Situation / Contract Type / Descendants | 3 códigos (claves A, B, C); 1 dígito 1–4, só Clave A, pos. 168; Descendants pos. 223–228 | Ejercicio 2025 | 6 códigos; 2 dígitos 01–05; pos. 266–267 | AEAT Diseños Lógicos 190; Orden HAC/1431/2025 (SR-83) |
| M111, nome da empresa | Denominación (23-82, 60) + Nombre (83-102, 20); complementar pos. 538; justificante anterior 539-551 | desenho vigente | campo único de 40 caracteres | AEAT dr111e16v18.xls (SR-82) |
| M296, retenção não residente com 58205=3 | 19% (saída "1900") | ⚠️ vigência? | 2400 (errado) | spec/BA (⚠️ sem fonte legal) (SR-85) |
| Finiquito / zero floor | regularização por cessação (Art. 87.2.3º RIRPF); base real acumulada; 0% se base − mínimo pessoal ≤ 0 (Art. 86.1/87.3); sem restituição; piso 2% só contratos < 1 ano (Art. 86.2) | ⚠️ vigência? | | RIRPF (SR-365) |
| Projeção anual do IRPF | total esperado no ano civil, pagas extra incluídas uma vez; `MAX(ano anterior; YTD + ainda esperado)` | vigente | | RIRPF art. 83.2 (chat: mercans-compliance); HRBS-10121 usa `MAX(0; var ano anterior − var YTD)` |
| Reduções art. 83.3.e | pensionista 600; NUMDES>2 600; desempregado 1.200; máx. 1.800 | 2026 | pensionista com mais de 2 descendentes = 1.200 só pela leitura literal (descartada) | Algoritmo AEAT 2026 (chat: mercans-compliance) |
| Regra da metade (art. 84) | descendente a 50% salvo direito exclusivo; acumulado 1→1.200 · 2→2.550 · 3→4.550 · 4→6.800 · +2.250 cada | vigente | | RIRPF art. 84 (chat: mercans-compliance) |
| Taxa regularizada | (cuota − retenções feitas) ÷ remuneração restante; piso zero; teto 47% (19% Ceuta/Melilla) | vigente | | RIRPF 87.3/87.5 (chat: mercans-compliance) |
| Regime Ceuta/Melilla estendido a La Palma | redução de 60% da taxa; mínimos 0,8%/6%; teto 19% | 2026-09-10 | | RDL 23/2026 (BOE-A-2026-18828) |
| Algoritmos AEAT 2026 | 1-jan a 9-set: ALGORITMO_2026.pdf / PRET-R200/R260; a partir de 10-set: Algoritmo Retenciones-2026_10sept.pdf / R261 | 2026-09-10 | até 2026-09-09 (versão anterior) | sede.agenciatributaria.gob.es |
| Prorrata de paga extra | entra na base de cotização, não na base de IRPF | vigente | | LGSS art. 147.1; LIRPF 14.1.a; RIRPF 78.1 |
| Limite previdência social | menor entre 30% da renda líquida e 1.500 (+ até 8.500 pela tabela de coeficientes); ingreso a cuenta só sobre o excedente | vigente | | LIRPF art. 52.1; RIRPF 102.1/102.2 |
| Escala IRPF, mínimos, isenções, Beckham, não residente, penhora | ver CCG v1.6 e CT-A-485 (ex.: não residente UE/EEE 19% / resto 24%; Beckham 24% até 600.000 e 47% acima; vale-refeição 11/dia; km 0,26) | 2026 | | CT-A-485 / CCG (⚠️ sem fonte nos tickets; não copiado) |

## Decisões
- ~2026-03: Authorized User ID/`Autorizado` → `$legal_entity_hr.red_authorization_code` (número de autorização RED do operador SILTRA, não é API key) — vale em AFI, CRA e Bases — Wallisson (SR-80)
- ~2026-03/04: 58197 (severance tributável rateado) → base code 701 apenas; 58198 não reportado — Wallisson (SR-79)
- ~2026-04: gerar base code só se valor > 0; sem registros zerados no Fichero de Bases — Wallisson (SR-79)
- ~2026-04: nome do arquivo e `referenciaExterna` únicos entre Legal Entities (rastrear status) — requisito de Illya (Integration), incluído por Lily (SR-79)
- ~2026-04: CRA: "TGSS CRA Action Type" default A; "TGSS CRA Settlement Type" default 00; "blank" não entra no mapper — Wallisson (SR-81)
- ~2026-05: MA/MB/MC/MG (Alta/Baja/Cambio de Contrato/Cambio de Grupo) não são 4 relatórios; são eventos de HR/onboarding fora da SR-80; se em escopo, ticket próprio — Wallisson (SR-80)
- ~2026-05: ES-AFI-001 fica em escopo; spec inbound também precisa de product mapping (HRB lê DatosTramo/DatoSolicitado para saber o que gerar no Bases). Check competitivo (SAP HCM, a3, Sage, etc.). Rebatido parecer do Gemini — Wallisson / Team Lead (SR-80; chat: mercans-compliance)
- ~2026-05: severance no CRA: 58184/58186/58188 (0054/E); 58197/58198 só BASES — Wallisson, após apontamento da BA (SR-81)
- ~2026-06: 65815 sem chave 296 (WTC V3.5) — Wallisson (autocorreção) (SR-85)
- ~2026-06: 62983 → CRA 0054/E + AEAT clave L/L05; 62980–62989 → L/L01 Exempt_InfoOnly — Wallisson (HRBS-10563)
- ~2026-06: 79411 = dia do acidente (empregador); 79412 = 75% BR pago delegado — Wallisson (HRBS-10563)
- 2026-06-18: redesign de ~40% da Regulation Design (`52560` combina IT+IMS por CNAE; floor/ceiling SS anuais) — gaps do implementation expert — Mohit (chat: design-dev-kb)
- ~2026-06/07: não renomear/criar estrutura no WTC da Lily sem aval; parciais de maternidade/paternidade/parental e ERE parcial/total não viram WT (coeficiente/status) — Wallisson (HRBS-10563)
- ~2026-07: as duas bases (BCCC e BCCP) continuam durante qualquer licença (Orden PJC/297/2026 Art. 6) — Wallisson (HRBS-10563, autocorreção)
- ~2026-07: retro (L13, L90–L93, V03, V90) por MesLiquidativo; C02/C03/C90/C91 fora de escopo; Rectification Indicator omitido — Wallisson (SR-79)
- 2026-07-21: Clave B entra no escopo do M190 (pago directo INSS/mútua; 79429/79430 → B.03; 79432 → L.27 após correção de 10/08) — Wallisson (SR-83)
- 2026-07-22: BIK clave G = zero derivado, não fixo — Wallisson (SR-83)
- ~2026-07: M111 clave G (linhas 29–31) acrescentadas — Wallisson (SR-82)
- ~2026-08-04: zero floor no finiquito é comportamento esperado (regularização, Art. 87.2.3º/86.1/87.3 RIRPF), sem correção retroativa, sem piso 2% — Wallisson (SR-365)
- ~2026-08-06: M296 = um registro Type 2 por natureza (D dinheiro, E espécie); Type 1 = soma; contagem de perceptores = nº de Type 2 — Wallisson (SR-85)
- ~2026-08: Bases L03 multi-mês = uma Liquidacion com vários LiquidacionMes (um por mês corrigido) — Wallisson (SR-79)
- ~2026-08: ReferenciaExterna = últimos 4 do CCC + MMyy (versão do Dev) — Wallisson (SR-79)
- ~2026-08-04: SR-80/TrabajadoresTramos = inbound (TGSS→usuário); SR-370/SolicitudTrabajadoresTramos = outbound; responder sempre com nome completo do arquivo — Wallisson/Drew (SR-80)
- Antes de 2026-08: M111 e M190 não são combinados (sem base legal de envio conjunto); integração outbound-dominante (HRBLIZZ gera, cliente submete no portal) — Team Lead (chat: mercans-compliance)
- ~2026-09-01: L00 e L13 coexistem; L03 sempre separado (períodos anteriores); L01 não existe na TGSS; CodProfesion completa até 7 dígitos com zeros à direita — Wallisson (HRBS-13757)
- ~2026-09-08: consolidar a spec do Bases num único arquivo (o linkado no ticket), sem versões paralelas — Wallisson, após reclamação da Lily (SR-79)
- ~2026-09-10/11: settlement type do Bases por gatilho por bloco, não por seleção única de legal entity; `tgss_bases_settlement_type` não é campo de LE — Wallisson (SR-79)
- ~2026-09-11: spec M111/M296 confirmadas; erro persistente de portal vai para o Dev; certificado anual verificado contra 5 certificados da AEAT — Wallisson (HRBS-13757)
- 2026-09-17: art. 83.3.e segue o algoritmo publicado pela AEAT, não a leitura literal do RIRPF — Team Lead / Claude (chat: mercans-compliance)
- 2026-09-18: novo campo `$hr.perceptor_situation` (SITUPER), ACTIVO para toda a população; clave B fora de escopo no CCG e clave C não listada — Team Lead (chat: mercans-compliance)
- 2026-09-23: estilo da coluna W nas specs: só inglês, veredito primeiro, uma linha curta, sem `$` paths — Team Lead (chat: mercans-compliance)
- 2026-09-25/28: AFI outbound Phase 1: 12 campos necessários, 7 constantes, 58 "not needed for now" removidos do DD — Team Lead (chat: mercans-compliance)
- 2026-09-29: reversão: Collective Agreement Code volta ao DD (13 campos AFI necessários) por Boletín Noticias RED 5/2018; segmentos OTD, DBA, DSC, DJD, PIT omitidos; tabela T-12 mantida — Team Lead (chat: mercans-compliance)

## Suporte (tickets)
| Data | Ticket | Assunto | Resolução | Mudou artefato? |
|---|---|---|---|---|
| 2026-10-23 | HRBS-16407 | STG (produção): "Gaps identified in regulation" (seguro-saúde 65630, solidariedade, AT/EP, IRPF sobre BIK). Pedido a nós (Lily): base legal do tipo de retenção (sistema 40% × cliente 39,5%) | Draft v2 (não postado): procedimento RIRPF art. 82 (arts. 83–87), art. 86.1 e 87.3.c (dois decimais), pedido do G2N da execução com 40% + algoritmo AEAT 2026 de 10/09 (truncado no 2º decimal), conferidos ao vivo em 23/10. Pontos 1 e 3 resolvidos pela Lily (flag 58223, WTC V4.7; ajuste AT/EP na entidade); 2 e 4 não pedidos a nós. Rascunho: `rascunhos/2026-10-23-HRBS-16407-resposta.md`. Postado pelo usuário às 13:08 UTC. Chat 23/10: a Nihita indicou o G2N do ticket, mas ele é o de agosto (58118 = 0,395, aplicado 34,85%) e não mostra 40%; ela também pediu a fórmula do 58223. Resposta digitada no grupo (não enviada): pedir o G2N com 40% + fórmula do 58223 da WTC V4.7. Depois, a Nihita mandou um G2N novo (REF-P204-318, ago/2026, gerado em 23/10) dizendo "40 e 35" e pediu para conferirmos a diferença de IRPF (a tabela do Claude dela usa 39,50%). Conferido no xlsx: 58118 = 0,395 (o formato `#,##0.00` mostra 0,40; não existe 40%); 58217 = 0,3485; 2552 = 9.429,51 × 34,85% = 3.286,18; 2572 = 100 × 34,85%. Alíquota calculada = 58115 ÷ 58117 = 48.880,75 ÷ 123.883,63 = 39,45% (art. 87.3.c, truncado) → caixa 3.719,94 (faltaram 433,76), BIK 39,45. Follow-up v4 postado no ticket (16:41 UTC) + resposta curta enviada no chat, seguindo a tabela do ticket (execuções REF-P204-240 e REF-P204-318; "using the system's own figures"): diferença confirmada; causa = alíquota, não base: 2552 = 9.429,51 × 34,85% e 2572 = 1.100 × 34,85% = 383,35 (não houve isenção do seguro-saúde, que era a hipótese do ponto 4); art. 88.5 → 58217 removido ou ≥ calculada; alíquota calculada 39,44% na execução do ticket (58115 48.866,71 ÷ 123.883,63; caixa 3.719,00, BIK 433,84) e 39,45% na de hoje (caixa 3.719,94, BIK 39,45); os 39,50% e o "40" vêm do 58118 = 0,395 arredondado. A cota (58115) não foi refeita pela escala do art. 85. **Chat 24–26/10:** a Nihita perguntou se vale para clientes live e quando corrige; a Lily respondeu (26/10 01:46) que a prioridade da alíquota voluntária foi configurada por instrução da Gulnaaz para o parallel run antes do go-live e que reverte se não for mais necessária (decisão Nihita/Gulnaaz; clientes live sem resposta). A Nihita acha que nem 34,85% nem 39,50% foram aplicados (leitura do "0.35" de 2 casas; 34,85% foi aplicado); a Christina corrigiu o input do seguro-saúde (58105 → 65630, 59 empregados); engine refresh pela Lily no fim do dia 26/10 e rerun. Decisão do usuário: nada a responder (perguntas dirigidas à Lily) | Não |
| 2026-10-19 | Chat STG (sem ticket) | ESS tax relief × Modelo 145: cliente STG disse que faltavam campos do 145 no ESS (call com Nihita Keer e Lily Li, transcript em `raw/chats/2026-10-19-stg-spain-modelo145/`) | 24 itens do 145 analisados contra LIRPF, RIRPF arts. 80-88, algoritmo AEAT 2026 e desenho do 190: 14 já cobertos, 8 incluídos na DD V5.0, 2 não viram campo (assinatura/recibo, RIRPF art. 88.1). Resposta enviada à Nihita no chat em 19/10 | Sim: DD V5.0 |
| 2026-09-25 | SR-79 | Fichero de Bases (ES-BASES-001), spec e testes | Em produção ~17/09; Phase Deployed To Production, ainda In Review; Lily pergunta sobre tipos além de L00/L03/L13 | Sim: spec consolidada, DD v3.12 |
| 2026-09-14 | SR-80 | AFI/TrabajadoresTramos (inbound) | Spec v2.0; ticket Open com Lily (alocação Integration × report config) · **SR-80 Done em 2026-09-28** (API, 27/10) | Sim: spec v2.0, DD v3.9 |
| 2026-09-04 | SR-81 | CRA (ES-CRA-001) | V2.3; aceite ~18/08; Final Review; revisão do registro ETI pendente · **SR-81 Done em 2026-09-14** (API, 27/10) | Sim |
| 2026-09-03 | SR-82 | Modelo 111 | Spec v4 com campos reconstruídos; Final Review | Sim |
| 2026-09-16 | SR-83 | Modelo 190 | Deploy ~15/09; novo erro de portal; posições e campos corrigidos; Final Review | Sim: spec, WTC V4.4, DD |
| 2026-09-04 | SR-85 | Modelo 296 | Estrutura D/E; spec V2.3; Final Review | Sim |
| 2026-09-09 | SR-144 | SEPE LLAMAMIENTO | Em produção ~08/09; evento-driven; pergunta sobre DATOS_USOLIBRE_EMPRESA | Não |
| 2026-09-11 | SR-342 | Employee Tax Certificate | Aceite ~10/09; pay elements novos no WTC | Sim: WTC v4.2 |
| ~2026-08-07 | SR-365 | Finiquito | Zero floor explicado (esperado); aceite Dev ~06/08 | Não |
| 2026-09-28 | SR-432 | AFI Outbound (Mensaje de Afiliación) | Product Mapping; DD VC 4.6 → ajustes até VC 1.4; 77 campos novos em dúvida | Sim: spec + DD |
| ~2026-06 | CT-4321 | Regulation Handover Checklist | Ready for Design; aba "Statutory Research" só para pay elements | Não |
| 2026-09-14 | CT-A-485 | KB SPAIN Regulation Specifications | Artigo da KB (Mohit/Lily), sem resposta nossa | Não |
| 2026-09-08 | HRBS-10563 | WTC, taxability matrix e lógica de licenças | 5 respostas + autocorreção; lógica ainda não funciona em produção (REF-03-069) | Sim: WTC V3.9, DD V3.7 |
| 2026-08-08 | HRBS-12839 | Confirmar se AFI Spec = AFI de pensão (KGS) | Sem resposta no snapshot; SLA violado · **HRBS-12839 Resolved em 2026-08-08** (API, 27/10) | Não |
| 2026-09-18 | HRBS-13757 | Feedback de testes dos relatórios (SEPE, M111/M190/M296, Bases, payslip) | Pending on reporter; correções de Bases v2.5 e CERTIFICA v1.1 | Sim |
| 2026-09-28 | HRBS-14528 | SILTRA Notifications Integration (cliente KGS) | Sem resposta; pesquisa de compliance pedida | Não |
| ~2026 (sem data) | HRBS-10121 | Projeção de variável conta em dobro no IRPF | Corrigido para `MAX(0; prev − YTD)` | Sim: CCG v1.1 |
| ~2026 (sem data) | HRBS-10272 | AT/EP por CNAE, recaída IT, data de incapacidade | Seções 5.1.3, 8.2.1, 7.1.2; 10 campos novos | Sim: CCG v1.2, DD v3.7 |
| 2026-09-16 | (CT-A-485, thread Spain Migration) | IRPF negativo/divergente do A3 em produção (Elessent) | Defeitos em 58163 e 58118: achado de fórmula entregue ao Dev | Não (CCG v1.6 depois) |
| 2026-10-23 | (e-mail Spain Migration Project-Updates, Lily) | STG km: cliente manda km e taxa por km? Taxa tem vigência? | Respondido (enviado pelo usuário): km no 63520 = única entrada de km do WTC V4.7 (58120 isento 0,26; 62520 excedente); taxa não é entrada do WTC, 0,31 pela ata de 28/09; vigência da taxa perguntada à Gulnaaz. Isenção 0,26/km a partir de 2023-07-17 (Orden HFP/792/2023, `raw/docs/oficiais/ES/2026-10-23-BOE-Orden-HFP-792-2023-km-0-26.md`) | Não |

- Rascunhos de comentário SR-432: [[rascunhos/2026-10-11-youtrack-drafts/SR-432|11/10]] · [[rascunhos/2026-10-14-youtrack-drafts/SR-432|14/10]] · [[rascunhos/2026-10-14-youtrack-drafts/v1/SR-432|14/10 v1]] · [[rascunhos/2026-10-15-youtrack-drafts/SR-432|15/10]] · [[rascunhos/2026-10-15-youtrack-drafts/v1/SR-432|15/10 v1]]
- Rascunhos de comentário HRBS-14528: [[rascunhos/2026-10-16-youtrack-drafts/HRBS-14528|16/10]]
- [[rascunhos/2026-10-20-chat-STG-modelo145-feedback|2026-10-20-chat-STG-modelo145-feedback]]: Análise do 2º retorno do cliente sobre o ESS do Modelo 145 (STG Spain)
- [[rascunhos/2026-10-23-HRBS-16407-resposta|2026-10-23-HRBS-16407-resposta]]: HRBS-16407 (STG Spain): referência legal da taxa de retenção IRPF (40% x 39,5%)
- [[rascunhos/2026-10-27-lily-L03-teto-codigos-retro|2026-10-27-lily-L03-teto-codigos-retro]]: Resposta à Lily (rascunho Gmail): teto, códigos e retroativo da migração Espanha

## Pendências
- [ ] Spec ES-BASES-001 (gsheet 1fo4mwbv…, aba Field Options, H39): diz que o excesso de indenização (58188) vai só no 701 e "NOT subject to CC (code 500)". Pelo Manual SLD da TGSS (14/09/2026, tabela de conceptos) o 701 é "Solo si tiene pluriempleo con exclusiones o si se trata del colectivo especial de Artistas (0112)"; o excesso entra em 500 e 601 (RD 2064/1995 art. 23.2.B; LGSS art. 147.1). Contradiz também a linha "Severance no Bases" (58197 → 701) desta nota. Não pedido pela Lily; não alterado. Resposta à Lily de 27/10 (L03, teto, 497–499, retro de ano anterior) gravada como rascunho no Gmail, não enviada: `rascunhos/2026-10-27-lily-L03-teto-codigos-retro.md`; fontes `raw/docs/oficiais/ES/2026-10-27-fontes-L03-teto-codigos-retro.md` (+ `-adendo.md`) — Wallisson.
- [ ] Taxa por km da empresa (e-mail "Spain Migration Project-Updates", Lily 26/10: HR field ou fixo 0,31?). Resposta em rascunho no Gmail (26/10, não enviada): não fixar; a regra fiscal só fixa a parte isenta, 0,26 €/km (RIRPF art. 9.A.2.b, consolidado BOE de 07/10/2026; Orden HFP/792/2023); a taxa paga vem de convenio e varia até por grupo de empregados (XIX Convenio de consultoría, BOE-A-2025-7766, art. 30: 0,27 áreas 1–5 / 0,25 área 6 em 2026; revistas, BOE-A-2025-9698, art. 57: 0,32) → HR field. Fontes: `raw/docs/oficiais/ES/2026-10-26-BOE-*`. **Se a Lily confirmar o HR field:** (1) DD V5.2: campo novo em Country Fields "Company mileage rate (EUR/km)", numérico, base legal acima, valor do convenio/política da empresa; (2) WTC V4.8: explicação de 58120 = km × MIN(taxa; 0,26) e 62520 = km × MAX(taxa − 0,26; 0) (taxa abaixo de 0,26 não gera excedente), citando o campo. Apresentar ao usuário antes de gravar — Wallisson.
- [ ] STG: origem (convenio ou política) e vigência dos 0,31/km — depende do cliente; e-mail de 23/10 à Gulnaaz voltou (gparveen@mercans.com bloqueado) — Wallisson.
- [ ] HRBS-16407 (STG, agosto/2026, achado fora do pedido, 2026-10-23): o holerite aplicou 34,85% de IRPF sobre dinheiro e BIK = campo 58217 Voluntary IRPF Rate, abaixo da alíquota calculada pelos números do próprio sistema (58115 ÷ 58117 = 39,44%). DD V5.1 exige "≥ system-calculated rate"; RIRPF art. 88.5 só permite alíquota voluntária superior. Explica a diferença de IRPF do ponto 4 da Nihita. Não comunicado no ticket — decidir se avisa Nihita/Lily. **2026-10-23:** comunicado à Nihita/Lily (ticket v4 postado e chat enviado): causa e alíquota calculada 39,44%/39,45%. Falta: ajuste do 58217 ou validação "≥ calculada" no sistema (Nihita/Lily). **2026-10-26:** não é defeito: prioridade da voluntária configurada por instrução da Gulnaaz (parallel run); reverter é decisão de Nihita/Gulnaaz.
- [ ] HRBS-16407 (achado fora do pedido, 2026-10-23): 6268 Benefits Gross-Up Full Value = 348,50 = 1.000 (65630) × 34,85%: a gratificação de imposto do seguro-saúde também usa a alíquota voluntária; muda quando o 58217 for corrigido. Não comunicado.
- [ ] HRBS-16407: 58118 (IRPF New Catch-Up Rate) sai arredondado (0,395), não com dois decimais truncados (RIRPF 86.1/87.3.c; algoritmo AEAT TRUNCAR). Achado fora do pedido. **2026-10-23:** confirmado de novo no REF-P204-318 (0,395 em vez de 0,3945) e comunicado (ticket v4 e chat, 23/10). **2026-10-26:** provável origem no nosso CCG v1.6 §6.1 (pseudo-código do catch-up: `Final_Rate = CEILING(TRUNCATE(New_Rate, 2))`), que contradiz o próprio CCG ("truncated to two decimal places… Do not round up") e o art. 87.3.c. Fórmula do 58118 no engine não vista. A fazer: CCG v1.7 com `TRUNCATE(New_Rate, 2)` (janela Pipeline) e pergunta à Lily sobre o arredondamento do 58118 no ticket (janela Suporte), antes do go-live. Ver [[correcoes]] 2026-10-26.
- [ ] Pisos de cotização errados (ver [[correcoes]] 2026-10-08) **confirmados em produção**: G2N STG agosto/2026 com 52981–52984 = 1.929,00 / 1.599,60 / 1.391,70 / 1.424,50 (Orden PJC/297/2026: 1.989,30 / 1.649,70 / 1.435,20 / 1.424,40). Sem efeito nesse caso (base acima do teto).
- [ ] DD V5.1, Country Fields ordinal 23 (Voluntary IRPF Rate): trocar a base legal "Art. 83.3 RIRPF" por art. 88.5 (descrição e Additional Notes). Ver [[correcoes]] 2026-10-23.
- [ ] Modelo 145/ESS (STG): permissão do grupo Employee Tax Relief Declaration no DD está MSS Write / ESS Read; perguntado à Nihita se deve ser ESS Write (implementação, não compliance) — Nihita (chat STG, 19/10)
- [ ] DD: aba oculta "Filteration for SaaS" não tem os 71 campos incluídos na V5.0 (só até Child 4); uso da aba não documentado — perguntar à Lily (achado de 2026-10-20)
- [ ] Modelo 190: reconferir posições citadas na DD V5.0 (197-209, 210-222, 223, 254) quando sair o desenho do exercício 2026 (usado o de 2025) — Wallisson
- [x] Divergência hub × skill: base mínima G4-7 "~1.424,50" e G1/G2/G3 do CT-A-485 — resolvido em 2026-10-08 (propostas 1 e 2 da revisão de 05/10 aprovadas): valores da Orden PJC/297/2026 acrescentados em Valores-chave
- [ ] Corrigir o KB CT-A-485 e as fórmulas dos WTs de piso (52982-52984, 529xx; itens "Group 4-7", "Ceiling Part-Time", "Floor Daily Employee": 1424.50 → 1424.40; G1/G2/G3 → 1.989,30 / 1.649,70 / 1.435,20) e confirmar se esses valores estão em produção — Design / Dev (CT-A-485)
- [ ] Bases mínimas part-time por hora (11,98 / 9,94 / 8,65 / 8,58): conferir se derivam dos pisos antigos; reverificar contra a Orden PJC/297/2026 — Wallisson (revisão 05/10, proposta 15)
- [ ] M190: possível regressão — em ~14/09 o Dev removeu os grupos B/03 e L/27 "por não terem wage type mapeado na spec", mas em ~14/08 dissera que 79429/79430 geram B/03 e 79432 gera L/27; conferir se continuam declarados — Wallisson / Dev (SR-83) [INCERTO] _(ticket SR-83 fechado; pendência mantida: SR-83 Done 22/09, mas o ticket nao resolve a duvida: Drew (14/08) disse que 79429/79430 geram B/03 e 79432 L/27; em 10/09 disse que a planilha 'Income Type Clave and Subclave' nao atribui wage type a B/03 e L/27 (filtro era copia…)_
- [ ] Amostra A3 `A26S0003.AFI`: dita em SR-80 (~09/09) como conferindo com TrabajadoresTramos (inbound) e em SR-432 (~25/09) usada para validar o AFI outbound (entidade de pensão pos. 40–44, 43/43). Esclarecer — Wallisson (SR-80 × SR-432) [INCERTO] _(ticket SR-432 fechado; pendência mantida: Contradicao nao reconciliada no ticket: SR-80 (Wallisson 09/09 e 14/09) diz que A26S0003.AFI confere com TrabajadoresTramos inbound; SR-432 (Wallisson 25/09) usa A26S0003.AFI para validar o AFI outbound (pensao pos. 40-44,…)_
- [x] SR-81: Lily pede revisão de posição/comprimento dos campos do registro ETI comparando A3 `tc260704.cra` com o gerado; sem resposta — Wallisson (SR-81) — _fechada em 27/10 (SR-81): Wallisson, 04/09/2026: tc260704.cra confere byte a byte com o layout ETI oficial da TGSS; spec corrigida (v2.4, campos do Authorized User ID, posicoes 7+). Drew refez o ETI em 08/09 e Lily confirmou aceite em 10/09._
- [ ] SR-81: decidir se External Reference é preenchido com `$payroll.reference_code` — BA/negócio (SR-81) _(ticket SR-81 fechado; pendência mantida: Drew (04/09) deixou External Reference em branco por design e sugeriu $payroll.reference_code, perguntando se devia incluir; ninguem respondeu. Wallisson (04/09) so esclareceu que pos. 42-49 e o nome externo do arquivo, sem…)_
- [x] SR-82: preencher campos em branco colunas B–S (Tax Year, [05], [11], [17], [23], [26], [29], Reserved), acrescentar `$legal_entity_hr.previous_m111_justificante_number` ao DD; impacto de só haver original/substitutiva no campo 538 — Wallisson / Lily (SR-82) — _fechada em 27/10 (SR-82): Wallisson, 03/09/2026: campos B-S confirmados contra dr111e16v18.xls; campo $legal_entity_hr.previous_m111_justificante_number adicionado ao DD v3.10; campo 538 so aceita complementar (nao ha substitutiva no formulario AEAT).…_
- [x] SR-83: explicar lógica de Descendants e remover campos duplicados do DD (pedido de Lily, 16/09) — Wallisson (SR-83) — _fechada em 27/10 (SR-83): Wallisson, 17/09/2026: explicou Descendants (minimo por descendientes; 223-228 sao contagens) e removeu linhas 38-44 duplicadas. Drew implementou em 17-18/09 e deploy em 22/09._
- [ ] SR-83: linha 107 (Accrual Year) bloqueada por `wage_type.accrual_period_year` inexistente (mesma lacuna do SR-342); linhas 55/56 e quota sindical (linha 58) sem wage type; Year of Birth resolvido (0000 fora de A/B/C, deploy 22/09) — Dev (SR-83) _(reescrita em 27/10 a partir do SR-83)_
- [x] M190 no portal ainda com erro (Hermes / REF-04-261, ~15/09) e Ejercicio = 2026 gera rejeição por regra da AEAT — Wallisson (HRBS-13757, SR-83) — _fechada em 27/10 (HRBS-13757): Lily, 22/09/2026: 'M190 ok now' apos Wallisson (19/09) confirmar spec v3.6 e correcoes de Year of Birth/Family/Contract/Descendants. Ejercicio=2026: Lily (31/08 e 11/09) explicou que a AEAT rejeita ano ainda em curso (regra de…_
- [ ] SR-85: campos condicionais T2-031 (endereco), T2-037 (NIF no pais de residencia) e T2-039 (local de nascimento) ainda sem decisao de mapeamento HR no ticket; lista de zeros e Record ID resolvidos (04/09) e T2-038 incluido — Wallisson (SR-85) [INCERTO se incorporado à spec] _(reescrita em 27/10 a partir do SR-85)_
- [ ] SR-365: Finiquito é só para residentes ou também para não residentes? Sem resposta (~07/08); Gulnaaz confirmar nas entidades — Wallisson / Gulnaaz (SR-365) _(ticket SR-365 fechado; pendência mantida: o ticket não mostra a confirmação da Gulnaaz; Wallisson, 10/08/2026: Finiquito e so para residentes (retencao IRPF); nao residentes (IRNR 24%/19%, Modelos 216/296) exigiriam ramo separado inexistente na spec. Deploy 04/09.…)_
- [x] SR-144: bloco `DATOS_USOLIBRE_EMPRESA` (opcional? o que mapear?) — Wallisson (SR-144) — _fechada em 27/10 (SR-144): Wallisson, 09/09/2026: DATOS_USOLIBRE_EMPRESA e opcional, referencia E3|T..|C..|F.. e montada pela empresa (nao e estrutura SEPE), nada a mapear; spec atualizada (linhas 33-34). Sem mudanca de engine._
- [ ] SR-79: Lily pergunta se tipos além de L00, L03, L13 estão em escopo (consultor Raul diz que não são usados); sem resposta — Wallisson (SR-79)
- [ ] SR-79: 563 = SUM(79415;79416) ou 58151 gated (respostas nossas divergentes); 501/602 leem 58554?; 2 pay elements no gatilho do L13 (não nomeados); 604 provável fantasma; H02–H06 e 537 sem wage type no WTC; `part_time_hours_per_week` ausente no DD; teste real de L03 — Wallisson / Produto-WTC (SR-79) [INCERTO]
- [x] SR-432: Lily pergunta se os 77 campos novos no DD devem mesmo ser criados (28/09); chat registra 58 campos removidos e 13 necessários — Wallisson (SR-432) [INCERTO: reconciliar contagens] — _fechada em 27/10 (SR-432): Wallisson, 28/09/2026: dos 77 campos, 12 necessarios, 7 constantes, 58 nao necessarios; em 29/09 corrigiu para 13 necessarios (Collective Agreement Code volta ao DD). Lily em 29/09: 'Mapping done'. Contagem final no ticket: 13…_
- [ ] SR-432/chat: tabelas T-79 e T-103 sem fonte; defeito ODL 2420 corrigido (18-23/len6, 25/09) — Wallisson / Regulatory Affairs (chat: mercans-compliance) _(reescrita em 27/10 a partir do SR-432)_
- [x] HRBS-12839: confirmar se a AFI Spec corresponde ao arquivo AFI de pensão (A26G0002, KGS); sem resposta, SLA violado — Wallisson (HRBS-12839) — _fechada em 27/10 (HRBS-12839): Wallisson, 08/08/2026: 'Confirmed - yes, same report (SR-80)' para a Gulnaaz; ticket fechado com SLA Met._
- [ ] HRBS-14528: pesquisa de compliance sobre formato/uso das notificações SILTRA (.msj, pasta `C:\SILTRA\SVA\Msjrec`), depois volta à Configuração — Wallisson (HRBS-14528)
- [ ] HRBS-13757: SEPE CERTIFICA (padding CNO corrigido 04/09) sem confirmação de aceite no portal; pedido da Gulnaaz de renomear relatórios do Bases com "L" sem resposta; payslip sem código de contrato/antiguidade avaliado em 22/09 (não obrigatório, sem alteração) — Wallisson [INCERTO] _(reescrita em 27/10 a partir do HRBS-13757)_
- [x] HRBS-10563: lógica de licença médica ainda não funciona em produção (REF-03-069, licença abr-mai 2026 deveria usar base de março) — Lily + Wallisson; "further query 4" (gatilho do cálculo segmentado) truncada; ponto 6 (15ª paga, campo "Extra Pay Month N (Accrual Month)") sem resposta nossa — [INCERTO se precisa de ação nossa] — _fechada em 27/10 (HRBS-10563): Wallisson, 08/09/2026: logica base correta, defeito de execucao (dev). Lily, 09/09: base 58151 correta apos restart do engine de producao; 13/10 fechado como corrigido. 'Further query 4' (gatilho) respondida por Wallisson em…_
- [x] SR-342: replicar a resposta "formato correto, verificado contra 5 certificados AEAT" e avaliar se a spec muda — Wallisson (SR-342) [INCERTO] — _fechada em 27/10 (SR-342): Wallisson, 11/09/2026: spec v2.1 atualizada (texto de fechamento do Box 15, art. 108.3 RIRPF) e demais pontos conferem com a amostra A3; Lily 14/09: sem mudanca de mapping; deploy 15/09. A frase 'verificado contra 5 certificados…_
- [ ] CCG: defeitos de fórmula em 58163 (extras) e 58118 (piso zero; 58117 negativo → 58118 ≈ 54,5%); lacunas de input no DD (RESICEME/RENCEME urgente incl. La Palma, PRESVIV, CONYUGE, ANUALIDADES, AÑOADOP, CONVIVENCIA; NUMDES com 5+ filhos); 58292 Tax Year End Date veio 20260930; U13/U280 ainda DDMMYYYY — Wallisson / Dev (chat: mercans-compliance)
- [ ] Ordinais 456/461 do design v2 ainda usam `ADD($58901;MULTIPLY($59009;12))`; confirmar correção em produção; ordinais 161/211 [TBD]; reteste do redesign de 40% — Dev / Compliance (chat: design-dev-kb) [INCERTO]
- [x] Conflito de versão do WTC e do DD — resolvido em 2026-10-05 pela regra 8: WTC V4.4, DD VC 4.6 (maior versão)
- [ ] CT-A-485: significado de 58208 = 2/3/4 (não consta na skill; 2/3 aparecem em linhas de estagiário) — Wallisson [INCERTO]. Resolvido em 2026-10-05: associação grupo-valor confirmada no PDF (G1 1929 / G2 1599,60 / G3 1391,70 / G4-7 1424,50; G3 < G4-7 é fato da fonte, que diverge da skill); rótulo "per km" nas diárias 26,67 / 91,35 / 48,08 é erro de rótulo da fonte: são valores por dia (skill 01-ccg.md §8: 53,34/91,35 com pernoite, 26,67/48,08 sem)
- [ ] Fora da CCG, com outros times: VUSA 1299 duplicados 58176/552, mapeamento 23640→64559, SOP de submissão, retro por período — outros times (chat: mercans-compliance)
- [ ] Itens pré-existentes na CCG (nome de cliente em 7.3.2, referências HRBS e destaques amarelo/ciano) — decisão separada (chat: mercans-compliance)
- [ ] Modelo 190: desde o exercício 2025 a subclave B.03 é de mutualidades de funcionários (Orden HAC/1431/2025, BOE-A-2025-25390); 79429/79430 não vão mais para B.03 e a chave nova não está na norma → confirmar com a AEAT e corrigir WTC/spec M190/skill. Ver [[correcoes]] 2026-10-27 (teste de exatidão T-003).
- [ ] CRA (TGSS): o Manual CRA "Actualizado a 1 de julio de 2026" (§2, CRA 0051 a 0054) manda prorratear E e I nos 12 meses anteriores ao fato, e o excesso sobre a indenização obrigatória entra na base (I, não E; LGSS art. 147.2.c). Conflita com 58188 "non SS subject" no WTC V4.6 e com a entrada de [[correcoes]] usada no T-001. Qual WT leva o 0054 é decisão de design → frente Suporte/design decide; não alterar sem isso. Fonte: `revisoes/2026-10-27-gabarito-T001-T003-T024.md`.

## Consolidado da sessão 2026-10-13
- **AFI (Mensaje de Afiliación), segmento EMP** — fonte: TGSS, *Instrucciones Técnicas Mensaje de Afiliación (AFI)*, v9.7, ed. 05/2025, campos 310 e 400 (texto idêntico na v9.1, ed. 09/2020); PDFs em `raw/docs/oficiais/ES/`.
  - Campo 310 = CCC ao qual o movimento se refere (formato RRSS PP NNNNNNNNN); por trabalhador → `$hr.work_center_ccc` (11 dígitos = 2 província + 9 número).
  - Campo 400 = **CCC principal** da empresa; repete o 310 só em empresa mono-CCC ou quando o movimento é no CCC principal.
- **SR-432** (Lily, 13/10, Work Center CCC como campo do empregado): rascunho gravado — 1º par (campo 310) confirmado; 2º par (campo 400) descrito como CCC principal. Ver [[sessoes/2026-10-13]].

## Entregas (conferências)
- 2026-10-19 · — · Modelo 145 × DD (caso STG Spain): [[Research Pipeline/Spain/2026-10-19-modelo145-x-DD/CONFERENCIA|conferência]]
- 2026-10-20 · — · DD V5.1: 2º retorno da STG sobre o ESS do Modelo 145: [[Research Pipeline/Spain/2026-10-20-modelo145-ESS-STG/CONFERENCIA|conferência]]
- [[rascunhos/2026-10-19-chat-STG-modelo145-DD|2026-10-19-chat-STG-modelo145-DD]]: Chat STG Spain: Modelo 145 x Data Dictionary V5.0 (necessidade de campos)
- [[rascunhos/2026-10-19-compliance-calendar-ES-conferencia|2026-10-19-compliance-calendar-ES-conferencia]]: Conferência dos eventos da Espanha 2026 no Compliance Calendar (nenhum publicado)
- [[rascunhos/2026-10-20-resposta-shruti-alerts|2026-10-20-resposta-shruti-alerts]]: Resposta à Shruti sobre baseline de alertas do Compliance Calendar (método)

## Correções ligadas
- _(entradas a serem consolidadas em [[correcoes]]; rascunho em scratchpad `correcoes-ES.md`)_
- BCCC/BCCP zerados durante licença → as duas bases continuam (Orden PJC/297/2026 Art. 6) (HRBS-10563)
- Per-day só no payout / Seção 5 do doc "BCCC/BCCP Base Logic" → per-day também na base de cotização (HRBS-10563)
- Severance no CRA: 58197/58198 → 58184/58186/58188 (0054/E); 58197/58198 só BASES (SR-81)
- TRL = Tipo de Relación Laboral (não Work Risk Type) (SR-80)
- 79432 = L.27 e não Clave B; 79429/79430 = B.03 e não B.01 (SR-83, WTC V4.4)
- Dupla contagem de renda variável no IRPF corrigida (HRBS-10121, CCG v1.1)
- Série 6298 e payouts 79417–79424: AEAT clave L/L05 e clave A, não clave A/withholding nem clave B (HRBS-10563)
- M190 posições/campos da spec (Family Situation, Contract Type, Descendants, Type 2, campo inventado) (SR-83)
- M111 nome da empresa com 40 caracteres → 60 + 20 (SR-82)
- Fichero de Bases: Control Date, 509/563/603/501-502, ReferenciaExterna, L02/L03, settlement type por LE (SR-79, HRBS-13757)
- CCG v1.6: 58163/58118, art. 83.3.e, ingreso a cuenta; AFI-OUT: datas Excel, DDMMYYYY, prazo de baja, ETI.160 (chat: mercans-compliance)
- DD Voluntary IRPF Rate: base legal "Art. 83.3 RIRPF" → art. 88.5 (2026-10-23, HRBS-16407)

## Fontes
- skill payroll-compliance-spain (lida em 2026-10-02)
- raw/tickets/extracao/2026-10-02-tickets-ES-A.md
- raw/tickets/extracao/2026-10-02-tickets-ES-B.md
- raw/tickets/extracao/2026-10-02-tickets-OUT.md (seção HRBS-10563)
- raw/chats/2026-10-01-mercans-compliance.md
- raw/chats/2026-10-01-mercans-design-dev-kb.md
- raw/chats/2026-10-01-compliance-research.md (apenas menções de contexto: Ilia Virchenko/Integration, AEAT no SI)
