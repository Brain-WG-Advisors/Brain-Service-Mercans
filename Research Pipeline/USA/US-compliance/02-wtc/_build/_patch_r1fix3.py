import io
p="wtc_requests.py"
s=io.open(p,encoding="utf-8").read()
s=s.replace('REL = f"02-wtc/{W.FILENAME}"\n','REL = f"02-wtc/{W.FILENAME}"\n# Review r1 item 16: the status reads the same everywhere (facts blocking = true). key -> impact on the WTC.\nBLOCKING = {"dc.sit.method.2026": "none: catalogue carries no method", "ut.sit.schedule.effective_date": "D412 dating"}\n')
s=s.replace("            _status=\"documented_limitation\", _cells=len(locs), _facts_blocking=bool(d.get(\"facts_blocking\"))))",
"            _status=\"documented_limitation\", _cells=len(locs), _facts_blocking=bool(d.get(\"facts_blocking\"))))\n        if key in BLOCKING:\n            reqs[-1][\"blocking\"] = True\n            reqs[-1][\"_wtc_impact\"] = BLOCKING[key]")
s=s.replace("research_request_id=gid, blocking=False,","research_request_id=gid, blocking=key in BLOCKING,")
s=s.replace("            decided_by=\"WTC build r1\"))","            decided_by=\"WTC build r1\"))\n        if key in BLOCKING:\n            entries[-1][\"_wtc_impact\"] = BLOCKING[key]")
s=s.replace("None blocks the artifact; each is","None blocks the artifact except those marked blocking (WTC-RQ-25 none for the catalogue, WTC-RQ-42 D412 dating); each is")
io.open(p,"w",encoding="utf-8",newline="\n").write(s)
