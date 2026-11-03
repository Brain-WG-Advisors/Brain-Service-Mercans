# -*- coding: utf-8 -*-
"""Row builders for the 21-column core sheet and the jurisdiction parameter rows."""
import re

from us_common import (STATE_NAMES, DD_REF, YEAR, fact, tag, rid, src, gap, gap_subject, gap_close,
                       channel_types, portals_in, RSPEC_GAPS, UNRESOLVED, at)

NONE_OPEN = "No open query."


def row(kind, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t=NONE_OPEN, u=None):
    """kind in payroll|system|constant|excluded. Returns (kind, 21 values).
    Column R carries the C15 class (Input / Output / Display-only / Calculated) and the value type."""
    if not re.match(r"(Input|Output|Display-only|Calculated)\b", str(r)):
        cls = ("Calculated" if str(r).startswith("Calculated") else
               "Display-only" if kind == "excluded" else "Input")
        r = f"{cls} ({r})" if not str(r).startswith("Calculated") else "Calculated (Amount)"
    return (kind, [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u])


def section(text):
    return ("section", text)


# ------------------------------------------------------ attribute classes ---
CLASSES = [
    (r"threshold|mandatory_payment|quarter_monthly|machine_readable|online_mandate|agent_efile|accelerated",
     "Electronic filing / payment threshold", "Amount or count", "C"),
    (r"penalt", "Late or incomplete filing penalty rule", "Rule", "N"),
    (r"(^|_)(due|deadline)|report_days|(^|\.)days$", "Due date rule", "Date rule", "Y"),
    (r"applicable|(^|\.)filed$|exists|no_payroll_report|state_return", "Return applicability", "Flag", "Y"),
    (r"zero", "Zero-return rule", "Flag / rule", "Y"),
    (r"frequency|schedule|class$|(^|\.)monthly$|(^|\.)quarterly$|(^|\.)annual$", "Filing and deposit frequency rule",
     "Code / rule", "Y"),
    (r"channel|format|efile$|flat_file|(^|\.)xml$|upload|file_spec|(^|\.)efile\.|mandate", "Submission channel and file format",
     "Text", "Y"),
    (r"layout|positions|(^|\.)records$", "Record layout", "Text", "C"),
    (r"fields|elements|content|employee_records", "Data elements reported", "Text", "Y"),
    (r"ssn|itin|permit|truncation|box15|placeholder", "Identifier and labelling rule", "Identifier rule", "Y"),
    (r"recipient|state_key", "Recipient / routing rule", "Rule", "Y"),
    (r"(^|\.)forms?$|other_forms|corrections_form|(^|\.)rule$|(^|\.)report$|returns|(^|\.)form\b", "Return form and filing rule",
     "Code / rule", "Y"),
]


def attr_of(key):
    p = key.split(".")
    if p[0] == "rspec":
        return ".".join(p[3:]) or p[-1]
    return p[-1]


def classify(key):
    a = attr_of(key)
    for rx, label, vtype, mand in CLASSES:
        if re.search(rx, a):
            return label, vtype, mand
    return "Reporting rule", "Rule", "C"


USE = {
    "Electronic filing / payment threshold": "The payroll compares the employer's count or amount with this threshold "
                                             "each period and switches the filing or payment route when it is reached.",
    "Late or incomplete filing penalty rule": "Not a filed value; it states the consequence of a late or incomplete return "
                                              "so that the validation rules on this sheet are applied before transmission.",
    "Due date rule": "Drives the filing calendar for the provider hand-off; a due date on a Saturday, Sunday or legal "
                     "holiday follows the roll-forward stated in the rule or the authority's calendar.",
    "Return applicability": "Controls whether the payroll generates this return at all for employers registered "
                            "in the jurisdiction.",
    "Zero-return rule": "When no wages or tax arise in the period the payroll still generates the return with zero "
                        "amounts if the rule requires it.",
    "Filing and deposit frequency rule": "The frequency is employer master data (assigned by the authority or derived "
                                         "from the lookback amount) and selects the period and form of each return.",
    "Submission channel and file format": "The provider transmits through this channel; the payroll supplies the data "
                                          "set of the common field model in the layout the provider imports.",
    "Record layout": "Used only when the return is transmitted as a file; positions and lengths are those the "
                     "authority publishes and are applied by the file generator.",
    "Data elements reported": "Each element listed must have a source in the payroll master data or the period "
                              "results before the return can be generated.",
    "Identifier and labelling rule": "Applied when identifiers are written to the return or statement; a value that "
                                     "breaks the rule is rejected by the authority.",
    "Recipient / routing rule": "Decides which jurisdiction receives the record for each employee and period.",
    "Return form and filing rule": "Names the authority form generated for the period and the condition under "
                                   "which it applies.",
    "Reporting rule": "Applied by the payroll when the situation named in the rule occurs.",
}

COND = {
    "Electronic filing / payment threshold": "Applies only when the employer reaches the threshold stated in column M; "
                                             "below it the other route of the same jurisdiction applies.",
    "Record layout": "Applies when the return is sent as a file upload; portal entry needs no layout.",
    "Reporting rule": "Applies only in the situation stated in column M.",
    "Late or incomplete filing penalty rule": "Informational; triggered only by a late or incomplete return.",
}

EXAMPLE = {
    "Electronic filing / payment threshold": "Employer at or above the threshold: electronic route",
    "Due date rule": "2026 Q1 return: due per the rule in column M",
    "Return applicability": "Flag read from the jurisdiction rule",
    "Zero-return rule": "Quarter with no wages: zero return filed",
    "Filing and deposit frequency rule": "Frequency held as employer master data",
    "Submission channel and file format": "Provider file in the authority format",
    "Record layout": "Positions applied by the file generator",
    "Data elements reported": "One record per employee paid in the period",
    "Identifier and labelling rule": "Identifier written as the rule states",
    "Recipient / routing rule": "Employee routed to one recipient State",
    "Return form and filing rule": "Form generated for the 2026 period",
    "Reporting rule": "Rule applied when its condition occurs",
    "Late or incomplete filing penalty rule": "No value transmitted",
}

MAPPING = {
    "Electronic filing / payment threshold": f"{DD_REF}: employer jurisdiction configuration (threshold flag), forward reference",
    "Due date rule": "Filing calendar of the payroll (system constant per jurisdiction)",
    "Return applicability": "Jurisdiction configuration (system constant)",
    "Zero-return rule": "Jurisdiction configuration (system constant)",
    "Filing and deposit frequency rule": f"{DD_REF}: employer State account and filing frequency (master data), forward reference",
    "Submission channel and file format": "Provider hand-off configuration per jurisdiction (system constant)",
    "Record layout": "File generator layout table per jurisdiction (system constant)",
    "Data elements reported": f"{DD_REF}: employee master data and payroll period results (see the common field model rows)",
    "Identifier and labelling rule": f"{DD_REF}: employer and employee identifiers, forward reference",
    "Recipient / routing rule": f"{DD_REF}: work State / UI State per employee, forward reference",
    "Return form and filing rule": "Jurisdiction configuration (system constant)",
    "Reporting rule": "Jurisdiction configuration (system constant)",
    "Late or incomplete filing penalty rule": "Not mapped (no transmitted value)",
}

KIND = {
    "Electronic filing / payment threshold": "system", "Due date rule": "system", "Return applicability": "constant",
    "Zero-return rule": "constant", "Filing and deposit frequency rule": "system",
    "Submission channel and file format": "system", "Record layout": "system", "Data elements reported": "payroll",
    "Identifier and labelling rule": "payroll", "Recipient / routing rule": "payroll",
    "Return form and filing rule": "constant", "Reporting rule": "system",
    "Late or incomplete filing penalty rule": "excluded",
}


def unit_hint(key):
    k = key.lower()
    if re.search(r"days$", k):
        return " days"
    if re.search(r"employees|employee", k):
        return " employees"
    if re.search(r"forms|w2|statements", k):
        return " forms"
    if re.search(r"payment|eft|usd|mandatory_payment|quarter_monthly|accelerated|threshold_usd", k):
        return " USD"
    return ""


def param_row(jur, key, n, freq, prefix):
    """One jurisdiction parameter row bound to a fact."""
    at(f"{prefix}-{n:03d}")
    label, vtype, mand = classify(key)
    f = fact(key)
    name = STATE_NAMES.get(jur, jur)
    v = f["value"]
    unit = unit_hint(key) if isinstance(v, (int, float)) and not isinstance(v, bool) else ""
    eff = str(f.get("effective_from") or "")
    per = ""
    if eff > f"{YEAR}-12-31":
        per = f" In force from {eff}; not applied to {YEAR}."
    elif f.get("effective_to") and str(f.get("effective_to")) < f"{YEAR}-12-31":
        per = f" Valid until {f.get('effective_to')}."
    expl = (f"{name}: {label.lower()}: {tag(key)}{unit}.{per} {USE[label]} {src(key)}")
    opts = "See Field Options (jurisdiction channel / frequency codes)" if label in (
        "Submission channel and file format", "Filing and deposit frequency rule") else "Value as stated in column M"
    kind = KIND[label]
    if label == "Submission channel and file format":
        ch = channel_types(v, xsd=bool(re.search(r"xsd|schema|spec", str(v), re.I)))
        if ch:
            opts = "Channel classes named by the authority: " + ", ".join(ch)
    t = NONE_OPEN
    if f.get("confidence") in ("low", "medium"):
        t = (f"Confirm against a real filing: the source carries confidence {f.get('confidence')} "
             f"[{f['register_id']}].")
    return row(kind,
               f"{jur} {label}",
               f"{name} authority wording (English filing language)",
               f"Jurisdiction parameter: {jur}",
               f"{prefix}-{n:03d}",
               "N" if kind in ("system", "constant", "excluded") else "Y",
               mand,
               COND.get(label, "Not conditional: applies to every employer filing this return in the jurisdiction.")
               if mand != "Y" else "Not conditional: applies to every employer filing this return in the jurisdiction.",
               "Return level (not a file position)" if label != "Record layout" else "Positions as stated in column M",
               "Not applicable (configuration value)" if label != "Record layout" else "As stated in column M",
               vtype,
               EXAMPLE[label],
               MAPPING[label],
               expl,
               f"Yes: governs how the {freq.lower()} return is produced for {name}",
               opts,
               "Not applicable" if vtype not in ("Amount or count",) else "Whole units as published",
               "N",
               "Rule" if vtype not in ("Flag", "Amount or count") else ("Flag" if vtype == "Flag" else "Amount"),
               freq,
               t)


def gap_row(jur, gkey, n, prefix, freq, what="Return parameters and file layout"):
    at(f"{prefix}-{n:03d}")
    name = STATE_NAMES.get(jur, jur)
    if gkey in RSPEC_GAPS or gkey in UNRESOLVED:
        text = (f"{name}: {what.lower()}: not configured in this release {gap(gkey)}. "
                f"Open point: {gap_subject(gkey)}. Closes with: {gap_close(gkey)}.")
        q = f"Open point {gap(gkey)}: {gap_close(gkey)}."
    else:
        text = f"{name}: {what.lower()}: not configured in this release {gap(gkey)}."
        q = f"Open point {gap(gkey)}."
    return row("system", f"{jur} {what}", f"{name} authority wording (English filing language)",
               f"Jurisdiction parameter: {jur}", f"{prefix}-{n:03d}", "N", "C",
               "Applies once the open point is closed; until then the return is prepared from the common field "
               "model only and checked against the authority portal before submission.",
               "Return level (not a file position)", "Not applicable (configuration value)", "Text",
               "No value configured", "Provider hand-off configuration per jurisdiction (system constant)",
               text, f"Yes: {name} {freq.lower()} return", "Not applicable", "Not applicable", "N", "Rule",
               freq, q)
