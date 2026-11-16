"""The "Flags by category" chart at the top of vulnerabilities/README*.md (light and dark, English and Czech).

    python -X utf8 flags_chart.py <data dir> <img dir>   -> <img>/flags-by-category[-dark][.<lang>].svg (labels from config.json)
Manrope and JetBrains Mono are embedded afterwards at the <!--fonts--> marker, subset to the glyphs each chart uses.
"""
import csv, json, os, sys

DATA, OUT = sys.argv[1], sys.argv[2]
CATS = list(csv.DictReader(open(os.path.join(DATA, "by_category.csv"), encoding="utf-8")))
W = 880
SANS = "Manrope, -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif"
MONO = "'JetBrains Mono', ui-monospace, SFMono-Regular, Consolas, 'Liberation Mono', monospace"
PAL = {
    "light": dict(bg="#ffffff", border="#dfe5e1", fg="#14201a", muted="#5f6e66", law="#1a7f4b", other="#9fcdb2", soft="#f4f6f5"),
    "dark": dict(bg="#0c120f", border="#26332c", fg="#e9f2ec", muted="#93a69b", law="#3fbf7f", other="#2a6b4a", soft="#141c18"),
}
WORDS_EN = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen"}
SHORT_EN = {"Retroactive or pre-publication dates": "Retroactive dates"}
CFG = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json"), encoding="utf-8"))
LANG, CH = CFG["lang"], CFG["chart"]   # chart: title ("{n} ... {k} ..."), words ({"8": "..."}), law, other, other_en, sep, tip, short
TOTAL = sum(int(c["flags"]) for c in CATS)
N = len(CATS)


def num(v, sep):
    return f"{v:,}".replace(",", sep)


TXT = {
    "en": dict(title=f"{num(TOTAL, ',')} flag{'s' * (TOTAL != 1)} in {WORDS_EN.get(N, N)} categor{'ies' if N != 1 else 'y'}", law="In law texts", other=CH["other_en"],
               cats=[SHORT_EN.get(c["category"], c["category"]) for c in CATS], sep=",", tip="{cat}: {n} flags, {law} in law texts"),
}
if LANG != "en":   # an English-only repository (lang "en") has no category_en column and one set of charts
    TXT[LANG] = dict(title=CH["title"].format(n=num(TOTAL, CH["sep"]), k=CH["words"].get(str(N), str(N))), law=CH["law"], other=CH["other"],
                     cats=[CH.get("short", {}).get(c["category_" + LANG], c["category_" + LANG]) for c in CATS], sep=CH["sep"], tip=CH["tip"], tip1=CH.get("tip1"))  # tip1: the tooltip for a category with one flag (Spanish "1 alerta")


def esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


RTL_LANGS = ("dv", "ar", "he", "fa", "ur")   # right-to-left scripts: the chart is drawn mirrored, its text set right to left


def width(s, size=12):
    """rough width in px at font-size 12: CJK a full em, Thaana vowel signs (fili) none, other characters 6.9"""
    return sum(0 if 0x07A6 <= ord(ch) <= 0x07B0 else 12.5 if ord(ch) > 0x2e80 else 6.9 for ch in s) * size / 12


def chart(mode, lang):
    c, L = PAL[mode], TXT[lang]
    if lang in RTL_LANGS:
        return mirror(chart_ltr(c, L))
    return chart_ltr(c, L)


def mirror(svg):
    """Mirrors the chart for a right-to-left language: every x is measured from the right edge, rectangles keep their
    width, and each text is set right to left with its start (now its right edge) at the mirrored x"""
    import re as _re

    def rect(m):
        a = m.group(0)
        if 'width="879"' in a:
            return a   # the frame
        x, w = float(_re.search(r' x="([\d.]+)"', a).group(1)), float(_re.search(r' width="([\d.]+)"', a).group(1))
        return _re.sub(r' x="[\d.]+"', f' x="{W - x - w:.1f}"', a, count=1)

    def text(m):
        a = m.group(0)
        x = float(_re.search(r' x="([\d.]+)"', a).group(1))
        return _re.sub(r' x="[\d.]+"', f' x="{W - x:.1f}" direction="rtl" unicode-bidi="embed"', a, count=1)

    svg = _re.sub(r"<rect\b[^>]*>", rect, svg)
    return _re.sub(r"<text\b[^>]*>", text, svg)


def chart_ltr(c, L):
    H = 104 + N * 30 + 18
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="{SANS}">', "<!--fonts-->",
         f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="8" fill="{c["bg"]}" stroke="{c["border"]}"/>',
         f'<text x="28" y="42" font-size="18" font-weight="700" fill="{c["fg"]}">{esc(L["title"])}</text>',
         f'<rect x="28" y="62" width="10" height="10" rx="2" fill="{c["law"]}"/>',
         f'<text x="44" y="71" font-size="12" fill="{c["muted"]}">{esc(L["law"])}</text>']
    lx = 44 + width(L["law"]) + 22   # CJK characters are a full em wide, Thaana vowel signs take no width
    if any(int(r["flags"]) > int(r["in_law_texts"]) for r in CATS):   # no "other" legend when every flag is in law texts
        o += [f'<rect x="{lx:.0f}" y="62" width="10" height="10" rx="2" fill="{c["other"]}"/>',
              f'<text x="{lx + 16:.0f}" y="71" font-size="12" fill="{c["muted"]}">{esc(L["other"])}</text>']
    x0, x1 = 250, W - 90
    mx = max(int(r["flags"]) for r in CATS)
    for i, r in enumerate(CATS):
        tot, law = int(r["flags"]), int(r["in_law_texts"])
        y = 96 + i * 30
        wl = (x1 - x0) * law / mx
        wo = (x1 - x0) * (tot - law) / mx
        tip = esc(((tot == 1 and L.get("tip1")) or L["tip"]).format(cat=L["cats"][i], n=num(tot, L["sep"]), law=num(law, L["sep"])).replace(": 1 flags", ": 1 flag"))
        o.append(f'<text x="28" y="{y + 12}" font-size="12.5" fill="{c["fg"]}">{esc(L["cats"][i])}</text>')
        bars = ""
        if law:
            bars += f'<rect x="{x0}" y="{y}" width="{max(3, wl):.1f}" height="16" rx="3" fill="{c["law"]}"/>'
        if tot - law:
            bars += f'<rect x="{x0 + (wl + 2 if law else 0):.1f}" y="{y}" width="{max(3, wo - (2 if law else 0)):.1f}" height="16" rx="3" fill="{c["other"]}"/>'
        o.append(f'<g><title>{tip}</title>{bars}</g>')
        o.append(f'<text x="{x0 + max(3, wl + wo) + 8:.1f}" y="{y + 12}" font-family="{MONO}" font-size="12" font-weight="600" fill="{c["fg"]}">{num(tot, L["sep"])}</text>')
    o.append("</svg>")
    return "\n".join(o) + "\n"


os.makedirs(OUT, exist_ok=True)
for lang in TXT:
    for mode in ("light", "dark"):
        name = f"flags-by-category{'-dark' if mode == 'dark' else ''}{'.' + LANG if lang != 'en' else ''}.svg"
        open(os.path.join(OUT, name), "w", encoding="utf-8", newline="\n").write(chart(mode, lang))
        print(name)
