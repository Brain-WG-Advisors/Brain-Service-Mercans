# Rascunhos — respostas de 2026-10-15

> Nada gravado no YouTrack nem enviado. Cada afirmação com a prova ao lado (linhas `>`). Arquivos dependem de exports novas (D5, D6 alteradas hoje; DD ES; WTC NL V3.3).

## SR-162 (D5) — resposta às perguntas de 15/10 09:08
Hi @lli,

1. Row 40 (C_DOC_VER): fixed "11", for reporting periods from July 2026.
2. Row 50 (D_FILL): DDMMYYYY, no separators, 8 characters.
3. Rows 53–54: not omitted. HBOS = director's full name, mandatory: $legal_entity_hr.director_authorized_person. HBUH = chief accountant's full name, optional: $legal_entity_hr.chief_accountant_name. Same as D1. The signature is not an XML element.
4. Root: yes, `<?xml version="1.0" encoding="windows-1251"?>` and `<DECLAR xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="J0510511.xsd">`.

Spec v3.4 updated: rows 40, 50, 53, 54 (light blue).

> 1: ДПС, notícia de 14/07/2026 (tax.gov.ua/nove-pro-podatki--novini-/1031674.html): наказ Мінфіну 243 (07.05.2026) e 284 (26.05.2026) vigentes desde 17.07.2026; novas formas a partir de 1/8 para o período de julho/2026 (agentes fiscais, exceto ФОП). XSD J0510511: C_DOC_VER fixed="11". SPR_VER de 06/03/2026 só tinha a v10 (anterior ao наказ 243).
> 2: XSD J0510511 linha 153 (D_FILL type DGDate); common_types DGDate length 8, padrão ddmmyyyy; Formato ДПС (наказ 729) п. 10.3.
> 3: XSD J0510511 linhas 199–202 (HKBOS obrigatório; HBOS DGHBOS minLength 1, obrigatório; HKBUH/HBUH nillable minOccurs 0); formulário oficial D5.xlsx (Drive, Official Government Files) linhas 44–48: por pessoa, РНОКПП | (підпис) | (власне ім'я та прізвище). DD UA V4.2: director_authorized_person (SaaS "Director / Authorized Person"), chief_accountant_name (V3.10). Spec D1 linhas 46–47 com esse mapeamento.
> 4: Formato ДПС (наказ 729), п. 7: "Кожний документ починається з директиви XML <?xml version="1.0" encoding="windows-1251"?>… Кодовою сторінкою є windows-1251"; exemplo do DECLAR com xmlns:xsi e xsi:noNamespaceSchemaLocation.

## SR-163 (D6) — resposta às perguntas de 15/10 10:43
Hi @lli,

1. Row 37 (C_DOC_VER): fixed "11", for reporting periods from July 2026.
2. Rows 50–51: not omitted. HBOS = director's full name, mandatory: $legal_entity_hr.director_authorized_person. HBUH = chief accountant's full name, optional: $legal_entity_hr.chief_accountant_name. Same as D1. The signature is not an XML element.
3. Yes: `<?xml version="1.0" encoding="windows-1251"?>` before the root element.

Spec v3.2 updated: rows 37, 50, 51 (light blue).

> Mesmas provas; XSD J0510611 (C_DOC_VER fixed "11"; HBOS/HBUH linhas 171–173); D6.xlsx oficial linhas 65–69.

## SR-432 (ES) — pedido de 15/10 05:55 ("create a new field for company's principal CCC")
Hi @lli,

Added to DD V4.1: $legal_entity_hr.social_security_principal_ccc (ID Information, row 15), the company's principal CCC used in field 400. In a single-CCC company, field 400 repeats field 310.

> Manual TGSS AFI v9.7, campo 400: "Se indicará el Código Cuenta Cotización principal. En caso de que el movimiento se refiera al CCC principal, o en empresas mono-CCC, debe repetirse el contenido del campo 310". Linha/código definitivos após a export atual do DD ES.

## HRBS-14394 (NL) — reabertura do HRBS-5499
Hi @ugaikwad,

The 2026 maximum premium wage (maximumpremieloon) per pay period is: day €305.41, week €1,527.09, 4 weeks €6,108.38, month €6,617.41, quarter €19,852.25, year €79,409.00. €5,509.00 is not a 2026 value.
Pay element 52990 is not in the Netherlands master WTC: it was removed in WTC v2.0 (31/07/2025). The 2026 ceiling is element 52999 (Social Security Ceiling), by the employee's pay period ($hr.max_ss_base).

Source: Belastingdienst, Handboek Loonheffingen 2026, Bijlage 1, tabel 11.

> Handboek 2026 (versie maart 2026, raw/docs/oficiais/NL/), p. 519, Tabel 11; p. 93: "Voor het hele jaar 2026 is dat € 79.409". WTC NL V3.2 (export 18/08): Version Control 2.0 "Delete 52990"; linhas 239 (52999 Social Security Ceiling) e 267 (58204 SSC Flag por $hr.max_ss_base). **Falta conferir na planilha ativa V3.3 (13/10).**

## SR-160 (D1) — pergunta de 15/10 12:17 (seção E ausente na aba D1 Spec)
Hi @lli,

Spec v3.3 updated: Section E added to the D1 Spec sheet (rows [a definir], light blue), with the DECLARHEAD elements in the XML sample, as in D5: TIN, C_DOC (fixed "J05"), C_DOC_SUB (fixed "101"), C_DOC_VER (fixed "11"), C_DOC_TYPE, C_DOC_CNT, C_REG, C_RAJ, PERIOD_MONTH, PERIOD_TYPE, PERIOD_YEAR, C_STI_ORIG, C_DOC_STAN, LINKED_DOCS, D_FILL, SOFTWARE.

> XSD J0510111, DHead (C_DOC fixed J05, C_DOC_SUB fixed 101, C_DOC_VER fixed 11). Campos do DD para C_REG/C_RAJ/C_STI_ORIG: DD UA V4.2 (dps_region_code, dps_district_code, dps_tax_authority_code). Linhas definitivas após a export atual da D1.

## SR-161 (4DF) — pergunta de 15/10 12:53 (seção E ausente na aba 4DF Spec)
Hi @lli,

Spec v3.3 updated: Section E added to the 4DF Spec sheet (rows [a definir], light blue), with the DECLARHEAD elements in the XML sample, as in D5: TIN, C_DOC (fixed "J05"), C_DOC_SUB (fixed "104"), C_DOC_VER (fixed "11"), C_DOC_TYPE, C_DOC_CNT, C_REG, C_RAJ, PERIOD_MONTH, PERIOD_TYPE, PERIOD_YEAR, C_STI_ORIG, C_DOC_STAN, LINKED_DOCS, D_FILL, SOFTWARE.

> XSD J0510411, DHead (C_DOC_SUB fixed 104, C_DOC_VER fixed 11).

## HRBS-12110 (Congo)
Sem pergunta nova (última: Daniel, 07/10, "still need" para o Pradeep). Atualização de 15/10 06:22 sem comentário. Nada a responder.
