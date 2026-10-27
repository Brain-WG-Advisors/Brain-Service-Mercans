# -*- coding: utf-8 -*-
import io, json, os

BASE = "03-statutory-integrations"
OUT = "08-skill/co-compliance/references/03-sir.md"
SIRMD = "_txt/skill/sir.md"

L = []
W = L.append

W("""# Colombia - Statutory Integration Register (SIR) - COMPLETE REFERENCE

**Source artifacts:**
- `03-statutory-integrations/CO-SIR-INDEX-001-v1.0.docx` (v1.0, 2026-09-04) - the authority index
- `03-statutory-integrations/integration-landscape.json` - the si-discovery landscape (Agent 3 / STAGE 6a)
- `03-statutory-integrations/DIAN-NE/` - the single Configuration Runbook, phases **P1-P7** + `INTERLINKAGES.md`
  + `effort-estimates.md`

**Jurisdiction:** Colombia (CO) - **Currency:** COP - **Tax year:** 2026
**Discovery verdict:** `HAS_INTEGRATIONS`
**Posture:** 4 authorities - **1 genuine machine-to-machine** (DIAN-NE) and **3 manual**. Of the 6 in-scope
filings, **1 is carried system-to-system and 5 are manual.**

> **[QA MAJOR-03 - naming correction]** CCG Module 10 refers to a register `CO-SIR-001 to CO-SIR-007`.
> **No such artifact family exists.** The register is **`CO-SIR-INDEX-001`**, an authority index over 4
> authorities, plus **one** runbook (DIAN-NE) organised as **7 phases P1-P7**. The "007" is a
> mis-transcription of the 7-phase runbook structure.

**Channel types absent from the Colombian landscape entirely:** SFTP - REST API published by an authority -
AS2 / AS4 - government-published message queue.

---

# Part A - Authority Index (CO-SIR-INDEX-001 v1.0, verbatim)

""")

sir = io.open(SIRMD, encoding="utf-8").read()
W(sir.strip())

# ---------------- Part B: landscape json ----------------
d = json.load(io.open(os.path.join(BASE, "integration-landscape.json"), encoding="utf-8"))

W("\n\n---\n\n# Part B - Integration landscape (`integration-landscape.json`, verbatim)\n")
W("| Key | Value |")
W("|---|---|")
for k in ("country", "code", "country_code", "currency", "year", "generated", "produced_by", "verdict"):
    W("| `%s` | %s |" % (k, d.get(k, "")))
W("\n**Verdict rationale:**\n")
W("> " + str(d["verdict_rationale"]).replace("\n", "\n> "))

W("\n**Schema note (verbatim):**\n")
W("> " + str(d["_schema_note"]).replace("\n", "\n> "))

W("\n**Inputs read:**\n")
for x in d["inputs_read"]:
    W("- `%s`" % x)

s = d["summary"]
W("\n## B.1 Summary\n")
W("| Metric | Value |")
W("|---|---|")
for k in ("authorities_total", "authorities_with_system_to_system", "authorities_manual_only",
          "in_scope_filings_total", "in_scope_filings_via_system_to_system", "in_scope_filings_manual"):
    W("| %s | **%s** |" % (k.replace("_", " "), s[k]))
W("| integration postures present | %s |" % " - ".join(s["integration_postures_present"]))
W("| no channel type found anywhere | %s |" % " - ".join(s["no_channel_type_found_anywhere"]))


def render_val(v, indent=""):
    if isinstance(v, list):
        out = []
        for x in v:
            if isinstance(x, dict):
                out.append("  - " + "; ".join("**%s**: %s" % (kk, vv) for kk, vv in x.items()))
            else:
                out.append("  - %s" % x)
        return "\n" + "\n".join(out)
    if isinstance(v, dict):
        return "\n" + "\n".join("  - **%s**: %s" % (kk, vv) for kk, vv in v.items())
    return " %s" % v


W("\n## B.2 Authorities - full record for each of the 4\n")
for a in d["authorities"]:
    W("\n### %s - %s\n" % (a["code"], a["name"]))
    for k, v in a.items():
        if k in ("code", "name"):
            continue
        W("- **%s**:%s" % (k, render_val(v)))

W("\n## B.3 Non-authority flows excluded from the verdict\n")
W("| ID | Name | Counterparty | Why excluded |")
W("|---|---|---|---|")
for x in d["non_authority_flows_excluded_from_the_verdict"]:
    W("| %s | %s | %s | %s |" % (x.get("id", ""), x.get("name", ""), x.get("counterparty", ""),
                                 str(x.get("why_excluded", "")).replace("|", "\\|")))

W("\n## B.4 Out-of-scope authorities\n")
W("| Code | Name | Channel | Integration | Status |")
W("|---|---|---|---|---|")
for x in d["out_of_scope_authorities"]:
    W("| %s | %s | %s | %s | %s |" % (x.get("code", ""), x.get("name", ""),
                                      str(x.get("channel", "")).replace("|", "\\|"),
                                      x.get("integration", ""), x.get("status", "")))

W("\n## B.5 Research method\n")
rm = d["research_method"]
for k, v in rm.items():
    W("- **%s**:%s" % (k, render_val(v)))

W("\n## B.6 Open questions\n")
for q in d["open_questions"]:
    if isinstance(q, dict):
        W("- " + "; ".join("**%s**: %s" % (kk, vv) for kk, vv in q.items()))
    else:
        W("- %s" % q)

W("\n## B.7 Sources (15)\n")
W("| Title | URL | Type | Retrieved |")
W("|---|---|---|---|")
for x in d["sources"]:
    W("| %s | %s | %s | %s |" % (x.get("title", ""), x.get("url", ""), x.get("type", ""), x.get("retrieved", "")))

# ---------------- Part C: DIAN-NE runbook ----------------
W("""

---

# Part C - DIAN-NE Configuration Runbook (the only integrable authority), phases P1-P7

Reproduced in full from `03-statutory-integrations/DIAN-NE/`. This is the **only** Configuration Runbook
produced for Colombia: DIAN-MUISCA, PILA-OI and FONDOS-CESANTIAS all carry `integration: false` and are
manual channels, so there is no connection to configure. That absence is a deliberate scoping decision,
not an omission.
""")

FILES = [
    ("_phase-index.md", "C.0 Phase index and readiness statement"),
    ("P1-authority-channel-profile.md", "C.1 P1 - Authority and channel profile"),
    ("P2-connectivity-and-security.md", "C.2 P2 - Connectivity and security"),
    ("P3-outbound-payload-spec.md", "C.3 P3 - Outbound payload specification"),
    ("P4-inbound-response-handling.md", "C.4 P4 - Inbound response handling"),
    ("P5-validation-rules-and-error-handling.md", "C.5 P5 - Validation rules and error handling"),
    ("P6-test-and-certification-habilitacion.md", "C.6 P6 - Test, certification and habilitacion"),
    ("P7-operations-monitoring-maintenance.md", "C.7 P7 - Operations, monitoring and maintenance"),
    ("INTERLINKAGES.md", "C.8 Interlinkages - payroll-engine dependencies and the other three authorities"),
    ("effort-estimates.md", "C.9 Build effort estimates"),
]

for fn, title in FILES:
    p = os.path.join(BASE, "DIAN-NE", fn)
    body = io.open(p, encoding="utf-8").read().strip()
    # demote headings by two levels so the assembled file keeps one hierarchy
    lines = []
    for ln in body.split("\n"):
        if ln.startswith("#"):
            lines.append("##" + ln)
        else:
            lines.append(ln)
    W("\n\n---\n\n## %s\n\n<!-- source: %s -->\n" % (title, p))
    W("\n".join(lines))

txt = "\n".join(L)
io.open(OUT, "w", encoding="utf-8").write(txt)
print(OUT, len(txt))
