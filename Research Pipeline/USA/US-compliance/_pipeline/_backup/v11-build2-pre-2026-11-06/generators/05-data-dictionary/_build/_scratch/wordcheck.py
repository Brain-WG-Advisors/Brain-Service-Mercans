# Builder-side pass (read-only): which words of each DD fact value are absent from the local copies of its register rows.
import csv, html, json, os, re, subprocess, sys, gzip

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
REG = {r["id"]: r for r in csv.DictReader(open(os.path.join(BASE, "00-official-sources", "legal-basis-register.csv"), encoding="utf-8"))}
F = json.load(open(os.path.join(BASE, "_research", "DD-8_sheets-facts.json"), encoding="utf-8"))["facts"]
CACHE = {}


def text_of(path):
    if path in CACHE:
        return CACHE[path]
    full = os.path.join(BASE, path)
    t = ""
    if os.path.exists(full) and os.path.isfile(full):
        low = full.lower()
        try:
            if low.endswith(".pdf"):
                t = subprocess.run(["pdftotext", "-layout", full, "-"], capture_output=True, text=True, encoding="utf-8", errors="replace").stdout
            else:
                raw = open(full, "rb").read()
                if raw[:2] == b"\x1f\x8b":
                    raw = gzip.decompress(raw)
                t = raw.decode("utf-8", errors="replace")
                if low.endswith((".html", ".htm", ".xml")):
                    t = re.sub(r"(?s)<(script|style).*?</\1>", " ", t)
                    t = html.unescape(re.sub(r"<[^>]+>", " ", t))
        except Exception as e:  # noqa
            t = ""
    CACHE[path] = t
    return t


def copies(rid):
    r = REG.get(rid)
    out = []
    if r and r.get("local_file"):
        out += [p.strip() for p in r["local_file"].split(";") if p.strip()]
    pc = os.path.join("00-official-sources", "precheck-copies")
    for ext in (".html", ".pdf"):
        if os.path.exists(os.path.join(BASE, pc, rid + ext)):
            out.append(os.path.join(pc, rid + ext).replace("\\", "/"))
    return out


STOP = set("""per each with from that this their which also under only other where when than into within without
used uses using must may required requires state states employer employers employee employees report reports
reporting field fields code codes number numbers date dates first quarter annual form forms data value values
carried carry holds held""".split())
res = []
for f in F:
    rids = [f["register_id"]] + list(f.get("_also_register_ids", []))
    blob = " ".join(text_of(p) for rid in rids for p in copies(rid)).lower()
    blob = re.sub(r"\s+", " ", blob)
    ncopies = sum(len(copies(r)) for r in rids)
    words = {w for w in re.findall(r"[a-z]{5,}", str(f["value"]).lower()) if w not in STOP}
    miss = sorted(w for w in words if w[:5] not in blob and w not in blob)
    res.append((len(miss), f["key"], f["register_id"], ncopies, miss, len(blob)))
res.sort(reverse=True)
for n, k, r, nc, miss, L in res:
    if n >= 1:
        print(n, k, r, "copies=%d len=%d" % (nc, L), miss[:12])
print("done", len(res))
