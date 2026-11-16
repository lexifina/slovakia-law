"""Salvadoran blind spot, in a copy of global-law's vulnerabilities/scripts (idempotent):
- ingest/textscan.py: dates written wholly in words, as Salvadoran decrees write them ("hasta el treinta y uno de
  diciembre de dos mil catorce", "hasta el día treinta de abril de mil novecientos ochenta y cinco", "HASTA EL TREINTA
  DE SEPTIEMBRE DE MIL NOVECIENTOS NOVENTA Y NUEVE"), which the time-limit search did not read: the day (primero, uno ...
  treinta y uno) and the year (mil novecientos ..., dos mil ...) are turned into figures;
- detectors/currency_scan.py: the Salvadoran colón ("¢2,000.00", "50 colones"), replaced by the US dollar under the Ley de
  Integración Monetaria (2001), was not read as a currency. It is added for El Salvador only (pins.json code SV), as Costa
  Rica's colón is still in use.

    python -X utf8 patch_sv.py <scripts dir>
"""
import sys
from pathlib import Path


def patch(rel, pairs):
    p = Path(sys.argv[1]) / rel
    s = p.read_text(encoding="utf-8")
    for name, a, b, *marker in pairs:
        if b in s or (marker and marker[0] in s):  # a marker: in place even if another patch edited the same text since
            print("in place:", name)
        elif a in s:
            s = s.replace(a, b, 1)
            print("patched:", name)
        else:
            raise SystemExit(f"not found: {name}")
    p.write_text(s, encoding="utf-8", newline="\n")


HELPERS = r'''# Spanish dates written in words (Salvadoran decrees): "treinta y uno de diciembre de dos mil catorce"
_ES_NUM = {"un": 1, "uno": 1, "primero": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5, "seis": 6, "siete": 7, "ocho": 8,
           "nueve": 9, "diez": 10, "once": 11, "doce": 12, "trece": 13, "catorce": 14, "quince": 15, "dieciséis": 16,
           "dieciseis": 16, "diecisiete": 17, "dieciocho": 18, "diecinueve": 19, "veinte": 20, "veintiuno": 21, "veintiún": 21,
           "veintidós": 22, "veintidos": 22, "veintitrés": 23, "veintitres": 23, "veinticuatro": 24, "veinticinco": 25,
           "veintiséis": 26, "veintiseis": 26, "veintisiete": 27, "veintiocho": 28, "veintinueve": 29, "treinta": 30,
           "cuarenta": 40, "cincuenta": 50, "sesenta": 60, "setenta": 70, "ochenta": 80, "noventa": 90, "novecientos": 900}


def es_words(s: str) -> int:
    """'treinta y uno' -> 31, 'mil novecientos noventa y nueve' -> 1999, 'dos mil catorce' -> 2014 (KeyError if not a number)"""
    total = cur = 0
    for w in s.lower().split():
        if w == "y":
            continue
        if w == "mil":
            total += (cur or 1) * 1000
            cur = 0
        else:
            cur += _ES_NUM[w]
    return total + cur


DEADLINE_RX = re.compile('''

ES_DAY = (r"(?:treinta\s+y\s+uno|treinta|veinti[a-záéíóúñ]+|veinte|diecis[ée]is|diecisiete|dieciocho|diecinueve|"
          r"primero|uno|dos|tres|cuatro|cinco|seis|siete|ocho|nueve|diez|once|doce|trece|catorce|quince)")
ES_UNIT = (r"(?:diecis[ée]is|diecisiete|dieciocho|diecinueve|veinti[a-záéíóúñ]+|veinte|treinta|cuarenta|cincuenta|"
           r"sesenta|setenta|ochenta|noventa|uno|un|dos|tres|cuatro|cinco|seis|siete|ocho|nueve|diez|once|doce|trece|"
           r"catorce|quince)")
WORD_DATE = (r'        r"|(?P<m5>\d{1,2})-(?P<d5>\d{1,2})-(?P<y5>\d{4})"' + "\n"
             r'        # a date wholly in words (Salvadoran decrees): "treinta y uno de diciembre de dos mil catorce"' + "\n"
             r'        rf"|(?P<dw>' + ES_DAY.replace("{", "{{").replace("}", "}}") + r')\s+de\s+(?P<monw>{MON})\s+(?:del?\s+)?(?:año\s+)?'
             r'(?P<yw>(?:mil\s+novecientos|dos\s+mil)(?:\s+(?:y\s+)?' + ES_UNIT + r')*)\b")')

patch("detectors/currency_scan.py", [
    # the colón is El Salvador's own: Costa Rica's colón is still its currency, so it is added by jurisdiction, not by language;
    # "colones" or "¢" next to an amount ("¢2,000.00", "50 colones"), not the singular, which is also a place ("Canal Río Colón 6.5")
    ("colón (SV)", "def pat_for(c):",
     '# a currency that is dead in one jurisdiction only (El Salvador\'s colón, replaced by the US dollar in 2001; Costa Rica\'s is live)\n'
     'EXTRA_CURRENCY_CODE = {"SV": r"|colones\\b|¢"}\n\n\n'
     'def pat_for(c):', "EXTRA_CURRENCY_CODE"),
    ("pat_for: currency by jurisdiction",
     'cur = cur[:-1] + EXTRA_CURRENCY.get((c.get("language") or "").lower(), "") + ")"',
     'cur = cur[:-1] + EXTRA_CURRENCY.get((c.get("language") or "").lower(), "") + EXTRA_CURRENCY_CODE.get((c.get("code") or "").upper(), "") + ")"'),
])
patch("ingest/textscan.py", [
    ("DATE: a date in words",
     r'        r"|(?P<m5>\d{1,2})-(?P<d5>\d{1,2})-(?P<y5>\d{4})")', WORD_DATE, "(?P<dw>"),
    ("es_words", "DEADLINE_RX = re.compile(", HELPERS, "def es_words("),
    ("limits: a date in words",
     '            elif g["y1"]:',
     '            elif g.get("yw"):\n'
     '                y, mo, d = es_words(g["yw"]), MI[g["monw"].lower()], es_words(g["dw"])\n'
     '            elif g["y1"]:', 'g.get("yw")'),
])
