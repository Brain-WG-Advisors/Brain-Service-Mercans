import re
p = "QA-REPORT.md"; s = open(p, encoding="utf-8").read()
s = re.sub(r"^- \*\*Verdict \(re-check on 2026-11-04.*$", "- **Verdict (re-check 4, 2026-11-05): RELEASE-READY.** C39 now passes (55/56 = 98.2 %), and every other gate already passed in re-check 3 (section 11). Section 12 has the details. Sections 2-11 record the earlier passes; where they differ, section 12 supersedes them.", s, count=1, flags=re.M)
s += open("_runclose/section12.md", encoding="utf-8").read()
open(p, "w", encoding="utf-8").write(s)
h = "handover_status.md"; t = open(h, encoding="utf-8").read()
t = t.replace("# US handover status (2026-11-04, re-check 3: F27 and minor fixes)", "# US handover status (2026-11-05, re-check 4: C39)")
t = re.sub(r"^\*\*State: BLOCKED by C39 only.*$", "**State: RELEASE-READY (re-check 4, 2026-11-05).** Every gate passes. C39 Test 0 is 55/56 = 98.2 %. The package has not been released yet: every artifact stays in status \"For QA\" until the release step. The full report is `07-qa-crosscheck/QA-REPORT.md`; section 12 holds this re-check.", t, count=1, flags=re.M)
i = t.index("## Blocking item"); j = t.index("## C-checks")
t = t[:i] + ("## Blocking item\nNone.\n\nC39 was closed on 2026-11-05: the user opened T46 IN, T49 NC, T50 KY, T55 TX and T56 OR live on the official hosts through a VPN, and the auditor checked each quote in the saved files (QA report section 12).\n\n"
             "**Non-blocking, before production:** re-read T51 (UT income tax 2026 = 4.45 %, [US-UTS5-001]) from a US IP, add the quote to `US-TEST0.json`, and re-run `test0_check.py`.\n\n") + t[j:]
t = t.replace("| Deterministic | C39 | **FAIL** |", "| Deterministic | C39 | PASS, 55/56 = 98.2 % (T51 UT still UNVERIFIED, non-blocking) |")
open(h, "w", encoding="utf-8").write(t)
print("verdict ok:", "RELEASE-READY" in s.split("\n", 6)[4] or "RELEASE-READY" in s[:2000], "| handover FAIL row left:", "**FAIL** |" in t)
