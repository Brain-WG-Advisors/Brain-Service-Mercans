# BE-COVERAGE — Belgium Scope Charter (canonical mandate document)

**Country:** Belgium (BE) | **Currency:** EUR | **Tax year:** 2026
**Scope version:** 1.0
**Decided by:** Wallisson Gomes
**Decided on:** 12 August 2026
**Pipeline:** mercans_pipeline_v2_9.sh (header self-reports v2.8 — stale; body is v2.9)

> This is a LIVING document. Per `shared/QA_METHODOLOGY_BAKE_IN.md` (Pre-Stage-1) and
> failure pattern F24, any real scope change must be written here THE SAME DAY, with a
> dated changelog line below. Do not let a downstream artifact or an external reviewer
> be the thing that exposes drift.

---

## 1. Scope

**Belgium NATIONAL (federal) payroll.** Regional and municipal income-tax layers are an
explicit, documented, unbuilt seam — see § 3.

---

## 2. Quebec-style wrinkle? — **NO**

The Pre-Stage-1 charter asks whether the country has a sub-national jurisdiction running
its OWN parallel statutory system (the Québec case), or merely a modifier on a national
base. Belgium is the second case:

| Element | Level | Evidence |
|---|---|---|
| Wage withholding tax (`bedrijfsvoorheffing` / `précompte professionnel`) | **Federal** | Withholding tables published annually by FPS Finance / FOD Financiën |
| Social security (`ONSS` / `RSZ`), 13.07% employee | **Federal** | Federal competence; distinct from income tax withholding |
| Regional PIT surcharges (~7–9%) | Regional | Settled at **annual assessment**, NOT at source |
| Municipal tax (`taxe communale` / `gemeentebelasting`), 0–~9% | Municipal | Settled at annual assessment; only *estimated* inside the withholding |

**Consequence:** national-only build, same architectural choice Canada made for
non-Québec provincial tax. There is no parallel regime to staff and scope separately.

---

## 3. Known limitations / unbuilt seams

| Seam | Status | Rationale |
|---|---|---|
| Regional PIT surcharges (Flanders / Wallonia / Brussels) | Documented, not built | Assessed annually, not withheld at source |
| Municipal tax (0–~9%, varies by commune) | Documented, not built | Assessed annually; approximated inside federal withholding |
| German-language payroll documents (DE) | Documented, not built | See § 4 |

---

## 4. Official languages — THE scope decision for this country

Belgium has **three** official languages. This exceeds the pipeline's usual
"EN + one local language" pattern, which `QA_METHODOLOGY_BAKE_IN.md` (Stage 7) requires
be flagged explicitly rather than assumed.

### 4.1 The legal constraint

The applicable language is fixed by the employer's **seat of operation**
(`exploitatiezetel` / `siège d'exploitation`) — not by the employee's residence, not by
the contract language, and not by preference:

| Region | Required language | Legal basis | Sanction if wrong |
|---|---|---|---|
| Dutch-speaking (Flanders) | Dutch | Decree of **19 July 1973** | **Nullity** — document deemed never to have existed |
| French-speaking (Wallonia) | French | Decree of **30 June 1982** | **Nullity** |
| Brussels-Capital (bilingual) | Language *of the employee* (NL or FR) | Coordinated laws of **18 July 1966** | Translation at employer's expense, retroactive |
| German-speaking (Ostbelgien) | German | German-language regime | Replacement of the document |

**Critical design constraint: there are NO bilingual personnel documents in Belgium, not
even in Brussels.** Every document is unilingual — either NL or FR. A payslip cannot
serve two languages in one sheet.

### 4.2 The decision

**Stage 7 local tab = Dutch (NL).** Pipeline invoked as `... Belgium BE EUR 2026 Dutch`.

Evidence for choosing NL as the first-built language:

1. **Largest share by place of work** — which is the axis the language law actually keys
   on. Statbel census (4,951,314 employed; 4,812,359 working in Belgium): of the top-10
   municipalities holding >25% of all workers, Flemish ones total **14.5%** (Antwerp 6.0,
   Ghent 4.0, Leuven 1.8, Bruges 1.5, Mechelen 1.2) vs Brussels-region **7.1%**
   (Brussels 5.8, Anderlecht 1.3) and Walloon **5.3%** (Liège 2.2, Charleroi 1.7,
   Namur 1.4).
2. **Highest legal exposure** — Flanders and Wallonia carry nullity; Brussels and the
   German region only require replacement/translation. Building a nullity-region language
   first retires the worst risk first.
3. **Pipeline precedent** — `REFERENCE_Payslip_Tunisia.xlsx` uses tabs `Tunisia (EN)` +
   `Tunisia (FR)`, although Tunisia's constitutionally official language is Arabic. The
   local tab follows the language actually used in payroll administration, and by that
   same test Belgium's highest-volume administrative language is Dutch.

### 4.3 What this decision does NOT authorise

**Belgium is NOT delivered when the NL payslip is done.** Because documents must be
unilingual and the language is set by the employer's seat:

- **FR — MANDATORY second deliverable, not optional.** A Dutch-only payslip is *null and
  void* for any client seated in Wallonia (~5.3% of the top-10 workplace concentration,
  and roughly a third of national employment overall). Scope this as a real work item.
- **DE — explicit unbuilt seam.** The German-speaking Community had 79,479 inhabitants at
  1 January 2024 (<1% of national employment) and the sanction there is replacement, not
  nullity. Document it; do not build it now.

---

## 5. Source material status

**No official source PDFs are present** under `BE-compliance/00-official-sources/`.
Pre-flight warned: the build will rely on web research only, and quality may be lower.
Primary sources to obtain (FPS Finance withholding tables, ONSS/RSZ instructions,
DmfA/Belcotax form documentation) before the artifacts are treated as final.

---

## 6. Changelog

| Date | Change | Artifacts to re-check |
|---|---|---|
| 12 Aug 2026 | Charter created. Scope = federal-only; no Québec-style wrinkle; local language = NL, with FR mandatory-second and DE as documented seam. | — (pre-Stage-1) |
| 12 Aug 2026 | Stage 1 (CCG) complete. `BE-CCG-001-v1.0.docx` produced (158 H3, 140 tables) and `scope_manifest.json` locked. Charter re-read end-to-end against the finished CCG: every OUT-OF-SCOPE tag in the CCG matches §1 and §3 of this charter — federal-only, regional/municipal surcharges documented not built, DE payslip a seam, FR mandatory-second. No drift found. | scope_manifest.json (§3 seams mirrored in `known_limitations`); Stage 3 Report Specs; Stage 7 Payslip (NL first, FR mandatory) |
| 12 Aug 2026 | **Gate 1 review (independent verification).** C1 13/13 modules PASS · C11 136/136 = 100% PASS · C8 zero residual markers PASS. Two corrections applied to Module 6 and the CCG rebuilt: (a) the CJEU reference now carries its case identity (*Chefquet*, C-119/24, ITC 92 Art. 245 vs Art. 45 TFEU) and its true status — set aside with immediate effect, corrective draft bill approved by the Council of Ministers 18 July 2026 and **before the Council of State, not enacted** — replacing the incorrect "being implemented by the tax administration"; (b) the unverified "notional 7% surcharge" figure removed from the withholding-levies table, since the two 7% figures in the guide are different mechanisms. | `scope_manifest.json` known_limitations (corrected + 1 added); Stage 3 Report Specs; Stage 5 WTC and Stage 4 DD — the Art. 245 levy is **assessment-level and must not be modelled in payroll** |
| 12 Aug 2026 | Source-material status unchanged: still **no official PDFs** for the CCG stage; two official PDFs since obtained for Stage 3 (ONSS/RSZ DmfA brochure, FPS Finance Belcotax-on-web brochure income year 2024 — structure only, not 2026 rates). Annex III text (RD 11 Dec 2025, updated 19 Mar 2026) still needed to close the notional-surcharge question. The CCG was built from FPS Finance, NSSO administrative instructions 2026/2 and FPS Employment web sources. This is recorded as a known limitation in `scope_manifest.json` and must be closed before any artifact is treated as final. | All downstream artifacts |
