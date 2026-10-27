# Lições aprendidas do `brain-service` para o próximo Research Pipeline

> Extraído em 2026-10-15, só leitura, de `C:\Users\instituto\Documents\brain-service`, da memória do Claude (`~\.claude\projects\c--Users-instituto-Documents-brain-service\memory\`) e de 7 transcrições `.jsonl` da mesma pasta (só as mensagens do usuário e trechos-chave).
> Raiz dos caminhos abaixo: `brain-service\`, salvo quando o caminho começa com `~` ou `memory\`.
> Nada aqui foi inventado. Onde a fonte marca `[INCERTO]` ou `⚠️`, a marca foi mantida.

---

## 1. Inventário

### 1.1 O que é a pasta
O "Brain Service" é a base de conhecimento (wiki em Markdown, no estilo Obsidian) do **serviço de compliance de payroll prestado à Mercans**: Research Pipeline → Design → (produção, outro time) → Suporte. Ele **não** é o pipeline. O pipeline roda em `~/mercans-pipeline/` noutra máquina (`mercans_pipeline_v2_4.sh` → v2.6/v2.8/v2.9, 11 estágios: CCG → Scope Lock-In → Report Specs → DD → WTC → SIR → Payslip → Alignment → Audit+Fixer → QA → Skill). O cérebro guarda o que as skills não guardam: correções, decisões, tickets, fronteiras e o estado de cada país (`CLAUDE.md`, regra 4).

| Item | Conteúdo |
|---|---|
| `00-INDEX.md` | Painel de 49 países × etapa (Research/Design/Suporte) |
| `CLAUDE.md` | Regras 1–8 e os comandos "responde o ticket X" (protocolo de 9 passos validado em 2026-10-13), "fecha a sessão", "ingere", "revisa o cérebro" |
| `correcoes.md` | **90 linhas de erros nossos** já corrigidos (2025-09 a 2026-10-15) |
| `fronteiras.md` | 40 fronteiras de escopo (o que não é do Compliance) |
| `log.md` | 80 entradas, de 2026-10-01 a 2026-10-15 |
| `ESTADO.md`, `PLANO.md`, `sessoes/2026-10-13.md` | Onde paramos, plano de implantação (fases 0–5), retrospectiva |
| `paises/*.md` | 49 hubs de país, mais o README. Cada hub tem valores com vigência e fonte, artefatos e versões, pendências e "Ficha do país (da skill)" |
| `revisoes/` | Revisão dos hubs (2026-10-05: 37 propostas, 33 perguntas) e **catálogo de erros dos tickets v1 (2026-10-08) e v2 (2026-10-09)**, com os padrões F48–F66 propostos para o `country_failure_log.md` do pipeline |
| `rascunhos/` | 26 arquivos: verificações em fonte primária (Congo, Lituânia), gaps do pipeline da Colômbia, respostas de ticket (UA/ES/NL) e pacote de 25 correções para a skill da Ucrânia |
| `raw/` | Material imutável: 3 extrações dos projetos Claude (`raw/chats/`), 101 PDFs e 137 tickets via API (`raw/tickets/`), 17 análises por agente (`raw/tickets/extracao/`), fontes oficiais baixadas (`raw/docs/oficiais/{UA,CG,CO,LT,ES,CA,NL,CI}`) e 3 docs do orquestrador (`raw/docs/`) |
| `scripts/` | `youtrack_fetch.ps1`, `youtrack_anexos.ps1`, `configurar_token.ps1` |
| `memory\` (Claude) | 9 memórias de feedback (100% de confiança antes de apresentar, base = linhagem do Drive, mapeamento fora do escopo etc.) |

### 1.2 O que foi feito ali (cronologia)
- **2026-10-01/02:** estrutura criada. Ingestão de 3 extrações de projetos Claude (compliance-research, mercans-compliance, design-dev-kb) e de 101 PDFs de tickets (04/08–29/09/2026). 49 hubs e 67 correções iniciais (`log.md` l.5–10).
- **2026-10-05:** revisão dos hubs contra as skills `payroll-compliance-*`. Regra 8 (versão vigente = maior número). Pacote de 25 correções para a skill da Ucrânia (`revisoes/2026-10-05-revisao.md`; `rascunhos/2026-10-05-pacote-skill-UA.md`).
- **2026-10-08/09:** varredura de 60 e depois de 137 tickets (API do YouTrack), com o catálogo de erros e os padrões F48–F66 propostos (`revisoes/2026-10-08-catalogo-erros-tickets.md`, `revisoes/2026-10-09-catalogo-erros-tickets-v2.md`).
- **2026-10-09 a 15:** fila real de tickets. UA SR-160/161/162/163/414/415 (specs J05/1-ПВ contra o XSD), ES SR-432 (AFI), Lituânia HRBS-15253 (matriz de cobertura), Congo HRBS-12110 (verificação em fonte primária), Colômbia (7 gaps da revisão Cinthya/Manju → WTC v1.4 e CCG v1.2), Canadá (T4127, DD V1.2), Holanda HRBS-14394, Costa do Marfim (teto CNPS).
- **2026-10-14:** "Internal Certification" de pacotes reais NL/NO/SE/DK/KZ (fora do pipeline, mas são o oráculo de produção; `log.md` l.57–79).

### 1.3 Período coberto
- Tickets analisados: **2024-05 a 2026-10** (137 tickets: 58 de 08–09/2026 com desfecho, mais 79 "novos").
- Correções registradas: **~2025-09 (TR CT-3945) a 2026-10-15**.
- Trabalho na pasta: **2026-10-01 a 2026-10-15**. Git: só 2 commits (2026-10-08). Depois disso, as mudanças estão sem commit (`git status`: CLAUDE.md, correcoes.md, fronteiras.md, log.md e 7 hubs modificados).

---

## 2. Catálogo de defeitos encontrados

Legenda da causa-raiz: **SEC** = fonte secundária ou desatualizada · **ANAL** = analogia, sem lei · **XSD** = spec não comparada com o leiaute/XSD oficial · **PROP** = correção não propagada aos outros artefatos · **VER** = versão errada usada como base · **ESC** = escopo/cobertura · **CALC** = conta, período ou acumulador · **RESID** = resíduo de outro país ou template · **RESP** = nossa resposta de ticket virou a fonte do erro · **FERR** = corrupção por ferramenta.

| ID | País | Artefato afetado | O que estava errado | Causa-raiz | Como foi detectado | Correção | Evidência |
|---|---|---|---|---|---|---|---|
| D01 | ES | WTC V3.9 | Série 6298 com AEAT clave A "subject to withholding"; 62983 (despido isento) incluso | ANAL | Ticket HRBS-10563 | 62983 → L/L05 Exempt_InfoOnly, fora de 111/216; demais 6298 → L/L01 (Art. 7.e LIRPF) | `correcoes.md` l.11 |
| D02 | ES | WTC V3.9 | Payouts 79416–79424 com clave B / "pago directo"; 296 indevido em 79422 | ANAL (metadado de reporte copiado do padrão "pago directo") | HRBS-10563 | Pago delegado = clave A; B só quando o INSS paga direto | `correcoes.md` l.12; `raw/tickets/extracao/2026-10-08-erros-solucoes-ES-*.md` |
| D03 | ES | Design BCCC/BCCP | Bases zeradas durante licença; piso proporcional aos dias trabalhados | ANAL | Autocorreção em HRBS-10563 (4ª resposta) | As duas bases continuam; piso/teto sobre a base mensal (Orden PJC/297/2026 art. 6) | `correcoes.md` l.9–10 |
| D04 | ES | Report Spec CRA | Resposta: CRA reporta 58197/58198 | RESP + mistura de conceitos (WT de cálculo do BASES herdou mapeamento CRA) | BA (SR-81) | CRA = 58184/58186/58188; 58197/58198 só no BASES | `correcoes.md` l.13 |
| D05 | ES | Spec ES-AFI-001 | TRL = "Work Risk Type", com escala 000/500/800 inventada; Epígrafe, CatProfesional e CausaBaseAdicional errados; L01 inexistente | ANAL + invenção | BA (SR-80) | TRL = Tipo de Relación Laboral; campos pelo schema TGSS | `correcoes.md` l.14–15 |
| D06 | ES | WTC V4.4 / spec M190 | 79432 = clave B.01; 79429/79430 = B.01 | ANAL | SR-83 | 79432 = L.27; 79429/79430 = B.03 (AEAT Diseños Lógicos 190) | `correcoes.md` l.16 |
| D07 | ES | Spec ES-M190-001 | Posições erradas (157/167/168/153–156/170/223–228); Type 2 em branco em vez de zeros; campo inventado "White Type 2"; Contract Type com 2 dígitos | XSD (sem diff contra o Diseño Lógico); teste do Dev circular | Rejeição do portal (erro 21902B) | Posições reconstruídas; Type 2 com zeros | `correcoes.md` l.17; catálogo v1 F48 |
| D08 | ES | Spec M111 | Company Legal Name como 1 campo de 40 caracteres; código 57176 | XSD + PROP | SR-82 | 2 campos AEAT (60+20), deslocando todas as posições; 58176 | `correcoes.md` l.18 |
| D09 | ES | Resposta SR-85 | Contestamos a remoção de 65815 do 296 usando uma cópia local do WTC (v3.3) | VER + RESP | Autocorreção | Na V3.5 a remoção estava certa | `correcoes.md` l.19 |
| D10 | ES | Spec M296 | Retenção NR 2400 em vez de 1900; Tax Residence em branco | XSD / falta de regra de zeros | SR-85 | 1900; ISO2 | `correcoes.md` l.20 |
| D11 | ES | Spec ES-BASES-001 | 10 defeitos: Control Date como "late filing"; 509 com flag genérico; C-563 ausente; ReferenciaExterna com 9 caracteres; "S" hardcoded; 501/502 trocados; L01 inexistente; VC sem v2.3/2.4 | XSD + ANAL | SR-79, HRBS-13757 (2026-03 a 09) | Manual TGSS SLD (ago/2025); Bases.xsd v2.0.2 | `correcoes.md` l.21 |
| D12 | ES | Spec SEPE CERTIFICA | CodProfesion com 4 dígitos, sem padding (rejeitava 3123) | XSD (padding) | HRBS-13757 | Zeros à direita até 7 dígitos | `correcoes.md` l.22 |
| D13 | ES | ES-AFI-OUT-001 | Excel converteu ranges de posição em datas (58 células); col. M DDMMYYYY; ETI.160 "N"; ASA na Population Rules; baja em 3 dias | FERR + XSD + SEC (RD 643/2026 não incorporado) | SR-432 (BA) | Posições recalculadas; AAAAMMDD; MB; baja em 6 dias | `correcoes.md` l.24 |
| D14 | ES | CCG v1.0–v1.6 | Projeção da variável contada em dobro; 58163 sem pagas extra; 58118 negativo; leitura literal da 83.3.e; "never ingreso a cuenta"; teto errado; MEI 2026 errada | ANAL + CALC | HRBS-10121; defeito em produção (Elessent) | `MAX(0; var ano anterior − YTD)`; piso zero (RIRPF 87.3.c); 1.200 pelo algoritmo AEAT; teto 5.101,20; MEI 0,90% | `correcoes.md` l.25; `raw/chats/2026-10-01-mercans-compliance.md` §5 |
| D15 | ES | KB / design (CT-A-485) | Bases mínimas G1 1.929 / G2 1.599,60 / G3 1.391,70 / G4-7 1.424,50 (G3 < G4-7, incoerente) | SEC / valor de outro ano | Revisão hub × skill, 2026-10-05 | G1 1.989,30 / G2 1.649,70 / G3 1.435,20 / G4-7 1.424,40; G8-11 47,48/dia (Orden PJC/297/2026 arts. 2–3). ⚠️ KB e fórmulas ainda não corrigidos | `correcoes.md` l.76; `revisoes/2026-10-05-revisao.md` #1–2 |
| D16 | ES | SR-80 × SR-432 | Amostra A26S0003.AFI usada para validar o inbound (TrabajadoresTramos) e também o outbound | Mesmo nome para arquivos oficiais diferentes | Revisão 2026-10-05 (pergunta 4) | SR-80 v2.1, ES-AFI-OUT-001 v1.0, DD v5.0. ⚠️ HRBS-12839 foi fechado com resposta errada | `correcoes.md` l.83; catálogo v1 F53 |
| D17 | ES | Drafts/runbooks | Citação "Art. 23.1.b/c" (L03); "(peculiaridad 35)" sem fonte; pré-produção `prewww10` | SEC (citação de memória) | Revisão | Art. 16.2.b/c RD 2064/1995; `prewww1` | `correcoes.md` l.27 |
| D18 | UA | WTC | Seguro de vida com USC = Não | ANAL (equiparado a seguro médico) | Cliente/especialista local (HRBS-14331) | USC = Sim (Poryadok 1170 p.2 rozd. II) | `correcoes.md` l.28 |
| D19 | UA | WTC/changelog | Changelog dizia que o WT 65894 tinha sido criado; ele não existe | Changelog sem mudança real | HRBS-14331 | Diferença de base, não de flags | `correcoes.md` l.29, l.43 |
| D20 | UA | WTC | Presente de aniversário PIT/ML = Sim; civil contractor PIT/ML/USC = Sim; código 157 "não é de empregado" | ANAL | HRBS-14331 / 12181 | Não/Não, 4DF 160; FOP 4DF 157, WT 62942, Não/Não/Não | `correcoes.md` l.30–31, l.79 |
| D21 | UA | CCG | Lista de exclusão do sick leave (1266) aplicada às férias; "Social Insurance Fund" (extinto em 2023); prazo PDFO "3 dias bancários" universal; base mínima ESV proporcional; complemento para deficientes; proração por dias corridos (Art. 115); 4DF trimestral; média única de 12 meses | ANAL + SEC (fonte desatualizada) | HRBS-12631 / 14331 (CCG v1.1 → v1.2) | Ver as 8 linhas de correção (Poryadok 100; Instr. 449; TCU 168.1; Law 4536-IX) | `correcoes.md` l.33–40 |
| D22 | UA | WTC v3.8 | Gross-up de BIK aplicado aos 109 códigos 4DF = 126; exemplo com base de PIT 2.360 | ANAL + CALC (exemplo digitado, não calculado) | HRBS-12181 | Só não monetário, limitado a 20 PEs; base 2.439,02 | `correcoes.md` l.41–42 |
| D23 | UA | WTC v3.5/v3.7 | v3.5 entregue com nome de arquivo V3.4; v3.7 com só 2 PEs renomeados; changelog citando fórmula em coluna vazia | Versionamento | HRBS-12181 | VC corrigido | `correcoes.md` l.43 |
| D24 | UA | Resposta (HRBS-14331/13389) | Período-base do sick leave = 6 meses; faixas 60/80/100% | RESP + SEC | Contradição entre tickets | 12 meses (Postanova 1266); faixas 50/60/70/100 (Lei 1105 art. 17). ⚠️ O "6 meses" nunca foi retirado por escrito | `correcoes.md` l.77–78 |
| D25 | UA | WTC master | 62180/62181 ESV = Sim e 4DF 101; 65700–65712 ESV = Não; 79406 4DF 128; 65808 4DF 126 | ANAL | HRBS-14331 (especialista local) | 62180/81 ESV = Não, 4DF 127; 65700–712 ESV = Sim; 79406 4DF 101; 65808 4DF 125; 128 só maternidade PFU | `correcoes.md` l.81 |
| D26 | UA | Specs J05 D1/4DF/D5/D6 | Sem HBOS/HBUH e sem 12 tags de cabeçalho; HBOS/HBUH descritos como "assinatura KEP" (são nomes); D5 com C_REG/C_RAJ/C_STI_ORIG "blank" (obrigatórios); D_FILL DD-MM-YYYY (correto: DDMMYYYY, 8); coluna 19 "unconfirmed" (é a patente militar) | XSD (construída a partir de template e não do XSD; o Dev reproduziu a spec) | BA/Dev (SR-160–163); teste da amostra do Dev contra o XSD em 2026-10-09: INVÁLIDA (5 erros, incluindo a ordem da tabela por coluna) | Specs v3/v3.2–3.4; amostras XML validadas no XSD J0510511 | `correcoes.md` l.45, 82, 89; `rascunhos/2026-10-09-UA-SR-162-414-415-respostas.md` l.17–46, 117–131 |
| D27 | UA | Spec D1 v3 | C_REG/C_RAJ/C_STI_ORIG "fixed 26/50/2650" ("Confirmed in tested template") | Valor do template de teste (Kyiv) tomado como constante | Releitura de SR-160/162 (2026-10-13) | Vêm do órgão da ДПС de cada entidade (SPR_STI, 161 órgãos); campos criados no DD V4.1, l.83–85 | `correcoes.md` l.89 |
| D28 | UA | Spec D6 | Amostra validada contra o formulário superado J0510610 (v10) | VER (versão do formulário) | SR-163 | J0510611 (v11), em vigor desde 2026-07-17 | `correcoes.md` l.49 |
| D29 | UA | Spec D5 | Gatilho "só data de início no período" | Regra de população rasa | SR-162 | Orientado a 7 tipos de evento | `correcoes.md` l.46 |
| D30 | UA | Spec 1-ПВ mensal | "Staff" por Employment Contract Type; р.1030 mapeado como **base** de PIT (era o imposto retido) | ANAL / leitura rasa do formulário | Conferência com o formulário (2026-10-10) | Labour Registry Person Category 1–2; soma do ПДФО retido, sem o auxílio-doença | `correcoes.md` l.48; `rascunhos/2026-10-09-UA-SR-162-414-415-respostas.md` l.134–141 |
| D31 | UA | Spec 1-ПВ trimestral | р.3070 marcado "Q4 only" (é trimestral); 7010/7030/7040 como `COUNT distinct` (são médias da Instrução 286); blocos I/II fora de escopo sem registro | Leitura rasa do formulário + ESC | Conferência com o formulário | Registrado como pendência (fora do pedido da BA) | idem, l.147–152 |
| D32 | UA | Pesquisa USC/ESV | Blogs concordavam numa resposta errada | SEC | Lei primária | Usar lei primária ("incidente USC", exemplo permanente) | `correcoes.md` l.50 |
| D33 | UA | WTC | Stock options 4DF 101 + ESV = Não; per diem PIT/ML "Sim" fixo, sem teto | ANAL | Chat mercans-compliance | Depende do recharge; teto na coluna Formula (Dev) | `correcoes.md` l.51–52 |
| D34 | UA | Amostras 1-ПВ (nossas) | Código de Kyiv da ДПС (26) no lugar do Держстат (80); citação de agente "Роз'яснення I.8" (correto: II.2) | Agente citou errado; diretório de outro órgão | Verificação pessoal antes de enviar | Corrigido antes do envio | `sessoes/2026-10-13.md` "Erros nossos" |
| D35 | CO | WTC v1.1–v1.3 / CCG m04 | Incapacidades e licenças (maternidade/paternidade/parental) "exempt within the statutory minimum (ET 206 nums. 1-2)", CO-TX-07 | Leitura errada da lei (ET 206 isenta só indenizações) | Revisão Cinthya/Manju (e-mail 2026-10-13) | Tributáveis, retenção aplica (DIAN Oficio 27408/2019 itens 7.1–7.4); WTC v1.4 / CCG v1.2 | `correcoes.md` l.91; `rascunhos/2026-10-13-CO-v1.2-proposta.md` C1 |
| D36 | CO | WTC v1.3 | ARL = Yes nas incapacidades e nas férias gozadas | ANAL | Revisão G2 | ARL = No (Decreto 1072 art. 2.2.4.2.1.6) | `correcoes.md` l.92 |
| D37 | CO | WTC v1.3 / CCG | Dias 1–2 de incapacidade "IN the payroll-levy base", embora a mesma linha os classifique como não salariais | Contradição interna não detectada | Auditoria de 100% (2026-10-13) | Fora dos parafiscales (Ley 21/1982 art. 17) | `correcoes.md` l.94 |
| D38 | CO | WTC/CCG (cobertura) | Faltavam a licença para cuidado da criança, a licença por perda gestacional, a incapacidade > 180 dias e a retención contingente (AFC/AVC/FVP); zero ocorrências de "contingent" no scope_manifest | ESC (lacuna do sweep) | Revisão do cliente + auditoria | Linhas novas (CO-INCAP-EG-181; CO-OUT-RETCONT); CO-GAP-15 aberto | `correcoes.md` l.95; `rascunhos/2026-10-13-CO-gaps-pipeline.md` |
| D39 | CO | Processo (v1.2) | v1.2 montada sobre a v1.1 do pipeline (24/09); a vigente era a linhagem do Drive (WTC v1.3, CCG v1.1 de 06/10) | VER (`~/mercans-pipeline` defasado) | O próprio usuário | Refeito como WTC v1.4 / CCG v1.2 | `correcoes.md` l.93; `memory\base-linhagem-drive.md` |
| D40 | CO | Batch anterior | Taxa máxima ARL Classe IV errada | SEC | Chat | 6,060% (⚠️ sem data) | `correcoes.md` l.63 |
| D41 | CO | Design/regulation | 1.340 UVT ÷ 12 (limite anual aplicado mensalmente sem acumulador) | CALC (convenção derivada, ~75% de confiança no QA) | HRBS-13627 | Em aberto (F51) | catálogo v1 F51; `paises/Colombia.md` l.117 |
| D42 | CG | Skill payroll-compliance-congo + rascunho HRBS-12110 | (a) CAMU "pelo circuito CNSS" (Décret 2024-131); (b) DAS até 31/03; (c) DAS3 no "art. 116 H–I"; (d) solidarité 0,5% atribuída ao Décret 2024-133; (e) DGID "agregada", "SYSTAF", "sem XML" como regra | SEC (blogs congopaie/PaySpace) + citação não lida | Verificação em fonte primária (JO, CGI), 2026-10-13 | (a) direto à CAMU em 5 dias; (b) janeiro (CGI art. 176); (c) art. 116 I; (d) LFR 2021 art. 42; (e) art. 177 bis exige état nominativo; dia 15, dia 20 em agosto. ⚠️ Não levado à skill | `correcoes.md` l.87; `rascunhos/2026-10-13-verificacao-Congo-HRBS-12110.md` |
| D43 | CG | Resposta HRBS-14055 | "Occupancy Tax não é desconto de folha" | Desconhecimento de tributo local | Réplica do Mohit | TOL de habitação 1.000 FCFA/mês retida na fonte (Loi 34-2013 art. 14, red. LF 2015) | `correcoes.md` l.90 |
| D44 | CG | WTC SS patronal | 3 linhas (Part 1/2/3) com a mesma fórmula combinada (o CCG estava certo) | PROP (CCG → WTC) | HRBS-11806 | Por ramo: PVID 8%/1,2 mi; PF 10,03%/600 mil; AT-MP 2,25%/600 mil | `correcoes.md` l.85 |
| D45 | CG | Design | Limiar de solidariedade anualizado (6.000.000); divisor fixo 12; 58204 como flag bilateral | CALC (valor em fórmula não é dividido pelo engine) | Design-dev-kb | 500.000; `$period_divisor` | `correcoes.md` l.56 |
| D46 | CG | Matriz do cliente (HRBS-12110) | Conteúdo do Senegal; ITS ~10× errado | RESID | Revisão; conta refeita (279.300 = ITS anual de 1 empregado) | Recalculado | `rascunhos/2026-10-13-verificacao-Congo-HRBS-12110.md` §Conta; catálogo v2 §5 |
| D47 | LT | CCG 2026 / Alerta 2026 / matriz / rascunho | 36/60 VDU = €82.962 / €138.270 (VDU implícito de €2.304,50, sem fonte); teto Sodra €138.270; CCG 2026 com a fórmula NPD de 2025; tabela do Alerta "Below 82 962 = 0%" | SEC + valor não recalculado a partir do ato | Verificação em e-seimas/e-TAR (2026-10-13) | VDU €2.312,15 (Lei XV-632 art. 4) → €83.237,40 / €138.729; NPD 747 − 0,49 × (renda − MMA €1.153) | `correcoes.md` l.88; `rascunhos/2026-10-13-verificacao-Lituania-HRBS-15253.md` |
| D48 | LT | WTC/DD V3.0, IG, Release Note | País em produção desde 2025-07-16 com regras de 2025 (20/32%, MMA 1.038); nenhum artefato aprovado tem a faixa de 25% de 2026 | Sem rotina de virada de ano (year-end changeover) | Matriz de cobertura (64 itens: 26 cobertos / 22 parciais / 10 lacunas / 6 fora) | Pendente (parameter sheet 2026) | `rascunhos/2026-10-10-HRBS-15253-matriz-cobertura-Lituania.md` l.73–85, 150 |
| D49 | LT | Resposta HRBS-15253 | "Não há documentação sobre corrigir o GPM313 após o GPM312" | Não lemos nossa própria spec | Leitura da GPM312 spec v1.0, regras 63–65 | Existe (regra 65) | `correcoes.md` l.86 |
| D50 | CI | Hub + skill CI §2.1 + parecer HRBS-14996 + CT-A-620 | Teto CNPS PF/AM/AT-MP = 70.000 XOF; "75.000 é o SMIG, não o teto" | SEC (CLEISS e página "employeur" da CNPS desatualizadas) | E-mail da Sivaranjani (2026-10-15) | 75.000 desde 2023-01-01 (Communiqué CNPS; Décret 2022-986); CT-A-620 reg. 4061 deveria ter 900.000/ano e não 840.000. ⚠️ Levar à skill | `correcoes.md` l.96; `paises/Costa-do-Marfim.md` l.48, 65 |
| D51 | CI | Parecer HRBS-14996 (22/09) | "ITS continua devido" (regime de microempresas) | Regime especial não pesquisado (a skill não tinha "pétrol"/"1068") | Corrigido em 23/09 | Regime dos prestadores petrolíferos: sem ITS na folha | `correcoes.md` l.53 |
| D52 | CI | Design v1.0 | Sem intern/apprentice/first-employment; `_table` sobre partes dava 44.000 para todos; defeito de 12× | ESC + CALC | Design-dev-kb | v1.1 | `correcoes.md` l.54 |
| D53 | GA | WTC v3.0 | Sem o bloco Global 21100–21900 e 23640–23673 (59 códigos); filtro salvo mostrando 8 códigos; VC sem 3.1 | Baseline Global WTC não carregado; FERR (filtro) | HRBS-14978 | v3.1 DRAFT | `correcoes.md` l.55 |
| D54 | TD | CCG / WTC / design / DD | Teto de 5.000 por filho (sem base); transporte como isenção total; severance na TFE; "Czechia Report" no DD | SEC (o 5.000 é o valor CNPS da CI) + RESID | Design-dev-kb | Sem teto (Art. 45-4°); transporte isento até 30%; remover o resíduo | `correcoes.md` l.57–59 |
| D55 | CL | Report Spec LRE | Versão anterior apagada e substituída, com a BA já trabalhando nela | Versionamento | SR-221 (Ruchi) | Nunca apagar versão em uso; versionar | `correcoes.md` l.60 |
| D56 | FR | QA / CCG / manifest / DD | QA autodeclarado 86,5%, real 73,2%; PASS 50.122 (correto 50.112) e faixa 4.440,01 (correto 4.480,01) de fontes secundárias; DPAE/DGFIP-003 com formato errado; "Description (NL)" e "FR-NSSO/FR-FIN" (resíduo da BE); DD com nome v1.0 e conteúdo v1.1; 264 linhas "NO DD COUNTERPART" (≥156 tinham) | SEC + RESID + autoavaliação inflada | QA cross-check / design-dev-kb | Corrigidos no FR-pack | `correcoes.md` l.68–71; `raw/chats/2026-10-01-mercans-design-dev-kb.md` §5 |
| D57 | CA | Payslip / DD | Máximo anual ÷ 12; nome legal e endereço ausentes do DD; OC na lista de PROVINCE_OF_EMPLOYMENT_CODE | CALC + ESC | Pipeline CA / comentário da Ruchi (2026-10-14) | Lesser-of por período; DD V1.2 sem OC (RC4120 Box 10) | `correcoes.md` l.74; `log.md` l.74 |
| D58 | GB | DD v3 | Defaults de AE invertidos (EE 3 / ER 5); LEL 542; tax code 2025/26 | Valor digitado sem fonte | Design-dev-kb | EE 5% / ER 3%; LEL £129/£559/£6.708 (proposta) | `correcoes.md` l.73; revisão 2026-10-05 #13 |
| D59 | IE | Hub/design | PRSI EE 4,1% (é só a Class H); ER 8,9/11,15%; A1 > 527 (é 2025); USC com faixas de 2025 | SEC (valores do ano anterior) | Revisão hub × skill | 4,20% → 4,35% desde 2026-10-01; A1 > 552; USC 2026 | `revisoes/2026-10-05-revisao.md` #9–12 |
| D60 | BW | Hub/design CT-A-507/508 | PAYE com 5 faixas (falta a de 27,5% desde 2026-07-01); gratuity "1/3 isento" | SEC / não atualizado | Revisão hub × skill | 6 faixas; 50% (s.17(3)) | idem #6–8 |
| D61 | BE | CCG | Taxa ER 24,92% para 2026 (é de 2015; desde 2018: 19,88% + moderação até 5,12%); 697,61 × 697,42 no Mod. 9 (conflito aberto); box 360; 90169 rotulado ORIGINAL | SEC | Comentário da Suman no BE-CCG-001-v1.0 | ⚠️ Candidato a correção, não aplicado | `rascunhos/2026-10-13-triagem-emails-desde-09-10.md` G5; `paises/Belgica.md` l.68–91 |
| D62 | NA | WTC 2550/2551 / hub | Teto SSC N$99 (mais tarde N$12.500 / N$112,50); data do novo teto: 2026-03-01 (Gazette) × 2026-09-01 (fontes secundárias) | Valor alegado pelo solicitante, sem fonte | HRBS-13602/14605 | GN 236/2026 (data ⚠️) | `paises/Namibia.md` l.26–31, 63 |
| D63 | NL | Hub / WTC | 52990 "Maximum SS Base" com 5.509 (não é valor de 2026); PE removido do master na v2.0 | Valor e código obsoletos no cliente | HRBS-14394 | Handboek 2026 tabel 11: €6.617,41/mês; teto em 52999 | `rascunhos/2026-10-15-respostas-fila.md` |
| D64 | NL | Resposta HRBS-10545; design | Lente de consultoria fiscal; redesign completo proposto para um bug pontual | Postura | Chat | Lente de fornecedor de software; fix restrito | `correcoes.md` l.64–65 |
| D65 | TR | Resposta CT-3945 | Seguro de vida com 3 limites cumulativos (3 versões da resposta no mesmo ticket) | RESP | Cliente | Só o teto anual é cumulativo | `correcoes.md` l.84 |
| D66 | IE/CL/HU/BG/EG | Designs de IA | Faltavam 21 regs (IE); circularidade inexistente (CL); idade no begin_date; years_worked usado como idade (HU); data em MMdd (EG); 52980 × 52560 (BG) | ANAL / engine desconhecido | Comparação com a produção | Ver correções | `correcoes.md` l.61–62, 66–67, 72, 75; design-dev-kb §5 |
| D67 | Global | Pipeline (Stage 9) | C8 acusava "todo" em ES/PT; C20 dá FAIL como falso positivo em todos os países; erro de parsing Stage 1 → 2 (v2.8) | Regex frágil; check sem calibração | Uso | C8 → `\bTODO\b`; C20 com override; parsing [INCERTO] | `raw/chats/2026-10-01-mercans-compliance.md` §5; `servicos/research-pipeline.md` |
| D68 | Global | Payslip (TR) | Sem bruto e líquido por elemento | Template | Reunião 30/06 | Exibir os dois | `raw/chats/2026-10-01-compliance-research.md` §5 |
| D69 | Global | Planilhas da BA | Claude editou Income Nature/Income Key sem pedido | Escopo | Usuário | Regra desde 2026-05-23: nunca editar | `servicos/research-pipeline.md` |

**Total: 69 linhas de defeito** (várias agrupam de 2 a 10 itens). Por artefato: Report Specs 17, WTC 18, CCG 11, DD 5, design 8, respostas de ticket 8, skill 2, processo/pipeline 4.

---

## 3. Padrões de falha recorrentes (generalizados)

As contagens vêm da tabela da seção 2 e, quando indicado, dos catálogos v1/v2 (60 + 79 tickets).

| # | Padrão | Ocorrências (seção 2) | Exemplos | Padrão do pipeline (existente ou proposto) |
|---|---|---|---|---|
| P1 | **Fonte secundária ou desatualizada adotada como fato** (CLEISS, blogs, PwC, valor do ano anterior) | 14 (D15, D17, D21, D32, D40, D42, D47, D50, D54, D56, D59, D60, D61, D62) | CI teto 70.000 (correto: 75.000 desde 2023); LT VDU €2.304,50 inventado; FR PASS 50.122; IE PRSI de 2025; CG DAS em 31/03 | F44; F63 (proposto) |
| P2 | **Tratamento de WT/flag decidido por analogia, sem lei** | 13 (D01–D03, D05, D06, D18, D20, D22, D25, D33, D35, D36, D66) | UA seguro de vida "como médico"; CO incapacidade "como indenização"; ES clave B "pago directo" | F7/F20; F50 (proposto; citado em 9 tickets novos) |
| P3 | **Spec de arquivo oficial nunca comparada com o XSD/leiaute; teste do Dev circular** | 10 (D07, D08, D10–D13, D26–D28, D30) | M190 (erro 21902B no portal), M111, CERTIFICA, J05 D5 inválido no XSD, D6 contra o formulário v10 | F4/F40/F41; **F48 + F55** (propostos). O check C35 (XSD) só estava ligado à França (`rascunhos/2026-10-09-UA-...` l.108) |
| P4 | **Correção não propagada aos outros artefatos; renomeação de WT sem varredura** | 6 (D08, D44, D48, D63; mais 57176→58176→58552 e 4DF da UA) | CCG CG certo × WTC errado; specs ES com códigos retirados; specs UA depois da mudança de 4DF | F27/F45 (os mais citados: F45 em 16 e F27 em 8 dos 60 tickets); **F49, F52** |
| P5 | **Nossa resposta de ticket virou a fonte do erro** (muda de posição, contradiz o artefato, nunca é retirada) | 8 (D04, D09, D24, D43, D49, D64, D65, "65816 now has the formula") | UA sick leave 6 → 12 meses; TR em 3 versões; SR-85 com cópia antiga | **F52** (10 tickets novos) |
| P6 | **Cobertura/escopo não publicado nem reconciliado** (relatórios, populações, ciclos, tributos locais) | 7 (D31, D38, D48, D51, D52, D57, mais a lista de relatórios NA) | NA VET/IT12E; LT 1-SD/2-SD/9-SD/12-SD/13-SD/NP-SD sem spec; CO retención contingente; CG TOL; CI regime petrolífero | F43/F15/F24; **F54** (o mais frequente: 20 dos 79 tickets novos), F58, F65 |
| P7 | **Limite anual, acumulador ou período mal definido** (÷12, 12×, anual × mensal, calculado × pago) | 6 (D14, D41, D45, D52, D57, D50 [CT-A-620 com 840.000/ano]) | CO 1.340 UVT ÷ 12; CI 12×; CG 6.000.000; CA máximo ÷ 12 | **F51**; F64 (sinal/arredondamento) |
| P8 | **Versão errada usada como base / versionamento quebrado** | 7 (D09, D19, D23, D28, D39, D55, FR "nome v1.0 conteúdo v1.1") | CO v1.2 sobre o pipeline defasado; Chile LRE apagada; UA v3.5 com nome V3.4 | F47; **F59** |
| P9 | **Resíduo de outro país ou de template** | 5 (D27, D46, D54, D56, CCG com IDs da BE) | "Description (NL)" na FR; "Czechia Report" no DD TD; Senegal na matriz CG; Kyiv 26/50/2650 tomado como fixo | C29 (marcadores residuais) |
| P10 | **Contradição interna não detectada / exemplo digitado, não calculado** | 5 (D22, D37, D47 tabela "0%", D61 697,61, Alerta LT) | UA PIT 439,03; CO "non-salary" mas "in levy base"; CCG LT com duas fórmulas NPD | F37/F42 |
| P11 | **Corrupção por ferramenta** | 3 (D13, D53, D-docx) | Excel transformou posições em datas; filtro salvo; `delete_rows` do openpyxl; python-docx não lê `w:ins` | — (regras de edição) |
| P12 | **Autoavaliação inflada do QA / do agente** | 3 (D56, D34, D67) | FR 86,5% × 73,2% real; agente citou "I.8" em vez de II.2; C20 sempre FAIL | F41 |

**Números dos catálogos de tickets** (`revisoes/2026-10-08-...` §2; `...-v2.md` §2):
- 60 tickets: T11 pedido/explicação 33 · T12 fonte ausente/contraditória 27 · T8 versão/sincronização 24 · T6 escopo 23 · T5 spec de relatório 21 · T7 fórmula 21 · T3 código de WT 18 · T4 DD 18 · T10 cliente × artefato 18 · **T1 valor estatutário errado 13** · T2 tratamento do WT 11 · T9 payslip 5.
- 79 tickets novos: T11 30 · T6 20 · T12 19 · T7 16 · T2 12 · T10 12. Padrões mais citados: F54 20 · F52 10 · F50 9 · F43 8 · F57 7 · F44/F41 7.
- Padrões existentes que deixaram passar mais erros (60 tickets): F45 16 · F43 15 · F41 11 · F6 9 · F5 8 · F27 8 · F1/F4/F7/F20 7 cada.
- Desfecho medido pela API: dos 58 tickets que os PDFs davam como "não resolvidos", 35 estavam Resolved/Done. Snapshot manual não serve para medir desfecho.
- Taxa de erro de IA citada pelo design: ~15% em pesquisa estatutária (TR e HU com retrabalho). Acurácia dos designs: IE ~72%, CG 77%, TD ~83%, CI ~85%. Meta ≥ 90–95%.

---

## 4. Regras e melhorias de processo estabelecidas

### 4.1 Escopo e mandato
| Regra | Evidência |
|---|---|
| Mapear ou cruzar os wage types do cliente com o master WTC **não é Compliance**, nem em versão "restrita" (M1 da Colômbia cancelado). Os gaps saem da lei e do que o revisor escreveu | `memory\mapeamento-fora-do-escopo.md`; `rascunhos/2026-10-13-CO-gaps-pipeline.md` "Ajuste de escopo" |
| Papel do Compliance em relatórios "manuais": dizer se o relatório é statutory; o formato do arquivo é da Implementation/Integration (CO: 8 relatórios classificados) | `rascunhos/2026-10-13-CO-gaps-pipeline.md` G4 |
| 40 fronteiras: coluna Formula e colunas laranja = Dev; status S/C/M/N = Config/Product; planilhas Income Nature/Key = BA (nunca editar); WTC do cliente = cliente/team lead; setor público fora; Singapura fora (2026-10-14) | `fronteiras.md` |
| Lente de fornecedor de software de folha, não de consultor fiscal; separar a obrigação do empregador do que o engine calcula | `correcoes.md` l.64; `fronteiras.md` |
| Bug fix tem escopo restrito por padrão (sem redesign) | `correcoes.md` l.65 |
| Decisões de escopo com base: não combinar relatórios sem base legal de envio conjunto (1-ПВ mensal × trimestral; M111 × M190); BG е-болнични/УП-2 fora (benchmark com SAP SF, Workday etc.); Collective Agreement Code de volta ao DD (RED 5/2018) | `raw/chats/2026-10-01-mercans-compliance.md` §3 |
| Pensionados pagos pela empresa (CO G1): decidir o escopo antes de pesquisar | `rascunhos/2026-10-13-CO-G1-pensionados-brief.md` |
| PII de cliente mascarada antes de qualquer processamento por IA (decisão ELT de 2026-06-30) | `servicos/research-pipeline.md` |

### 4.2 Pesquisa de fontes
| Regra | Evidência |
|---|---|
| Fonte primária lida no ato para cada afirmação. Duas secundárias concordando não bastam; template ou valor de outro artefato não é fonte; agente erra citação, então reabrir | `CLAUDE.md` protocolo passo 5; `memory\cem-por-cento-antes-de-apresentar.md`; `servicos/research-pipeline.md` |
| Valor derivado (36 × VDU, 27% × 7,5%, 12 × mensal) é recalculado a partir do ato, nunca copiado de outro documento | `rascunhos/2026-10-13-verificacao-Lituania-...` (VDU); `...-Congo-...` §3 (TUS) |
| Confirmar a **versão vigente** do formulário/XSD/ato (J05 v10 → v11; SPR_VER sem a v11; algoritmo AEAT de 10/09; RD 643/2026). Havendo duas, vale a de número maior | `CLAUDE.md` passo 4 e regra 8; `rascunhos/2026-10-15-respostas-fila.md` SR-162 |
| Antes da web, procurar nos arquivos locais (Downloads, Drive `G:\...\Country Folders\<País>`): a v11 já estava na máquina | `sessoes/2026-10-13.md` lição 2 |
| Divergência portal × lei vira pergunta registrada, não escolha silenciosa (LF 2026 do Congo: dia 15 × dia 20) | catálogo v2 F63; verificação Congo §1b |
| Doutrina posterior vence a anterior (DIAN Oficio 27408/2019 > 321/2015) | `rascunhos/2026-10-13-CO-v1.2-proposta.md` C1 |
| Pesquisa no idioma local; fontes oficiais salvas com data em `raw/docs/oficiais/<CC>/` | `raw/chats/...mercans-compliance.md` §6; `CLAUDE.md` |
| Tributos locais/municipais (TOL do Congo, taxa régionale) ficam fora do radar do sweep nacional: incluir o domínio | `raw/tickets/extracao/2026-10-08-erros-solucoes-AF.md` (lição) |
| Problemas de aquisição: e-TAR/Sodra bloqueiam por Cloudflare/403 (usar extrato literal lido no navegador); Mintrabajo não publica conceitos; CGI do Congo só em edição antiga (~2003); CLEISS e página "employeur" da CNPS CI desatualizados | `verificacao-Lituania` "Pendências"; `CO-gaps-pipeline` G2; `correcoes.md` l.96 |

### 4.3 Construção de artefato
| Regra | Evidência |
|---|---|
| Spec de arquivo oficial nasce do XSD/leiaute e traz **amostra XML validada no XSD oficial** (aba Sample) e a coluna com o elemento por linha | `rascunhos/2026-10-09-UA-...` l.108; `log.md` l.27, 31 |
| Formatos: AEAT numérico vazio = zeros, alfanumérico = espaços; datas AAAAMMDD (AFI) ou DDMMYYYY sem separador (ДПС); windows-1251; `xsi:nil`; ordem da tabela por coluna no J05; `xs:choice` exclusivo | `raw/chats/...mercans-compliance.md` §4; `rascunhos/2026-10-09-UA-...` l.39–46 |
| Título da spec = nome oficial + direção (inbound/outbound) | catálogo v1 F53 |
| Campos que dependem da entidade (C_REG/C_RAJ/C_STI_ORIG) vão para o DD (Legal Entity), não como constante | `correcoes.md` l.89 |
| Nova versão parte da **maior versão na linhagem do Drive/Downloads**, não do `~/mercans-pipeline` (que pode estar defasado). Se o `.gsheet` foi editado depois da export, pedir export nova | `memory\base-linhagem-drive.md`; `CLAUDE.md` passo 7 |
| Edição de xlsx: alterar só o pedido; destacar em azul-claro `FFDDEBF7` (cor não usada no arquivo); conferir célula a célula; patch cirúrgico no XML quando há desenhos (nunca `delete_rows`); conferir well-formedness e hash; não sobrescrever o `.gsheet` (copiar `<nome>_vX.Y.xlsx` para o Drive; o usuário importa) | `CLAUDE.md` passo 7; `servicos/research-pipeline.md` |
| python-docx não lê texto dentro de `w:ins`: conferir o XML antes de afirmar que falta conteúdo na CCG | `memory\base-linhagem-drive.md` |
| CCG com controle de alterações (autor "Claude") ao corrigir a linhagem do Drive; `modules/*.md` do pipeline defasados não devem ser regerados | `paises/Colombia.md` l.65 |
| Contrato do WTC: Global WTC baseline (~300 códigos) é "load-bearing" (Gabão perdeu 59); coluna Report Code por WT (Chile SR-221); coluna de base legal por flag (F50) | `correcoes.md` l.55; `raw/tickets/extracao/...` (SR-221); catálogo F50 |
| Engine: valores dentro de fórmula não são divididos; só Income From/To, Floor e Ceiling são anuais; flags numéricas; não arredondar intermediárias; fatores ≥ 4 casas; combinação de flags não codificada retorna zero sem erro | `raw/chats/...design-dev-kb.md` §6.3–6.4 |
| Skill de país: router fino + `references/`; **restatar o valor com base e vigência**, não só citar o dispositivo (automação S3 do Muneeb: opção 2 escolhida, resposta lida na fonte oficial citada com link) | `rascunhos/2026-10-13-triagem-chat-desde-09-10.md` C3 |

### 4.4 QA e auditoria
| Regra | Evidência |
|---|---|
| Tabela afirmação → fonte primária antes de apresentar; o que não se confirma sai ou fica marcado "não confirmado" | `memory\cem-por-cento-antes-de-apresentar.md` |
| "Tem certeza?" / "100%?" = reverificar do zero | `servicos/research-pipeline.md` |
| Teste mecânico sempre que possível (XML × XSD com lxml; contas refeitas; recontagem por script) | `CLAUDE.md` passo 5; `verificacao-Lituania` #3 |
| Revisão hub × skill revela valores divergentes: IE, BW, GB, ES, CI (37 propostas) | `revisoes/2026-10-05-revisao.md` |
| Auditoria de 100% depois da correção pedida acha erros herdados (CO parafiscales dias 1–2; novas lacunas de licença) | `log.md` l.49 |
| Review Prompt v2: descrição verbal não confirma correção; reconstruir os downstreams com código; ao achar um erro, procurar a mesma classe de erro | `raw/chats/...design-dev-kb.md` §6.7 |
| Score: não citar percentual sem a dimensão de executabilidade; QA autodeclarado não vale | `correcoes.md` l.68 |
| Oráculo de produção: validar contra pacotes reais (A3 na Espanha; Internal Certification NL/NO/SE/DK/KZ achou High em casos reais) | `log.md` l.57–77 |

### 4.5 Entrega e promoção
| Regra | Evidência |
|---|---|
| Nunca apagar versão em que a BA já trabalha; nome do arquivo = VC = conteúdo; uma final vigente; `{CC}-{TYPE}-{SEQ}-v{M}.{m}[-DRAFT-{TICKET}-{data}]` | `correcoes.md` l.60; `servicos/research-pipeline.md` |
| Versão que nunca foi ao Drive não "existe": usar a numeração do que está publicado (DD UA sobe como V4.1, não V4.2) | `log.md` l.39 |
| Atualizar o link do artefato no Monday (quadro Compliance Artifacts) ao promover | `log.md` l.69 |
| Cópia para o Drive com md5 conferido; o usuário importa no `.gsheet` | `log.md` l.30, 52, 64 |
| Comentário de ticket: só o pedido, na altura da pergunta; não repetir o conteúdo do arquivo; tom neutro (confirmar o certo e descrever o resto, com fonte); sem "Correction"; achados fora do pedido vão para o hub | `memory\respostas-ticket-objetivas.md`; `memory\resposta-sem-enquadrar-correcao.md` |
| Nada enviado ou postado sem ok; rascunho (draftComment) conferido sem edição alheia | `CLAUDE.md` passo 9; `log.md` l.59, 62 |
| Carregar `mercans-compliance-workflow` (e a skill do país) **antes** do primeiro rascunho | `memory\skill-antes-de-responder-ticket.md` |
| Se o pedido repete o padrão de um ticket resolvido, aplicar a mesma tratativa (SR-414 → SR-415) | `CLAUDE.md` passo 6 |

### 4.6 Operação e infraestrutura
| Regra | Evidência |
|---|---|
| YouTrack pela REST API (`youtrack_fetch.ps1`); `for: me` funciona e `(a or b) updated:` dá HTTP 400; artigos CT-A-* quebram lote; `.env` não vem no clone; token nunca exibido | `memory\youtrack-via-chrome.md` |
| Rodar `for: me #Unresolved` a cada rodada (SR-432 foi atribuído depois da primeira busca) | `sessoes/2026-10-13.md` lição 6 |
| Medir desfecho pela API, não por PDF exportado à mão | catálogo v2 §2 |
| `raw/tickets/api/` fora do git (dados pessoais; senha colada no HRBS-14714) | `log.md` l.18 |
| Chrome/Claude-in-Chrome: conflito de ponte com o Claude Desktop; selecionar o navegador certo (2 janelas, ID do Chrome) | `log.md` l.60; transcrições de 2026-10-09 e 2026-10-14 |
| Pipeline: `${CODE,,}` no bash 3.2; `tail -1` no Windows; path mangling em `python3 -c`; Stage 2 bloqueante; `--max-turns` | `raw/chats/...mercans-compliance.md` §6 |
| Orquestrador: só Anthropic; modelo por estágio (Haiku 2/4; Sonnet 1/3/5/6/7; Opus 8–11); verificação pós-hoc do arquivo (nunca confiar no "done" do modelo); uma ferramenta estreita por estágio | `raw/docs/2026-09-11-orchestrator-handoff.md` §2–3 |
| "Fecha a sessão": nota da sessão, hubs, `correcoes.md`, `ESTADO.md`, `log.md` (aprendizado contínuo LLM-wiki/KCS) | `CLAUDE.md`; `memory\fecha-a-sessao.md` |
| Internal Certification: `pdftotext` obrigatório (pdfplumber reprovado); bloqueio de zip slip e caminhos > 260; parser de tabela NL descartava linhas | `log.md` l.58 |

---

## 5. Recomendações para o próximo pipeline (checks e gates)

Os IDs C48–C66 seguem a numeração proposta nos catálogos (ainda não aprovada). Os demais são novos e saem desta análise.

### Gate 0: escopo/mandato (scaffolder)
1. **Matriz de cobertura publicada (F54)** por país: cada relatório, população, ciclo e tributo com status Coberto/Parcial/Lacuna/Fora e dono. Modelo: `rascunhos/2026-10-10-HRBS-15253-matriz-cobertura-Lituania.md` (64 itens). Relatório sem dono = fora de escopo explícito.
2. **Eixos obrigatórios da coverage matrix:** populações (F43), **ciclos** (off-cycle, advance, retro, licença entre meses, ordem de runs: F58), **competência × pagamento** (F65) e **tributos locais/regionais** (13º domínio).
3. **Pergunta de escopo para pagamentos não-emprego** (pensionados pagos pela empresa, CO G1) e regimes especiais (petrolífero CI, Diia City UA).
4. **Data de virada (year-end changeover):** o manifest declara o ano fiscal e gera tarefa de parâmetros do ano seguinte (a Lituânia ficou em 2025 em produção).

### Gate 1: fonte (source-hunter)
5. **Tier por fonte no `legal-basis-register`:** primária (diário oficial/autoridade) × secundária (CLEISS, PwC, blogs). **Proibido número de tier B em artefato** sem a primária. Os casos CI 70.000, LT VDU, FR PASS, IE PRSI, CG DAS e BW faixas teriam sido barrados.
6. **Check "valor derivado recalculado":** todo valor que é múltiplo de outro (36 × VDU, 12 × mensal, 27% × 7,5%) traz a conta e o insumo citado; o script recalcula.
7. **Check de vigência do instrumento:** registrar a versão e a data do ato/formulário/XSD (v10 × v11) e a data de consulta; alertar quando houver ato mais novo do mesmo emissor (SPR_VER, наказ 243/284).
8. **Check de citação literal:** artigo e trecho copiados da fonte (o agente errou "I.8", "116 H–I", "Art. 23.1", "Décret 2024-133" para a solidarité).
9. **Doutrina mais recente vence:** registrar a data do parecer/oficio e o superado.

### Gate 2: construção (artifact-builder)
10. **C48 / C55: spec de arquivo oficial gerada a partir do XSD/Diseño Lógico**, com diff mecânico (todas as tags/posições, comprimentos, padding, enums, zeros obrigatórios, ordem, `xs:choice`, `nillable`) e **amostra XML validada pelo XSD** na própria spec. Estender o C35 (hoje só França) a todos os países.
11. **C53:** título da spec = nome oficial + direção; tabela única arquivo × direção × spec × amostra.
12. **C50:** coluna "base legal" por flag de WT (tributo/SS/levy/ARL/parafiscal), com o artigo. Flag sem base legal = bloqueio. Teste negativo: "esta linha é indenização?" (CO), "pago delegado ou directo?" (ES).
13. **C60:** WT de ajuste herda as flags do WT principal ou declara a exceção com fonte.
14. **C51 / C64:** todo limite declara período, acumulador, status calculado/pago, sinal, arredondamento e um teste por banda (inclusive acima do teto e população especial, como o aprendiz da CI).
15. **Global WTC baseline obrigatório** e coluna **Report Code por WT** (Chile); C61: toda contribuição do CCG tem WT ativo.
16. **C56:** todo campo-fonte de spec existe no DD; campos dependentes da entidade (órgão fiscal, CCC principal) nascem no DD Legal Entity.
17. **C57:** checklist de campos legais do payslip por país (bruto e líquido por elemento, nome legal, endereço) e diff template × Payslip Spec 1.
18. **Skill compilada restata valores** (com base e vigência) em vez de só citar o dispositivo, para servir à automação S3.
19. **Proibir constantes vindas de template de teste** (26/50/2650): lint para valores "fixed" com origem "tested template".

### Gate 3: QA/auditoria (qa-auditor)
20. **Contradição interna:** o mesmo WT/conceito com classificações conflitantes na mesma linha ou entre CCG e WTC (CO "non-salary" × "in levy base"; LT duas fórmulas de NPD; tabela "0%").
21. **F42:** exemplos trabalhados recalculados por script (UA 439,03; CG ITS 10×).
22. **C29 ampliado:** resíduo de país/template (`Description (NL)`, `Czechia Report`, IDs de série de outro país, conteúdo do Senegal) e marcadores `TBC`, `Check WTC`, `[VERIFY WITH RA]`, `[provisional]`.
23. **Calibrar os checks:** C20 (falso positivo universal) e C8 (`\bTODO\b`) não podem gerar FAIL automático sem calibração; o score do QA é recalculado por script, nunca autodeclarado (FR 86,5% × 73,2%).
24. **Revisão independente por classe de erro:** ao achar um erro, varrer a mesma classe no artefato inteiro (a auditoria de 100% da CO achou erros herdados).
25. **Oráculo real:** aceite exige comparação com amostra real (A3/portal, pacote de cliente) e exercício fechado.

### Gate 4: entrega/promoção
26. **C59:** nome do arquivo = Version Control = conteúdo; versão revisada nunca apagada; changelog só com mudança real (UA 65894).
27. **Base = maior versão da linhagem publicada (Drive)**: o builder compara com Downloads/Drive antes de qualquer patch e recusa partir de um `~/mercans-pipeline` mais antigo.
28. **Propagação obrigatória (F27/F45/F49/F52):** toda correção (inclusive a feita via ticket) gera um ledger de propagação CCG ↔ WTC ↔ DD ↔ Specs ↔ Skill e reverse lookup de códigos de WT renomeados/retirados (C49) **antes** de responder "done".
29. **Resposta de ticket cita a versão vigente do artefato**; fato novo vindo de ticket entra no CCG/WTC antes da resposta; ticket não vai para Resolved com pergunta aberta (F6).
30. **Handover com folha de configuração por WT** (C66) e lista de versões vigentes.

### Gate 5: operação
31. Reaplicar as correções do cérebro às skills (CG, CI, LT, CO, UA) no próximo Stage 11; hoje elas estão só no `correcoes.md`.
32. Ingerir os padrões F48–F66 no `country_failure_log.md` (v2.12) depois da aprovação.
33. Registrar no `legal-basis-register` os bloqueios de aquisição por site (e-TAR 403, Sodra Cloudflare, Mintrabajo) com o método alternativo (extrato literal pelo navegador, pedido de download manual).

---

## 6. Pendências e itens abertos

| # | Item | Onde |
|---|---|---|
| 1 | **F48–F66 aguardam aprovação** do usuário para ir ao `country_failure_log.md` / `PRESUBMISSION_AUDIT.md` (nada aplicado ao pipeline) | `ESTADO.md`; catálogos v1/v2 §6–7 |
| 2 | Levar às skills: Congo (CAMU, DAS, DAS3, solidarité), CI (teto 75.000; CT-A-620 com 840.000 → 900.000), LT (VDU 2026), CO (DIAN 27408, ARL, parafiscales), UA (pacote de 25 correções) | `correcoes.md` l.87–96; `rascunhos/2026-10-05-pacote-skill-UA.md` |
| 3 | ES: KB CT-A-485 e fórmulas dos WTs de piso 52982–52984 ainda com as bases antigas; bases horárias a reverificar; WT 563 SUM(79415;79416) × 58151; ODL 2420 (comprimento 4 × an6) [INCERTO] | `correcoes.md` l.76; `raw/chats/...mercans-compliance.md` §8 |
| 4 | UA: "6 meses" do sick leave nunca retirado por escrito (conferir a coluna K do WTC V3.9); 1-ПВ trimestral (3070 Q4-only; médias × contagem; blocos I/II fora); ZERO_ZVIT/REASON sem regra oficial; não existe spec do J0500111 (principal ao qual o LINKED_DOCS aponta); seção E nas abas D1/4DF | `paises/Ucrania.md` Pendências; `log.md` l.55, 81 |
| 5 | LT: CCG 2026 / Alerta / WTC / DD / IG em 2025; artigo da Lei I-1336 (teto de 60 VDU) não lido; sem specs de 1-SD/2-SD/9-SD/12-SD/13-SD/NP-SD/PT; origem do 82.962/138.270 desconhecida | `verificacao-Lituania`; matriz |
| 6 | CO: taxa do benefício a partir do dia 541 (nenhuma fonte fixa); tensão p.26 × p.28 da SL1659-2025; CO-GAP-15 (perda gestacional no WTC); escopo dos pensionados (G1); 1.340 UVT ÷ 12; retención contingente sem formato | `rascunhos/2026-10-13-CO-*.md`; `paises/Colombia.md` |
| 7 | CG: prazo CNSS (dia 15 só para > 20 empregados, texto oficial não achado); taxa régionale sem fonte vigente (CGI art. 327 b, edição antiga); prazo DAS (CGI antigo, ~2003) | `verificacao-Congo` |
| 8 | CI: confirmar se o forfait petrolífero cobre CN/TA/TFPC/CE; defeitos do GTN (banda apprentice / flag 58216) com Stop Tax ligado em 09-29 | `raw/chats/...mercans-compliance.md` §8; catálogo v2 §5 |
| 9 | BE: 24,92% × 19,88% + 5,12% no CCG; 697,61 × 697,42; box 360; 90169 ORIGINAL; Field Explanation em inglês; séries 62/65/74 contra o Global WTC; skill BE no MB | `paises/Belgica.md`; `ESTADO.md` |
| 10 | NA: data do teto SSC N$12.500 (2026-03-01 × 2026-09-01); lista coberto/não coberto; VET levy | `paises/Namibia.md` l.63 |
| 11 | NL: HRBS-9807 (DD Contract Type) e HRBS-1535 (58552) fechados sem decisão; conferir 52999 na V3.3 ativa | catálogo v2 §5; `respostas-fila 15/10` |
| 12 | IE HRBS-13860 (classe PRSI J0 para leavers, defeito do motor); GB DD (LEL 542, 16 × 17 letras NI) | catálogo v2 §5; revisão 2026-10-05 |
| 13 | Processo: OD-13 (ticket HRBS edita artefato ou escala para CT?) sem decisão; erro de parsing Stage 1 → 2 da v2.8 sem correção registrada; C20 sem correção; chave Anthropic exposta (rotacionar) | `servicos/research-pipeline.md` |
| 14 | Orquestrador Hermes parado no `DESKTOP-TKRQLF7` (faltam CCG_TEMPLATE_QUESTIONS.md, country_failure_log.md, REFERENCE_CCG_Bulgaria) | `raw/docs/2026-09-11-orchestrator-handoff.md` §4 |
| 15 | Git do cérebro sem commit desde 2026-10-08 (falta configurar nome/e-mail) | `ESTADO.md` |
| 16 | 33 perguntas da revisão de 2026-10-05 e 80 `[INCERTO]` / 44 `⚠️ sem fonte` nos hubs (contagem de 05/10) | `revisoes/2026-10-05-revisao.md` §3, §5 |
