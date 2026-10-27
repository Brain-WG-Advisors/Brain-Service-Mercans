# CONFERÊNCIA: BE Report Specs em inglês, v1.1 final (9 specs)

> Pasta renomeada de `2026-10-19-specs-idioma-M-G` para `2026-10-19-specs-idioma-ingles` quando a versão final foi entregue.
> **Arquivado para análise e comparação; Drive só após ok do usuário.**

## Pedido
Janela geral, 2026-10-19, com decisão do usuário: fechar as Report Specs BE por inteiro antes de qualquer compartilhamento. Todas as recomendações das auditorias foram aprovadas.

Origem: a Suman pediu "Field Explanation em inglês" ([[2026-10-13-triagem-chat-desde-09-10]] C4; call de 16/10). Auditoria em [[2026-10-16-BE-auditoria-idioma]]; verificação em [[2026-10-19-BE-specs-idioma-verificacao]].

Escopo:
1. Revisar as 56 linhas amarelas da 1ª tradução de G e M.
2. **J Format:** máscaras literais, texto em inglês e equivalente em inglês da máscara entre parênteses.
3. **O Option Values:** códigos e valores XML literais; rótulos em inglês, com o rótulo oficial FR entre parênteses.
4. **T Query to RA:** rótulos das anomalias da ACRF traduzidos; código e gravidade iguais.
5. **Field Options "CP …":** nome da comissão em inglês, com o nome oficial FR entre parênteses.
6. **"BE-DD-001-v1.4" → "BE-DD-001-v1.0"** nas 9 specs. O DD vigente no Drive é o v1.0; não existe v1.4.

## Versionamento
- **v1.1 final** de cada spec reconstruída a partir da **1.0**, com tudo junto: G e M de 19/10, a revisão das linhas amarelas e os itens 2 a 6.
- As 4 specs sem problema de idioma (Limosa, Finprof 274, Belcotax 281.10, SEPA) ganharam v1.1 só pela citação do DD.
- A v1.1 parcial (só G e M), que nunca foi compartilhada, ficou como `*_v1.1-parcial.xlsx`.
- Linha 1.1 Draft no Version Control de cada spec, descrevendo o que mudou nela. Células alteradas em azul claro FFDDEBF7.

## Entradas
- Base: exports vigentes `Downloads\BE-export-2026-10-16\` (todos 1.0, md5 na verificação de 19/10).

## Decisões de tradução
- **G e M:** os 587 textos traduzidos em 19/10 (`traducoes_FR_EN.json`), mais a revisão das 56 linhas amarelas (`yfix.py`), aplicada a todas as células com o mesmo termo:
  - "tiers payant" → "third-party payer (tiers payant)" na 1ª ocorrência;
  - "accident de droit commun" → "non-occupational accident (accident de droit commun)";
  - RCC e RCIC ganham a glosa na 1ª ocorrência da célula: "RCC (unemployment with company supplement)", "RCIC (unemployment with supplementary allowance for older workers)";
  - "volontaire de la Sécurité Civile" → "Civil Security volunteer (volontaire de la Sécurité Civile)" em todas (antes havia "Civil Protection" numa célula);
  - "sous curatelle" → "under bankruptcy administration (sous curatelle)", o mesmo termo em M e O nas 4 specs (DmfA, DmfA Mod., DRS, FEDRIS). Na O: "0=Period not under bankruptcy administration 1=Period under bankruptcy administration (sous curatelle)";
  - DRS O126 e O127: "(= prestation)" → "(= service performed (prestation))" (prestation aqui é o serviço executado, não o tempo de trabalho);
  - "mutualité" → "health insurance fund (mutualité)". Mantido;
  - "étage" → "floor" (étage).
- **J (`jdict.py`):** 17 textos com explicação em FR. Máscara literal + equivalente em inglês, ex.: "AN(10) — format: AAAA-MM-JJ (YYYY-MM-DD) · AAAA is the year · MM is the month · JJ is the day". Os 45 textos só de tipo/tamanho (`AN(7)`, `N(4)`…) ficaram iguais.
- **O:** 357 textos únicos, traduzidos em 3 lotes com o mesmo glossário.
  - Códigos e valores literais iguais; rótulo FR oficial entre parênteses, ex.: "3=Cancellation (Annulation)".
  - Em rótulos longos ou com números, o FR não foi repetido, para não duplicar valores.
  - Revisão: "Employeur étranger sans UE" — UE aqui é "unité d'établissement", então "Foreign employer without a local unit (unité d'établissement, UE)".
- **T (`tdict.py` + `tparse.py`), deterministico:**
  - cada célula foi lida como sequência rótulo + código `NNNNN-NNN` + gravidade (B/NP/P) e reescrita como "ACRF anomaly codes, Annexe 30 (FR labels translated): Not present 00296-001 B; …";
  - 114 rótulos traduzidos num dicionário único, para a mesma tradução nas 5 specs;
  - os 25 finais cortados na fonte ("Incompatibilité avec la...") foram traduzidos cortados no mesmo ponto;
  - as células que só tinham o cabeçalho da tabela da ACRF viraram "…: Anomaly label | Anomaly code | Severity".
- **CP:** 9 comissões (Dimona, DmfA, FEDRIS), ex.: "Auxiliary joint committee for manual workers (Commission paritaire auxiliaire pour ouvriers)."
- **Erros de digitação da fonte**, traduzidos pelo sentido pretendido:
  - "sien cas" = "si, en cas";
  - "l'ndemnité" = "l'indemnité";
  - "échouera" (lido como "will probably lapse");
  - "la date d 4 acquisition" = "date d'acquisition", mantido como "[sic]".
- **Edição por XML** (`build_final.py`), sem openpyxl.save: só as partes alteradas foram regravadas (abas com células mudadas e styles.xml); as demais foram copiadas byte a byte.

## Resultado
| Spec (v1.1 final) | G | M | J | O | T | CP | só v1.4→v1.0 | VC | Total | md5 |
|---|---|---|---|---|---|---|---|---|---|---|
| BE-NSSO-001-Dimona-Spec_v1.1.xlsx | 46 | 76 | 26 | 57 | 71 | 9 + 1 | 96 | 5 | 387 | 29d1d6381cf0a029470217dba5971ad6 |
| BE-NSSO-002-DmfA-Spec_v1.1.xlsx | 126 | 234 | 47 | 191 | 237 | 9 + 2 | 211 | 5 | 1.062 | 85fe9fcc2d5deb8a0643e7f3b98b69d9 |
| BE-NSSO-003-DmfAModification-Spec_v1.1.xlsx | 126 | 234 | 47 | 191 | 237 | 0 | 120 | 5 | 960 | a332e8299e5ddba55d868878d48e963e |
| BE-NSSO-004-DRS-Spec_v1.1.xlsx | 78 | 221 | 44 | 193 | 235 | 0 + 1 | 159 | 5 | 936 | 7c9d62ac74c64ed450e05fde66f6e65f |
| BE-FEDRIS-001-WorkAccident-Spec_v1.1.xlsx | 76 | 160 | 33 | 156 | 179 | 9 + 1 | 127 | 5 | 746 | 2fd4b5dd4d11fc934bc24ea555d3b1fa |
| BE-NSSO-005-Limosa-Spec_v1.1.xlsx | – | – | – | – | – | – | 26 | 5 | 31 | fdaef6f17e27a6a5c2c988d1e3cbcb92 |
| BE-FIN-001-Finprof274-Spec_v1.1.xlsx | – | – | – | – | – | – | 4 | 5 | 9 | 7aa460e7686e3b05b65ce30fd60a4952 |
| BE-FIN-002-Belcotax28110-Spec_v1.1.xlsx | – | – | – | – | – | – | 37 | 5 | 42 | eb2dc5efaf26f1258f3557c2496f707d |
| BE-FEBELFIN-001-SEPACreditTransfer-Spec_v1.1.xlsx | – | – | – | – | – | – | 7 | 5 | 12 | 45e5b8ab39cbd1818e090df33ac4ab4e |

- Citações v1.4: 787 em células só com a citação, mais 4 dentro de células de O já traduzidas = **791 corrigidas**.
- VC = as 5 células da linha 1.1 no Version Control. Coluna CP: "+ n" = outras células da Field Options C ajustadas em 19/10 ("Statutory workers (Travailleurs statutaires)." e "[permitted value, description not found]").

## Conferência (`conf_final.py`)
- **Célula a célula, 1.0 × 1.1 final, 9 specs, todas as abas:**
  - toda célula alterada está no escopo: G, M, J, O, T, CP, ou a troca exata v1.4 → v1.0 em qualquer aba;
  - **0 fora do escopo**; 0 diferenças só de estilo;
  - toda célula alterada tem FFDDEBF7 e o resto do estilo igual ao da 1.0;
  - zip íntegro.
- **Literais**, comparação por máquina FR × EN de cada célula alterada:
  - números iguais (multiconjunto de dígitos) em todas;
  - em T, a sequência (código, gravidade) idêntica em todas;
  - em J, todas as máscaras (`AN(n)`, `AAAA`, `MM`, `JJ`, `CCC`, `HH`, `SS`, `NNN…CC`) presentes;
  - em G, M e O, os valores entre aspas e « » presentes.
  - **0 divergências**, salvo 1 falso positivo: FEDRIS G166, onde a fonte tem aspas desbalanceadas; os valores "001", "2", "3", "6", "1" e "5" foram conferidos à mão e estão todos lá.
- **v1.4:** 0 ocorrências nas 9 specs.
- **Validador do toolkit** (`validate_workbook.py --artifact RSPEC`): PASS (0/0/0) nas 9, na 1.0 e na 1.1.
- **Varredura de idioma, todas as abas e colunas da 1.1** (exceto as colunas locais por cabeçalho, as abas Sample File e o texto entre parênteses e aspas). Sobraram:
  - **nomes oficiais** (permitidos pela regra): Report Matrix B4 e C27 (títulos oficiais NL/FR do formulário); DRS Field Options C6 ("NSSO Annexe 12 — Identification du risque") e C19 ("Annexe 34 — Jours relatifs à la grille de travail"); DRS File Structure A80 e Field Options C4 ('Déclaration de début de travail à temps partiel', valor oficial entre aspas); FEDRIS Population Rules D18 ('Obligatoire si', termo do glossário entre aspas); DmfA e DmfA Mod. O256 (nomes oficiais das linhas entre aspas, com o inglês ao lado);
  - **literais**: Field Options B "LA" (código de opção) em Dimona B41, DmfA B110, DRS B52 e FEDRIS B79;
  - **falsos positivos em inglês**: "moment", "minutes", "maximum", e "Annexe 30" no prefixo de T;
  - as duas sobras da Field Options C foram corrigidas em 19/10 por decisão do usuário (ver Histórico).

## Planilha de revisão
`rascunhos/2026-10-19-BE-specs-v1.0-vs-v1.1.xlsx`, refeita a partir dos xlsx 1.0 e 1.1 final:
- 4.185 linhas (todas as células alteradas, inclusive Version Control);
- 0 em amarelo: as 37 escolhas de termo foram revisadas e aprovadas pela janela geral/usuário em 19/10, com 2 ajustes (ver Histórico).

## Histórico por frente
| Data | Frente | O quê |
|---|---|---|
| 2026-10-19 | Pipeline | Passo 1: v1.1 das 5 specs com G e M em inglês (1.377 células). Hoje guardada como `*_v1.1-parcial.xlsx`. |
| 2026-10-19 | Pipeline | Arquivado para análise e comparação; Drive só após ok do usuário |
| 2026-10-19 | Pipeline | v1.1 final das 9 specs, reconstruída da 1.0: G, M (revisão das linhas amarelas), J, O, T, CP e citação v1.0. Conferência célula a célula com 0 fora do escopo; 0 divergências de literal (1 falso positivo explicado); 0 "v1.4"; validador PASS. Drive não tocado. |
| 2026-10-19 | Pipeline | Gravadas as 9 finais nesta pasta (renomeada para `2026-10-19-specs-idioma-ingles`; a parcial FEDRIS virou `-parcial` depois de fechada no Excel). md5 dos 9 gravados = md5 gerados; conferência e validador refeitos sobre os arquivos gravados, com o mesmo resultado. |
| 2026-10-19 | Pipeline | Revisão das 37 linhas amarelas aprovada, com 4 ajustes (decisão do usuário): (1) "sous curatelle" unificado como "under bankruptcy administration (sous curatelle)" em M e O (DmfA M16/O16, DmfA Mod. M16/O16, DRS M54/M255/O54/O255, FEDRIS M69/O69); (2) DRS O126 "(= service performed (prestation))"; (3) Field Options C "Statutory workers (Travailleurs statutaires)." (DmfA C49, DRS C30, FEDRIS C39); (4) "[permitted value, description not found]" (Dimona C82, DmfA C86). Reconstruído da 1.0; md5 gravado = gerado; conferência sobre os gravados: 0 fora do escopo, 0 divergências de literal (G166 falso positivo), 0 "v1.4", validador PASS. Planilha de comparação: 4.185 linhas, 0 amarelas. Drive não tocado. |
| 2026-10-19 | Pipeline | DRS O127 (irmã da O126) corrigida para "(= service performed (prestation))". Varredura das 9 specs: era a única ocorrência restante de "working time (prestation)". "Trusteeship or Receivership Indicator" (coluna L e Field Options E, nome do campo no DD) não foi tocado. Só a DRS mudou (md5 7c9d62ac74c64ed450e05fde66f6e65f); as outras 8 continuam idênticas. Conferência sobre os gravados: 0 fora do escopo, 0 "v1.4"; validador PASS. Planilha de comparação refeita (4.185 linhas). |
| 2026-10-19 | Pipeline | Ok explícito do usuário (via janela geral): as 9 finais `*_v1.1.xlsx` copiadas para o Drive `Belgium\12- Country Report Codes\` com o mesmo nome (nenhum arquivo com esse nome existia; .gsheet não tocados; o usuário importa). md5 local = Drive nos 9: SEPA 45e5b8ab…, FEDRIS 2fd4b5dd…, Finprof 7aa460e7…, Belcotax eb2dc5ef…, Dimona 29d1d638…, DmfA 85fe9fcc…, DmfA Mod. a332e829…, DRS 7c9d62ac…, Limosa fdaef6f1…. |
