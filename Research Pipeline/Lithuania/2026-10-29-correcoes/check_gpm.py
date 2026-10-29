#!/usr/bin/env python3
"""check_gpm.py - conferencia mecanica das specs LT GPM313 / GPM312 contra o script do MXFD da VMI.

O que faz
  1. Le o ScriptModule (VBScript) de dentro de GPM313.mxfd e GPM312.mxfd (so leitura, em raw/).
     Confere ancoras: cada linha citada abaixo tem de conter o trecho esperado, senao aborta.
  2. Porta para Python, linha a linha, as funcoes de validacao usadas nos exemplos:
       GPM313.mxfd  ID_formatas_simple_f (l. 197-325) e Sub GPM313 (l. 19-120)
       GPM312.mxfd  JAR_tikrinimas (l. 3843-3916), TIN_tikrinimas (l. 3697-3749),
                    AK_tikrinimas (l. 3751-3841), PVM_kodas (l. 3657-3688),
                    verslo_nr (l. 3576-3611), IVPN (l. 3613-3655), L5/U5_Ne_Is_L7/U7_M_Saraso
                    (l. 3926-3944), Sub GPM312 (l. 1203-1311), regras de linha de GPM312L
                    (l. 1423-2239) e de GPM312U (l. 2441-3348).
     As listas de codigos/taxas sao lidas do proprio script (linha citada), nao redigitadas.
     Ramos de ano: so os de metai >= 2025/2026 (os exemplos sao de 2026).
  3. Roda sobre TODOS os exemplos das duas specs: coluna K da aba Spec, Example Analysis e Sample File.
  4. Confere: caixas de totais = soma das linhas (GPM312 l. 1265-1311); valores iguais entre K / Example
     Analysis / Sample; separador decimal "," (MXFD DecimalSeparator); nenhuma celula comeca com "=".

Saida: lista de ERROS (SetError sem el_warning) e AVISOS (el_warning). Codigo de saida 0 = zero erros.
Uso:  python check_gpm.py [GPM313.xlsx] [GPM312.xlsx]
"""
from __future__ import annotations

import datetime
import pathlib
import re
import sys
import xml.etree.ElementTree as ET
from decimal import Decimal, ROUND_HALF_EVEN

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

import openpyxl  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent
BRAIN = HERE.parents[2]
MXFD_DIR = BRAIN / "raw" / "docs" / "oficiais" / "LT" / "2026-10-27-VMI-reports"
MXFD313 = MXFD_DIR / "x_GPM313_mxfd" / "GPM313.mxfd"
MXFD312 = MXFD_DIR / "x_GPM312_mxfd" / "GPM312.mxfd"
X313 = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "LT-VMI-001-GPM313-Spec_v1.2.xlsx"
X312 = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else HERE / "LT-VMI-002-GPM312-Spec_v1.2.xlsx"

ERR, WARN = "ERRO", "AVISO"


# --------------------------------------------------------------------------- script do MXFD
def load_script(p: pathlib.Path) -> list[str]:
    root = ET.fromstring(p.read_text(encoding="utf-8"))
    for e in root.iter("ScriptModule"):
        return e.text.replace("\r", "").split("\n")
    raise SystemExit(f"ScriptModule nao encontrado em {p}")


S313 = load_script(MXFD313)
S312 = load_script(MXFD312)


def line(script, n):           # numeracao 1-based, igual a citada no relatorio de validacao
    return script[n - 1]


def anchor(script, n, frag, name):
    if frag not in line(script, n):
        raise SystemExit(f"ANCORA FALHOU {name} l.{n}: esperado {frag!r}, achado {line(script, n).strip()[:120]!r}")


def vbs_array(script, n):
    """Le array("..","..") da linha n (com continuacao ' _'), ignorando o resto da linha."""
    txt = line(script, n)
    k = n
    while txt.rstrip().endswith("_"):
        k += 1
        txt = txt.rstrip()[:-1] + line(script, k)
    m = re.search(r"array\s*\((.*?)\)", txt, re.IGNORECASE)
    if not m:
        raise SystemExit(f"array() nao achado na linha {n}")
    return re.findall(r'"([^"]*)"', m.group(1))


ANCHORS = [
    (S313, 6, 'Form.SetDefaultDecimalSeparator ","', "GPM313"),
    (S313, 20, "<> 9 and len(", "GPM313"),
    (S313, 197, "function ID_formatas_simple_f", "GPM313"),
    (S313, 203, "For i = 1 to 8", "GPM313"),
    (S313, 207, "If suma >= 10 Then", "GPM313"),
    (S313, 32, "neegzistuojantis m", "GPM313"),
    (S312, 6, 'Form.SetDefaultDecimalSeparator ","', "GPM312"),
    (S312, 1209,'len(fieldsGPM312.Itembyname("B_MM_ID").value) = 9', "GPM312"),
    (S312, 1244, ">= 2026", "GPM312"),
    (S312, 1274, '<> "C"', "GPM312"),
    (S312, 1308, 'setcheckvalue cstr(sumLU8)', "GPM312"),
    (S312, 1309, 'setcheckvalue cstr(sumLU10)', "GPM312"),
    (S312, 1556, "elseif metai >= 2026", "GPM312"),
    (S312, 1617, '"77"', "GPM312"),
    (S312, 1619, '"92"', "GPM312"),
    (S312, 1845, '"25", "27", "32"', "GPM312"),
    (S312, 2513, 'value = "6"', "GPM312"),
    (S312, 2557, "isfilled(fieldsGPM312U.Itembyname(\"U12-\"&j)) or isfilled(fieldsGPM312U.Itembyname(\"U13-\"&j)) or isfilled(fieldsGPM312U.Itembyname(\"U15-\"&j))", "GPM312"),
    (S312, 2569, '"62" or', "GPM312"),
    (S312, 3243, "turi būti užpildyti U12 ir / ar U13", "GPM312"),
    (S312, 3657, "Function PVM_kodas", "GPM312"),
    (S312, 3673, 'if cstr(strngs) = "1" then', "GPM312"),
    (S312, 3751, "function AK_tikrinimas", "GPM312"),
    (S312, 3843, "Function JAR_tikrinimas", "GPM312"),
]


# --------------------------------------------------------------------------- utilidades VB
def todec(s) -> Decimal:
    """Field.ToDecimal: vazio -> 0; aceita ',' (separador do formulario)."""
    s = "" if s is None else str(s).strip()
    if s == "":
        return Decimal(0)
    try:
        return Decimal(s.replace(",", "."))
    except Exception:
        return Decimal(0)


def isnumeric(s) -> bool:
    try:
        float(str(s).replace(",", "."))
        return str(s).strip() != ""
    except ValueError:
        return False


def is_digit(s) -> bool:      # GPM312 l. 3542-3557  ^[0-9]*$
    return re.fullmatch(r"[0-9]*", s) is not None


def is_alpha(s) -> bool:      # GPM312 l. 3559-3574  ^[A-Za-z]*$
    return re.fullmatch(r"[A-Za-z]*", s) is not None


def is_date(y_m_d: str) -> bool:
    try:
        datetime.date.fromisoformat(y_m_d)
        return True
    except ValueError:
        return False


def vb_round2(x: Decimal) -> Decimal:   # VBScript Round() = arredondamento bancario
    return x.quantize(Decimal("0.01"), rounding=ROUND_HALF_EVEN)


# --------------------------------------------------------------------------- funcoes portadas
def ID_formatas_simple_f(reiksme: str) -> list:
    """GPM313.mxfd l. 197-325."""
    out = []
    msg = "1 laukelyje įrašytas neteisingas mokesčių mokėtojo identifikacinis numeris"
    if not isnumeric(reiksme):
        return out
    n = len(reiksme)
    if n == 9:                                                            # l. 201-213
        suma = sum(int(reiksme[:8][i - 1]) * i for i in range(1, 9)) % 11
        if suma >= 10:
            out.append((ERR, "GPM313 l.207-208", msg + f" (suma mod 11 = {suma})"))
        elif int(reiksme[-1]) != suma:
            out.append((ERR, "GPM313 l.210-211", msg + f" (digito {reiksme[-1]} != {suma})"))
    elif n == 10:                                                         # l. 214-246
        suma = sum(int(reiksme[:9][i - 1]) * (10 - i) for i in range(1, 10))
        if int(reiksme[:2]) != 0:
            suma = suma % int(reiksme[:2])
            for _ in range(3):
                if suma >= 10:
                    suma = sum(int(c) for c in str(suma))
            if int(reiksme[-1]) != suma:
                out.append((ERR, "GPM313 l.242-244", msg))
    elif n == 11:                                                         # l. 247-322
        bad = ak_core(reiksme)
        if reiksme[0] != "9":
            if bad:
                out.append((WARN, "GPM313 l.253/266/290", "1 laukelyje įrašytas neteisingas ... (kodas)"))
        elif bad:
            out.append((ERR, "GPM313 l.316-319", "1 laukelyje įrašytas neteisingas ILTU kodas"))
    return out


def ak_core(reiksme: str) -> bool:
    """Nucleo comum de AK_tikrinimas (GPM312 l. 3759-3840) e do case 11 de ID_formatas_simple_f.
    Devolve True quando ha problema (AK_tikrinimas = true)."""
    if not is_digit(reiksme.strip()):
        return True                                                       # l. 3838-3839
    if len(reiksme) != 11:
        return False                                                      # Select Case so trata 11
    bad = False
    stabdis = 0
    if reiksme[0] != "9":                                                 # l. 3762
        if reiksme[0] not in "123456":                                    # l. 3764-3768
            stabdis, bad = 1, True
        cent = {"1": "18", "2": "18", "3": "19", "4": "19", "5": "20", "6": "20"}.get(reiksme[0], "")
        gimd = f"{cent}{reiksme[1:3]}-{reiksme[3:5]}-{reiksme[5:7]}"     # l. 3769-3776
        if stabdis == 0 and not is_date(gimd):                            # l. 3777-3783
            stabdis, bad = 1, True
    suma = sum(int(reiksme[i - 1]) * i for i in range(1, 10)) + int(reiksme[9])   # l. 3784-3788
    suma %= 11
    if suma >= 10:                                                        # l. 3791-3800
        suma = sum(int(reiksme[i - 3]) * i for i in range(3, 10)) + sum(int(reiksme[i + 6]) * i for i in range(1, 4))
        suma %= 11
    if suma == 10:                                                        # l. 3801
        suma = 0
    if stabdis == 0 and suma != int(reiksme[10]):                         # l. 3802-3807
        bad = True
    return bad


def AK_tikrinimas(reiksme: str) -> bool:
    """GPM312 l. 3751-3841 (True = codigo pessoal com problema)."""
    return ak_core(reiksme)


def JAR_tikrinimas(value: str, klaida: str) -> tuple[bool, list]:
    """GPM312 l. 3843-3916. Devolve (rt, achados); rt=True quando valido."""
    out = []
    rt = True
    if is_digit(value.strip()):
        n = len(str(int(value))) if value.strip() else 0                  # Len(kodas.ToDecimal)
        if n == 9:
            suma = sum(int(value[:8][i - 1]) * i for i in range(1, 9)) % 11   # l. 3852-3857
            if suma >= 10 or int(value[-1]) != suma:                          # l. 3859-3866
                out.append((ERR, "GPM312 l.3859-3865", klaida))
                rt = False
        elif n == 10:
            flag, o = TIN_tikrinimas(value, klaida)
            out += o
            rt = not flag
        else:
            out.append((ERR, "GPM312 l.3909", klaida))
            rt = False
    else:
        rt = False
    return rt, out


def TIN_tikrinimas(value: str, klaida: str) -> tuple[bool, list]:
    """GPM312 l. 3697-3749. Devolve (TIN_tikrinimas, achados); True = erro emitido."""
    out = []
    if is_digit(value.strip()) and value.strip():
        if len(str(int(value))) == 10:
            suma = sum(int(value[:9][i - 1]) * (10 - i) for i in range(1, 10))
            div = int(value[:2])
            if div == 0:
                out.append((ERR, "GPM312 l.3712", "divisao por zero no script (codigo comeca com 00)"))
                return True, out
            suma %= div
            for _ in range(3):
                if suma >= 10:
                    suma = sum(int(c) for c in str(suma))
            if int(value[-1]) != suma:
                out.append((ERR, "GPM312 l.3740-3743", klaida))
                return True, out
    return False, out


def PVM_kodas(reiksme: str) -> bool:
    """GPM312 l. 3657-3688: 14 caracteres, 'LT' + 12 digitos, 13o caractere = '1'."""
    if len(reiksme) != 14:
        return False
    if reiksme[0:2] != "LT":
        return False
    if not is_digit(reiksme[2:14].strip()):
        return False
    return reiksme[12:13] == "1"


def verslo_nr(reiksme: str) -> bool:
    """GPM312 l. 3576-3611."""
    if len(reiksme) != 8:
        return False
    if not is_alpha(reiksme[0].strip()):
        return False
    if not (is_alpha(reiksme[1].strip()) or is_digit(reiksme[1].strip())):
        return False
    return is_digit(reiksme[2:8].strip())


def IVPN(kodas: str) -> bool:
    """GPM312 l. 3613-3655 (SetCheckValue tira espacos antes)."""
    r = kodas.replace(" ", "")
    if len(r) == 6:
        return is_digit(r) and int(r) != 0
    if len(r) == 7:
        return is_digit(r) and int(r) >= 1000001
    return False


M_SARASAS = None


def L5_Ne_Is_L7_M_Saraso(code: str) -> bool:     # GPM312 l. 3926-3934
    return code in M_SARASAS


# --------------------------------------------------------------------------- GPM313
def check_gpm313(f: dict, where: str) -> list:
    """Sub GPM313, GPM313.mxfd l. 19-120. f = {campo MXFD: valor texto}."""
    out = []
    v = lambda k: (f.get(k) or "").strip()
    d = lambda k: todec(f.get(k))
    if v("B_MM_ID"):                                                      # l. 19-25
        if len(v("B_MM_ID")) not in (9, 10, 11):
            out.append((ERR, "GPM313 l.20-21", "1 laukelyje įrašytas negalimas kodas (ilgis ne 9, 10 ar 11)"))
        else:
            out += ID_formatas_simple_f(v("B_MM_ID"))
    if not v("B_ML_Metai"):                                               # l. 29
        out.append((ERR, "GPM313 l.29", "3 laukelyje negalimi metai"))
    if v("B_ML_Menuo"):                                                   # l. 31-33 (+ ListItems 1..12)
        if v("B_ML_Menuo") not in [str(i) for i in range(1, 13)]:
            out.append((ERR, "GPM313 l.32 / ListItems", f"4 laukelyje neegzistuojantis mėnesis ({v('B_ML_Menuo')!r})"))
    if d("G5") < d("G6") + d("G7"):                                      # l. 35-37
        out.append((WARN, "GPM313 l.35-36", "G5 < G6+G7"))
    if d("G8") < d("G9") + d("G10"):                                     # l. 39-41
        out.append((WARN, "GPM313 l.39-40", "G8 < G9+G10"))
    if d("G11") < d("G12"):                                              # l. 43-45
        out.append((WARN, "GPM313 l.43-44", "G11 < G12"))
    empty = [k for k in ("G5", "G6", "G7", "G8", "G9", "G10", "G11", "G12") if not v(k)]
    if empty:                                                             # l. 47-87
        out.append((WARN, "GPM313 l.86", f"campos 5-12 vazios = declarar que nada foi pago: {','.join(empty)}"))
    if d("G5") > 0 and d("G6") == 0 and d("G7") == 0:                    # l. 89-93
        out.append((WARN, "GPM313 l.91", "G5 > 0 sem GPM em G6/G7"))
    if d("G5") > 99000000 or d("G8") > 99000000:                         # l. 95-97
        out.append((WARN, "GPM313 l.96", "G5/G8 > 99 000 000"))
    if any(d(k) > 9000000 for k in ("G6", "G7", "G9", "G10")):           # l. 99-101
        out.append((WARN, "GPM313 l.100", "GPM > 9 000 000"))
    if d("G8") > 0 and d("G9") == 0 and d("G10") == 0:                   # l. 103-107
        out.append((ERR, "GPM313 l.105", "G8 > 0 exige GPM em G9 e/ou G10"))
    if d("G11") > 0:                                                      # l. 109-116
        if d("G11") > 1000000:
            out.append((WARN, "GPM313 l.111", "G11 > 1 000 000"))
        if d("G12") == 0:
            out.append((ERR, "GPM313 l.114", "G11 > 0 exige G12"))
    if d("G12") > 100000:                                                 # l. 118-120
        out.append((WARN, "GPM313 l.119", "G12 > 100 000"))
    return [(s, r, f"[{where}] {m}") for s, r, m in out]


# --------------------------------------------------------------------------- GPM312 linhas
def check_L(f: dict, metai: int, payer: str, where: str) -> list:
    """Regras de linha do GPM312L (l. 1423-2217), ramo metai >= 2025/2026."""
    out = []
    F = lambda k: (f.get(k) or "").strip()
    filled = lambda k: F(k) != ""
    d = lambda k: todec(F(k))
    if not any(filled(f"L{k}") for k in range(1, 14)):
        return out
    if metai >= 2025:                                                     # l. 1423-1442
        req = ["L1", "L2", "L3", "L4", "L5", "L8", "L9"] if F("L7") != "C" else ["L1", "L2", "L3", "L5", "L8", "L9"]
        miss = [k for k in req if not filled(k)]
        if miss:
            out.append((ERR, "GPM312 l.1431/1440", f"Visi privalomi eilutės laukeliai turi būti užpildyti: {miss}"))
    if (d("L10") > 0 and d("L11") > 0) and F("L10") == F("L11"):         # l. 1448-1453 -> 2293
        out.append((WARN, "GPM312 l.2293", "L10 = L11"))
    if filled("L1") and len(F("L1")) == 9:                                # l. 1457-1462
        rt, o = JAR_tikrinimas(F("L1"), "L1 laukelyje nurodytas neteisingas kodas")
        out += o
        if rt:
            out.append((ERR, "GPM312 l.1462", "codigo de entidade no L1: vai no anexo U"))
    tmp, tmp2 = False, False                                              # l. 1464-1472
    if d("L2") == 1 and filled("L1"):
        if len(F("L1")) not in (10, 11):
            tmp2 = True
        if len(F("L1")) == 10:
            tmp, o = TIN_tikrinimas(F("L1"), "L1 laukelyje nurodytas neteisingas asmens kodas arba VMI suteiktas mokėtojo numeris")
            out += o
        if not isnumeric(F("L1")):
            tmp2 = True
    if not tmp and tmp2:
        out.append((ERR, "GPM312 l.1472", "L1 laukelyje nurodytas neteisingas asmens kodas arba VMI suteiktas mokėtojo numeris"))
    if d("L2") == 1 and filled("L1") and len(F("L1")) == 11:              # l. 1474-1483 -> 2272
        if AK_tikrinimas(F("L1")):
            out.append((WARN, "GPM312 l.1476/2272", f"Pasitikrinkite L1 laukelyje įrašytą asmens kodą ({F('L1')})"))
    if d("L2") == 2 and filled("L1") and not verslo_nr(F("L1")):         # l. 1485-1495
        out.append((ERR, "GPM312 l.1492", "L1 laukelyje nurodytas neteisingas verslo liudijimo numeris"))
    if d("L2") == 3 and filled("L1") and not PVM_kodas(F("L1")):         # l. 1497-1505
        out.append((ERR, "GPM312 l.1502", "L1 laukelyje nurodytas neteisingas PVM mokėtojo kodas"))
    if d("L2") == 4 and filled("L1") and not IVPN(F("L1")):              # l. 1507-1516
        out.append((ERR, "GPM312 l.1513", "L1 laukelyje nurodytas neteisingas individualios veiklos pažymos numeris"))
    if filled("L2") and F("L2") not in ("1", "2", "3", "4", "5"):         # l. 1518-1528
        out.append((ERR, "GPM312 l.1527", "L2 fora da lista"))
    if filled("L4") and F("L4") not in ("A", "B"):                        # l. 1531-1542
        out.append((ERR, "GPM312 l.1540", "L4 laukelyje nurodyta neteisinga išmokų klasė"))
    if filled("L5") and metai >= 2026 and F("L5") not in vbs_array(S312, 1557):   # l. 1544-1571
        out.append((ERR, "GPM312 l.1557/1570", f"L5 laukelyje nurodyta neteisinga išmokų rūšis ({F('L5')})"))
    if filled("L4") and F("L4") in ("A", "B") and filled("L5") and metai >= 2026:  # l. 1574-1653
        lst = vbs_array(S312, 1617) if F("L4") == "A" else vbs_array(S312, 1619)
        if F("L5") not in lst and F("L7") not in ("M", "C"):
            out.append((WARN, "GPM312 l.1617/1619/1647", f"L4 {F('L4')} incompativel com L5 {F('L5')} (2 priedas)"))
    if filled("L5"):                                                      # l. 1655-1712
        c = d("L5")
        if c in (35, 92, 93, 94, 95, 96, 97) and F("L7") == "":           # l. 1659 -> 2276
            out.append((WARN, "GPM312 l.1659/2276", "individual-activity code: se pago pelo empregador, L7 = D"))
        if c == 58 and F("L4") == "A" and len(payer) not in (10, 11):
            out.append((ERR, "GPM312 l.1669", "codigo 58 A so quando quem paga e pessoa fisica"))
        if c == 46 and len(payer) not in (10, 9):
            out.append((ERR, "GPM312 l.1672", "codigo 46 so quando doador e pessoa juridica"))
        if c == 7 and d("L8") > 200:
            out.append((WARN, "GPM312 l.2273", "codigo 07 > 200 EUR"))
        if c == 92 and not (not filled("L9") or d("L9") == 0):            # l. 1682-1683
            out.append((ERR, "GPM312 l.1683", "1_L9: codigo 92 exige L9 vazio ou 0"))
        if metai > 2020 and d("L2") in (2, 4) and c == 88:
            out.append((WARN, "GPM312 l.1692", "codigo 88 com L2 2/4"))
        if c in (23, 24):
            out.append((WARN, "GPM312 l.1696", "conferir 23/24"))
        if c in (14, 16):
            out.append((WARN, "GPM312 l.1701", "conferir 14/16"))
        if c == 13:
            out.append((WARN, "GPM312 l.1704", "conferir 13"))
        if c == 16 and d("L8") <= 100:
            out.append((WARN, "GPM312 l.1708", "16 com L8 <= 100"))
    if filled("L6"):                                                      # l. 1715-1748
        if F("L6") not in ("A", "N"):
            out.append((ERR, "GPM312 l.1740", "L6 fora da lista A/N"))
        if F("L6") == "N":
            out.append((WARN, "GPM312 l.2274", "PASITIKRINKITE IŠMOKAS NATŪRA (L6 = N)"))
    if filled("L7"):                                                      # l. 1752-1813
        if F("L7") not in ("D", "M", "P", "C"):
            out.append((ERR, "GPM312 l.1762", f"L7 fora da lista D/M/P/C ({F('L7')})"))
        if F("L7") == "P" and F("L5") != "23":
            out.append((ERR, "GPM312 l.1790", "L7 P exige L5 23"))
        if F("L7") == "C" and F("L5") != "42":
            out.append((ERR, "GPM312 l.1799", "L7 C exige L5 42"))
        if F("L7") == "C" and F("L5") == "42":
            if F("L4"):
                out.append((ERR, "GPM312 l.1807", "L4 vazio quando 42/C"))
            if F("L9") and d("L9") != 0:
                out.append((ERR, "GPM312 l.1810", "L9 = 0 quando 42/C"))
    if d("L8") == 0:                                                      # l. 1820-1823
        out.append((WARN, "GPM312 l.1822", "L8 = 0"))
    if filled("L8") and d("L8") <= d("L10") + d("L11"):                  # l. 1824-1829 -> 2277
        out.append((WARN, "GPM312 l.2277", "L8 <= L10 + L11"))
    code01_04 = F("L5") in ("01", "02", "03", "04")
    if filled("L9"):                                                      # l. 1839-1876
        if not any(d("L9") == todec(k) for k in vbs_array(S312, 1845)):
            out.append((ERR, "GPM312 l.1845/1854", f"L9 laukelyje nurodytas neteisingas GPM tarifas ({F('L9')})"))
        if d("L9") == 25 and metai < 2026:
            out.append((ERR, "GPM312 l.1856", "25 % so a partir de 2026"))
        if not code01_04 and F("L4") == "A" and d("L8") > Decimal("0.9") and d("L9") != 0 and d("L10") == 0 and d("L11") == 0:
            out.append((WARN, "GPM312 l.1858/2279", "L9 > 0 sem GPM em L10/L11"))
        if filled("L8") and (filled("L10") or filled("L11")) and d("L9") > 0 and not code01_04 \
                and d("L10") + d("L11") != vb_round2(d("L8") * d("L9") / 100):
            out.append((WARN, "GPM312 l.1865/2280", "L10+L11 != L8 x L9"))
    if filled("L4") and F("L4") == "A":                                   # l. 1878-2064
        if d("L9") == 0 or not filled("L9"):
            if d("L9") == 0 and d("L8") > 0 and (d("L10") > 0 or d("L11") > 0):
                out.append((WARN, "GPM312 l.2278", "L9 = 0 com GPM"))
            if filled("L5") and metai >= 2026 and F("L5") not in vbs_array(S312, 1899):
                out.append((ERR, "GPM312 l.1899/1910", f"2_L9: taxa 0 nao usada para o codigo {F('L5')}"))
        rate_lines = {5: (1925, "3_L9"), 15: (1952, "4_L9"), 20: (1977, "5_L9"), 25: (2002, "6_L9"),
                      27: (2027, "7_L9"), 32: (2052, "8_L9")}
        for rate, (ln, tag) in rate_lines.items():
            if d("L9") == rate and filled("L5") and metai >= 2026 and F("L5") not in vbs_array(S312, ln):
                out.append((ERR, f"GPM312 l.{ln}", f"{tag}: taxa {rate} nao usada para o codigo {F('L5')}"))
    else:                                                                 # l. 2065-2090 (B ou vazio)
        if F("L9") != "" and metai >= 2026 and d("L9") not in (0, 5, 15, 20, 25, 32):
            out.append((ERR, "GPM312 l.2081/2087", "9_L9: taxa nao usada"))
    if filled("L8") and filled("L10") and filled("L11") and d("L9") > 0 and \
            d("L10") + d("L11") == vb_round2(d("L8") * d("L9") / 100) * 2 and F("L10") == F("L11"):   # l. 2092
        out.append((ERR, "GPM312 l.2294", "GPM duplicado em L10 e L11"))
    if (F("L9") == "0" or not filled("L9")) and F("L5") == "01":         # l. 2101 -> 2292
        out.append((WARN, "GPM312 l.2101/2292", "codigo 01 com L9 0/vazio"))
    if d("L9") == 0 and F("L5") in ("01", "03", "04") and not filled("L12"):   # l. 2108 -> 2289
        out.append((WARN, "GPM312 l.2108/2289", "0 % so para isentos do art. 37"))
    if (d("L10") > 0 or d("L11") > 0) and (F("L9") == "0" or not filled("L9")):   # l. 2114-2120 -> 2291
        out.append((ERR, "GPM312 l.2291", "L9 0 com GPM"))
    if (d("L10") > 0 or d("L11") > 0 or d("L9") > 0) and filled("L12"):   # l. 2121-2127 -> 2287
        out.append((ERR, "GPM312 l.2287", "L12 preenchido exige L9/L10/L11 = 0"))
    if filled("L12") and F("L12") != "LT" and filled("L5") and F("L5") not in vbs_array(S312, 2146):
        out.append((ERR, "GPM312 l.2152", "L12 so para salario/honorarios/juros"))
    if filled("L12") and F("L12") not in vbs_array(S312, 2161):
        out.append((ERR, "GPM312 l.2168", "L12 fora da lista de paises"))
    if not filled("L12") and d("L13") > 0:                                # l. 2201-2217
        out.append((ERR, "GPM312 l.2215", "L13 so com L12"))
    return [(s, r, f"[{where}] {m}") for s, r, m in out]


def check_U(f: dict, metai: int, payer: str, where: str) -> list:
    """Regras de linha do GPM312U (l. 2441-3348), ramo metai >= 2025/2026."""
    out = []
    F = lambda k: (f.get(k) or "").strip()
    filled = lambda k: F(k) != ""
    d = lambda k: todec(F(k))
    if not any(filled(f"U{k}") for k in range(1, 16)):
        return out
    tmp, tmp2 = False, False                                              # l. 2458-2467
    if d("U2") == 1 and filled("U1"):
        if len(F("U1")) not in (10, 11):
            tmp2 = True
        if len(F("U1")) == 10:
            tmp, o = TIN_tikrinimas(F("U1"), "U1 laukelyje nurodytas neteisingas asmens kodas arba VMI suteiktas mokėtojo numeris")
            out += o
        if not isnumeric(F("U1")):
            tmp2 = True
    if not tmp and tmp2:
        out.append((ERR, "GPM312 l.2467", "U1 laukelyje nurodytas neteisingas asmens kodas arba VMI suteiktas mokėtojo numeris"))
    if d("U2") == 1 and filled("U1") and len(F("U1")) == 11 and AK_tikrinimas(F("U1")):   # l. 2469-2477
        out.append((WARN, "GPM312 l.3425", "Pasitikrinkite U1 laukelyje įrašytą asmens kodą"))
    if d("U2") == 2 and filled("U1") and not verslo_nr(F("U1")):         # l. 2480-2489
        out.append((ERR, "GPM312 l.2486", "U1 verslo liudijimo numeris neteisingas"))
    if d("U2") == 3 and filled("U1") and not PVM_kodas(F("U1")):         # l. 2491-2499
        out.append((ERR, "GPM312 l.2496", "U1 laukelyje nurodytas neteisingas PVM mokėtojo kodas"))
    if d("U2") == 4 and filled("U1") and not IVPN(F("U1")):              # l. 2501-2510
        out.append((ERR, "GPM312 l.2507", "U1 individualios veiklos pažymos numeris neteisingas"))
    if F("U2") == "6" and F("U14") == "LT" and F("U5") in ("26", "67"):   # l. 2512-2534
        if len(F("U1")) == 9:
            _, o = JAR_tikrinimas(F("U1"), "U1 laukelyje nurodytas neteisingas kodas")
            out += o
        elif len(F("U1")) == 10:
            _, o = TIN_tikrinimas(F("U1"), "U1 laukelyje nurodytas neteisingas kodas")
            out += o
        elif F("U1"):
            out.append((ERR, "GPM312 l.2525", "U1 laukelyje nurodytas neteisingas kodas"))
    if filled("U2") != filled("U1"):                                      # l. 2538-2540
        out.append((ERR, "GPM312 l.2539", "U1 ir U2 laukeliai turi būti užpildyti"))
    if filled("U2") and F("U2") not in ("1", "2", "3", "4", "5", "6"):    # l. 2544-2553
        out.append((ERR, "GPM312 l.2552", "U2 fora da lista"))
    if filled("U2") and F("U2") == "6":                                   # l. 2555-2575
        if filled("U12") or filled("U13") or filled("U15"):
            out.append((ERR, "GPM312 l.2558", "Kai U2 = 6, nepildomi U12, U13, U15 laukeliai"))
        if filled("U5"):
            ok = ("26", "62", "67") if metai <= 2025 else ("62", "67", "52", "51")
            if F("U5") not in ok:
                out.append((ERR, "GPM312 l.2563/2570", f"U2 = 6 nao aceito com U5 {F('U5')} no periodo {metai}"))
    if filled("U4") and F("U4") not in ("A", "B"):                        # l. 2578-2589
        out.append((ERR, "GPM312 l.2587", "U4 fora da lista"))
    if filled("U5") and metai >= 2026 and F("U5") not in vbs_array(S312, 2604):   # l. 2591-2619
        out.append((ERR, "GPM312 l.2604/2617", f"U5 laukelyje nurodyta neteisinga išmokų rūšis ({F('U5')})"))
    if filled("U4") and F("U4") in ("A", "B") and filled("U5") and metai >= 2026:  # l. 2621-2698
        lst = vbs_array(S312, 2664) if F("U4") == "A" else vbs_array(S312, 2666)
        if F("U5") not in lst and F("U7") not in ("M", "C"):
            out.append((WARN, "GPM312 l.2694", f"U4 {F('U4')} incompativel com U5 {F('U5')}"))
    if filled("U5"):
        c = d("U5")
        if c in (35, 92, 93, 94, 95, 96, 97) and F("U7") == "":           # l. 2706 -> 3431
            out.append((WARN, "GPM312 l.3431", "individual-activity code: se pago pelo empregador, U7 = D"))
        if c == 46 and len(payer) not in (10, 9):
            out.append((ERR, "GPM312 l.2716", "codigo 46"))
        if c == 92 and not (not filled("U9") or d("U9") == 0):
            out.append((ERR, "GPM312 l.2727", "1_U9: codigo 92 exige U9 vazio ou 0"))
        if c in (23, 24):
            out.append((WARN, "GPM312 l.2739", "conferir 23/24"))
        if c in (14, 16):
            out.append((WARN, "GPM312 l.2744", "conferir 14/16"))
        if c == 13:
            out.append((WARN, "GPM312 l.2747", "conferir 13"))
    if filled("U6"):                                                      # l. 2759-2792
        if F("U6") not in ("A", "N"):
            out.append((ERR, "GPM312 l.2784", "U6 fora da lista"))
        if F("U6") == "N":
            out.append((WARN, "GPM312 l.3428", "PASITIKRINKITE IŠMOKAS NATŪRA (U6 = N)"))
    if filled("U7"):                                                      # l. 2796-2865
        if F("U7") not in ("D", "M", "P", "C", "U"):
            out.append((ERR, "GPM312 l.2806", "U7 fora da lista"))
        if F("U7") == "P" and F("U5") != "23":
            out.append((ERR, "GPM312 l.2836", "U7 P exige U5 23"))
        if F("U7") == "C" and F("U5") != "42":
            out.append((ERR, "GPM312 l.2846", "U7 C exige U5 42"))
        if metai > 2025 and F("U7") == "U" and F("U5") not in ("23", "01", "52", "51", "17", "18", "16"):
            out.append((ERR, "GPM312 l.2861", "U7 U so com 01/52/51/17/18/16/23"))
        if (metai < 2026 and F("U7") == "U") or (F("U2") == "6" and F("U7") == "U"):
            out.append((ERR, "GPM312 l.2864", "U7 U so para nao residente, a partir de 2026"))
    if d("U8") == 0:                                                      # l. 2875-2878
        out.append((WARN, "GPM312 l.2877", "U8 = 0"))
    if d("U8") <= d("U10") + d("U11") and d("U10") + d("U11") > 0:       # l. 2880-2884
        out.append((WARN, "GPM312 l.3432", "U8 <= U10 + U11"))
    code01_04 = F("U5") in ("01", "02", "03", "04")
    if filled("U9"):                                                      # l. 2894-2925
        if not any(d("U9") == todec(k) for k in vbs_array(S312, 2897)):
            out.append((ERR, "GPM312 l.2897/2903", f"U9 laukelyje nurodytas neteisingas GPM tarifas ({F('U9')})"))
        if not code01_04 and F("U4") == "A" and d("U8") > Decimal("0.9") and d("U9") != 0 and d("U10") == 0 and d("U11") == 0:
            out.append((WARN, "GPM312 l.2907/3434", "U9 > 0 sem GPM"))
        if filled("U8") and (filled("U10") or filled("U11")) and d("U9") > 0 and not code01_04 \
                and d("U10") + d("U11") != vb_round2(d("U8") * d("U9") / 100):
            out.append((WARN, "GPM312 l.2914/3435", "U10+U11 != U8 x U9"))
    if F("U4") == "A":                                                    # l. 2927-3162
        if d("U9") == 0 or not filled("U9"):
            if filled("U5") and metai >= 2026 and F("U5") not in vbs_array(S312, 2946):
                out.append((ERR, "GPM312 l.2946/2956", f"2_U9: taxa 0 nao usada para o codigo {F('U5')}"))
        rate_lines = {Decimal(5): (2972, "3_U9"), Decimal("7.5"): (2997, "4_U9"), Decimal(10): (3022, "5_U9"),
                      Decimal(15): (3047, "6_U9"), Decimal(20): (3073, "7_U9"), Decimal(25): (3099, "8_U9"),
                      Decimal(27): (3124, "9_U9"), Decimal(32): (3150, "10_U9")}
        for rate, (ln, tag) in rate_lines.items():
            if d("U9") == rate and filled("U5") and metai >= 2026 and F("U5") not in vbs_array(S312, ln):
                out.append((ERR, f"GPM312 l.{ln}", f"{tag}: taxa {rate} nao usada para o codigo {F('U5')}"))
    else:                                                                 # l. 3163-3189
        if F("U9") != "" and metai >= 2026 and d("U9") not in (0, 5, Decimal("7.5"), 15, 20, 25, 32):
            out.append((ERR, "GPM312 l.3185", "11_U9: taxa nao usada"))
    if filled("U8") and filled("U10") and filled("U11") and d("U9") > 0 and \
            d("U10") + d("U11") == vb_round2(d("U8") * d("U9") / 100) * 2 and d("U10") == d("U11"):   # l. 3191
        out.append((ERR, "GPM312 l.3445", "GPM duplicado em U10 e U11"))
    if F("U14") and F("U14") != "LT" and not filled("U13") and not filled("U12") and d("U2") != 6:   # l. 3237-3248
        out.append((ERR, "GPM312 l.3243", "U14 != LT exige U12 e/ou U13"))
    if filled("U14") and F("U14") not in vbs_array(S312, 3255):           # l. 3250-3264
        out.append((ERR, "GPM312 l.3263", "U14 fora da lista de paises"))
    if F("U14") == "LT":                                                  # l. 3272-3280
        if not (filled("U2") and filled("U5")) or not (d("U2") == 6 and F("U5") in ("26", "67", "62")):
            out.append((ERR, "GPM312 l.3279", "U14 = LT so com U2 = 6 e U5 26/62/67"))
    if metai >= 2025:                                                     # l. 3283-3323
        req = ["U3", "U4", "U5", "U8", "U9", "U14"] if F("U7") != "C" else ["U3", "U5", "U8", "U9", "U14"]
        miss = [k for k in req if not filled(k)]
        if miss:
            out.append((ERR, "GPM312 l.3311/3319", f"Visi privalomi eilutės laukeliai turi būti užpildyti: {miss}"))
    if filled("U14") and F("U14") != "LT" and d("U2") != 6:               # l. 3334-3350 -> 3426
        if not all(filled(k) for k in ("U1", "U2", "U12", "U13", "U15")):
            out.append((WARN, "GPM312 l.3426", "Pasitikrinkite U1/U13/U12/U15 (algum vazio)"))
    if F("U12") and not (re.fullmatch(r"\d{4}-\d{2}-\d{2}", F("U12")) and is_date(F("U12"))):   # DataType Date
        out.append((ERR, "MXFD U12 Date", "U12 fora do formato AAAA-MM-DD"))
    return [(s, r, f"[{where}] {m}") for s, r, m in out]


def check_gpm312_decl(decl: dict, Ls: list, Us: list, where: str) -> list:
    """Sub GPM312 (l. 1172-1311): paginas, B_MM_ID, ano, e caixas 4-7 = somas das linhas (setcheckvalue)."""
    out = []
    pid = (decl.get("B_MM_ID") or "").strip()
    if not Ls and not Us:
        out.append((ERR, "GPM312 l.1172", "nenhum anexo L/U"))
    if pid and not 9 <= len(pid) <= 11:
        out.append((ERR, "GPM312 l.1204-1205", "B_MM_ID com 9, 10 ou 11 digitos"))
    if len(pid) == 9:
        _, o = JAR_tikrinimas(pid, "1 laukelyje įrašytas neteisingas mokesčių mokėtojo identifikacinis numeris")
        out += o
    elif len(pid) == 10:
        _, o = TIN_tikrinimas(pid, "1 laukelyje įrašytas neteisingas mokesčių mokėtojo identifikacinis numeris")
        out += o
    if len(pid) == 11 and AK_tikrinimas(pid):
        out.append((WARN, "GPM312 l.1218", "Pasitikrinkite 1 laukelyje įrašytą asmens kodą"))
    if todec(decl.get("B_ML_Metai")) >= 2026:
        out.append((WARN, "GPM312 l.1244-1247", "periodo corrente: aviso de ano (versao do MXFD de 2026-06-12)"))
    sL8 = sum((todec(l.get("L8")) for l in Ls if (l.get("L7") or "") != "C"), Decimal(0))   # l. 1273-1276
    sL10 = sum((todec(l.get("L10")) for l in Ls), Decimal(0))
    sL11 = sum((todec(l.get("L11")) for l in Ls), Decimal(0))
    sL13 = sum((todec(l.get("L13")) for l in Ls), Decimal(0))
    sU8 = sum((todec(u.get("U8")) for u in Us if (u.get("U7") or "") != "C"), Decimal(0))   # l. 1291-1293
    sU10 = sum((todec(u.get("U10")) for u in Us), Decimal(0))
    sU11 = sum((todec(u.get("U11")) for u in Us), Decimal(0))
    calc = {"G4": sL8 + sU8, "G5": sL10 + sU10, "G6": sL11 + sU11, "G7": sL13}   # l. 1304-1311
    for k, v in calc.items():
        got = todec(decl.get(k))
        status = "ok" if got == v else "DIFERENTE"
        line_ = f"{k}: declarado {decl.get(k)!r} / soma das linhas {str(v).replace('.', ',')} -> {status}"
        out.append((ERR if got != v else "INFO", "GPM312 l.1308-1311 setcheckvalue", line_))
    return [(s, r, f"[{where}] {m}") for s, r, m in out]


# --------------------------------------------------------------------------- leitura das planilhas
def sval(c):
    return "" if c is None else str(c)


def norm_ex(v):
    v = sval(v).strip()
    return "" if v in ("(empty)", "--") else v


def spec_map(ws, prefix_ok):
    """{campo MXFD: (valor K, formato J, celula)} a partir da coluna H da aba Spec."""
    m = {}
    for r in range(2, ws.max_row + 1):
        h = sval(ws.cell(r, 8).value)
        if "/" not in h:
            continue
        page, name = h.split("/", 1)
        name = re.sub(r"-n.*$", "", name).strip()
        if page in prefix_ok:
            m[(page, name)] = (norm_ex(ws.cell(r, 11).value), sval(ws.cell(r, 10).value), f"K{r}")
    return m


DEC_RE = re.compile(r"^-?\d+,\d{2}$")


def dec_format(val, where, out):
    if val and not DEC_RE.match(val):
        out.append((ERR, "MXFD DecimalSeparator ','", f"[{where}] valor decimal fora do formato 0,00: {val!r}"))


def parse_cols(header: str, labels: list[str]):
    """posicao de inicio de cada rotulo no cabecalho (rotulos separados por espaco)."""
    pos, start = [], 0
    for lab in labels:
        i = re.search(r"(?<!\S)" + re.escape(lab) + r"(?!\S)", header[start:])
        if not i:
            raise SystemExit(f"rotulo {lab} nao achado no cabecalho: {header!r}")
        pos.append(start + i.start())
        start = start + i.end()
    return pos


def slice_line(text: str, labels, pos):
    out = {}
    for k, lab in enumerate(labels):
        a = pos[k]
        b = pos[k + 1] if k + 1 < len(pos) else len(text) + 1
        out[lab] = text[a:b].strip() if a < len(text) else ""
    return {k: ("" if v == "--" else v) for k, v in out.items()}


def sample_lines(ws):
    return [(r, sval(ws.cell(r, 2).value)) for r in range(2, ws.max_row + 1)]


def no_equals(wb, fname, out):
    n = 0
    for ws in wb.worksheets:
        for row in ws.iter_rows():
            for c in row:
                n += 1
                if isinstance(c.value, str) and c.value.startswith("="):
                    out.append((ERR, "regra Drive", f"[{fname}!{ws.title}!{c.coordinate}] celula comeca com '=': {c.value[:40]!r}"))
                if c.data_type == "f":
                    out.append((ERR, "regra Drive", f"[{fname}!{ws.title}!{c.coordinate}] celula com formula"))
    return n


SEX = {"3": "M", "5": "M", "4": "F", "6": "F"}


def sex_of_name(full):
    first = full.split()[0].lower() if full.strip() else ""
    if re.search(r"(as|is|ys|us)$", first):
        return "M"
    if re.search(r"(a|ė|e)$", first):
        return "F"
    return "?"


# --------------------------------------------------------------------------- execucao
def main():
    global M_SARASAS
    for s, n, frag, name in ANCHORS:
        anchor(s, n, frag, name)
    M_SARASAS = re.findall(r'"([^"]*)"', line(S312, 3928) + line(S312, 3929))   # Select Case l. 3928-3929
    print(f"Ancoras do script conferidas: {len(ANCHORS)} (GPM313.mxfd {len(S313)} linhas, GPM312.mxfd {len(S312)} linhas)")
    allf = []

    # ---------------- GPM313
    wb = openpyxl.load_workbook(X313)
    n313 = no_equals(wb, X313.name, allf)
    sp = spec_map(wb["GPM313 Spec"], {"GPM313"})
    k = {name: v for (pg, name), v in sp.items()}
    f_spec = {name: v[0] for name, v in k.items()}
    for name, (val, fmt, cell) in k.items():
        if "Decimal, 2 dp" in fmt:
            dec_format(val, f"GPM313 Spec!{cell} {name}", allf)
    allf += check_gpm313(f_spec, "GPM313 Spec col. K")
    ea = wb["Example Analysis"]
    boxmap = {"1": "B_MM_ID", "2": "B_MM_Pavadinimas", "3": "B_ML_Metai", "4": "B_ML_Menuo"}
    boxmap.update({str(i): f"G{i}" for i in range(5, 13)})
    f_ea = {}
    for r in range(2, ea.max_row + 1):
        m = re.match(r"^(\d+) - ", sval(ea.cell(r, 2).value))
        if m:
            name = boxmap[m.group(1)]
            f_ea[name] = norm_ex(ea.cell(r, 1).value)
            if name.startswith("G"):
                dec_format(f_ea[name], f"GPM313 Example Analysis!A{r} {name}", allf)
    allf += check_gpm313(f_ea, "GPM313 Example Analysis")
    f_sf = {}
    for r, t in sample_lines(wb["Sample File"]):
        m = re.match(r"^\s*(\d{1,2})\s{2}\S.*?\.{3,}\s*(.*)$", t)
        if m:
            name = boxmap[m.group(1)]
            f_sf[name] = m.group(2).strip()
            if name.startswith("G"):
                dec_format(f_sf[name], f"GPM313 Sample File!B{r} {name}", allf)
    allf += check_gpm313(f_sf, "GPM313 Sample File")
    for name in boxmap.values():
        a, b, c = f_spec.get(name, ""), f_ea.get(name, ""), f_sf.get(name, "")
        if not (a == b == c):
            allf.append((ERR, "coerencia", f"[GPM313 {name}] K={a!r} Example={b!r} Sample={c!r}"))
    print(f"GPM313: {len(f_spec)} campos na coluna K, {len(f_ea)} no Example Analysis, {len(f_sf)} no Sample File; {n313} celulas lidas")
    print(f"        valores: {f_sf}")

    # ---------------- GPM312
    wb = openpyxl.load_workbook(X312)
    n312 = no_equals(wb, X312.name, allf)
    sp = spec_map(wb["GPM312 Spec"], {"GPM312", "GPM312L", "GPM312U"})
    decl = {n: v[0] for (pg, n), v in sp.items() if pg == "GPM312"}
    Lk = {n: v[0] for (pg, n), v in sp.items() if pg == "GPM312L"}
    Uk = {n: v[0] for (pg, n), v in sp.items() if pg == "GPM312U"}
    for (pg, name), (val, fmt, cell) in sp.items():
        if fmt.startswith("Decimal"):
            dec_format(val, f"GPM312 Spec!{cell} {pg}/{name}", allf)
    metai = int(todec(decl.get("B_ML_Metai")))
    payer = decl.get("B_MM_ID", "")
    for pg, dct in (("GPM312L", Lk), ("GPM312U", Uk)):
        if dct.get("B_MM_ID") != payer or dct.get("B_ML_Metai") != decl.get("B_ML_Metai"):
            allf.append((ERR, "GPM312 l.1379-1380 / 2414-2415", f"[GPM312 Spec] {pg} caixas 1/3 diferentes da declaracao"))
    allf += check_L(Lk, metai, payer, "GPM312 Spec col. K linha L")
    allf += check_U(Uk, metai, payer, "GPM312 Spec col. K linha U")
    pid_issues = [x for x in check_gpm312_decl(decl, [Lk], [Uk], "GPM312 Spec col. K") if x[0] != "INFO" and "setcheckvalue" not in x[1]]
    allf += pid_issues

    ea = wb["Example Analysis"]
    eav = {}
    for r in range(2, ea.max_row + 1):
        b = sval(ea.cell(r, 2).value).strip()
        eav.setdefault(b, (norm_ex(ea.cell(r, 1).value), r))
    L_ea = {k: eav[k][0] for k in [f"L{i}" for i in range(1, 12)] if k in eav}
    for k in ("L8", "L10", "L11"):
        dec_format(L_ea.get(k, ""), f"GPM312 Example Analysis!A{eav[k][1]} {k}", allf)
    if "L9" in L_ea:
        dec_format(L_ea["L9"], f"GPM312 Example Analysis!A{eav['L9'][1]} L9", allf)
    ea_payer = eav.get("Box 1 / L annex box 1 / U annex box 1", ("", 0))[0]
    allf += check_gpm312_decl({"B_MM_ID": ea_payer, "B_ML_Metai": "2026"}, [L_ea], [], "GPM312 Example Analysis (ID)")[:-4]
    allf += check_L(L_ea, metai, ea_payer, "GPM312 Example Analysis linha L (A4-A15)")
    if "L1 (passport fallback)" in eav:
        pas = dict(L_ea, L1=eav["L1 (passport fallback)"][0], L2="5")
        allf += check_L(pas, metai, ea_payer, "GPM312 Example Analysis A6 (passaporte, L2 = 5)")
    if "U2" in eav and eav["U2"][0] not in ("1", "2", "3", "4", "5", "6"):
        allf.append((ERR, "GPM312 l.2552", "[GPM312 Example Analysis] U2 fora da lista"))
    if "U12" in eav and not is_date(eav["U12"][0]):
        allf.append((ERR, "MXFD U12 Date", "[GPM312 Example Analysis] U12"))
    if "U14" in eav and eav["U14"][0] not in vbs_array(S312, 3255):
        allf.append((ERR, "GPM312 l.3263", "[GPM312 Example Analysis] U14"))

    sf = sample_lines(wb["Sample File"])
    sdecl, Ls, Us = {}, [], []
    mode, hdrL, hdrU1, hdrU2 = None, None, None, None
    Llab = [f"L{i}" for i in range(1, 12)]
    U1lab = [f"U{i}" for i in range(1, 12)]
    U2lab = ["U12", "U13", "U14", "U15"]
    pending_u = None
    for r, t in sf:
        if t.startswith("GPM312L priedas"):
            mode = "L"
            continue
        if t.startswith("GPM312U priedas"):
            mode = "U"
            continue
        if mode is None:
            m = re.match(r"^\s*([1-7])\s{2}\S.*\s(\S+)$", t)
            if m and m.group(1) != "2":
                key = {"1": "B_MM_ID", "3": "B_ML_Metai", "4": "G4", "5": "G5", "6": "G6", "7": "G7"}[m.group(1)]
                sdecl[key] = m.group(2)
                if key.startswith("G"):
                    dec_format(m.group(2), f"GPM312 Sample File!B{r} {key}", allf)
            continue
        if re.match(r"^\s*1\s+\d", t):
            pid = t.split()[1]
            if pid != sdecl.get("B_MM_ID"):
                allf.append((ERR, "GPM312 l.1379/2414", f"[GPM312 Sample File!B{r}] caixa 1 do anexo != declaracao"))
            continue
        if mode == "L":
            if re.match(r"^\s+L1\s+L2\s", t):
                hdrL = parse_cols(t, Llab)
                continue
            if hdrL and t.strip() and not set(t.strip()) <= set("-—") and "L12:" not in t:
                rec = slice_line(t, Llab, hdrL)
                rec["_cell"] = f"B{r}"
                Ls.append(rec)
            elif "L12:" in t and Ls:
                m = re.search(r"L12:\s*(\S+)\s+L13:\s*(\S+)", t)
                for rec in Ls:
                    rec.setdefault("L12", "" if m.group(1) == "--" else m.group(1))
                    rec.setdefault("L13", "" if m.group(2) == "--" else m.group(2))
        elif mode == "U":
            if re.match(r"^\s+U1\s+U2\s", t):
                hdrU1 = parse_cols(t, U1lab)
                continue
            if re.match(r"^\s+U12\s+U13\s", t):
                hdrU2 = parse_cols(t, U2lab)
                continue
            if hdrU1 and hdrU2 and t.strip() and not set(t.strip()) <= set("-—"):
                if pending_u is None:
                    pending_u = slice_line(t, U1lab, hdrU1)
                    pending_u["_cell"] = f"B{r}"
                else:
                    pending_u.update(slice_line(t, U2lab, hdrU2))
                    pending_u["_cell"] += f"/B{r}"
                    Us.append(pending_u)
                    pending_u = None
    if pending_u is not None:
        allf.append((ERR, "parser", f"[GPM312 Sample File] linha U sem a segunda linha (U12-U15): {pending_u['_cell']}"))
    for rec in Ls:
        for k in ("L8", "L10", "L11", "L13"):
            dec_format(rec.get(k, ""), f"GPM312 Sample File!{rec['_cell']} {k}", allf)
        allf += check_L(rec, metai, sdecl.get("B_MM_ID", ""), f"GPM312 Sample File!{rec['_cell']}")
        if rec.get("L2") == "1" and len(rec.get("L1", "")) == 11:
            sx, nx = SEX.get(rec["L1"][0], "?"), sex_of_name(rec.get("L3", ""))
            if sx != nx:
                allf.append((ERR, "1o digito do asmens kodas", f"[GPM312 Sample File!{rec['_cell']}] sexo do codigo {sx} x nome {nx}"))
    for rec in Us:
        for k in ("U8", "U10", "U11"):
            dec_format(rec.get(k, ""), f"GPM312 Sample File!{rec['_cell']} {k}", allf)
        allf += check_U(rec, metai, sdecl.get("B_MM_ID", ""), f"GPM312 Sample File!{rec['_cell']}")
    allf += check_gpm312_decl(sdecl, Ls, Us, "GPM312 Sample File")
    # caixas 4-7 da coluna K da spec = somas das linhas da amostra (M2)
    for kname in ("G4", "G5", "G6", "G7"):
        if todec(decl.get(kname)) != todec(sdecl.get(kname)):
            allf.append((ERR, "coerencia M2", f"[GPM312 Spec col. K {kname}] {decl.get(kname)!r} != Sample {sdecl.get(kname)!r}"))
    sx = sex_of_name(L_ea.get("L3", ""))
    if L_ea.get("L1") and SEX.get(L_ea["L1"][0]) != sx:
        allf.append((ERR, "1o digito do asmens kodas", "[GPM312 Example Analysis] L1 x L3"))
    if Lk.get("L1") and SEX.get(Lk["L1"][0]) != sex_of_name(Lk.get("L3", "")):
        allf.append((ERR, "1o digito do asmens kodas", "[GPM312 Spec] K14 x K16"))
    print(f"GPM312: declaracao {sdecl}; {len(Ls)} linhas L e {len(Us)} linhas U na amostra; {n312} celulas lidas")
    for rec in Ls + Us:
        print("        ", {k: v for k, v in rec.items() if v})

    # ---------------- resultado
    errs = [x for x in allf if x[0] == ERR]
    warns = [x for x in allf if x[0] == WARN]
    infos = [x for x in allf if x[0] == "INFO"]
    print("\n== INFO ==")
    for s, r, m in infos:
        print(f"  {m}   ({r})")
    print("\n== AVISOS (el_warning: nao impedem a entrega no EDS) ==")
    for s, r, m in warns:
        print(f"  {m}   ({r})")
    print("\n== ERROS ==")
    for s, r, m in errs:
        print(f"  {m}   ({r})")
    print(f"\nRESULTADO: {'PASS' if not errs else 'FAIL'} - {len(errs)} erro(s), {len(warns)} aviso(s)")
    return 0 if not errs else 1


if __name__ == "__main__":
    raise SystemExit(main())
