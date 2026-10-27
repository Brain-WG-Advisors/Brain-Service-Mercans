# Matriz Modelo 145 × Data Dictionary Espanha (V5.0)

> Caso STG Spain — ESS "Employee Tax Relief Declaration". Frente Pipeline, 2026-10-19. Aprovado pelo usuário antes de gravar. Atualizada para o DD **V5.0** final (`Spain_Data_Dictionary_V5.0.xlsx`, md5 9f83bb035ed615d5fe0131a8105d57ac); a primeira versão comparava com a V4.9.
> Critério: um campo do 145 só entra no DD se a fonte oficial provar que é insumo do cálculo da retenção de IRPF ou de um report estatutário (não espelhar o formulário).

**Base legal geral:** RIRPF art. 88.1 — a comunicação (Modelo 145) cobre "la situación personal y familiar que influye en el importe excepcionado de retener, en la determinación del tipo de retención o en las regularizaciones de éste". Art. 88.2: sem a comunicação, o pagador retém sem considerar a circunstância.

**Resultado (DD V5.0):** 24 linhas do 145 → **22 necessárias, todas cobertas** (14 já existiam na V4.9 + **8 incluídas na V5.0**) e **2 não necessárias como campo**; 0 a confirmar.

**Siglas de fonte** (arquivos em `raw/docs/oficiais/ES/`, baixados em 2026-10-19):
- **Alg** = AEAT, *Algoritmo de cálculo del tipo de retención IRPF 2026 (a partir de 10 de septiembre)* — `2026-10-19-AEAT-Algoritmo-Retenciones-2026-10sept.pdf` (páginas do PDF).
- **XSD** = AEAT, `AEATRetenciones2026.xsd` (serviço de cálculo de retenções 2026).
- **190** = AEAT, *Diseños de registro Modelo 190 (2025)*, inclui Orden HAC/1431/2025 — registro tipo 2 (perceptor), posições.
- **RIRPF** = RD 439/2007, consolidado BOE (últ. atualização 07/10/2026). **LIRPF** = Lei 35/2006, consolidada BOE (últ. atualização 07/10/2026).

| # | Campo do Modelo 145 | Campo do DD (código) | Necessário? | Por quê | Fonte |
|---|---|---|---|---|---|
| 1 | Apellidos y nombre | First Name / First Surname / Second Surname (Universal) | ✅ Necessário — existe | identificação do perceptor | XSD `ApellidosNombre`; 190 pos. 36-75 |
| 2 | NIF | `$person.national_id` (ID Information) | ✅ Necessário — existe | dado obrigatório do cálculo | Alg p.5 (validação A.1); 190 pos. 18-26 |
| 3 | Año de nacimiento | Date of Birth (Universal "Birth Date") | ✅ Necessário — existe | mínimo por idade >65 / >75 | LIRPF art. 57.2; Alg p.24; 190 pos. 153-156 |
| 4 | Situación familiar (1/2/3) | `$hr.family_situation` | ✅ Necessário — existe | limite excludente de retenção; situação familiar | RIRPF art. 81.1; 190 pos. 157 |
| 5 | NIF del cónyuge | `$hr.related_person_nif` | ✅ Necessário — existe | obrigatório se situação = 2 | Alg p.5 (A.4, C.4); 190 pos. 158-166 |
| 6 | Discapacidad do perceptor (33–65% / ≥65%) | `$hr.disability_code` | ✅ Necessário — existe | mínimo por discapacidade; aumento de gastos dedutíveis | LIRPF arts. 60.1 e 19.2.f; Alg p.22 e p.26; 190 pos. 167 |
| 7 | Ayuda de terceras personas / movilidad reducida (perceptor) | `$hr.disability_assistance_reduced_mobility_flag` | ✅ Necessário — existe | +3.000 assistência; gastos 7.750 | LIRPF arts. 60.1 e 19.2.f; Alg p.22; 190 pos. 167 (código 2) |
| 8 | Movilidad geográfica — **fecha del traslado** | `$hr.geographic_mobility_relocation_date` — Employee Information #14 (CM se `$hr.geographic_mobility` = Yes) | ✅ Incluído na V5.0 | o incremento de 2.000 vale no período da mudança e no seguinte; a data define o S/N de cada exercício (inferência a partir do art. 19.2.f; a entrada do algoritmo é S/N) | LIRPF art. 19.2.f, 2º par.; RIRPF art. 87.2.5º; Alg p.22 (MOVIL); 190 pos. 170 |
| 9 | Rendimentos com período de geração > 2 anos nos 5 exercícios anteriores (art. 18.2) — casilla | `$hr.irregular_income_reduction_not_applied_flag` — Employee Information #13 | ✅ Incluído na V5.0 | sem a comunicação, o pagador considera a redução já aplicada e não pode reaplicar os 30% | LIRPF art. 18.2, 3º par.; RIRPF art. 83.3.a, 2º par.; Alg p.22 (IRREGULAR1) |
| 10 | Descendente: año de nacimiento | `$hr.child_1..4_birth_year` | ✅ Necessário — existe | <3 anos +2.800; corte de 25 anos | LIRPF art. 58; Alg p.11 e p.25; 190 pos. 223-228 |
| 11 | Descendente: **año de adopción o acogimiento** | `$hr.child_1..4_adoption_year` — Descendants #17-20; Child 5-16 em #25, #30 … #80 | ✅ Incluído na V5.0 | +2.800 no ano da inscrição e nos 2 seguintes, qualquer que seja a idade | LIRPF art. 58.2, 2º par.; Alg p.25 (AÑOADOP); XSD `Adopcion`; 190 pos. 223 |
| 12 | Descendente: cómputo por entero | `$hr.child_1..4_full_computation_flag` | ✅ Necessário — existe | descendentes computados por metade salvo direito exclusivo | RIRPF art. 84.2º; 190 pos. 224, 227-228, 251-253 |
| 13 | Descendente: discapacidad | `$hr.child_1..4_disability_code` | ✅ Necessário — existe | mínimo por discapacidade de descendentes | LIRPF art. 60.2; 190 pos. 229-240 |
| 14 | Descendente: ayuda / movilidad reducida | `$hr.child_1..4_disability_assistance_flag` | ✅ Necessário — existe | +3.000 assistência | LIRPF art. 60.2; 190 pos. 233-236 |
| 15 | **5º descendente e seguintes** (o 145 manda anexar outro ejemplar) | `$hr.child_5..16_*` — Descendants #21-80: estrutura até o **Child 16** (teto do XSD da AEAT), 5 campos por filho (Disability Code, Disability Assistance/Reduced Mobility Flag, Full Computation Flag, Birth Year, Adoption/Foster Year) | ✅ Incluído na V5.0 | 4.500 por cada um a partir do 4º; cálculo por descendente (ano, por entero, discapacidade); o serviço aceita até 16 | LIRPF art. 58.1; XSD `Descendiente maxOccurs="16"`; Alg p.10 |
| 16 | Ascendente: año de nacimiento | `$hr.ascendant_1..2_birth_year` | ✅ Necessário — existe | >65 anos 1.150; >75 +1.400 | LIRPF art. 59; 190 pos. 241-244 |
| 17 | Ascendente: **nº de descendentes com quem convive** | `$hr.ascendant_1..2_cohabitation_count` — Ascendants #7-8 (padrão 1) | ✅ Incluído na V5.0 | o mínimo é rateado entre os descendentes do mesmo grau | LIRPF art. 61.1ª; Alg p.25 (`1.150 / CONVIVENCIA`); XSD `Convivencia` |
| 18 | Ascendente: discapacidad | `$hr.ascendant_1..2_disability_code` | ✅ Necessário — existe | mínimo por discapacidade de ascendentes | LIRPF art. 60.2; 190 pos. 245-250 |
| 19 | Ascendente: ayuda / movilidad reducida | `$hr.ascendant_1..2_disability_assistance_flag` | ✅ Necessário — existe | +3.000 assistência | LIRPF art. 60.2; 190 pos. 247-248 |
| 20 | **Pensión compensatoria** ao cônjuge (valor anual, decisão judicial) | `$hr.spousal_compensatory_pension_annual` — Employee Information #10 | ✅ Incluído na V5.0 | reduz a base para calcular o tipo | RIRPF art. 83.3.f; Alg p.29 (`REDU = … + CONYUGE`); 190 pos. 197-209 |
| 21 | **Anualidades por alimentos** a favor dos filhos (valor anual, decisão judicial) | `$hr.child_maintenance_annuities_annual` — Employee Information #11 | ✅ Incluído na V5.0 | escala aplicada em separado; mínimo +1.980 | RIRPF art. 85.2; LIRPF art. 64; Alg p.31; 190 pos. 210-222 |
| 22 | **Préstamo vivienda habitual** (aquisição/reabilitação antes de 2013) — casilla | `$hr.home_loan_deduction_flag` — Employee Information #12 | ✅ Incluído na V5.0 | tipo −2 pontos se retribuição < 33.007,20 | RIRPF arts. 86.1 (últ. par.) e 88.1; LIRPF DT 18ª; Alg p.32 (MINOPAGO); 190 pos. 254 |
| 23 | Lugar, fecha y firma del perceptor | — | ⚪ Não necessário como campo de cálculo | é a própria comunicação; o pagador deve **conservá-la** assinada (meio eletrônico permitido) | RIRPF art. 88.1, 1º e 2º par. |
| 24 | Acuse de recibo (firma y sello del pagador) | — | ⚪ Não necessário como campo de cálculo | comprovante do pagador, não é insumo | Modelo 145, seção 7 |

## Observações
- **SITUPER** (`$hr.perceptor_situation`, no DD e fora da tela do ESS) não é campo do Modelo 145: é a situação laboral que o pagador determina (Alg p.39, dados de entrada; o 145 não tem esse campo).
- As linhas 9, 11, 15, 17 e 22 só se aplicam a casos específicos, mas o pagador não tem outra fonte para elas (RIRPF art. 88.2).
- Campos do DD fora do 145 (Disability Degree %, Child Count, Perceptor Situation; e, fora do grupo, Child Count (Under 3) e as flags separadas Third Party Assistance / Reduced Mobility) não foram avaliados aqui: o pedido foi 145 → DD.

## Pendência
- **Permissão ESS do grupo Employee Tax Relief Declaration:** hoje todos os campos, inclusive os novos, estão como **MSS Write / ESS Read**, apesar de o 145 ser preenchido pelo empregado no ESS. É pergunta de implementação, não de compliance; levada à Nihita no chat STG em 2026-10-19.
