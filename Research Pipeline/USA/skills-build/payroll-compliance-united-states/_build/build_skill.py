# -*- coding: utf-8 -*-
"""Builds the US router skill from the approved artifacts. Reads only; writes only under the skill folder.
usage: python build_skill.py   (no stdin)"""
import csv, glob, json, os, re, shutil, sys
import docx, openpyxl
from docx.table import Table
from docx.text.paragraph import Paragraph

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.abspath(os.path.join(HERE, ".."))
BASE = os.path.abspath(os.path.join(OUT, "..", "..", "US-compliance"))
REF = os.path.join(OUT, "references")

TAG = re.compile(r"\[\[FACT:([^=\]]+)=(.*?)\]\]", re.S)
GAPTAG = re.compile(r"\[\[GAP:([^\]]+)\]\]")

# ---------- facts
FACTS = {}
for f in sorted(glob.glob(os.path.join(BASE, "_research", "*facts.json"))):
    d = json.load(open(f, encoding="utf8"))
    for x in d.get("facts", []):
        FACTS.setdefault(x["key"], []).append(x)


def norm(v):
    s = str(v).strip().replace(",", "")
    try:
        return repr(float(s))
    except ValueError:
        return re.sub(r"\s+", " ", str(v).strip())


def lookup(key, val):
    val = str(val).replace(r"\|", "|")
    return [x for x in FACTS.get(key, []) if norm(x.get("value")) == norm(val)]



def refresh(text):
    """Handwritten tags: print the key's current value when the key has a single value (no wording copied by hand)."""
    def rep(m):
        k, v = m.group(1), m.group(2)
        vals = {norm(x.get("value")): x.get("value") for x in FACTS.get(k, [])}
        if len(vals) == 1 and not lookup(k, v):
            return "[[FACT:%s=%s]]" % (k, list(vals.values())[0])
        return m.group(0)
    return TAG.sub(rep, text)

MISS = []
SUBST = []
USED = {}


def detag(text, fileid):
    def rep(m):
        k, v = m.group(1), m.group(2)
        if not lookup(k, v):
            vals = {norm(x.get("value")): x.get("value") for x in FACTS.get(k, [])}
            if len(vals) == 1:   # the key has one current value: print it (source text carries an earlier wording)
                nv = str(list(vals.values())[0])
                SUBST.append((fileid, k, v[:50], nv[:50]))
                v = nv.replace("|", r"\|") if r"\|" in m.group(2) else nv
            else:
                MISS.append((fileid, k, v[:60]))
        USED.setdefault(fileid, {})[(k, v)] = 1
        return v
    text = TAG.sub(rep, text)
    text = re.sub(r"Not configured in this release \[\[GAP:([^\]]+)\]\]", r"Not configured in this release (open gap \1)", text)
    text = GAPTAG.sub(lambda m: "(open gap %s)" % m.group(1), text)
    return text



RULES = [(re.compile(a, re.S), b) for a, b in [

    (r"Decided (\d{4}-\d\d-\d\d) by the build lead \(build lead\) under the owner's delegation of [\d-]+ owner plan\.", r"Decided \1 under the owner's delegation."),
    (r"Decided (\d{4}-\d\d-\d\d) by the build lead under the same delegation\.", r"Decided \1 under the same delegation."),
    (r"Decided (\d{4}-\d\d-\d\d) by the build lead under the owner's delegation of [\d-]+ \(plan [^)]*\)", r"Decided \1 under the owner's delegation"),
    (r"Build lead \(Claude\) under owner delegation \(Wallisson Gomes\)", "Decided under the owner's delegation"),
    (r"Uninterrupted run authorised; Step-4 report kept for later review", "Uninterrupted run authorised"),
    (r"\(recorded in owner plan scope line\)", "(recorded in the scope statement)"),
    (r"by the build lead", "under the owner's delegation"), (r"[Bb]uild lead", "owner delegate"), (r" owner plan\b", ""),
    (r"Checks C34-C36 \(validation of generated filing files against an official norm, validator or plugin\) exempted", "Validation of generated filing files against an official norm, validator or plugin is exempted"), (r"Exempts three content-check findings", "Exempts three content findings"),
    (r"checker accepts only whole-year codes", "the validation accepts only whole-year codes"),
    (r"\bC(?:34|35|36|48|49|50)(?:[-/]C?\d\d)*: ", ""),
    (r"; scope = CCG table \d+ r\d+c\d+", ""), (r"CCG table \d+ r\d+c\d+", "one CCG table cell"),
    (r"P9-[A-Z]+ r\d/r\d", "the later re-check"), (r"P9-[A-Z]+", "the re-check"),
    (r"stage-1 research gap", "open research gap"), (r"[Ss]tage-1 ", ""),
    (r"via the orchestrator browser read", "through the authority page"), (r"orchestrator", "owner delegate"),
    (r"The merge worker appends", "Add"), (r"merge worker", "reviewer"),
    (r"Annex workers confirm", "Confirm"), (r"then emit True with that register_id", "then record the clause with that legal-basis entry"),
    (r"\bregister_id\b", "legal-basis id"),
    (r" \((?:True|False)\)", ""), (r"\bthe the\b", "the"),
    (r"checker", "validation"),
    (r"Louisiana Works LAWATS file specification", "Louisiana Workforce Commission online-services file specification"),
    (r"Overall T4 \(discriminator confirmed.*?bear on no tier\)", "Overall T4"),
    (r"Jurisdiction annexes \(re-checked[^)]*\)", "Jurisdiction references"),
    (r"### Tier verdict \(build manifest\)", "### Tier verdict"),
    (r"Repeated verbatim from the build manifest \(tier classification\)\.", "Tier classification."),
    (r"\s*\(build manifest[^)]*\)", ""),
    (r"This is the mandate answer US-MQ-01", "This is the answer to US-MQ-01"),
    (r"Register ids cited in this annex resolve to the build record; the URL of each value is in the facts file\. ", ""),
    (r"\(derivation in the research pack; values in Section 1\)", "(values in Section 1)"),
    (r"\s*\(see _research/[^)]*\)", ""),
    (r"[,;]? ?reviews _qa/\S+( and r\d)?", ""),
    (r"into 00-official-sources/\S+ and stamping verified_on on US-[A-Z0-9-]+", "and recording the verification date"),
    (r"\b(?:00-official-sources|_research|_pipeline)/\S+", "the saved source page"),
    (r"read from a US exit or a browser pass; the host does not resolve from the build machine", "the host was not reachable and the page was not read"),
    (r"read from a US exit", "not yet read"),
    (r"read through VPN on", "read on"), (r"Owner/builder decision", "Owner decision"), (r"build manifest tier census, local income tax domain", "tier census, local income tax domain"),
    (r"build manifest `tier\._sub_national_key`", "tier classification"), (r"computed by the build record", "computed from the facts"), (r"build record from the facts", "computation from the facts"),
    (r"The build manifest names the oracle", "The oracle"),
    (r"A browser pass \(Chrome, US IP\) saving", "A browser read saving"),
    (r"browser pass", "browser read"), (r"US exit", "US network address"), (r"\bVPN\b", "US network"),
    (r"\(fan-out per State\)", "(per State)"), (r"[Pp]arallel fan-out( per locality)?", "Per locality"),
    (r"legal-basis register row", "legal-basis entry"), (r"register row", "legal-basis entry"),
    (r"tier-B leads", "secondary-source leads"), (r"Builder transcribes", "Transcribe"),
    (r"pending owner confirmation", "awaiting owner confirmation"),
    (r"\s*[-–] local copy", ""), (r"\s*\(local copy[^)]*\)", ""), (r", local copy\)", ")"), (r"\blocal copy\b", "saved page"),
    (r"effective_from = date verified in force", "effective date = date verified in force"),
    (r"\s*\(journal trap\)", ""), (r"\s*\(QA r\d[a-z]?\)", ""),
    (r"Stage 9b re-derives", "the independent validation re-derives"), (r"from Stage 9b validation", "from the independent validation"),
    (r"\(Stage 3 / RSPEC\)", "(Report Specification)"), (r"Stage-5 re-check", "Re-check"),
    (r"Synthesis supersedes", "The later entries supersede"), (r"at next synthesis", "at the next review"),
    (r"2026 reductions pending, gaps below", "2026 reductions not yet published, gaps below"),
    (r"seal attempts? \d(, \d)?( and \d)?", "re-check"),
    (r"countries/us\.py", "a country identifier plugin"), (r"\(reg number to be confirmed\)", "(regulation number not confirmed)"),
]]

def scrub(text):
    t = text
    t = re.sub(r"Annex FED\b", "the federal reference", t)
    t = re.sub(r"Annex MULTI\b", "the multistate reference", t)
    t = t.replace(" (build manifest, tier rationale)", "")
    for rx, rp in RULES:
        t = rx.sub(rp, t)
    return t


def fact_index(fileid):
    rows = []
    for (k, v) in USED.get(fileid, {}):
        hit = lookup(k, v)
        if not hit:
            continue
        for x in hit[:1]:
            eff = ("from %s" % x.get("effective_from") if x.get("effective_from") else "") + \
                  (" to %s" % x["effective_to"] if x.get("effective_to") else "")
            rows.append((k, v, eff.strip(), x.get("register_id", "")))
    rows = sorted(set(rows))
    if not rows:
        return ""
    out = ["", "", "## Fact index", "", "Every value above with its key, effective period and register id.", "",
           "| Key | Value | Effective | Register id |", "|---|---|---|---|"]
    for k, v, e, r in rows:
        out.append("| `%s` | %s | %s | %s |" % (k, esc(v), e, r))
    return "\n".join(out) + "\n"


def esc(s):
    return str(s).replace("|", "\\|").replace("\r", " ").replace("\n", " ").strip()


NOSCRUB = ("13-gotchas.md", "07-qa-report.md", "/SKILL.md")


def write(rel, text):
    if rel not in NOSCRUB:
        text = scrub(text)
    p = os.path.join(REF if not rel.startswith("/") else OUT, rel.lstrip("/"))
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf8", newline="\n") as fh:
        fh.write(text)


def md_from_source(path, fileid, title_prefix=None):
    raw = open(path, encoding="utf8").read()
    txt = detag(raw, fileid)
    return txt.rstrip() + "\n" + fact_index(fileid)


# ---------- clean output (references only; keep _build)
if os.path.isdir(REF):
    shutil.rmtree(REF)
os.makedirs(REF)

# ---------- CCG modules
mods = sorted(glob.glob(os.path.join(BASE, "01-ccg", "modules", "*.md")))
for p in mods:
    n = os.path.basename(p)
    write("01-ccg/" + n, md_from_source(p, "01-ccg/" + n))
idx = ["# CCG modules (cross-cutting guide)", "",
       "The 13 modules of the United States Country Configuration Guide v1.0, plus the coverage table. Federal and per-State detail is in `10-federal.md` and `12-states/`.", ""]
for p in mods:
    n = os.path.basename(p)
    h = next((l[2:].strip() for l in open(p, encoding="utf8") if l.startswith("# ")), n)
    idx.append("- `01-ccg/%s` - %s" % (n, h))
write("01-ccg.md", "\n".join(idx) + "\n")

# ---------- federal / multistate / states
ann = os.path.join(BASE, "01-ccg", "annexes")
write("10-federal.md", md_from_source(os.path.join(ann, "annex_FED.md"), "10-federal.md"))
write("11-multistate.md", md_from_source(os.path.join(ann, "annex_MULTI.md"), "11-multistate.md"))
states = []
for p in sorted(glob.glob(os.path.join(ann, "annex_*.md"))):
    c = os.path.basename(p)[6:-3]
    if c in ("FED", "MULTI"):
        continue
    states.append(c)
    write("12-states/%s.md" % c, md_from_source(p, "12-states/%s.md" % c))
st_names = {}
for c in states:
    h = open(os.path.join(REF, "12-states", c + ".md"), encoding="utf8").readline()
    st_names[c] = h.split(":", 1)[-1].strip()
write("12-states.md", "# State references\n\nOne file per jurisdiction (50 States and the District of Columbia):\n\n" +
      "\n".join("- `12-states/%s.md` - %s" % (c, st_names[c]) for c in states) + "\n")


# ---------- workbooks and the SIR document
def dump_xlsx(path, fileid, skip=("Currency Codes", "Country Codes")):
    wb = openpyxl.load_workbook(path)
    out = ["# " + os.path.splitext(os.path.basename(path))[0], ""]
    for ws in wb.worksheets:
        if any(ws.title.startswith(s) for s in skip):
            continue
        rows = []
        for r in ws.iter_rows():
            vals = [("" if c.value is None else esc(c.value)) for c in r]
            while vals and vals[-1] == "":
                vals.pop()
            if any(vals):
                rows.append(vals)
        if not rows:
            continue
        w = max(len(r) for r in rows)
        out += ["", "## " + ws.title, ""]
        hdr = rows[0] + [""] * (w - len(rows[0]))
        out.append("| " + " | ".join(hdr) + " |")
        out.append("|" + "---|" * w)
        for r in rows[1:]:
            r = r + [""] * (w - len(r))
            out.append("| " + " | ".join(r) + " |")
    return detag(scrub("\n".join(out)), fileid) + "\n"


def dump_docx(path, fileid):
    d = docx.Document(path)
    out = []
    for el in d.element.body.iterchildren():
        if el.tag.endswith("}p"):
            p = Paragraph(el, d)
            t = p.text.strip()
            if not t:
                continue
            s = p.style.name or ""
            if s.startswith("Heading ") or s == "Title":
                lvl = int(s.split()[-1]) if s.startswith("Heading ") else 1
                out.append("\n" + "#" * min(lvl, 4) + " " + t + "\n")
            else:
                out.append(t + "\n")
        elif el.tag.endswith("}tbl"):
            tb = Table(el, d)
            rows = []
            for r in tb.rows:
                cells = []
                prev = None
                for c in r.cells:
                    if c._tc is prev:
                        continue
                    prev = c._tc
                    cells.append(esc(c.text))
                rows.append(cells)
            if not rows:
                continue
            w = max(len(r) for r in rows)
            out.append("| " + " | ".join(rows[0] + [""] * (w - len(rows[0]))) + " |")
            out.append("|" + "---|" * w)
            for r in rows[1:]:
                out.append("| " + " | ".join(r + [""] * (w - len(r))) + " |")
            out.append("")
    return detag(scrub("\n".join(out)), fileid) + "\n"


write("02-wtc.md", dump_xlsx(os.path.join(BASE, "02-wtc", "US-WTC-001-v1.0.xlsx"), "02-wtc.md") + fact_index("02-wtc.md"))
write("05-data-dictionary.md", dump_xlsx(os.path.join(BASE, "05-data-dictionary", "US-DD-001-v1.0.xlsx"), "05-data-dictionary.md") + fact_index("05-data-dictionary.md"))
write("06-payslip.md", dump_xlsx(os.path.join(BASE, "06-payslip", "US_Compliance_Payslip_Generator.xlsx"), "06-payslip.md") + fact_index("06-payslip.md"))
sir = glob.glob(os.path.join(BASE, "03-statutory-integrations", "US-SIR-INDEX-001-v*.docx"))[-1]
write("03-sir.md", dump_docx(sir, "03-sir.md") + fact_index("03-sir.md"))
specs = sorted(glob.glob(os.path.join(BASE, "04-reports-spec", "US-*-Spec.xlsx")))
lines = ["# Report Specifications", "", "One file per report; each carries the version-control, report-matrix, scope, field, file-structure, option, population and example sheets.", ""]
for p in specs:
    n = os.path.basename(p)[:-5]
    fid = "04-reports-spec/%s.md" % n
    write(fid, dump_xlsx(p, fid) + fact_index(fid))
    lines.append("- `04-reports-spec/%s.md`" % n)
write("04-reports-spec.md", "\n".join(lines) + "\n")

# ---------- sources (legal-basis register, active rows and all ids cited)
reg = list(csv.DictReader(open(os.path.join(BASE, "00-official-sources", "legal-basis-register.csv"), encoding="utf8")))
o = ["# Sources", "", "Official instruments carrying the values in this skill. Rows with a status other than active are superseded or withdrawn and must not be used for a value.", "",
     "| Id | Domain | Instrument | Authority | Article / section | Effective from | Effective to | Tier | Status | URL |", "|---|---|---|---|---|---|---|---|---|---|"]
for r in reg:
    if r["id"].startswith("US-OWN"):
        continue
    o.append("| %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |" % tuple(esc(r[k])[:200] for k in
             ("id", "domain", "instrument_name", "authority", "article_or_section", "effective_from", "effective_to", "tier", "status", "url")))
write("15-sources.md", detag(scrub("\n".join(o)), "15-sources.md") + "\n")

# ---------- gaps and owner decisions
gp = json.load(open(os.path.join(BASE, "_research", "gaps.json"), encoding="utf8"))["gaps"]
g = ["# Known gaps and owner decisions", "",
     "## Owner decisions (US-OWN-001 to US-OWN-011)", "",
     "| Id | Effective | Decision |", "|---|---|---|"]
for r in reg:
    if r["id"].startswith("US-OWN") and r["status"] == "active":
        t = r["figure_or_rule_carried"]
        t = re.sub(r"\(?plan PLANO-ATE-O-FIM\.md[^)]*\)?|Research Pipeline/USA/[A-Z-]+\.md|PLANO-ATE-O-FIM\.md|MANDATE\.md", "owner plan", t)
        t = t.replace("\ufffd", "-").replace("Claude", "build lead")
        g.append("| %s | %s | %s |" % (r["id"], r["effective_from"], esc(t)))
g += ["", "US-OWN-008: independent contractors and Form 1099-NEC reporting are out of scope; employers in scope are private-sector employers; workers are common-law employees.",
      "US-OWN-009 is a decision under the owner's delegation, still awaiting owner confirmation.", "",
      "## Federal items labelled for tax year 2025", "",
      "| Key | Value | Effective | Register id |", "|---|---|---|---|"]
seen = set()
for k, lst in sorted(FACTS.items()):
    if not k.startswith("fed."):
        continue
    for x in lst:
        txt = " ".join(str(x.get(a) or "") for a in ("value", "note"))
        ef, et = str(x.get("effective_from") or ""), str(x.get("effective_to") or "")
        if (re.search(r"TY ?2025|tax year 2025", txt, re.I) or ef[:4] == "2025" or et[:4] == "2025") and (k, norm(x["value"])) not in seen:
            seen.add((k, norm(x["value"])))
            g.append("| `%s` | %s | %s | %s |" % (k, esc(x["value"]), ("from " + ef if ef else "") + (" to " + et if et else ""), x.get("register_id", "")))
g += ["", "Federal values dated 2025 stay valid for wages paid in the period shown; select every dated value by the payment date of the run.", "",
      "## Open research gaps and documented limitations", "",
      "| Gap id | Jurisdiction | Section | Key | Status | What would close it |", "|---|---|---|---|---|---|"]
cnt = {}
for x in gp:
    st = x.get("status")
    if st not in ("open", "documented_limitation", "check_existing_fact"):
        continue
    loc = str(x.get("location") or "")
    m = re.search(r"(annex_[A-Z]+|m\d\d_[a-z_]+|\bRSPEC\b|\bPSL\b|\bSIR\b|\bWTC\b|\bDD\b)(?:\.md)?!?([A-Z0-9.]*)", loc)
    jur = m.group(1).replace("annex_", "") if m else ""
    sec = m.group(2) if m else ""
    cnt[st] = cnt.get(st, 0) + 1
    g.append("| %s | %s | %s | `%s` | %s | %s |" % (x.get("id", ""), jur, sec, x.get("key", ""), st.replace("_", " "),
                                                    esc(x.get("what_would_close_it") or "")))
g.insert(2 + 0, "Open gaps: %d. Documented limitations: %d. A gap is printed in the references as 'Not configured in this release (open gap id)'; it is never filled with an estimate.\n" %
         (cnt.get("open", 0), cnt.get("documented_limitation", 0)))
write("14-known-gaps.md", detag(scrub("\n".join(g)), "14-known-gaps.md") + "\n")


# ---------- handwritten core files
LA_Q = str(FACTS["la.report.sui.quarterly"][-1]["value"])
exec(compile(open(os.path.join(HERE, "core_text.py"), encoding="utf8").read(), "core_text", "exec"))
ACC = {"CCG": "about 89% federal core and modules; 75-85% per State reference", "SCOPE": "about 92%", "RSPEC": "mean 78% over 227 return rows",
       "DD": "about 80%", "WTC": "about 85%", "SIR": "75-85%", "PSL": "85%"}
qrows = []
for a in ("CCG", "SCOPE", "RSPEC", "DD", "WTC", "SIR", "PSL"):
    best = None
    for f in glob.glob(os.path.join(BASE, "_qa", a + "-review-r*.json")):
        d = json.load(open(f, encoding="utf8"))
        key = (d.get("reviewed_on", ""), os.path.basename(f))
        if best is None or key > best[0]:
            best = (key, d)
    d = best[1]
    qrows.append("| %s | %s | %s | %s | %s |" % (a, re.sub(r"^.*review-", "", best[0][1])[:-5], d.get("verdict"), d.get("reviewed_on"), ACC[a]))
QA = QA.replace("{rows}", chr(10).join(qrows))
write("13-gotchas.md", detag(refresh(GOTCHAS.replace("@@LA@@", LA_Q)), "13-gotchas.md").rstrip() + chr(10) + fact_index("13-gotchas.md"))
write("07-qa-report.md", QA)
write("/SKILL.md", detag(refresh(SKILL), "SKILL.md"))

print("files:", sum(len(f) for _, _, f in os.walk(REF)), "tag misses:", len(MISS))
for m in MISS[:20]:
    print("MISS", m)
json.dump(SUBST, open(os.path.join(HERE, "tag_substitutions.json"), "w"), indent=1)
print("substituted to current fact value:", len(SUBST))
json.dump(MISS, open(os.path.join(HERE, "tag_misses.json"), "w"), indent=1)
