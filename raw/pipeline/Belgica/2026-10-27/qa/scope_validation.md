# Belgium - Scope Lock-In Validation

**Artifact validated:** `BE-compliance/scope_manifest.json` (27,504 bytes, UTF-8, no BOM)
**Schema reference:** `shared/scope_manifest_template.json` (+ pipeline v2.9 key overrides)
**Validated on:** 12 August 2026
**Manifest version:** 1.0 - scope_decided_by Wallisson Gomes, scope_decided_on 2026-08-12
**Source artifact:** BE-CCG-001-v1.0.docx | **Mandate:** BE-compliance/BE-COVERAGE.md

## VERDICT: PASS - of the 5 warnings raised, W1, W2 and W3 are RESOLVED; W4 and W5 remain OPEN

> **W3 RESOLVED 17 August 2026** (scope_manifest.json v1.8). Superseding the "verified sufficient as-is" status this file recorded on 12 August: the WACC-010 boundary is now stated explicitly and the filing is a Mercans-owned round-trip. See [W3](#w3---wacc-010-is-a-milder-instance-of-the-same-pattern) and Required Action 3.

No blocking finding. The pipeline may proceed to Stage 2 (WTC).

---

## 1. Check Results

| # | Check | Result | Evidence |
|---|-------|--------|----------|
| 1 | File exists, valid JSON | **PASS** | Strict UTF-8 decode OK; 0 U+FFFD; only non-ASCII is U+2014 em-dash (x11). Parses to 21 top-level keys. |
| 2 | All required sections present and non-empty | **PASS** | `employment_types` (10 in / 6 out / rationale), `authority_filings` (9 in / 9 out), `wage_type_categories` (31 in / 7 out / 10 special_rules), `option_mapper_scope` (10 mappers, 44 codes), `integrations` (12 outbound / 12 inbound / 3 both). |
| 3 | Every in-scope filing has all 6 required fields | **PASS** | 10/10 filings carry filing_id, authority, frequency, format, integration_type, product_mapping_required. All integration_type values in {inbound, outbound, both}. All product_mapping_required are real booleans, none null. |
| 4 | Every inbound integration has product_mapping_required set | **PASS** | 12/12 set. All 12 are now `true`; the single `false` (BE-IN-GARNISHMENT-ORDER) was corrected on 12 August 2026 - see **W1, RESOLVED**. |
| 5 | No code in both in_scope and out_of_scope for the same mapper | **PASS** | `option_mapper_scope` is in-scope-only by design (per template `_comment`), so no intra-mapper collision is possible. Cross-section sweep of employment_types and wage_type_categories found 0 exact duplicates and 0 near-duplicates above 0.45 Jaccard similarity. No option-mapper code collides with any out-of-scope entry. |
| 6 | known_failure_patterns_to_check populated with F1-F15 | **PASS** | F1-F22 present (superset of F1-F15; none missing), in the exact bare-code form specified by `_prompts/ccg.md:201`. Canonical definitions live in `shared/country_failure_log.md` (F1-F28). A further 6 patterns (F23-F28) are recorded in `additional_failure_patterns_checked` with disposition notes. |

### Note on `descoping_reason` vs `reason`

`shared/scope_manifest_template.json` specifies `reason` for descoped filings. The manifest uses `descoping_reason` + `client_impact`. **The manifest is correct and the shared template is stale.** Pipeline v2.9 explicitly mandates the newer key (`mercans_pipeline_v2_9.sh:619` - *use `"descoping_reason"` (NOT "reason")*), and the mechanical auditor C20 keys on `descoping_reason` (`mercans_pipeline_v2_9.sh:2219`). All 7 descoped filings carry a non-empty `descoping_reason` and a `client_impact`. **Action: refresh `shared/scope_manifest_template.json` to v2.9 key names** so the next country is not validated against the stale schema.

### B1 - Non-resident handling

**SATISFIED.** Non-residents are not a gap:

- `employment_types.in_scope` includes "Non-resident employee working in Belgium under a Belgian employment contract".
- `option_mapper_scope.withholding_scale` includes "Scale III (non-resident failing the 75% condition)" - non-residents are routed through the same covered income types via the ordinary Annex III scales.
- The non-resident-specific Article 245 ITC 92 fixed 7% additional levy is correctly excluded with a documented basis: it is assessment-level, not withholding-level; CJEU *Chefquet* C-119/24 (12 March 2026) held the fixed rate contrary to Art. 45 TFEU; corrective bill approved by Council of Ministers 18 July 2026 but **not enacted**. Re-check before go-live.
- `known_limitations` warns against conflating the notional 7% surcharge embedded in the Annex III scales with the Art. 245 levy - a correct and non-obvious distinction.

No covered income type lacks non-resident treatment.

---

## 2. B7 Scope Decision Audit Trail

`REVERSIBLE = Y` means reversal is a contained edit against an already-specified data contract. `N` means reversal needs new master data, a new population, or a new engine path.

| DECISION | IN-SCOPE | OWNED-UPSTREAM | INBOUND-DATA-CONTRACT | REVERSIBLE | BASIS |
|---|---|---|---|---|---|
| Federal payroll only; regional/municipal surcharges not modelled | Federal wage withholding tax, embedding a notional 7% surcharge | FPS Finance and the communes, at the annual PIT assessment | None - no commune rate feed needed, nothing withheld at source | **N** | Surcharges are never withheld at source. Reversal needs a per-employee commune code in master data plus an annual municipal rate table. |
| Blue-collar holiday pay paid by the holiday fund, not the employer | The 108% contribution base and the DmfA data feeding the fund | National Annual Holidays Office / sectoral holiday funds | BE-IN-HOLIDAY-FUND: INSZ, service year, gross holiday pay, payment date | **Y** | Statutory split. Inbound contract already specified; used for payslip and leave admin display only. |
| DB2P supplementary pension declarations filed by the pension institution | 8.86% employer contribution, Wijninckx 12.5%, personal contribution deduction and its 30% withholding reduction | Insurer or pension fund (Sigedis filing) | None inbound required; BE-OUT-PENSION-PREMIUM carries INSZ, plan ref, employer premium, employee premium, period | **Y** | All contribution math stays in the engine; only the filing is upstream. |
| Company car data owned by the leasing company | Taxable benefit calculation and the CO2 solidarity contribution | Leasing company / fleet manager | BE-IN-FLEET: INSZ, registration, catalogue value, CO2 g/km, fuel type, first registration date, order date (before/from 1 July 2023), availability dates, employee contribution | **Y** | Fully specified inbound contract including the 1 July 2023 order-date split that drives the formula variant. |
| Student quota authoritative at the NSSO, not in payroll | 2.71% / 5.42% solidarity contributions within quota; ordinary rates beyond it | NSSO Student@work counter | BE-IN-STUDENT-QUOTA: INSZ, calendar year, hours consumed, hours remaining | **Y** | Quota is a counter, not a calculation. Engine applies the rate switch on the inbound value. |
| NL is the first-built payslip language; FR is a mandatory second deliverable; DE is a documented unbuilt seam | EN + NL payslip sheets | None - build sequencing, not an ownership decision | Employer seat-of-operation region per establishment unit must exist in master data | **Y** | Language follows the seat of operation; a Dutch-only payslip is null and void for a Wallonia-seated client. FR is not optional. |
| Directors / form 281.20 out of employment scope | - | Client's accountant; RSVZ/INASTI scheme | None | **N** | Royal Decree no. 38 of 27 July 1967 - directors are self-employed and never enter the DmfA, so the payroll engine cannot produce them. |
| A1-covered posted workers out of scope | - | Home-state social security scheme | None | **N** | Declared in the home scheme under the A1 certificate. Different population and different contribution basis. |
| Temporary agency workers out of scope | - | The agency (employer of record) | None | **N** | Agency is the paying employer; the user undertaking never declares them. |
| Public-sector statutory staff and domestic staff out of scope | - | Own administrative statute / dedicated NSSO schemes | None | **N** | Separate statutory regimes outside the federal private-sector employee population. |
| HR-scope filings descoped: SOCBAL-011, DIVERSITY-012, OHS-013, WORKRULES-016, PERMIT-017 | - | HRMS team / respective authorities | None | **N** | All five require data the payroll system does not hold (headcount demographics, training hours, prevention records, work rules text, permit status). Client impact recorded: refer to HRMS team. |
| Students and flexi-job workers retained IN scope | Solidarity contribution (students, 650h quota), 28% employer regime (flexi-jobs) | - | BE-IN-STUDENT-QUOTA for the quota counter | **Y** | Declared in the same DmfA under a distinct worker code; the calculation is a variant of the ordinary engine, not a separate system. Correct call. |
| LIMOSA-009 descoped to `out_of_scope` (reclassified 12 August 2026) | - | Posting (foreign) employer, via the Limosa web channel - Loi-programme du 27 decembre 2006, arts. 137 et seq. | None | **N** | **W2 RESOLVED.** Not a Belgian entity obligation; the posted-worker (A1) population is already out of employment scope and the engine holds none of the source data. Entry carries `descoping_reason` + `client_impact`. The Belgian host entity's own art. 141 L-1 verification duty is recorded separately as descoped entry BE-NSSO-LIMOSA-L1-VERIFY. |
| ~~WACC-010 kept in_scope with product_mapping_required=false~~ **SUPERSEDED - WACC-010 is in_scope, `integration_type: both`, `product_mapping_required: true`** | Payroll owns the wage basis and working-time regime the declaration reports; the insurer owns adjudication of the claim | The employer's private work accident insurer, and Fedris | `BE-OUT-WACC` (OUT-07) + `BE-IN-WACC-RESPONSE` (IN-16), viewed as `BE-BOTH-WACC` | **Y** | **W3 RESOLVED.** The pmr=false / insurer's-own-portal reading in this row was the 12 August state; it was corrected on 17 August 2026 at scope_manifest v1.2 (finding BE-X10-001) and the boundary was stated at v1.8. See **W3**. |
| Garnishment order inbound corrected to product_mapping_required=true (12 August 2026) | Wage garnishment / assignment (Judicial Code Art. 1409) IS an in-scope wage type, and the Art. 1409 attachable-portion calculation is mapped into the engine | Court, bailiff or administration | BE-IN-GARNISHMENT-ORDER (CSV) - flag and rationale now set; **field-level contract still not specified** | **Y** | **W1 RESOLVED** (F8 flag corrected). Residual open for Stage 3: the Art. 1409 band input fields. |

---

## 3. Warnings Carried Forward

### W1 - F8 risk: inbound garnishment order marked product_mapping_required=false (HIGHEST PRIORITY)

**STATUS: RESOLVED** - fixed directly in `scope_manifest.json` on 12 August 2026, 14:08. The finding below is retained as the audit record; the manifest no longer matches it.

**What was done.** `BE-IN-GARNISHMENT-ORDER.product_mapping_required` was flipped `false` -> `true`, and the `rationale` field the entry previously lacked was added, stating the Judicial Code Art. 1409 attachable-portion touchpoint that makes this a genuine product mapping. Current state of the entry:

```json
{
  "id": "BE-IN-GARNISHMENT-ORDER",
  "from": "Court, bailiff or administration",
  "format": "CSV",
  "product_mapping_required": true,
  "rationale": "The inbound garnishment order supplies the attachable-portion calculation inputs that the payroll engine must map: the order identifies the debt type and creditor, and the engine must apply the Judicial Code Art. 1409 net-wage bands to determine the attachable portion and compute the correct withholding amount. This is a genuine product touchpoint — the Art. 1409 band calculation cannot be performed without the order being mapped into the engine, and it feeds the matching outbound leg BE-OUT-GARNISHMENT to the bailiff or creditor. Contrast with LIMOSA and work-accident-insurer entries, which are filed entirely outside the payroll engine and therefore require no product mapping."
}
```

**Residual (not closed by this fix).** The field-level data contract for the inbound CSV - the Art. 1409 band inputs the engine consumes - is still unspecified: the entry carries `format: "CSV"` but no field list. That half of Required Action 1 remains open for Stage 3.

**Original finding (retained for the audit trail):**

```json
{ "id": "BE-IN-GARNISHMENT-ORDER", "from": "Court, bailiff or administration",
  "format": "CSV", "product_mapping_required": false }
```

This was the one inbound integration with `pmr=false`, and the least defensible of the three `false` values in the manifest:

- `wage_type_categories.in_scope` includes **"Wage garnishment and wage assignment (Judicial Code Article 1409)"** - payroll demonstrably parses and acts on this order.
- `integrations.outbound` includes `BE-OUT-GARNISHMENT` - there is an outbound leg, so the inbound leg is what triggers it.
- Unlike LIMOSA-009 and WACC-010, this entry carried **no `rationale` field** justifying the `false`.
- The manifest's own `_note` states: *"Inbound files where HRB must parse/act = product_mapping_required=true. Never default inbound=not-in-scope."*

This is textbook F8 (inbound integration wrongly excluded from product mapping). The instruction set specifies WARN rather than FAIL for this condition, so it did not block the gate. Art. 1409 attachable-portion bands drive a real calculation; without product mapping the seizure ceiling cannot be computed.

### W2 - LIMOSA-009 classification contradicts the employment-type scope

**STATUS: RESOLVED** - fixed directly in `scope_manifest.json` on 12 August 2026, 14:24. The finding below is retained as the audit record.

**What was done.** `BE-NSSO-LIMOSA-009` was moved out of `authority_filings.in_scope` into `authority_filings.out_of_scope`, carrying the `descoping_reason` + `client_impact` pair the v2.9 schema requires. The legal attribution is now stated on the entry: the Limosa declaration is the foreign posting employer's obligation under the Loi-programme du 27 décembre 2006, arts. 137 et seq., not the Belgian entity's. Current entry:

```json
{
  "filing_id": "BE-NSSO-LIMOSA-009",
  "authority": "National Social Security Office (Limosa declaration)",
  "descoping_reason": "Filed by the foreign posting employer under Loi-programme du 27 décembre 2006, arts. 137 et seq. — not a Belgian entity obligation. The posted-worker population is already excluded from employment_types (A1-certificate holders). The Belgian payroll engine holds none of the source data needed.",
  "client_impact": "No client action from the Belgian payroll product. The posting (foreign) employer files the Limosa declaration through www.limosa.be before the posting starts."
}
```

**A second, previously undocumented gap surfaced by the same research - also now closed.** Verifying the arts. 137 et seq. attribution showed that the *same* law places a separate and distinct duty on the Belgian host entity. Under art. 141, any person for whom or at whose premises activities are performed must verify that the prior declaration under art. 139 was made and must be able to produce the L-1 acknowledgement of receipt; where the L-1 cannot be produced, the Belgian user must report the worker's identification data electronically to the NSSO. Failure carries a level 3 sanction under the Code pénal social. Art. 155 is the parallel provision for posted self-employed persons; both are executed by the Arrêté royal du 20 mars 2007.

That duty was represented **nowhere** in the manifest - not in-scope, not descoped, not mentioned. This is the exact **F15** pattern (*"Removed artifact without descoping decision"*): a real country obligation with no decision record, so scope drifts silently and C20 has nothing to key on. It is worth noting that descoping LIMOSA-009 on its own would have *created* the F15 condition rather than avoided it - removing the last trace of Limosa from the manifest would have left the host entity's own duty invisible.

It is now recorded as a new `authority_filings.out_of_scope` entry, `BE-NSSO-LIMOSA-L1-VERIFY`, descoped as HR-scope with reason and client impact:

```json
{
  "filing_id": "BE-NSSO-LIMOSA-L1-VERIFY",
  "authority": "National Social Security Office (RSZ/ONSS) — recipient of the Limosa \"absence de formulaire L-1\" report; enforced by the Belgian social inspection services under the Code pénal social",
  "descoping_reason": "HR-scope — the host entity's duty to verify a posted worker's Limosa-1 (L-1) acknowledgement of receipt and to report non-compliance is an onboarding/immigration-compliance check, not a payroll computation; it requires no payroll data and produces no payroll output. Legal basis independently confirmed: Loi-programme (I) du 27 décembre 2006, art. 141 (MB 28 décembre 2006) — \"Toute personne auprès de laquelle ou pour laquelle des activités sont exercées doit vérifier que la déclaration préalable visée à l'article 139 a été effectuée et doit pouvoir produire l'accusé de réception de cette déclaration\" — with art. 155 the parallel provision for posted self-employed persons, both executed by the Arrêté royal du 20 mars 2007. Where the L-1 cannot be produced, the Belgian user must report the identification data electronically to the NSSO; failure carries a level 3 sanction under the Code pénal social.",
  "client_impact": "Refer to HRMS/onboarding team. This is a verification and reporting duty, not a filing the payroll product produces."
}
```

**Original finding (retained for the audit trail):**

`BE-NSSO-LIMOSA-009` sat in `authority_filings.in_scope`, but:

- its population (workers posted to Belgium under an A1 certificate) is explicitly in `employment_types.out_of_scope`; and
- its own rationale said *"Filed through the Limosa web channel by the posting (foreign) employer; the Belgian payroll engine does not hold the source data."*

An entry that is owned upstream, whose population is out of scope, and which carries `pmr=false` is functionally descoped while being counted as in-scope coverage. Downstream agents read `authority_filings.in_scope` to decide what to build; C20 would later flag it as "in-scope without spec".

### W3 - WACC-010 is a milder instance of the same pattern

`BE-INS-WACC-010` is in_scope with `pmr=false`, while `wage_type_categories.out_of_scope` lists "Work accident benefit paid by the private insurer". The in-scope reading is defensible - payroll supplies the wage data underpinning the benefit - but the boundary should be stated explicitly (payroll produces the wage declaration; the insurer owns the accident declaration) so Stage 4 does not attempt a full spec.

**STATUS: RESOLVED 17 August 2026 — `scope_manifest.json` v1.8.**

The 12 August status on this item read *"VERIFIED SUFFICIENT AS-IS — no edit made"*, on the ground that the entry's own rationale already stated the boundary ("Filed on the insurer's own portal. Payroll supplies the wage data used for the benefit calculation but does not own the declaration"). **That status is superseded, and the premise it rested on is no longer true**: both the `pmr=false` reading and that rationale text were corrected on 17 August 2026 at scope_manifest v1.2 by the fix closing blocker **BE-X10-001**, which set `BE-INS-WACC-010` to `integration_type: both` / `product_mapping_required: true` (old values preserved in the entry's `_reconciled` block). The W3 question therefore reopened in substance even while this file recorded it as sufficient.

**The boundary, now stated explicitly:**

- **Payroll owns** the wage basis and the working-time regime the declaration reports. `BE-SIR-001` OUT-07 records that these are drawn *from payroll*, and `BE-FEDRIS-001-WorkAccident-Spec.xlsx` v1.2 specifies the mapping field by field — so `product_mapping_required: true` is correct, and Stage 4 **does** build the wage-side mapping.
- **The insurer owns** adjudication of the claim, and the benefit it pays remains **out of scope** as a wage type (`wage_type_categories.out_of_scope`, "Work accident benefit paid by the private insurer"). That exclusion is unchanged and does not contradict the above: the benefit is not a payroll wage type, while the declaration reporting the wage basis is a payroll integration. W3's concern touched only the second.
- **The round-trip is Mercans-owned**, not an insurer-owned leg pair. Ruled by the scope owner (Wallisson Gomes) on 17 August 2026, and **not as a Belgium-specific call**: work accident insurer round-trips are treated as Mercans-owned `both` flows consistently across all country pipelines. Belgium therefore takes the same treatment already given here to Dimona, DmfA, BV and Belcotax.

**Recorded at v1.8:** `BE-BOTH-WACC` added to `integrations.both` (`BE-OUT-WACC` / OUT-07 + `BE-IN-WACC-RESPONSE` / IN-16), in the exact 4-field shape of its four siblings, with `with` and `format` copied from the existing legs rather than re-derived. `integrations.both` is a **view** over the outbound and inbound arrays, so this adds nothing to the flow count — outbound 18, inbound 18, distinct total 36, unchanged. See `integrations._both_note`, which previously registered this entry as deliberately left open pending exactly this ruling.

### W4 - F4 risk: formats declared without verified schema citations

`known_limitations[0]` states plainly that **no official source PDFs were available** under `00-official-sources/` and that the CCG was built from official web sources plus specialist publishers. Formats are asserted (XML for Dimona/DmfA/BV/Belcotax/ASR/WACC, XLSX for the individual account and payslip, CSV for LIMOSA and the garnishment order) but no XSD or cahier des charges is cited. Two look inferred rather than verified: LIMOSA as CSV (it is a web-form channel) and the garnishment order as CSV.

Auditor **C23 will FAIL any Stage-4 spec containing XML without an XSD citation.** Obtain the DmfA and Belcotax schemas, the NSSO 2026/2 administrative instructions, and the Annex III 2026 rules text before Stage 4.

### W5 - Annex III notional surcharge percentage unconfirmed

`known_limitations[6]`: the exact notional surcharge component embedded in the withholding scales could not be confirmed from FPS Finance's published pages, while `special_rules[7]` already asserts a specific figure (7%, giving 26.75 / 42.80 / 48.15 / 53.50 against PIT rates of 25 / 40 / 45 / 50). **A rate the manifest simultaneously asserts and flags as unconfirmed must be read off the Annex III text (RD 11 December 2025, last updated 19 March 2026) before any WTC rate, DD field or worked example depends on it.**

---

## 4. Observations (no action required)

- **Coverage depth is strong.** 31 in-scope wage-type categories and 10 special_rules capture the genuinely non-obvious Belgian mechanics: the 108% blue-collar base applied to both sides, double holiday pay carrying employee-only contributions, meal-voucher all-or-nothing requalification, the quarterly (not monthly) basis of the special social security contribution with an end-of-quarter true-up, and the non-cumulative nature of Belgian wage withholding tax with no December true-up.
- **2026 legislative deltas are captured**, not assumed from a prior year: removal of the EUR 15 rounding of the withholding base (RD 11 December 2025), the voluntary overtime 360-hour regime from 1 April 2026, the homeworking allowance at EUR 160.99/month from 1 March 2026, and the two notice-period reform dates (1 June and 1 August 2026).
- **The CBA no. 90 dual-ceiling trap is documented** (social EUR 4,255 vs tax EUR 3,701, with the band between them socially exempt but taxable) - a classic source of wage-type errors.
- **The stock-option boundary is drawn correctly**: `benefit_type` includes "Stock options accepted within 60 days" (the taxable grant event) while `wage_type_categories.out_of_scope` excludes gains on later exercise or disposal. These are different events, not a contradiction - the overlap scan correctly cleared it.
- `integrations.both` (3 entries) restates Dimona, DmfA and Belcotax, which also appear as outbound legs. Distinct IDs, so no collision; the redundancy is by template design. *(State as at 12 August 2026. The array now holds 5 - BV was added at manifest v1.7 and WACC at v1.8 - and `integrations._both_note`, added at v1.7, makes the "redundancy by design" reading explicit: the array is a **view** over the outbound and inbound arrays and must never be added to an integration count.)*
- **C20 second half not evaluable at this gate.** `04-reports-spec/` is empty, so "every in-scope filing has a spec file" cannot pass yet. That is a Stage-4 check, not a scope lock-in check.

---

## 5. Required Actions Before Stage 3 and Stage 4

| # | Action | Owner | Gate |
|---|--------|-------|------|
| 1 | **PARTLY DONE 2026-08-12 14:08** - `product_mapping_required` flipped to `true` with a rationale (see W1). **Still open:** specify its field-level contract (Art. 1409 band inputs) | CCG / integrations | Stage 3 |
| 2 | **DONE 2026-08-12 14:24** - LIMOSA-009 reclassified to `out_of_scope` with `descoping_reason` + `client_impact`; the art. 141 host-entity verification duty it surfaced added as a new descoped entry `BE-NSSO-LIMOSA-L1-VERIFY` (F15 gap closed). No further action | CCG | Closed |
| 3 | **DONE 2026-08-17** - WACC-010 boundary stated explicitly, and the ruling went the other way on the second limb: payroll = the wage basis and working-time regime the declaration reports (`pmr: true`); the insurer = adjudication of the claim, and the benefit it pays stays out of scope as a wage type. The declaration itself is a **Mercans-owned round-trip**, per pipeline-wide practice, registered as `BE-BOTH-WACC` at scope_manifest v1.8. The "insurer = declaration" phrasing of this action, drafted on 12 August, is superseded. No further action | CCG / integrations | Closed |
| 4 | Obtain DmfA / Belcotax XSDs, NSSO instructions 2026/2, Annex III 2026 text into `00-official-sources/` | Research | Stage 4 (C23) |
| 5 | Confirm the Annex III notional surcharge percentage against the primary text before any dependent rate is published | WTC | Stage 2 |
| 6 | Re-check the Art. 245 corrective bill's enactment status before go-live | Compliance | Go-live |
| 7 | Update `shared/scope_manifest_template.json` from `reason` to `descoping_reason` / `client_impact` to match pipeline v2.9 | Shared templates | Before next country |

---

**Validated by:** Scope Lock-In Validation gate (v2.9, B7 + B1 controls)
**Result:** PASS - proceed to Stage 2 (WTC). **W1 RESOLVED** (pmr flipped to `true` with rationale; field-level contract residual open for Stage 3) and **W2 RESOLVED** (LIMOSA-009 descoped, art. 141 F15 gap closed) in `scope_manifest.json` on 12 August 2026. **W3 RESOLVED** on 17 August 2026 (WACC-010 boundary stated; `BE-INS-WACC-010` corrected to `both` / `pmr: true` at scope_manifest v1.2 per BE-X10-001, and the Mercans-owned round-trip registered as `BE-BOTH-WACC` at v1.8; Required Action 3 closed) - superseding this file's 12 August "verified sufficient as-is" status on that item. **W4 OPEN** (Required Action 4, Stage 4 / C23) and **W5 OPEN** (Required Action 5, Stage 2) are carried forward.
