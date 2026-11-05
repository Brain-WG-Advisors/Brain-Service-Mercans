# DESIGN QA r1 - source-hunter part, facts ready 2026-11-04
Backups: _research/design-fix/_backup/ (MD5-BEFORE.txt). Lock taken/released. Ledger lines added. validate_contract --all PASS (108 files).

## 1. Seven practice-note keys (CCG-m13_practices-facts.json)
All seven reworded to what the held copies carry, none made a limitation; the elements already sit in register rows (no new rows needed):
- practice.ne.use_circular_en_tables -> register_id US-NES5-010 (Circular EN 2026, 2.26-4.60%, A.2) + _also US-NES5-018 (statute 4.55%)
- practice.oh.flat_rate_vs_tables -> US-OHS5-007 + _also US-OHS5-008 (ORC 5747.06), US-OH-006 and US-OHS5-001 (tables 1.6/2.99/3.4% from 2026-08-01)
- practice.wi.use_w166_tables -> US-WIS5-010 + _also US-WIS5-011 (W-166 PDF read: 3.54/4.65/5.30/7.65)
- practice.sc.withholding_rates_2026 -> US-SCS5-004 + _also US-SCS5-005 (Act 110 1.99/5.21, IL 26-20)
- practice.ma.pfml_split -> US-MAS5-012 + _also US-MAS5-026 (Ch. 101 s.45)
- practice.ga.rate_change_2026 -> value now "OPB trigger holds at 1 December" (the "2026-12-01 report" date is not in the act text read)
- practice.ct.tables_vs_rules -> "up to 0.48/period" removed (TPG-211 states no difference size); 0.48 is a derived comparison (rules 79.30 vs table 78.82, CT annex example 10)

## 2. Register consumed_by
DESIGN appended on 173 rows (the 165 of _pipeline/DESIGN-bindings.csv plus 8 re-bound rows). Backup taken first.

## 3. Facts for the two DD fields (keys for the DD builder)
Supplemental wage withholding method election (all exist, US-FEDS5-003 / US-FEDQ1-002 / US-FEDQ1-007):
fed.fit.supplemental.flat_rate (22), fed.fit.supplemental.mandatory_rate (37), fed.fit.supplemental.mandatory_threshold (1000000), fed.fit.supplemental.aggregate_method, fed.fit.nra.addon.flat_rate_supplemental.applies; State-level: <st>.wh.supplemental.rate / wi.pit.supplemental.flat_rates / vt.pit.supplemental.ratio_of_federal / sc.pit.supplemental.flat_rate.exists.
State-assigned SUI rate: no per-State "rate notice" principle fact exists and none could be read from a held copy (DOL US-FEDP51-010 gives min/max only). Existing keys to use: <st>.sui.employer.rate.min, <st>.sui.employer.rate.max, <st>.sui.new_employer.rate (+ .total, .range variants). Open limitation: the notice mechanism per State (e.g. TX US-TXP52-002 "rate notices mailed early December" is register text only, no local copy). Closing document: each State UI agency's employer rate-notice / experience-rating page.

## 4. Facts the design builder needs - already present, nothing added except MA
- Student FICA exemption: fed.students.treatment (US-FEDS5-029)
- F/J/M/Q FICA exemption: fed.fica.nra.fjmq_exempt, fed.fica.nra.fjmq_exempt.scope, fed.fica.nra.other_visas.liable (US-FEDR2-001, US-FEDS5-016); totalization: fed.fica.totalization.exemption_rule (US-FEDR2-003)
- Statutory employee FUTA: fed.statutory_employee.treatment (US-FEDR3-005: FUTA for drivers and traveling salespersons only)
- Thresholds: fed.household.fica_cash_threshold, fed.household.futa_quarter_threshold, fed.agricultural.per_worker_threshold / total_threshold / futa_quarter_threshold, fed.election_worker.fica_threshold
- Reciprocity -> residence State: multi.resident_out_of_state.<st>.withholding_rule (CT GA SC OK NY MS MA WI IL KS VT NC CO OH LA), multi.reciprocity.<st>.partners / .certificate (NJ-165, REV-419EX US-MULTI-011), multi.reciprocity.dc.nonresident_exempt
- MA PFML by date earned: NEW ma.pfml.rate.selection_basis (US-MAS5-012, quoted); with ma.pfml.split (2026 and 2027 objects), ma.pfml.split.decision

STATUS: COMPLETE
