# NORWAY PAYROLL FILING: STEP-BY-STEP GUIDE
Tax and social security (a-ordningen) · NAV · Tax cards · Payments · as of 29 October 2026 · Pilot v1.1

> **Nota interna (pt-BR):** piloto do formato ([[TAP_fluxo_entregas]], §3, S1–S8). O documento segue a estrutura do guia do Vietnã (`raw/drive/2026-10-29-modelo-manju/`) e está em inglês porque vai para a Manju e o Marko.
> Histórico: [[NO_fluxo_entregas_v0.1]] (v0.1); a v1.0 em pt-BR foi substituída por esta. Hub: [[Noruega]].
> Evidência de hoje: pacote `Norway/Henkel Norway - 2026-09/` e `dados/monday_12paises.md`.

## 1. How to use this guide
**Parts:**
1. **A-melding:** the monthly report of pay, employment, withholding tax, employer's contribution (AGA) and finance tax.
2. **NAV filings:** income reports (inntektsmelding) for benefit claims, and layoff notices.
3. **Tax cards:** retrieving each employee's skattekort.
4. **Payments.**
5. **Roadmap, open questions and onboarding.**

**Target model:** HR Blizz builds the a-melding and sends it through the Skatteetaten API, using an Altinn system user that the customer approves once. Mercans files for many customers through a client relationship. There is no per-filing signature.

| Step type | Meaning |
|---|---|
| **SYSTEM STEP** | Done automatically by Mercans' platform (HR Blizz) |
| **PORTAL STEP** | Done by a person on skatteetaten.no, Altinn or nav.no |
| **CUSTOMER ACTION** | Approval by the customer (the employer) |
| **AUTHORITY** | Skatteetaten, NAV or another authority response |
| **[Verify]** | To confirm with Dev, BAU or the authority before go-live |

## 2. Channel per report
| Part | Report | Target route | Current route (evidence) |
|---|---|---|---|
| 01 | **A-melding** (monthly) to Skatteetaten, NAV and SSB [C3] | Skatteetaten API (Altinn 3): "Fra 2026 er dette den eneste måten å sende inn a-melding fra system" ("From 2026 this is the only way to send the a-melding from a system") [C1]. Authenticated with a system user on Maskinporten [R2, C2]. | Sep 2026: the receipt shows `"kildesystem":"HR Blizz"` and `"mottakstatus":"mottatt"`, with no deviations. **BAU (Umesh, e-mail 30 Oct 2026):** "We currently upload the XML file manually via the Altinn portal." So today the file comes from HR Blizz but is **uploaded by hand** [C7]. **[Verify]** whose login is used (follow-up sent 30 Oct). |
| 02 | **Inntektsmelding** (per event: sickness, parental, pregnancy, care and training benefits) to NAV | Since 21 May 2026 only on NAV's portal: "Alle inntektsmeldinger og refusjonskrav må fra den datoen sendes via Min side – arbeidsgiver" ("from that date all income reports and refund claims must be sent via My page – employer") [C8]. An API for payroll systems is being built: "Våren 2026 har Nav startet arbeidet med å tilby API…" ("In spring 2026 NAV started work on offering an API…") [C8]. The parental-benefit API runs on Maskinporten + Altinn 3 [C9]. | ⚠️ Not seen. Not in the certification pack. |
| 02 | **Layoff notice** (permittering) to NAV | "Skal du permittere ansatte, melder du fra til Nav så tidlig som mulig" ("if you lay off employees, notify NAV as early as possible") [C10] | Customer-owned (HR event, no payroll file). **[Verify]** |
| 03 | **Tax cards** (retrieved, not filed) | "For at du skal kunne hente skattekort direkte fra lønnssystemet, må lønnssystemet være integrert med Skatteetatens API-er" ("to fetch tax cards directly from the payroll system, the system must be integrated with Skatteetaten's APIs"); new solution "fra 15. juni 2026" ("from 15 June 2026") [C11] | ⚠️ Not seen. **[Verify]** whether HR Blizz fetches tax cards through the API. |

## 3. Channel per payment
| Payment | Amount | Deadline | How and to whom |
|---|---|---|---|
| **Withholding tax** (forskuddstrekk) | As declared on the a-melding | "senest første virkedag etter utbetaling av ytelsen" ("no later than the first working day after the payment"), skattebetalingsloven § 10-10(1) [S13] | To Skatteetaten. The account and KID reference "følger med tilbakemeldingene" ("come with the feedback") on the a-melding [S22]. |
| **Employer's contribution** (AGA) and finance tax | Sum of the feedback for the two months of the term [S22] | 15 Jan, 15 Mar, 15 May, 15 Jul, 15 Sep, 15 Nov (§ 10-10(2)) [S13] | Same: account and KID from the feedback [S22] |
| **Wage garnishment for tax debt** (utleggstrekk) | As declared on the a-melding | On the employer's own initiative [S22] | To Skatteetaten [S22] |

Current route: in monday, **Statutory Payments is unticked for all Norwegian clients**, so Mercans does not appear to pay (BAU Master, 29 Oct 2026). This is an INFERENCE. **[Verify]** that the customer pays.

## 4. Part 01: A-melding

### 4.1 Model at a glance
| # | Step | Who | Type |
|---|---|---|---|
| 01 | Lock the month's payroll | HR Blizz | SYSTEM STEP |
| 02 | Build the a-melding XML v2.3; validate against the XSD [S01] and the R1 2026 business rules [S04] | HR Blizz | SYSTEM STEP |
| 03 | One-time approval: the customer approves HR Blizz's system user with the a-melding access package (4.2). No signature is needed per filing. | Customer | CUSTOMER ACTION |
| 04 | Get the system-user token from Maskinporten and send to the a-melding API | HR Blizz | SYSTEM STEP |
| 05 | Receive the feedback (A03): status, deviations, amounts, account and KID [S02, S03, S22] | Skatteetaten | AUTHORITY |
| 06 | On deviations: correct and resend the same month, back to step 02 | HR Blizz | SYSTEM STEP |
| 07 | Store the feedback with the filing; pass the amounts and KID to the payment step (section 3) | HR Blizz | SYSTEM STEP |

**Deadline:** "senest den 5. i måneden etter utløpet av den kalendermåned opplysningene gjelder" ("no later than the 5th of the month after the calendar month the information covers"), a-opplysningsforskriften § 2-1 [S21].

### 4.2 Mercans one-time set-up
| # | Step | Who | Type | Source |
|---|---|---|---|---|
| 01 | Register HR Blizz in Altinn as a system and declare the access packages it needs: "Systemleverandører må registrere sine systemer i Altinn og angi hvilke tilgangspakker som er nødvendige" ("system vendors must register their systems in Altinn and state which access packages are needed") | Mercans Dev | SYSTEM STEP | R2 |
| 02 | Maskinporten client for the system: "Systembruker bygger videre på Maskinporten" ("the system user builds on Maskinporten"). **[Verify]** the requirements for a non-Norwegian vendor. | Mercans Dev | SYSTEM STEP | C2 |
| 03 | The customer approves: "må du godkjenne tilgangspakkene som settes opp og gi systemet rettigheter til å levere på vegne av deg" ("you must approve the access packages and give the system rights to file on your behalf"). The vendor can let the customer create the system user on the Altinn portal or guide the customer through it in the vendor's own system [C2]. | Customer | CUSTOMER ACTION | R1, C2 |
| 04 | **Agent model**, one Mercans set-up for many customers: "Systembruker støtter både kunder som jobber på vegne av seg selv … og på vegne av klienter (regnskapsførere etc.)" ("the system user supports customers acting for themselves and on behalf of clients, such as accountants"). "Regnskapsfører lønn" (payroll accountant) is one of the packages that give access to the a-melding [C6, C7]. **[Verify]** whether Mercans qualifies for that role. | Mercans + customer | CUSTOMER ACTION | C2, C6, C7 |

**Hard date:** "Fra 17. november vil det ikke lenger være mulig å sende inn med gamle Altinn-roller" ("from 17 November it will no longer be possible to submit with the old Altinn roles") [C6, updated 01 Oct 2026; also R1].

### 4.3 Interim route: a-melding as a file upload (filvedlegg)
Used when the payroll system is not integrated with the API [C7]: "Virksomheter som skal rapportere opplysninger via a-melding, men som ikke har systemintegrasjon mot a-ordningens API" ("businesses that report through the a-melding but have no system integration with the a-ordning API").

| # | Step | Where | Type |
|---|---|---|---|
| 1 | Export the a-melding XML from HR Blizz: "hent ut en XML‑fil fra lønnssystemet" ("get an XML file from the payroll system") [C4] | HR Blizz | SYSTEM STEP |
| 2 | Log in to the service "A-melding som filvedlegg" on skatteetaten.no with a person who holds one of these access packages: A-ordningen, Ansvarlig revisor, Regnskapsfører lønn, Regnskapsfører med/uten signeringsrettighet, Revisormedarbeider [C7] | skatteetaten.no | PORTAL STEP |
| 3 | "Logg inn, last opp fil og send inn" ("log in, upload the file and submit") [C7] | skatteetaten.no | PORTAL STEP |
| 4 | Read the feedback (A03) in the Altinn inbox or on skatteetaten.no [S22] | Altinn | PORTAL STEP |

**[Verify]** the screens and click path. The service needs an ID-porten login, and we do not log in to portals.

**Context:** "Mandag 15. juni stenges a-ordningen sine tjenester i Altinn II", including system submission (A02) and feedback (A03) ("on Monday 15 June the a-ordning services in Altinn II close") [C4]. The September 2026 a-melding was accepted after that date, so it went through the new solution, either by API or by upload. This is an INFERENCE; question Q1 confirms it.

## 5. Part 02: NAV filings
| Filing | Steps today (target = API when NAV publishes it) | Type |
|---|---|---|
| **Inntektsmelding** | 1. NAV notifies the employer: "Du skal først sende inn inntektsmelding når du får melding fra Nav" ("send it only when NAV asks") [C12]. 2. Mercans builds the income data from payroll. 3. Someone with NAV access sends it on "Min side – arbeidsgiver" [C8]. 4. NAV handles the claim and any refund. | SYSTEM STEP (2) + PORTAL STEP (3) + AUTHORITY (1, 4) |
| **Layoff notice** | The customer notifies NAV [C10] | Customer-owned |

**Gap:** the API for payroll systems exists for parental benefit (Maskinporten scope `nav:inntektsmelding/foreldrepenger`) [C9]; the other benefits are still being built [C8]. **[Verify]** the sickness-benefit channel.

## 6. Roadmap to full automation
| Workstream | What is missing | Owner | Priority |
|---|---|---|---|
| **01 Rulings** | Can Mercans act as "regnskapsfører lønn" for its customers, or must each customer approve HR Blizz directly? (4.2 step 04) | Compliance research | Medium |
| **02 Entity and access** | Maskinporten requirements for Mercans as a vendor. **[Verify]** | Dev | Medium |
| **03 Product build: critical path** | Confirm that HR Blizz sends through the API with a system user on access packages, not old Altinn roles, **before 17 Nov 2026**. If it is an upload today, build the API integration. | Dev | **High** |
| 03 Product build | Store the A03 feedback with each filing and pass account and KID to payments (improvement M-07) | Dev | Medium |
| 03 Product build | Tax cards through the Skatteetaten API (new solution since 15 Jun 2026) [C11] | Dev | Medium |
| 03 Product build | Inntektsmelding through NAV's API as each benefit's API is released [C8, C9] | Dev | Low (depends on NAV) |
| **04 Interim operations** | If uploads are used: document who uploads and with whose login | BAU | High |
| Onboarding | Every Norwegian customer approves the system user or access package (section 8) **by 17 Nov 2026** | Implementation + customer | **High** |

**Main risk:** after 17 Nov 2026, filing with old Altinn roles stops [C6]. The channel itself already works (accepted Sep 2026). The risk is the authorisation behind it. If it rests on an old role, the November a-melding (due 5 Dec) will not go through.

## 7. Open questions
**To Dev and BAU (current route):**
- **Q1 (answered 30 Oct: manual XML upload on Altinn; login still open):** is the a-melding sent from HR Blizz through the Skatteetaten API, or exported as XML and uploaded on skatteetaten.no? Under whose login?
- **Q2 (Dev):** does HR Blizz use a system user with the new access packages, and has every Norwegian customer approved it?
- **Q3 (BAU Umesh):** who sends the inntektsmelding to NAV? Who pays the withholding tax and the AGA?

**To research or the authority ([Verify]):**
- Maskinporten and system user for a non-Norwegian vendor.
- What the "Regnskapsfører lønn" role requires.
- The NAV channel for sickness-benefit inntektsmelding.

## 8. Customer onboarding (once per entity)
- Organisation number and employer registration active.
- HR Blizz system user approved in Altinn with the a-melding access package [R1, C2], **by 17 Nov 2026** for existing customers [C6].
- Agent model: client relationship with Mercans and the matching package [C2, C6] **[Verify]**.
- Tax cards: the system integrated with the tax-card API, or a manual fetch until it is ready [C11].
- NAV: a person with access to "Min side – arbeidsgiver" for income reports, until NAV's API covers them [C8].
- Payments: account and KID come with each month's feedback [S22]; agree who pays (section 3).

## 9. Link index
| ID | Source | URL | Local file (`raw/docs/oficiais/NO/`) |
|---|---|---|---|
| C1 | Skatteetaten: A-meldingen for end-user systems | https://www.skatteetaten.no/samarbeidspartnere/sluttbrukersystemer/a-meldingen-sbs/ | `2026-10-29-canal/amelding_sbs_2026-10-29.html` |
| C2 | Altinn docs: System user | https://docs.altinn.studio/nb/authorization/what-do-you-get/systemuser/ | `2026-10-29-canal/altinn_systembruker.html` |
| C3 | Skatteetaten: A-meldingen | https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/a-meldingen/ | `2026-10-29-canal/amelding_forside.html` |
| C4 | Skatteetaten: Altinn II closes 15 June | https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/a-meldingen/siste-fra-a-ordningen/altinn-ii-stenges-15.-juni/ | `2026-10-29-canal/altinn_ii_stenges_15juni.html` |
| C6 | Skatteetaten: New access packages for the a-melding (updated 01.10.2026) | https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/a-meldingen/siste-fra-a-ordningen/nye-tilgangspakker-for-a-meldingen/ | `2026-10-29-canal/nye_tilgangspakker_amelding.html` |
| C7 | Skatteetaten: A-melding as file upload | https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/a-meldingen/levere/levering-fra-system/ | `2026-10-29-canal/amelding_levering_fra_system.html` |
| C8 | NAV: New income reports | https://www.nav.no/arbeidsgiver/nye-inntektsmeldinger | `2026-10-29-canal/nav_nye_inntektsmeldinger.html` |
| C9 | NAV (navikt): fp-inntektsmelding-api | https://github.com/navikt/fp-inntektsmelding-api | `2026-10-29-canal/github_fp_inntektsmelding_api.html` |
| C10 | NAV: Layoffs | https://www.nav.no/arbeidsgiver/permittere | `2026-10-29-canal/nav_permittere.html` |
| C11 | Skatteetaten: Fetch tax cards via payroll system | https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/skattekort-og-skattetrekk/skattekort/hent-skattekort-via-lonnssystem/ | `2026-10-29-canal/skattekort_via_lonnssystem.html` |
| C12 | NAV: Send income report on nav.no | https://www.nav.no/arbeidsgiver/sende-inntektsmelding | `2026-10-29-canal/nav_sende_inntektsmelding.html` |
| C5 | NAV: Inntektsmelding (overview) | https://www.nav.no/arbeidsgiver/inntektsmelding | `2026-10-29-canal/nav_inntektsmelding.html` |
| R1–R3 | Skatteetaten: Altinn re-establishment (businesses, vendors, accountants) | https://www.skatteetaten.no/samarbeidspartnere/reetablering-altinn/ | `2026-10-29-altinn3/` |
| S01–S04, S13, S21, S22 | XSD, A02/A03 models, formats, business rules, skattebetalingsloven § 10-10, a-opplysningsforskriften § 2-1, deadlines and payment | see `sources.md` | `internal-certification/references/Norway/2026/` |

## Bloco de prova (pt-BR, interno)
- **Pedido → resposta:** as 8 seções do modelo estão cobertas e o documento está em inglês. As 3 lacunas da v1.0 foram fechadas com fonte oficial:
  - filvedlegg: C7;
  - skattekort: C11;
  - inntektsmelding: C8, C9 e C12.

  A lista de entregas foi conferida contra as páginas para empregador da Skatteetaten e da NAV. Entrou o aviso de permittering como entrega do cliente.
- **Teste:** cada trecho entre aspas foi buscado no texto limpo do HTML baixado (C1, C2, C4, C6, C7, C8, C9, C10, C11, C12, R1, R2, S13, S21, S22).
- **Ainda [Verify]:** a rota de hoje (Q1–Q3), o Maskinporten para fornecedor estrangeiro, o papel de "regnskapsfører lønn", o canal da inntektsmelding de sykepenger e as telas do portal (não fazemos login).
- **Confiança 90%** na rota-alvo e nos prazos. A rota de hoje depende das respostas.
