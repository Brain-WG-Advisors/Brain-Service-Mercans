# Skill `payroll-compliance-colombia` recompilada (28/10/2026)

Hub: [[paises/Colombia|Colômbia]] · Entrega anterior dos artefatos: [[Research Pipeline/Colombia/2026-10-22-auditoria-lote1/CONFERENCIA|CONFERENCIA do lote 1 (22–26/10)]]

**O que é:** a skill de 05–06/10/2026 (última publicada, hoje em `~/.claude/skills/.trash/1791418175888-24024-OfSiYE/payroll-compliance-colombia/`) refeita com os artefatos vigentes. Só arquivos locais; nada foi instalado, publicado, enviado nem gravado no Drive. A skill continua em inglês; esta conferência em português.

**Saída:** `payroll-compliance-colombia/SKILL.md` + `references/01-ccg.md … 07-qa-report.md` (mesma estrutura da skill antiga).

## 1. Artefatos usados

| Artefato | Versão | Caminho | md5 |
|---|---|---|---|
| CCG | CO-CCG-001 v1.4 (VC 1.4, 22/10; vigente no Drive desde 26/10) | `Research Pipeline/Colombia/2026-10-22-auditoria-lote1/CO-CCG-001-v1.4.docx` | 8b087e4d008cb2d50506f32566ec48b0 |
| WTC | CO-WTC-001 v1.6 (VC linha 18) | mesma pasta, `CO-WTC-001-v1.6.xlsx` | 05b839bbf8af912c905fc227ed0653e6 |
| DD | CO-DD-001 v1.3 (VC linha 16) | mesma pasta, `CO-DD-001-v1.3.xlsx` | f5a14676f2db93a7e2ed555b36a98bb1 |
| Spec | CO-DIAN-001 v1.0 | `co-report-crosscheck/05-final/CO-DIAN-001-NominaElectronica-Spec.xlsx` | b9f0d815d1dd7dc617fa11ca5145ee55 |
| Spec | CO-DIAN-002 v1.0 | `…/CO-DIAN-002-Formulario350-Spec.xlsx` | ff91e90d88e9cf13c938b49f9c442aa0 |
| Spec | CO-PILA-003 v1.0 | `…/CO-PILA-003-AportesSeguridadSocial-Spec.xlsx` | 12225906639ca12917356719698062ce |
| Spec | CO-DIAN-004 v1.0 | `…/CO-DIAN-004-Formulario220-Spec.xlsx` | a9ebaf29e3217fecd476a66cf99641e1 |
| Spec | CO-DIAN-005 v1.0 | `…/CO-DIAN-005-Formato2276-Spec.xlsx` | f48c5a76a0533bcb505239f02a592e0e |
| Spec | CO-CESANTIAS-006 v1.0 | `…/CO-CESANTIAS-006-ConsignacionAnual-Spec.xlsx` | 93b389077889e34cd828f6f20a3aacee |
| Spec | CO-PILA-007 v1.0 (**nova**, VC 21/10) | `…/CO-PILA-007-AportesPensionados-Spec.xlsx` | 4bfea69840f5140de58860ecea8a573b |
| SIR | CO-SIR-001 v1.1 (Google Doc, não baixável aqui) | Drive `19 - Staturory Integration` | — (aplicada só a mudança do Version history: Res. 13/2021 → Res. 227/2025) |
| Payslip | v1.1 DRAFT (24/09), sem versão nova | — | conteúdo do `06-payslip.md` antigo mantido |
| Mapeamento Res. 13 → 227 | — | `rascunhos/2026-10-15-CO-SIR-001-Res227-sugestoes.md` | art. 1 → 1.5.3.1.1; 3 → 1.5.3.2.2; 4 → 1.5.3.2.3; 8 → 1.5.3.4.1.1; 22 → 1.5.3.8.1 |

md5 dos 10 arquivos conferidos em 28/10 (`md5sum`), iguais aos da CONFERENCIA do lote 1 e ao pedido. Não usados (defasados, como pedido): `~/mercans-pipeline/CO-compliance/08-skill/` e `modules/*.md`.

## 2. Como foi feito

- `01-ccg.md`, `02-wtc.md`, `04-reports-spec.md`, `05-data-dictionary.md`: **texto integral** dos artefatos, convertido por script (python-docx; openpyxl `read_only`, `data_only`). docx: títulos, parágrafos e as 248 tabelas na ordem do documento (sumário com nº de página fica de fora; fluxogramas em bloco de código). xlsx: todas as abas, colunas vazias omitidas, **nº da linha do Excel** na 1ª coluna de cada tabela (para citar "WTC row 156 column Q"). Cabeçalho de cada arquivo: versão, md5, guia de leitura e notas das pendências.
- `03-sir.md`, `06-payslip.md`: texto da skill de 05/10 + troca de citação Res. 13/2021 → Res. 227/2025 + aviso de status no topo.
- `07-qa-report.md`: QA de 27/08 mantido como histórico + **§0 Status update 28 Oct 2026** (situação de cada Q-item contra os artefatos vigentes).
- `SKILL.md`: mesmo formato (frontmatter, 15 clarifications, roteamento, "How to answer", escopo, exemplos), reescrito contra CCG v1.4 / WTC v1.6 / DD v1.3 / specs, com seção nova "Open items pending validation".
- Scripts de conversão e verificação no scratchpad da sessão (`co-skill/conv.py`, `assemble.py`, `verify.py`), fora do cérebro.

## 3. O que mudou × skill de 05/10

### 3.1 Por clarification do SKILL.md

| # | Antes (05/10) | Depois (28/10) | Fonte |
|---|---|---|---|
| 1 SMMLV | COP 1.750.905; instrumento = Decreto 0159/2026 (1469/2025 suspenso) | Valor igual; **instrumento em conflito, validação pendente**: CCG v1.4 diz que em 9-jul-2026 o Consejo de Estado revogou a suspensão e o 1469/2025 voltou (0159 exaurido); skill antiga dizia 0159 | CCG v1.4 Módulo 4.1; hub C21 |
| 2 divisor | 220 até 14-jul / 210 desde 15-jul; Q-19 | Igual; marcado "Circular não relida" (C26) | CCG v1.4 Módulo 4.4 |
| 3 dois cortes | 80→90% em 1-jul; 210 em 15-jul | Igual + resíduo "75%" do §5.1 da Circular (não configurar), validação pendente (C26) | CCG v1.4 Módulo 4.4 |
| 4 noturno 19:00 | igual | igual (35%) | CCG v1.4 Módulo 4.4 |
| 5 exoneração | < 10 SMMLV; custo "~$2.363.800" | Igual; custo como conta: 13,5% × 17.509.050 = 2.363.721,75 antes do arredondamento PILA; pessoa natural com < 2 empregados sem exoneração | CCG v1.4 Módulos 4.1 e 9.1 |
| 6 três bases | igual | igual (IBC 25 SMMLV = 43.772.625; parafiscal sem teto) | CCG v1.4 Módulo 3.1 |
| 7 trava 40% | só pactados (SU 25185) | + **denominador = UGPP ABC Empleadores 2025** (salariais + não salariais pactados + licenças remuneradas; sem indenizações, licenças não remuneradas, incapacidades, prestações; férias fora); WTC `Non-Salary - pacted` × `non-remunerative` | CCG v1.4 Módulo 5.2; WTC v1.6 V1, F393, F395 (decisões #56/#57, 26/10) |
| 8 renta exenta | igual | igual; Q-2 (1/12) citado | CCG v1.4 Módulos 3.1, 5.3, 6 |
| 9 FSP | "1% desde 4 SMMLV + subcuenta 0,2–1,0% desde 16" | **Solidariedade 0,5% + subsistência 0,5% desde 4 SMMLV; subsistência + 0,2/0,4/0,6/0,8/1,0% de 16 a > 20 SMMLV** (totais iguais) | CCG v1.4 VC 1.1 e Módulos 3.1/5.1; WTC VC 1.3 |
| 10 arredondamento | igual | igual | CCG v1.4 Módulo 1.5 |
| 11 férias | férias entram no IBC e na base parafiscal | **Férias gozadas:** saúde e pensão sobre o IBC anterior às férias (Decreto 780 art. 3.2.5.1), sem ARL (Decreto 1072 art. 2.2.4.2.1.6 num. 1.3), férias na base CCF/SENA/ICBF. **Férias em dinheiro:** fora de saúde/FSP/ARL/pensão, dentro dos parafiscais | CCG v1.4 Módulo 5.2 (novidades VAC/LR); WTC v1.6 linhas 156 e 324 |
| 12 enum DIAN | "conflito não resolvido" | **Conflito entre artefatos, validação pendente:** CCG v1.4 diz resolvido pelo DIAN Concepto 013840 (int. 1568) de 1-out-2025 (reportar 80/90%); CO-DIAN-001 Field Options linha 65 mantém o valor do anexo até "posição escrita da DIAN" | CCG v1.4 Módulo 4.4; CO-DIAN-001 Field Options linha 65 |
| 13 canais | NE M2M; 350 e 2276 portal; PILA via operador | Igual + PILA pensionados (CO-PILA-007) e depósito de cesantías via operador (CO-CESANTIAS-006) | CCG v1.4 Módulos 10.1/10.2; specs (Report Matrix) |
| 14 payslip | Res. 13/2021 arts. 5, 24, 26 | **Res. 227/2025 arts. 1.5.3.3.1 / 1.5.3.8.3 / 1.5.3.8.5 (formerly 5/24/26), nº pendente de validação (C19)** + divergência nova: lista de 13 itens do CCG v1.4 10.3 ≠ texto literal do art. 5 em `06-payslip.md` §2.1 | CCG v1.4 Módulos 1.1 e 10.3; hub C19 |
| 15 reforma previdenciária | não vale em 2026; data 1-abr-2027 só imprensa | Igual na conclusão; CCG v1.4 cita C-264 de 25-ago-2026 e 1-abr-2027; **data não confirmada em fonte A (C24)** | CCG v1.4 Módulo 5.1 |

Outras mudanças no SKILL.md: descrição (frontmatter, 920 caracteres) cita as versões dos artefatos e os 7 relatórios (inclui PILA pensionados); roteamento por Módulo do CCG (1–13) e por spec ID (CO-DIAN-001 … CO-PILA-007); "How to answer" pede citação artefato + local (Módulo, linha/coluna); escopo: CO-RPT-007 (MinTrabajo) fora do escopo, 2276 com XML DERIVED, adiantamento mensal de cesantías não operável, códigos `CO-` sem número; exemplo "GOOD" atualizado para o conflito do enum.

### 3.2 Por arquivo de referência

| Arquivo | Antes (05/10) | Depois (28/10) | Tamanho antigo → novo (bytes) |
|---|---|---|---|
| `SKILL.md` | roteador + 15 clarifications | idem, atualizado + tabela de pendências | 16.770 → 23.494 |
| `01-ccg.md` | texto de pesquisa de ago/2026 (14 seções próprias) | texto integral do CCG v1.4 (13 módulos do template) + notas | 89.686 → 475.161 |
| `02-wtc.md` | catálogo resumido por elemento XSD da nómina electrónica (11 seções) | WTC v1.6 integral: 6 abas, 405 linhas do catálogo com as colunas de sujeição | 44.354 → 353.389 |
| `03-sir.md` | 7 integrações, Res. 13/2021 | idem + Res. 227/2025 (mapa do SIR v1.1) + aviso (nome CO-SIR-001 v1.1, §007 fora do escopo, defeitos C27) | 28.872 → 32.046 |
| `04-reports-spec.md` | CO-RPT-001…007 (PILA ~55%, 350 ~60%) | 7 specs v1.0 integrais (9 abas cada) + índice com IDs antigos → novos; **CO-PILA-007 é novo** (não existia na skill antiga) | 42.436 → 1.087.570 |
| `05-data-dictionary.md` | dicionário resumido | DD v1.3 integral (8 abas) | 24.554 → 157.575 |
| `06-payslip.md` | Res. 13/2021 | idem + Res. 227/2025 (formerly) + aviso C19 e divergência da lista | 24.213 → 27.431 |
| `07-qa-report.md` | QA de 27/08 | idem + §0 status em 28/10 | 36.190 → 41.927 |

Total novo: ~2,2 MB (antes ~307 kB). O `04-reports-spec.md` sozinho tem ~1,09 MB; ao subir para o claude.ai, conferir se o limite de tamanho da skill aceita (não testado).

Correspondência de IDs de relatório: CO-RPT-001 → CO-DIAN-001; -002 → CO-DIAN-002; -003 → CO-PILA-003; -004 → CO-DIAN-004; -005 → CO-DIAN-005; -006 → CO-CESANTIAS-006; -007 → fora do escopo (C29); CO-PILA-007 novo.

## Arquivos principais
- [[Research Pipeline/Colombia/2026-10-28-skill/payroll-compliance-colombia/SKILL|SKILL.md]]: roteador da skill recompilada (não instalada no claude.ai).
- [[Research Pipeline/Colombia/2026-10-28-skill/payroll-compliance-colombia/references/07-qa-report|07-qa-report]]: seção 0 = situação de cada ponto em aberto em 28/10 contra os artefatos vigentes.
- Os outros arquivos de `references/` (01–06) ficam fora do cofre do Obsidian: são cópia dos artefatos (regra 4 do CLAUDE.md).

## 4. Pendências mantidas abertas (não apresentadas como resolvidas)

| Item do hub | Onde aparece na skill | Tratamento |
|---|---|---|
| F6-20261027-CO-C19 (Res. 13 → 227, nº dos arts. 5 e 24) | SKILL #14 e tabela; `01-ccg.md` notas; `03-sir.md`; `06-payslip.md` | cita 1.5.3.3.1 / 1.5.3.8.3 / 1.5.3.8.5 "formerly 5/24/26", sempre com "pending validation" |
| F6-20261027-CO-C21 (SMMLV, instrumento) | SKILL #1 e tabela; `01-ccg.md` notas; `06-payslip.md` aviso; `07` §0 | valor COP 1.750.905; instrumento em conflito (0159/2026 × 1469/2025) |
| F6-20261027-CO-C24 (reforma, data 1-abr-2027) | SKILL #15 e tabela; `01-ccg.md` notas; `07` §0 Q-24 | nada vale em 2026; data não confirmada em fonte A |
| F6-20261027-CO-C26 (Circular 101/2025, §5.1 "75%", divisor) | SKILL #2, #3 e tabela; `01-ccg.md` notas; `07` §0 Q-19 | escada 80/90/100 e divisor 220→210 como no CCG; Circular não relida |
| C15, C22, C25, C31 (também tocam a skill) | tabela do SKILL; notas dos arquivos | registrados como conflito, sem escolher lado |

## 5. Achados fora do pedido (não corrigidos; para o hub/pendências)

1. **Lista dos 13 itens do art. 5 (Res. 13/2021):** CCG v1.4 Módulo 10.3 imprime lista em inglês diferente do texto literal em espanhol do `06-payslip.md` §2.1 (acrescenta data de pagamento, período e país/departamento/município; omite "denominado expresamente", firma digital e provedor de tecnologia). A tabela de requisitos formais do mesmo Módulo 10.3 ainda diz "(art. 26)", numeração antiga.
2. **Enum de horas extras:** CCG v1.4 Módulo 4.4 (Concepto DIAN 013840/2025 → reportar 80/90%) × CO-DIAN-001 Field Options linha 65 (mantém o valor do anexo até posição escrita da DIAN) e exemplos das linhas 109–124 (100/75/150).
3. **Adiantamento mensal de cesantías:** CO-DIAN-001 Population Rules linha 24 ainda chama de "a configurable engine option" o depósito mensal da Ley 2466 art. 64 par. 1, retirado da CO-CESANTIAS-006 em 23/10 (ligado ao C20).
4. **CO-PILA-007 Example Analysis** cita "SMLMV 2026 = COP 1,750,905 (Decreto 0159 de 2026)" (instrumento, C21).

## 6. Conferência

- **Completude da conversão** (script `verify.py`: cada célula/parágrafo não vazio do artefato procurado no .md): WTC 8.363 células, 0 faltando; DD 3.976, 0; specs 1.544 + 5.053 + 1.996 + 2.005 + 1.554 + 4.203 + 2.647, 0 faltando; CCG 7.544 parágrafos, 113 sem correspondência literal = entradas do sumário (com nº de página) e fluxogramas de várias linhas, conferidos à mão como presentes (em bloco de código).
- **Valores do SKILL.md** conferidos por grep no texto convertido, com Módulo localizado: 1.750.905, 17.509.050, 43.772.625, 249.095, 52.374, 220/210, 80/90%, 19:00, FSP 0,5/0,5 + 0,2–1,0%, 100/1.000/half-to-even, SendNominaSync/500 KB, Auto 841, C-264, art. 114-1 inciso 2. Conta da exoneração refeita: 17.509.050 × 0,135 = 2.363.721,75.
- **grep "0159"**: só onde se justifica — SKILL #1 (conflito), `01-ccg.md` e `02-wtc.md` (histórico do instrumento, texto do artefato), `04-reports-spec.md` CO-PILA-007 Example Analysis (resíduo do artefato, achado 4), `07-qa-report.md` (histórico, anotado "now in conflict").
- **grep "000013"**: só como "formerly"/compilada, ou dentro de linhas de Version Control e avisos que descrevem a própria troca (CCG VC 1.3 e Módulo 10.1 "which compile…"; WTC VC 1.5; DD VC 1.2; avisos de `03-sir.md` e `06-payslip.md`; tabela de pendências do SKILL).
- **Lint de marcadores** (TODO/TBD/FIXME/XXXXX/placeholder/RESEARCH-GAP): 0 no SKILL.md; nas referências só ocorrências legítimas — "todos" (espanhol) e "the placeholders used in the worked example (AFP001…)" no CO-PILA-003 Example Analysis (texto do artefato).
- Frontmatter: `name: payroll-compliance-colombia` igual; `description` com 920 caracteres (< 1024).

## 7. O que não foi feito

- SIR v1.1 não baixado (Google Doc); `03-sir.md` é o texto da skill antiga com a única mudança registrada no Version history do SIR v1.1.
- Não lidos em fonte primária: auto do Consejo de Estado de 9-jul-2026, Decreto 0159, Circular 101/2025, Sentencia C-264/2026, tabela de concordância da Res. 227/2025 (por isso C19/C21/C24/C26 seguem pendentes).
- Skill não instalada em `~/.claude/skills/`, não zipada, não publicada no claude.ai; hub e `log.md` não editados (pedido restrito a esta pasta).

| Data | Frente | O quê |
|---|---|---|
| 2026-10-28 | pipeline | Skill recompilada a partir de CCG v1.4, WTC v1.6, DD v1.3, 7 Report Specs v1.0 (CO-PILA-007 nova) e SIR v1.1 (Res. 13/2021 → 227/2025); pendências C19/C21/C24/C26 mantidas abertas; 4 achados fora do pedido para o hub |
| 2026-10-28 | geral | Links das notas para o grafo do Obsidian (seções/pesquisas/arquivos principais); conteúdo não alterado |
