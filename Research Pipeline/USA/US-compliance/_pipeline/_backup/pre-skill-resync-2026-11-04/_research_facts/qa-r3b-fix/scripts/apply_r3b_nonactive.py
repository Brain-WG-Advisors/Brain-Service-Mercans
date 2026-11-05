"""Agent 2, 2026-11-02: re-point / qualify citations of non-active register rows in facts and packs.
No fetch. Backups in _research/qa-r3b-fix/_backup3/. Log: apply-nonactive-log.json."""
import os, glob, json, shutil

B = r"C:/Users/instituto/Documents/brain-service/Research Pipeline/USA/US-compliance"
R = B + "/_research"
BK = R + "/qa-r3b-fix/_backup3"
os.makedirs(BK, exist_ok=True)
for f in (glob.glob(R + "/*-facts.json") + glob.glob(R + "/*-research-pack.md")
          + [B + "/00-official-sources/SOURCE-REGISTER.md", B + "/00-official-sources/legal-basis-register.csv"]):
    d = BK + "/" + os.path.basename(f)
    if not os.path.exists(d):
        shutil.copy2(f, d)

FACT_NOTE = [
    ("CCG-annex_AL-*", "Birmingham 1% is tier C (US-ALP7-001 MANUAL) - not a fact.",
     "Birmingham 1% rests only on a tier-C MANUAL lead (see the AL pack) - not a fact."),
    ("CCG-annex_AZ-*", "(superseded derivation row US-AZS5-028)",
     "(the earlier derived row, now superseded by US-AZB5-001)"),
    ("CCG-annex_CO-*", "2027 15.71 is a PROPOSED rule (US-COB5-002, provisional): not a fact until adopted.",
     "2027 15.71 is a PROPOSED rule (provisional register row, see unresolved): not a fact until adopted."),
    ("CCG-annex_DE-*", "Live page text identical to the 2026-10-13 Wayback copy of US-DEP51-003.",
     "Live page text identical to the 2026-10-13 Wayback copy (earlier row, superseded by US-DES5-006)."),
    ("CCG-annex_FED-*", "Supersedes US-FEDP6-001.",
     "Supersedes the earlier P6 row (lineage in the register supersedes column of US-FEDS5-028)."),
    ("CCG-annex_HI-*", "Act text gated (403) [US-HIS5-030];",
     "Act text gated (403; gated row listed in the HI pack);"),
    ("CCG-annex_LA-*", "supersedes the NOI (US-MULTIS5-022)",
     "supersedes the NOI (lineage in the register supersedes column of US-LAS5-002)"),
    ("CCG-annex_ME-*", "CORRECTS US-MEP51-004 / US-MEP52-006 (superseded).",
     "CORRECTS two earlier superseded ME payslip rows (listed in the ME pack)."),
    ("CCG-annex_MULTI-*", "supersedes the NOI row US-MULTIS5-022.",
     "supersedes the NOI row (lineage in the register supersedes column of US-LAS5-002)."),
    ("CCG-annex_RI-*", "US-RI-006 value is wrong (do not use)",
     "the superseded 280-RICR-20-55-10 summary row carried a wrong value (do not use)"),
    ("CCG-annex_RI-facts.json", "(US-RI-006 MANUAL)", "(US-RI-006, superseded)"),
    ("CCG-annex_TX-*", "supersedes MANUAL US-TXPIT-001",
     "supersedes the earlier MANUAL row (lineage in the register supersedes column of US-TXS5-001)"),
    ("CCG-annex_WV-*", "supersedes US-WVLAB-001;",
     "supersedes the 21-5-3 snippet row (lineage in the register supersedes column of US-WVS5-008);"),
    ("PSL-facts.json", 'Corrects earlier \\"no itemised duty\\" rows (US-MEP51-004 / -2-006 superseded).',
     'Corrects earlier superseded \\"no itemised duty\\" rows (listed in the ME pack).'),
    ("PSL-facts.json", "US-NYS5-023 (MANUAL B)", "US-NYS5-023 (superseded by US-NYB5-003)"),
    ("RSPEC-*", "MI statute and penalty not located; US-MIS5-026 partial",
     "MI statute and penalty not located (the earlier partial row is superseded by US-MIB5-001)"),
    ("RSPEC-*", "Michigan new-hire statute and penalty not located; US-MIS5-026 partial",
     "Michigan new-hire statute and penalty not located (the earlier partial row is superseded by US-MIB5-001)"),
    ("WTC-country_specific-facts.json", "Journal: US-RI-006 (other rate) is wrong.",
     "Journal: the superseded 280-RICR-20-55-10 summary row (other rate) is wrong."),
    ("CCG-m05_social_security-facts.json", "CCG-annex_CA-facts.json (US-CAEDD-004)", "CCG-annex_CA-facts.json (US-CAP7-002)"),
    ("CCG-research-pack.md", "CCG-annex_CA-facts.json (US-CAEDD-004)", "CCG-annex_CA-facts.json (US-CAP7-002)"),
]

PACK = [
    ("CCG-annex_AZ-research-pack.md",
     "State minimum wage 2026/2027: the derived 15.15 (2026) and 15.65 (2027) rest on an unconfirmed 2025 base of 14.70 and on the tier-C MANUAL row US-AZS5-028 (ICA page 403). They are NOT facts (see unresolved az.minwage.hourly). The CPI-U steps are facts. Tipped cash wage likewise derived (12.15/12.65) and not emitted.",
     "State minimum wage 2026/2027: 15.15 (2026) and 15.65 (2027), tipped cash wage 12.15/12.65, are facts quoted from the ICA posters [A.2, US-AZB5-001 / US-AZB5-002], which supersede the earlier tier-C derived row US-AZS5-028. The CPI-U steps are facts."),
    ("CCG-annex_CO-research-pack.md",
     "2027 state 15.71 / tipped 12.69 and Denver 19.84, and 2026 Edgewater 18.17 / Boulder 16.82 are tier-B leads only [US-COS5-011 MANUAL]: not facts (CO-OQ-3).",
     "2027 state 15.71 / tipped 12.69 exists only as a PROPOSED rule (US-COB5-002, provisional): not a fact. Denver 2027 19.84 and Edgewater 2026 18.17 remain tier-B leads only (US-COS5-011 MANUAL): not facts (CO-OQ-3). Boulder City and unincorporated Boulder County are facts [A.2, US-COB5-302 / US-COB5-303]."),
    ("CCG-annex_CO-research-pack.md",
     "[A.2, US-COS5-001, quoted from authority page, conf high] \u2014 COMPS Rule 3; highest applicable (local) minimum applies. 2027 15.71 is tier-B only (US-COS5-011 MANUAL), not a fact.",
     "[A.2, US-COB5-001, quoted from authority page, conf high] \u2014 COMPS Rule 3; highest applicable (local) minimum applies. 2027 15.71 is a PROPOSED rule (US-COB5-002, provisional): not a fact until adopted."),
    ("CCG-annex_IA-research-pack.md", "No SDI/TDI/PFML [US-IAP52-004 legacy; mandate US-MQ-32].",
     "No SDI/TDI/PFML located; not a fact: the absence rests only on tier-B MANUAL US-IAP52-004 (open: `ia.pfml.state_program.none`; mandate US-MQ-32)."),
    ("CCG-annex_MS-research-pack.md", "- **SDI/TDI/PFML/LTC:** none in MS [US-MSP52-006].",
     "- **SDI/TDI/PFML/LTC:** none located in MS; not a fact: the absence rests only on tier-B MANUAL US-MSP52-006 (open: `ms.sdi_pfml.exists`)."),
    ("CCG-annex_MS-research-pack.md", "Local paid-leave mandates are preempted (17-1-51) [US-MSS5-009, US-MSP52-006].",
     "Local paid-leave mandates are preempted (17-1-51) [US-MSS5-009]. The PFML absence rests only on tier-B MANUAL US-MSP52-006 (open: `ms.sdi_pfml.exists`)."),
    ("CCG-annex_NC-research-pack.md", "- **SDI/TDI/PFML:** none in NC [US-NCP51-005].",
     "- **SDI/TDI/PFML:** none located in NC. Agency level: the only NCDOR wage-based tax is withholding [US-NCP9V-002]; the programme-level absence rests only on tier-B MANUAL US-NCP51-005, so it is not a fact."),
    ("CCG-annex_NC-research-pack.md", "- **PFML:** none [US-NCP51-005].",
     "- **PFML:** none located [US-NCP9V-002, agency level; programme-level absence rests only on tier-B MANUAL US-NCP51-005, not a fact]."),
    ("CCG-annex_OH-research-pack.md", "- **No SDI/TDI/PFML** [US-OHP51-004].",
     "- **No SDI/TDI/PFML located;** not a fact: the absence rests only on tier-B MANUAL US-OHP51-004 (open: `oh.sdi_pfml.exists`)."),
    ("CCG-annex_OH-research-pack.md", "- **No PFML,** so there is no benefit-side payroll interaction [US-OHP51-004].",
     "- **No PFML located,** so no benefit-side payroll interaction is modelled (absence rests only on tier-B MANUAL US-OHP51-004; open: `oh.sdi_pfml.exists`)."),
    ("CCG-annex_UT-research-pack.md", "Utah is not among the 13 states + DC with PFML programmes [US-UTP52-006].",
     "The USTC tax list carries Employer Withholding Tax as the only wage-based employer tax [A.2, US-UTB5-003; fact `ut.sdi_pfml.exists`]."),
    ("CCG-annex_UT-research-pack.md", "- **PFML:** none [US-UTP52-006].",
     "- **PFML:** none [US-UTB5-003; fact `ut.sdi_pfml.exists`]."),
    ("CCG-annex_UT-research-pack.md", "- **Language:** no Utah language rule [US-UTL-001].",
     "- **Language:** no Utah language requirement stated in the required-postings list [US-UTP9L-001]; the statute check (34-28-3) was not read (gated row US-UTL-001), so the statutory absence is not a fact."),
    ("CCG-annex_PA-research-pack.md",
     "multiplied by 3.07% [US-PA-008, US-PAP52-001]. **Rounding rule for PIT: none published** [US-PAP52-001/002].",
     "multiplied by 3.07% [US-PA-008]. **Rounding rule for PIT: none published** [US-PAP52-002; the guide-level check sits on MANUAL US-PAP52-001]."),
    ("CCG-annex_SC-research-pack.md", "The statute does not mention paycards [US-SC-004, US-SCP52-006].",
     "The statute does not mention paycards [US-SCP52-006 for 41-10-30; the 41-10-40 text is held only in the superseded chapter copy US-SC-004, so the 41-10-40 detail is not a fact]."),
    ("CCG-annex_SC-research-pack.md", "such as hours, rates or employer address [US-SCP52-006, US-SC-004].",
     "such as hours, rates or employer address [US-SCP52-006; the 41-10-40(B) clause is held only in the superseded chapter copy US-SC-004]."),
    ("CCG-annex_SC-research-pack.md", "[US-SCR3-009, US-SCP51-004]. Confidence: 90%.", "[US-SCR3-009]. Confidence: 90%."),
    ("CCG-annex_SC-research-pack.md", "| US-SCS5-018, US-SCP52-004 |", "| US-SCS5-018, US-SCR3-001 |"),
    ("CCG-annex_SD-research-pack.md", "[US-SDS5-002 A.1; US-SD-002]", "[US-SDS5-002 A.1]"),
    ("CCG-annex_SD-research-pack.md", "[US-SDP51-002, US-SDP52-002]", "[US-SDP51-002]"),
    ("CCG-annex_SD-research-pack.md", "[US-SDS5-011 A.3; US-SDP52-002]", "[US-SDS5-011 A.3; PFML: US-SDP51-002]"),
    ("CCG-annex_VT-research-pack.md", "  - **Employee contribution:** none, and the tax cannot be withheld [US-VTP51-007].",
     "  - **Employee contribution:** none located; not a fact: the statement sat on US-VTP51-007, superseded by US-VTS5-009, which does not restate it (open: `vt.sui.employee.rate`)."),
    ("CCG-annex_NY-research-pack.md",
     "The DCWP FAQ (02/2026) PDF and NYC Admin. Code 20-911 ff. were not reached (US-NYS5-023).",
     "The DCWP FAQ (02/2026) PDF is now held [A.3, US-NYB5-003, superseding the lead row US-NYS5-023]; NYC Admin. Code 20-911 ff. was not reached."),
    ("CCG-annex_OR-research-pack.md", "- **Content (ORS 652.610(1)(b))** [US-ORP51-003; US-ORS5-026]:",
     "- **Content (ORS 652.610(1)(b))** [US-ORS5-026; its local file holds the full ORS 652.610 text; items (A)-(K) were first transcribed under the superseded row US-ORP51-003]:"),
    ("CCG-research-pack.md", "CA SDI 1.3%, no cap [US-CAEDD-004];", "CA SDI 1.3%, no cap [US-CAP7-002];"),
    ("RSPEC-research-pack.md", "NCDOR GEN-58 [US-NCW1B-002];", "NCDOR GEN-58 [US-NCP51-003];"),
]

log = []
for pat, old, new in FACT_NOTE + PACK:
    hit = 0
    for f in glob.glob(R + "/" + pat):
        t = open(f, "rb").read().decode("utf-8")
        n = t.count(old)
        if n:
            open(f, "wb").write(t.replace(old, new).encode("utf-8"))
            hit += n
            log.append({"file": os.path.basename(f), "old": old, "new": new, "count": n})
    if not hit:
        print("NO HIT:", pat, old[:90])
for f in glob.glob(R + "/*-facts.json"):
    json.load(open(f, encoding="utf-8"))
json.dump(log, open(R + "/qa-r3b-fix/apply-nonactive-log.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print("edits", len(log), "files", len(set(x["file"] for x in log)))
