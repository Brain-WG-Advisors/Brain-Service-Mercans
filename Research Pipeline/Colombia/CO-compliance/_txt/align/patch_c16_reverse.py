# -*- coding: utf-8 -*-
"""CO v1.1 alignment patch - CHECK 3 / v2.4 C16 BIDIRECTIONAL REFERENCES.

A prior pass of this stage enforced C16 only in the direction

    DD note  ->  spec field ID

It never tested the spec-internal direction the rule actually states:

    "if A's condition mentions B, then B's notes must mention A"

Sweeping all 563 spec fields for Mandatory=C rows whose Conditional Reason
names another field on the same artefact, and then testing whether that other
field references it back (accepting an ID range such as 'NIE206-NIE209' or
'T2R2-036 to T2R2-039' as a valid reverse reference), leaves 45 B-side fields
with no reverse reference at all: 18 on CO-DIAN-001 and 27 on CO-PILA-003.

This patch installs the missing reverse references as a post-assembly pass over
FIELDS, keyed by field ID, so the enrichment survives a rebuild and cannot
drift out of step with the row it belongs to. A conditional B-side field takes
the sentence in its Conditional Reason (column G); an unconditional one takes
it in its Explanation (column M), because a Mandatory=Y row must not acquire a
conditional reason.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SP = os.path.abspath(os.path.join(HERE, "..", "..", "04-reports-spec"))

# --------------------------------------------------------------------------
#  CO-DIAN-001  Nomina Electronica - 18 fields
# --------------------------------------------------------------------------
NE = {
    "NIAE214":
        "Bidirectional set with the whole adjustment-note payload: the value chosen here decides "
        "which block is populated - 1 (Reemplazar) requires the full replaced-document block "
        "NIAE001 to NIAE213, and 2 (Eliminar) requires only the cancelled-document block from "
        "NIAE236 onward.",
    "NIE003":
        "Bidirectional set with the termination-only accrual elements 'Retirement bonus' (NIE159) "
        "and 'Dismissal indemnity' (NIE160), which are admissible only on a document that carries "
        "this date.",
    "NIE004":
        "Bidirectional pair with 'Termination date' (NIE003): where NIE003 is present it must fall "
        "inside or before the settlement window this field opens.",
    "NIE005":
        "Bidirectional pair with 'Termination date' (NIE003): where NIE003 is present it must fall "
        "inside or before the settlement window this field closes.",
    "NIE011":
        "Bidirectional pair with 'Numbering prefix' (NIE010): the prefix and this consecutive "
        "together must fall inside the numbering range DIAN authorised, and 'Document number' "
        "(NIE012) is the concatenation of the two.",
    "NIE030":
        "Bidirectional pair with 'Exchange rate' (NIE200): NIE200 is present only where this field "
        "is a non-COP ISO code, and must be absent where it is COP.",
    "NIE041":
        "Bidirectional pair with 'Apprentice maintenance support' (NIE157): where NIE157 is present "
        "this field must be worker type 12 or 19 (aprendiz).",
    "NIE061":
        "Bidirectional pair with 'Apprentice maintenance support' (NIE157): where NIE157 is present "
        "this field must be contract type 4 (aprendizaje).",
    "NIE065":
        "Bidirectional set with 'Bank' (NIE066), 'Account type' (NIE067) and 'Account number' "
        "(NIE068): the three are populated together wherever this field is a bank-mediated medium, "
        "and all three must be absent where it is 10 Efectivo.",
    "NIE066":
        "Also bidirectional with 'Account type' (NIE067), which is populated in the same cases.",
    "NIE118":
        "Bidirectional pair with 'Service bonus - amount (non-salary)' (NIE119): the salary and "
        "non-salary portions are separate elements and must never be summed into one.",
    "NIE146":
        "Bidirectional set with 'Other concept - salary' (NIE147) and 'Other concept - non-salary' "
        "(NIE148): at least one of the two amounts must be present wherever this description is "
        "populated.",
    "NIE160":
        "Bidirectional pair with 'Retirement bonus' (NIE159), which co-occurs on the same "
        "termination document.",
    "NIE168":
        "Part of the bidirectional set of four: the subsistence limb - 'Solidarity fund - "
        "subsistence rate' (NIE169) and 'Solidarity fund - subsistence amount' (NIE170) - switches "
        "on only at the higher 16 SMMLV trigger, so this amount can be present while those two are "
        "absent.",
    "NIE170":
        "Part of the bidirectional set of four: the solidarity limb - 'Solidarity fund - solidarity "
        "rate' (NIE167) and 'Solidarity fund - solidarity amount' (NIE168) - switches on at the "
        "lower 4 SMMLV trigger, so wherever this amount is present those two must be present too.",
    "NIE187":
        "Bidirectional set with 'Rounding residual' (NIE186), which is present only where "
        "round-half-to-even rounding of the individual concepts leaves this total differing from "
        "the sum of its parts.",
    "NIE188":
        "Bidirectional set with 'Rounding residual' (NIE186), which is present only where "
        "round-half-to-even rounding of the individual concepts leaves this total differing from "
        "the sum of its parts.",
    "NIE189":
        "Bidirectional set with 'Rounding residual' (NIE186), which is present only where "
        "round-half-to-even rounding of the individual concepts leaves this total differing from "
        "the sum of its parts.",
}

# --------------------------------------------------------------------------
#  CO-PILA-003  PILA - 27 fields
# --------------------------------------------------------------------------
NOVEDAD_DRIVES = (
    "Bidirectional set with the whole novedad block (T2R2-015 to T2R2-030): those change-event "
    "flags are what drive this day count, so a novedad reported without a matching movement in "
    "the day counters is a reconciliation error the operador will surface.")
NOVEDAD_GATED = (
    "More broadly, this field sits in the date block T2R2-080 to T2R2-097 that the whole novedad "
    "block (T2R2-015 to T2R2-030) gates.")
EXON_ZERO = (
    "Also bidirectional with '%s' (%s), which is the amount this rate produces and is zero in the "
    "same cases.")
AVP_053 = (
    "Also bidirectional with 'Value not withheld for voluntary contributions' (T2R2-053), which "
    "reports the amount this contribution removes from the withholding.")

PILA = {
    "A1-007":
        "Bidirectional set with 'Commercial registry date' (A1-031) and 'Department code "
        "(registered seat)' (A1-032), both of which become mandatory where this field = D, the Ley "
        "1429 de 2010 formalisation beneficiary.",
    "A1-019":
        "Bidirectional pair with 'Legal representative identification number' (A1-018): the "
        "operador validates this digit against the number carried in A1-018.",
    "A1-024":
        "Part of the bidirectional legal-representative name set governed by 'Legal representative "
        "identification number' (A1-018) and 'Employer person type' (A1-009).",
    "A1-033":
        "Bidirectional set with the Registro Tipo 2 exoneration fields: 'Contributor exonerated "
        "from payment' (T2R2-076), and the SENA and ICBF rate fields (T2R2-066 and T2R2-068) which "
        "must be ZERO wherever the ET art. 114-1 exoneration reaches the individual employee.",
    "T2R1-008":
        "Bidirectional set with 'Associated planilla number' (T2R1-009) and 'Associated planilla "
        "payment date' (T2R1-010), which are populated only where this type is N or F, and with "
        "the 'Corrections' novedad (T2R2-022).",
    "T2R1-011":
        "Bidirectional pair with 'Branch code' (T2R1-012), which is blank where this field = U "
        "(Unico) and populated where it = S (Sucursal).",
    "T2R1-012":
        "Also bidirectional with 'Branch name' (T2R1-013), which is populated together with this "
        "code.",
    "T2R1-019":
        "Bidirectional pair with 'Additional UPC value' (T2R2-056): contributor type 40 records are "
        "precisely the records that carry that value and that are excluded from this count.",
    "T2R2-003":
        "Bidirectional set with 'Foreign national not liable to contribute to pension' (T2R2-007), "
        "which where marked restricts this field to CE, PA, CD, SC or PE, and with 'Colombian "
        "abroad' (T2R2-008), which is used only where this field is CC or TI.",
    "T2R2-005":
        "Bidirectional set with the fields this code gates: 'Work location department code' "
        "(T2R2-009) and 'Work location municipality code' (T2R2-010) are blank for type 40; "
        "'Additional UPC value' (T2R2-056) and 'Principal contributor document type' (T2R2-074) "
        "are populated only for type 40; 'Hours worked' (T2R2-096) only for part-time type 51; and "
        "'Pension fund of the member' (T2R2-031) may be blank only for a type not obliged to "
        "contribute to pension.",
    "T2R2-006":
        "Bidirectional pair with 'Pension fund of the member' (T2R2-031), which may be blank only "
        "where this sub-type is one not obliged to contribute to the Sistema General de Pensiones.",
    "T2R2-008":
        "Also bidirectional with 'Date of filing abroad' (T2R2-097), which is populated only where "
        "this flag is marked.",
    "T2R2-009":
        "Also bidirectional with 'Work location municipality code' (T2R2-010), which is left blank "
        "in the same two cases.",
    "T2R2-031":
        "Also bidirectional with the 'TDP - transfer from another pension administrator' novedad "
        "(T2R2-019), which reports the move between administrators that changes the value carried "
        "here.",
    "T2R2-033":
        "Bidirectional pair with the 'TDE - transfer from another EPS' novedad (T2R2-017), which "
        "reports the move between health insurers that changes the value carried here.",
    "T2R2-036": NOVEDAD_DRIVES,
    "T2R2-039": NOVEDAD_DRIVES,
    "T2R2-042":
        "Bidirectional set with 'All-inclusive salary flag' (T2R2-041), which where marked sets "
        "this base to 70% of the all-inclusive salary, and with 'Solidarity pension fund - "
        "solidarity sub-account' (T2R2-051), which is payable only where this base reaches 4 SMMLV.",
    "T2R2-043":
        "Bidirectional pair with 'Contributor exonerated from payment' (T2R2-076), which is marked "
        "only where this base is below 10 SMMLV.",
    "T2R2-045":
        "Bidirectional pair with 'All-inclusive salary flag' (T2R2-041), which where marked sets "
        "this base to 70% of the all-inclusive salary.",
    "T2R2-046":
        "Bidirectional pair with 'Special pension rate indicator' (T2R2-079), which is populated "
        "wherever a non-standard rate - notably a Decreto Ley 2090 de 2003 high-risk rate - "
        "replaces the standard 16%.",
    "T2R2-048": AVP_053,
    "T2R2-049": AVP_053,
    "T2R2-066": EXON_ZERO % ("SENA contribution value", "T2R2-067"),
    "T2R2-068": EXON_ZERO % ("ICBF contribution value", "T2R2-069"),
    "T2R2-080": NOVEDAD_GATED,
    "T2R2-097": NOVEDAD_GATED,
}

# --------------------------------------------------------------------------
PASS_SRC = '''
# ---------------------------------------------------------------------------
#  v1.1 ALIGNMENT PATCH - CHECK 3 / v2.4 C16 BIDIRECTIONAL REFERENCES
#  Where a Mandatory=C field's Conditional Reason names another field on this
#  artefact, that other field must reference it back. The reverse references
#  below were the ones still missing after the first pass of this stage, which
#  had tested only the DD-note -> spec-field-ID direction. Applied as a keyed
#  post-assembly pass so each sentence travels with the row it belongs to and
#  survives a rebuild.
#  A conditional row takes the sentence in its Conditional Reason (column G);
#  an unconditional row takes it in its Explanation (column M), because a
#  Mandatory=Y row must never acquire a conditional reason.
# ---------------------------------------------------------------------------
_C16_REVERSE = %s


def _apply_c16(fields):
    seen = set()
    for row in fields:
        if not isinstance(row, list) or len(row) < 13:
            continue
        s = _C16_REVERSE.get(row[3])
        if not s or row[3] in seen:
            continue
        seen.add(row[3])
        i = 6 if row[5] == "C" else 12
        cur = (row[i] or "").strip()
        if s in cur:
            continue
        row[i] = (cur + " " + s).strip() if cur and cur != "-" else s
    missing = set(_C16_REVERSE) - seen
    assert not missing, "C16 reverse target not found: %%s" %% sorted(missing)
    return fields


FIELDS = _apply_c16(FIELDS)

'''


def render(d):
    out = ["{"]
    for k in sorted(d):
        out.append("    %r:" % k)
        words, line, lines = d[k].split(" "), "", []
        for w in words:
            if len(line) + len(w) + 1 > 92:
                lines.append(line)
                line = w
            else:
                line = (line + " " + w).strip()
        lines.append(line)
        for i, ln in enumerate(lines):
            if i < len(lines) - 1:
                ln = ln + " "
            out.append('        "%s"' % ln.replace("\\", "\\\\").replace('"', '\\"'))
        out[-1] = out[-1] + ","
    out.append("}")
    return "\n".join(out)


def install(fn, table):
    p = os.path.join(SP, fn)
    src = open(p, encoding="utf-8").read()
    assert "_C16_REVERSE" not in src, "%s: C16 pass already installed" % fn
    anchor = "\nCFG = {"
    assert src.count(anchor) == 1, "%s: CFG anchor not unique" % fn
    src = src.replace(anchor, "\n" + (PASS_SRC % render(table)) + "\nCFG = {")
    open(p, "w", encoding="utf-8").write(src)
    print("  installed C16 pass in %-32s %d reverse references" % (fn, len(table)))


install("co_r1_nomina_electronica.py", NE)
install("co_r3_pila.py", PILA)
