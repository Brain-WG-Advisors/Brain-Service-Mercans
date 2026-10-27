# SR-472 — Dinamarca — eIndkomst: IndberetningsID dos registros 3101, 4101 e 5000

> Análise só leitura, 2026-10-22. Nada foi postado no YouTrack, nada foi alterado no Drive. Rascunho para o usuário revisar.

## Metadados
| Item | Valor |
|---|---|
| Ticket | SR-472 — "DK-e-indkomst report changes" (https://youtrack.hrblizz.dev/issue/SR-472) |
| Estado / prioridade | Open / Normal — Phase: Product Mapping Phase - Business Analyst |
| Assignee / reporter | Enaakshi Vats (evats) / Enaakshi Vats |
| Due date | 2026-10-30 (campo `Due Date` = 1793361600000) |
| País | DK |
| Artefato | `DK-EINDK-001_eIndkomst_Specification` (Google Sheet `1qbQhmqhvz…RelUo`), versão vigente **v3.5 (Draft, 2026-09-30)** |
| Export usado | `raw/docs/drive-exports/2026-10-22/DK-EINDK-001_eIndkomst_Specification.xlsx` (aba `eIndkomst Spec`) |
| Ticket local | `raw/tickets/api/2026-10-22-for-evats/SR-472.md`; anexo `raw/tickets/api/anexos/SR-472/20260930-1436 - image.png` |
| Fonte primária | eIndkomst: Teknisk vejledning **v11.6** (publ. 10 ago 2026, S nr. 36) e eIndkomst: Indberetningsvejledning **v17.0** (publ. 12 out 2026, S nr. 49), ambas baixadas hoje de info.skat.dk (ver "Fonte primária") |

## O que foi pedido a nós
- **Ruchi Gupta (BA), 07/10:** "Please clarify the query on below field of the report: SE Submission NUMBER | IndberetningsID" (linha 64 da spec, registro 4101).
- **Ruchi, 13/10:** "As discussed, you will check and confirm on the Submission ID for 3101, 4101 and 5000 record. Accordingly we will change the report."
- **Pergunta a responder:** o que vai no campo IndberetningsID (e, por consequência, no ReferenceID) dos registros 3101, 4101 e 5000.
- Fora da pergunta: o mapeamento de 0013/0069 (já pedido ao dev em 16/10 e feito). Conferido abaixo só para registro.

## Histórico do ticket
| Data (UTC) | Quem | O quê |
|---|---|---|
| 2026-09-30 14:36 | Enaakshi | Abre o ticket: lacunas na spec do eIndkomst, alterações na v3.5 (link do Sheet). Anexo: print da aba `eIndkomst Spec` filtrada em 4 linhas (21 REPORTING MARKER/1000, 58 ZERO RETURN MARKER/3101, 64 SE Submission NUMBER/4101, 67 REVERSAL MARKER/4101), com o texto antigo riscado e o novo em vermelho. |
| 2026-10-07 10:47 | Ruchi | Pede esclarecimento de "SE Submission NUMBER / IndberetningsID". |
| 2026-10-13 09:32 | Ruchi | Combina que a Enaakshi confirma o Submission ID de 3101, 4101 e 5000 e então o report muda. **← pendente** |
| 2026-10-16 06:38 | Ruchi → Drew (dev) | Alterar 0013 (subtrair 58109 no lugar de 62181) e 0069 (somar 62180–62182 + 62210–62212). |
| 2026-10-16 07:34 | Drew | "I have done the changes". |

Discussão paralela nos comentários da própria planilha (threads Ruchi × Enaakshi):
- **L64 (4101 IndberetningsID):** Ruchi pergunta qual ID vai ali, já que o ID a cancelar está no ReferenceID; Enaakshi: "New submission ID needs to be generated"; Hoved_indberetningsID identifica o arquivo, IndberetningsID do 4101 identifica a reversão e é diferente dos de 5000 e 3101. Ruchi: "we are not handling employee level cancellation. Only full reversal is handled. Code J".
- **L55 (3101 ReferenceID), L65 (4101 ReferenceID), L73 (5000 ReferenceID):** Enaakshi pede trocar o Hoved-ID pelo IndberetningsID anterior; Ruchi responde que no relatório original não existe ID de 3101/4101 ("3101 is created only when CORRECTION MARKER … is R in record 5000") e que só existe o main submission id. Enaakshi: "for every new occurrence of 3101, IndberetningsID should be there. and in case of any correction in 3101, previous IndberetningsID is mentioned in Reference ID." Thread de L73 sem resposta.

**Conferência 0013/0069 (fora da pergunta):** a spec exportada hoje já tem o pedido de 16/10 — L95 (0013): "Subtract (21640:21650+2518+2551+2556+2558+58109)" com 58109 em roxo; L123 (0069): "Show the sum of wage range(62180:62182+62210:62212)". Diferença menor: L95 diz `21640:21650` na fórmula e `(21640:21649)` na explicação logo abaixo; o comentário do ticket diz `21640:21649` (ver Achados).

## O que nossa spec diz
Aba `eIndkomst Spec` (export de 2026-10-22). Posições conferidas contra a fonte oficial: **todas as posições e comprimentos de IndberetningsID/ReferenceID estão corretos**. O problema está no conteúdo/mapeamento.

| Linha | Registro | Campo (B / C) | Pos. | Mapeamento (col. L, literal) | Explicação (col. M, literal) | Avaliação |
|---|---|---|---|---|---|---|
| 24 | 1000 | MAIN SUBMISSION ID / Hoved_indberetningsID | 90-105, String(16) | "to be handled by report configuration as per standard configuration logic. This is report submission id. Example: Report Generation Date + Payroll Reference Code" | "Unique file-level ID. Cannot reuse across files…" | Conceito certo. Formato de exemplo pode repetir (ver Achados). |
| 54 | 3101 | REPORTING ID / IndberetningsID | 13-28, String(16) | "…This is employee level submission id. Example: numeric part of entity code + period end date (MMyyyy) + count as 001" | "Unique reporting ID." | **Incompleto/impreciso.** Não é "employee level" (3101 é nível SE). Faltam as regras: novo a cada ocorrência, nunca usado antes no SE-nr., diferente de 4101/5000. "count as 001" reinicia por período → repete numa 2ª execução do mesmo período. |
| 55 | 3101 | REFERENCE ID / ReferenceID | 29-44 | "required for submitting a correction report i.e., when Correction Marker is R, else blank. This field should show the main submission id of the original report… $legal_entity_hr.original_submission_id_for_reversal_correction_report" | "Used, optionally, for changes to an earlier reporting." | **Errado.** Oficial: opcional e, se preenchido, é o IndberetningsID anterior (do 3101), não o Hoved-ID. 3101 não tem Correction Marker (o "R" é campo do 5000). |
| 64 | 4101 | ~~SE~~ Submission NUMBER / IndberetningsID | 12-27, String(16) | **"$legal_entity_hr.se_number"** (inalterado; célula em vermelho) | "~~SE number for which the reversal applies. SE number for reversal scope~~ Unique reporting ID. New ID is specified for this and subsequent records. The ID must not have been used in records 3101 and 5000. …" | **Errado no mapeamento.** M já foi corrigida na v3.5; L continua apontando para o SE-nr. Exemplo K64 "12345678" e nota T64 ("Restored to 12-19 (SE number, 8 digits)") também ficaram do conceito antigo. |
| 65 | 4101 | REFERENCE ID / ReferenceID | 28-43, obrig. Y | "Show MAIN SUBMISSION ID of the orginal report which is getting cancelled now. IF(EQUALS(EQUALS($legal_entity_hr.generate_reversal_report::key;1);$legal_entity_hr.original_submission_id_for_reversal_correction_report;'')" | "IndberetningsID of the submission to be reversed. Must match the original submission ID from Record 5000." | **Errado (L) e certo (M).** L manda o Hoved-ID; a fonte proíbe reverter no nível do Hoved-ID. A fórmula também tem `EQUALS` aninhado e o `IF` sem 3º argumento. |
| 67 | 4101 | REVERSAL MARKER / Tilbagefør_SE_j/n | 45 | "Fixed Value J To be shown only when record 4101 is created." | "\"J\" results in a full reversal on the specified ref. ID. \"N\" requires that the CPR number be filled in…" | Correto (v3.5). |
| 72 | 5000 | SUBMISSION ID / IndberetningsID | 13-28, String(16) | "…This is employee level submission id. Example: Employee ID + Period End Date + Count as 001" | "Unique ID per SE-nr. Cannot reuse. Must differ from IDs in 3101 and 4101. Used for reversals reference." | M correto. **L impreciso:** 5000 é por grupo de pessoas, não por empregado; "Employee ID + period end + 001" repete numa reexecução do mesmo período e não garante unicidade frente aos IDs do 3101. |
| 73 | 5000 | REFERENCE ID / ReferenceID | 29-44, opcional | igual à linha 55 (Hoved-ID do relatório original quando Correction Marker = R) | "Optional: reference to previous submission for audit trail when making corrections." | **Errado (L).** Mesmo problema da linha 55. |

Report Matrix B11: "Primary Keys: SE-nr + CPR-nr + IndberetningsID; HovedindberetningsID unique per file" — o Hoved-ID é único por indberetter entre todos os arquivos aceitos, não só "per file".

## Fonte primária
Todas lidas no texto oficial (dinamarquês); tradução livre entre colchetes.

**A. eIndkomst: Teknisk vejledning v11.6** — info.skat.dk, oid=1745538 (publicada 10 Aug 2026, S nr. 36; "Nyt i version 11.6" só altera o registro 2101). Local: `raw/docs/oficiais/DK/2026-10-22-eindkomst-teknisk-vejledning-v11.6.html` (md5 `ec4e336555935b5f97fb1c7213c31b67`). Conferida também contra a impressão do Drive `…\DK-EINDK-001_eIndkomst - Official Documents\Udskrift af eIndkomst_ Teknisk vejledning … V11.6.pdf` (impressa 17/08/2026, vid=221236): mesmo texto.

1. **§ 3.2 Særlige forhold vedr. indberetningsidenter og rettelser:**
   - "Den der indberetter skal angive unikke indberetningsID-er i record 3101, 4101 og 5000." [Quem reporta deve informar IndberetningsIDs únicos nos registros 3101, 4101 e 5000.] Motivos: autoridades referenciam as indberetninger; evitar duplicidade; a empresa usa os IDs como referência em correções/reversões.
   - "Tilbageførsler kan ske på enten indberetningsID niveau eller pr. cpr-nr. under en indberetningsID (jvf. record 4101). En tilbageførsel på indberetningsID niveau vil tilbageføre alle indberetninger for den pågældende indberetningsID, der svarer til den referenceident, der er angivet i record 4101."
   - "…hvis der reelt ønskes en fuld tilbageførsel af det indberettede, så skal det ske ved tilbageførsel af hver indberetningsID. I praksis en record 4101 pr. indberetningsident." [Reversão total = um 4101 por IndberetningsID.]
   - "Der kan ikke tilbageføres på hovedindberetningsID/fil niveau." [Não se reverte no nível do Hoved-ID/arquivo.] (Repetido em § 3.1.)
   - "En tilbageførsel kan ikke tilbageføres."
2. **§ 3.4 Forretningsmæssige regler:** "Enhver indberetning skal have en unik hovedindberetningsID i record 1000. Hvis samme ID modtages igen fra den samme indberetter, afvises hele indberetningen. På persongruppeniveau pr virksomhed (record 5000) findes en tilsvarende indberetningsID. Hvis denne tidligere har været anvendt på samme se-nr. (angivet i record 2001), afvises indberetningen. Hvis der skal ske tilbageførsler af tidligere indberetninger på record 5000-niveau, skal virksomheden referere til den indberetningsID, den oprindelige indberetning har."
3. **§ 2.2 Teknisk kommunikation:** ISO 8859-1; proibidos `' < > & "`; "I indberetningsID'er og hovedindberetningsID tilrådes det at undlade specialtegn, herunder æ, ø og å." Rejeição por caractere proibido no Hoved-ID não gera mensagem de erro.
4. **§ 3.3 Generelle regler:** campos alfanuméricos alinhados à esquerda, completados com brancos, "Dog må der ikke forekomme foranstillede blanke værdier."
5. **§ 4.2 Record 1000, felt 12 Hoved_indberetningsID** — pos 90, 16, A, obrig. J: "Indberetterens unikke indberetnings identifikation. Den angivne ident må ikke være anvendt tidligere som hovedindberetningsident i en accepteret fil."
6. **§ 4.6 Record 3101 (Periodeoplysninger på se-nr.)** — Anvendelse: "Enten Nulangivelse med N i felt 8 … -eller feltnr. 0059 eller 0400 i felt 9 og beløb i felt 10." Forekomst: "Indsendes, hvis der er periodeoplysninger. Dvs udelukkende oplysninger, der ikke vedr. et specifikt cpr-nr." Sekvens: "Efter record 21xx".
   - Felt 4 **IndberetningsID**, pos 13, 16, A, obrig. J: "Unik indberetningsID, der ikke tidligere har været brugt for det pågældende se-nr. Må ikke være identisk med rec. 4101, 5000. Der skal være en ny, for hver ny forekomst af record 3101."
   - Felt 5 **ReferenceID**, pos 29, 16, A, não obrigatório: "Bruges ved ændringer (frivilligt), hvis et lønsystem ønsker at gøre brug af sporbarhed ifm. ændringer til tidligere indberetninger. Den tidligere indberetningsident skal bruges her, for præcist at identificere (referere) den indberetning der ønskes ændret."
   - Felt 3 Forud/Bagud: "Private virksomheder skal ikke anvende feltet." Felt 8 Nulangivelse: "N = nulangivelse, blank = i andre tilfælde". Felt 9: "0000 ved nulangivelse". Felt 11 Fortegn pos 82.
7. **§ 4.7 Record 4101 (Tilbageførsel på se-nr. og cpr-nr. niveau)** — "ReferenceID bruges til, at identificere den ønskede indberetning. Hvis der er anført cpr-nr., er det kun det cpr-nr. under referenceID'en, der tilbageføres." Sekvens: "Efter 2001, kan gentages indtil alle de ønskede indberetninger er tilbageført."
   - Felt 3 **IndberetningsID**, pos 12, 16, A, obrig. J: "Unik indberetningsID. Ny ID angives for denne og efterfølgende records. ID'en må ikke være brugt i record 3101 og 5000."
   - Felt 4 **ReferenceID**, pos 28, 16, A, obrig. J: "ReferenceID=IndberetningsID på den indberetning som ønskes tilbageført. Skal bruges for præcist at identificere den indberetning, der ønskes tilbageført/tilbageført fra."
   - Felt 5 Fillerfelt 44; felt 6 Tilbagefør_SE_j/n pos 45 (J/N; "J" = reversão total do ref. ID; "N" exige CPR no felt 7); felt 7 CPR pos 46-55.
8. **§ 4.8 Record 5000 (Start pr. personalegruppe mv.)** — "Indberetning af grupper af personer under hvert se-nr. …" "Hvis du har flere medarbejdere med samme data i record 5000 bør de indeholdes i en og samme record 5000. Der bør kun i undtagelsestilfælde forekomme flere enslydende record 5000 pr. se-nr. Flere enslydende record 5000 med forskellige indberetningsID kan føre til forlængede svartider." Sekvens: "Efter record 4101."
   - Felt 4 **IndberetningsID**, pos 13, 16, A, obrig. J: "Skal være unik. Må ikke være brugt tidligere på det indberetningpligtige se-nr. eller forekomme flere gange på record 5000 i samme indberetning, eller på record 3101 og 4101."
   - Felt 5 **ReferenceID**, pos 29, 16, A, não obrigatório: mesmo texto do 3101 ("frivilligt … Den tidligere indberetningsident skal bruges her").
   - Felt 3 Rettelse_tidl_periode (R): "må kun undtagelsesvist benyttes … Må ikke angives sammen med en række felter, bl.a. A-skat og am-bidrag og krydsfelter."

**B. eIndkomst: Indberetningsvejledning v17.0** — info.skat.dk, oid=79741 (publicada 12 Oct 2026, S nr. 49). Local: `raw/docs/oficiais/DK/2026-10-22-eindkomst-indberetningsvejledning-v17.0.html` (md5 `988835da1d63d59ce8505b35eaea46d4`). Apoio:
- Afsnit 20, quadro "Begreber i dette afsnit": "HovedindberetningsID — Unik ID på op til 16 karakterer for den fysiske indberetter, der identificerer en given filindberetning under indberetters cvr-/SE-nr. Angives i recordttype 1000." / "IndberetningsID — Unik ID på op til 16 karakterer for den indberetningspligtige, der identificerer en given gruppe af indberetninger i en fil. Angives i recordtype 5000." / tabela: "IndberetningsID 5000 — Identifikation af indberetning. Skal være unik og dermed ikke være brugt tidligere på det indberetningspligtige se-nr. eller forekomme flere gange i samme indberetning."
- § 14 Rettelser / 14.3 Tilbageførsler: "Når du skal rette en indberetning, skal den kun tilbageføres, hvis selve indberetningen er en fejl. Hvis beløbene … blot skal rettes, bør dette ske ved indberetning af forskelsbeløb…"; "Ved en tilbageførsel forstås, at hele indberetningen tilbageføres på enten virksomheds- eller personniveau og alle tidligere registrerede indkomstfelter … tilbageføres (nulstilles)."
- § 14.2: "R-markering må ikke forekomme, når indberetningen indeholder beløb i felter vedrørende A-skat og am-bidrag eller felter med krydsmarkering … ellers afvises indberetningen" (felter 15, 16, 23, 42; kryds 40, 63, 220).

**O que acontece em correções (resumo das fontes):**
- Correção só de valor → nova indberetning com a diferença (+/−), mesmo período; novo 5000 com **novo** IndberetningsID; ReferenceID opcional (IndberetningsID do 5000 original). (IV § 14, 14.1; TV § 3.2, § 4.8 felt 5.)
- Correção de período/código/cruz/texto ou indberetning indevida → reversão (4101) + nova indberetning, no mesmo dia. O 4101 tem IndberetningsID **novo** e ReferenceID = IndberetningsID do 5000/3101 original; um 4101 por IndberetningsID original. (TV § 3.2, § 4.7; IV § 14.3.)
- Reuso de IndberetningsID no mesmo SE-nr. → indberetning rejeitada; reuso de Hoved-ID → arquivo inteiro rejeitado. (TV § 3.4.)

## Veredito por registro
| Registro | IndberetningsID (o campo da pergunta) | ReferenceID (ligado) |
|---|---|---|
| **3101** (pos 13-28) | ID **novo gerado por nós** a cada ocorrência do 3101 (nulangivelse ou 0059/0400). Alfanumérico, até 16, alinhado à esquerda com brancos, sem æøå/`'<>&"`. Nunca usado antes no mesmo SE-nr. (o do 2001) e diferente de qualquer ID de 4101/5000. Não é SE-nr. nem Hoved-ID. | Pos 29-44, **opcional**. Deixar em branco. Só preencher se o produto guardar o IndberetningsID do 3101 anterior que está sendo alterado; nesse caso, esse ID. Nunca o Hoved-ID. |
| **4101** (pos 12-27) | ID **novo gerado por nós** para a reversão (mesma regra de unicidade). Não é o SE-nr. (mapeamento atual `$legal_entity_hr.se_number` está errado) nem o Hoved-ID. Confirma a resposta já dada pela Enaakshi na planilha: haverá dois IDs no arquivo de cancelamento (Hoved-ID no 1000 e IndberetningsID no 4101). | Pos 28-43, **obrigatório**: IndberetningsID do 5000 (ou 3101) original que está sendo revertido. **Não pode** ser o Hoved-ID do relatório original (reversão no nível do Hoved-ID não existe). Reversão total do período = **um 4101 por IndberetningsID** de 5000/3101 do relatório original. Com J no felt 6 e CPR em branco. |
| **5000** (pos 13-28) | ID **novo gerado por nós** para cada 5000 (cada grupo), nunca usado antes no SE-nr., sem repetir entre dois 5000 do mesmo arquivo nem com 3101/4101. É por grupo de pessoas, não por empregado. | Pos 29-44, **opcional**: em correção, IndberetningsID do 5000 original; se o produto não tiver esse dado, deixar em branco. Nunca o Hoved-ID. |

Consequência para o produto (não é regra estatutária, é o que a regra exige do sistema): para gerar o 4101 é preciso **guardar os IndberetningsIDs de cada 3101/5000 já enviados** por SE-nr. e período. O campo atual `$legal_entity_hr.original_submission_id_for_reversal_correction_report` guarda um único valor (o Hoved-ID) e não basta quando o arquivo original teve mais de um 5000 (o nosso gera um 5000 por indkomsttype; ver a aba `5000-6000-6001 sample`).

**Formato sugerido** (decisão de design nossa; a fonte só exige unicidade, até 16 caracteres e o conjunto de caracteres): prefixo por registro + carimbo da execução + sequencial no arquivo, por exemplo `N` (3101) / `T` (4101) / `G` (5000) + `yyMMddHHmmss` + `nnn` = 16 caracteres. O prefixo impede colisão entre 3101/4101/5000; o carimbo impede repetição numa reexecução do mesmo período. Alternativa: contador persistente por SE-nr. Confirmar com o dev qual o sistema suporta.

## Mudança na spec
Aba `eIndkomst Spec`. Proposta para a v3.6 (realce próprio, ex.: amarelo claro); sem alteração de posições.

| Célula | Antes | Depois |
|---|---|---|
| B54 | `REPORTING ID` | `REPORTING ID` (sem mudança) |
| L54 | "…This is employee level submission id. Example: numeric part of entity code + period end date (MMyyyy) + count as 001" | "Generate a new ID for every record 3101 in the file (SE-level, not employee level). Max 16 characters, left-aligned, blank-padded, no leading blanks; ISO 8859-1 without ' < > & \" and without æ, ø, å. Must never have been used before for the same SE-nr. (record 2001) and must not equal any IndberetningsID of records 4101 or 5000. The generated ID must be stored per SE-nr. and period so that it can be referenced by a later 4101. Format: as per standard configuration (proposed: 'N' + yyMMddHHmmss of the run + 3-digit sequence in the file)." |
| M54 | "Unique reporting ID." | "Unique reporting ID. Must not have been used before for the SE-nr.; must differ from 4101 and 5000; a new ID for each new occurrence of record 3101. Source: eIndkomst Teknisk vejledning v11.6, § 4.6 field 4, § 3.2." |
| L55 | "This filed is required for submitting a correction report i.e., when Correction Marker is R, else blank. This field should show the main submission id of the original report… $legal_entity_hr.original_submission_id_for_reversal_correction_report" | "Optional. Leave blank. If filled, it must be the IndberetningsID (field 4) of the earlier record 3101 being changed — never the Hoved_indberetningsID of record 1000. (Record 3101 has no correction marker.)" |
| B64 | "~~SE~~ Submission NUMBER" | `REPORTING ID` |
| K64 | `12345678` | exemplo de 16 posições no formato definido (ex.: `T261022143000001`) |
| L64 | `$legal_entity_hr.se_number` | "Generate a new ID for every record 4101 (one 4101 per original IndberetningsID being reversed). Same rules as row 54: max 16, left-aligned, blank-padded; never used before for the SE-nr.; must differ from all IDs in records 3101 and 5000; not the SE-nr. and not the Hoved_indberetningsID. Proposed: 'T' + yyMMddHHmmss + 3-digit sequence." |
| M64 | (texto v3.5) | manter o texto novo; retirar o trecho riscado. |
| T64 | "Position corrected from an Excel date-conversion. Restored to 12-19 (SE number, 8 digits)." | "v3.6: field 3 is IndberetningsID (12-27, A16), not SE number. Source: Teknisk vejledning v11.6 § 4.7." |
| L65 | "Show MAIN SUBMISSION ID of the orginal report which is getting cancelled now. IF(EQUALS(EQUALS(…generate_reversal_report::key;1);…original_submission_id_for_reversal_correction_report;'')" | "Mandatory when record 4101 is generated. Show the IndberetningsID of the original record 5000 (or 3101) being reversed — NOT the Hoved_indberetningsID (reversal at main-ID / file level is not possible). For a full reversal of a period, generate one 4101 per IndberetningsID of the original file. Requires the product to store the IndberetningsIDs of every submitted 3101/5000 per SE-nr. and period." (fórmula a ser reescrita pelo TA com a nova fonte de dados) |
| M65 | "IndberetningsID of the submission to be reversed. Must match the original submission ID from Record 5000." | "IndberetningsID of the record 5000 (or 3101) to be reversed. Cannot be the Hoved_indberetningsID. Source: Teknisk vejledning v11.6 § 3.2, § 4.7 field 4." |
| L72 | "…This is employee level submission id. Example: Employee ID + Period End Date + Count as 001" | "Generate a new ID for every record 5000 (one per group, not per employee). Same rules as row 54: max 16, never used before for the SE-nr., not repeated on another 5000 in the same file, different from all 3101/4101 IDs. Store it per SE-nr. and period for later reversal. Proposed: 'G' + yyMMddHHmmss + 3-digit sequence." |
| L73 | igual ao L55 antigo (Hoved-ID quando Correction Marker = R) | "Optional. Leave blank. If filled, it must be the IndberetningsID (field 4) of the earlier record 5000 being corrected — never the Hoved_indberetningsID." |
| Version Control B20 | — | nova linha v3.6 com a descrição acima. |

## Achados fora do pedido
Não entram na resposta do ticket; registrar no hub (`paises/Dinamarca.md`, Pendências) se o usuário aprovar.

1. **Alta — 5000 L71 Correction Marker "R" em todo off-cycle.** A spec diz "This will go as 'R' if it is generated for off-cycle". Fonte: R "må kun undtagelsesvist benyttes" e não pode vir com A-skat/am-bidrag (felter 15/16) nem cruzes, "ellers afvises indberetningen" (IV § 14.2; TV § 4.8 felt 3). Off-cycle com imposto seria rejeitado. Correção normal é sem R, com diferença no período original (IV § 14.1).
2. **Alta — aba `5000-6000-6001 sample`:** quatro registros 5000 no mesmo arquivo com o mesmo IndberetningsID (`DK1120250731`) → viola "må ikke … forekomme flere gange på record 5000 i samme indberetning" (TV § 4.8). Os blocos 2 e 3 (indkomsttype 09) têm 5000 idênticos e deveriam ser um só 5000 com dois 6000 ("bør de indeholdes i en og samme record 5000"). A aba também tem um número de 10 dígitos com cara de CPR: confirmar que é fictício.
3. **Média — 3101 L58 Nulangivelse:** "Show 1, Else 0". Oficial: `N` = nulangivelse, branco nos outros casos (TV § 4.6 felt 8). A explicação M58 já está certa; só o mapeamento está errado.
4. **Média — 3101 L53 Forud/Bagud:** mapeado do indicador da LE. Oficial: "Private virksomheder skal ikke anvende feltet" (só setor público). Escopo da skill é setor privado → deixar em branco.
5. **Média — premissa do BA:** "3101 is created only when CORRECTION MARKER … is R in record 5000" (comentário em L55) não tem base: 3101 é enviado para nulangivelse por SE-nr. ou para 0059/0400 (TV § 4.6). Falta na spec a regra de quando gerar o 3101 (L51 só diz "to be handled by report configuration").
6. **Média — 1000 L24 Hoved-ID** "Report Generation Date + Payroll Reference Code": regerar o mesmo payroll no mesmo dia repete o ID → arquivo inteiro rejeitado (TV § 3.4; § 4.2 felt 12). Incluir hora/sequencial.
7. **Baixa — 0013 L95:** fórmula `21640:21650` × explicação e ticket `21640:21649`. Confirmar com a Ruchi qual vale.
8. **Baixa — Indberetningsvejledning v17.0** (12/10/2026) já publicada; Report Matrix B6 cita v16.9. A v17.0 muda indtægtsart 60/61 (§ 8.4.1) e Groenlândia (§ 16, fora do escopo). Teknisk vejledning continua 11.6.
9. **Baixa — Report Matrix B11:** "HovedindberetningsID unique per file" → é único por indberetter entre todos os arquivos aceitos.
10. **Baixa — 3101 F60 Amount** = "C" (não é Y/N) e L60 "Show 0000": o campo tem 16 posições, em nulangivelse vai preenchido com zeros (TV § 4.6 felt 10).

## Rascunho de resposta (EN)
> Para a Enaakshi postar (ela é a assignee). Não postado.

@rgupta Confirming the Submission ID for records 3101, 4101 and 5000. Source: eIndkomst: Teknisk vejledning v11.6 (info.skat.dk, oid=1745538), §§ 3.2, 3.4, 4.6, 4.7, 4.8.

1. **IndberetningsID** (3101 pos 13-28, 4101 pos 12-27, 5000 pos 13-28; alphanumeric, max 16) is a **new ID we generate for every occurrence of the record**. It must never have been used before for the same SE-nr. and must not repeat across 3101, 4101 and 5000, or on two 5000 records in the same file. It is neither the SE number nor the Hoved_indberetningsID of record 1000. § 3.2: "Den der indberetter skal angive unikke indberetningsID-er i record 3101, 4101 og 5000."
2. **Record 4101** therefore has two IDs: field 3 IndberetningsID = a new ID for the reversal itself; field 4 ReferenceID = the IndberetningsID of the **original record 5000 (or 3101)** being reversed. It cannot be the main submission ID: "Der kan ikke tilbageføres på hovedindberetningsID/fil niveau" (§ 3.2). A full reversal of a period needs one 4101 per original IndberetningsID ("I praksis en record 4101 pr. indberetningsident").
3. **ReferenceID in 3101 and 5000** (pos 29-44) is optional. If filled, it must be the earlier IndberetningsID of the record being changed ("Den tidligere indberetningsident skal bruges her"), not the main submission ID. Otherwise leave it blank.
4. Record 3101 is not linked to the correction marker. It is sent for a zero return (field 8 = "N", field 9 = 0000) or for fields 0059/0400 (§ 4.6).

For development, this means the IndberetningsIDs of every submitted 3101/5000 need to be stored per SE-nr. and period, so that the 4101 can reference them. Spec rows 54, 55, 64, 65, 72 and 73 will be updated in v3.6 accordingly.

## O que precisa ser feito
| # | O quê | Quem | Urgência |
|---|---|---|---|
| 1 | Revisar este rascunho; decidir o formato do ID (sugestão `N/T/G` + timestamp + seq) | Usuário / Enaakshi | Antes de 30/10 (due date) |
| 2 | Atualizar a spec v3.6 (linhas 54, 55, 64, 65, 72, 73 + Version Control), partindo do export mais recente; realçar as mudanças | Enaakshi (RA) | Alta — o 4101 com SE-nr. ou Hoved-ID é rejeitado |
| 3 | Postar a resposta no SR-472 (rascunho acima) | Enaakshi, com ok do usuário | Alta |
| 4 | Gerar os IndberetningsIDs conforme a regra; guardar os IDs de 3101/5000 por SE-nr./período; trocar a fonte do ReferenceID do 4101 (hoje `original_submission_id_for_reversal_correction_report` = Hoved-ID) e gerar um 4101 por ID original | Ruchi (BA) → Drew (dev/TA) | Alta, antes de qualquer cliente precisar de reversão |
| 5 | Achados 1–6 (R em off-cycle, sample com ID repetido, Nulangivelse 1/0, Forud/Bagud em privado, regra de geração do 3101, Hoved-ID repetível) | Usuário decide se abre no ticket ou em outro; registrar no hub | Média-alta (1 e 2 causam rejeição) |
| 6 | Registrar no hub `paises/Dinamarca.md` (Suporte + Pendências) e, se houver erro nosso, em `correcoes.md` | Janela Suporte, com ok do usuário | Ao fechar |

## Lacunas
- **"Ny ID angives for denne og efterfølgende records"** (4101 felt 3): a fonte não explica o "efterfølgende records" (registros seguintes). A leitura adotada, coerente com § 3.2 e § 4.8, é que cada registro 3101/4101/5000 recebe o seu ID novo. ⚠️ sem fonte para outra leitura; não usar isso para reaproveitar o ID do 4101 nos 5000 seguintes.
- **ReferenceID opcional preenchido com valor que não é IndberetningsID** (como faz a spec hoje no 3101/5000): a fonte não diz se é rejeitado ou ignorado. ⚠️ sem fonte. Por isso a recomendação é deixar em branco.
- **Como o produto guarda os IDs** (tabela por SE-nr./período, contador persistente ou derivação determinística): decisão de design do dev, sem fonte estatutária.
- **Se o produto gera um 5000 por indkomsttype ou por empregado na produção real:** a única evidência é a aba de amostra (um por indkomsttype). Não vi arquivo TXT real (os pacotes da Certificação DK de set/26 são no formato Excel, DK-EINDK-002).
- **Arquivo de reversão também com nova indberetning:** a fonte permite 4101 seguido de 5000 novos no mesmo arquivo (sequência 2001 → 4101 → 5000); a spec (M63) descreve só 1000+2001+4101+9999. Não é erro, mas o fluxo "reverter e reenviar no mesmo dia" (IV § 14.3) não está desenhado na spec.
- Faixa de 0013 (`21640:21649` × `21640:21650`): só a Ruchi/o catálogo respondem.
