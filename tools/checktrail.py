"""Read this repository's check trail: every time an official source was read, what was read, and what came of it.

    python tools/checktrail.py                      the latest check of every source, and the sources not watched
    python tools/checktrail.py --day 2026-11-23     every check made on a day (UTC)
    python tools/checktrail.py --act <id>           every check that saw an act, or did not publish it, and why
    python tools/checktrail.py --source <id>        the checks of one source
    python tools/checktrail.py --json ...           the same records as JSON lines

Records (schema lexifina-check/1) are JSON lines in data/checks/<YYYY-MM>.jsonl, one per check, failed checks
included; data/checks/sources.json lists every official source and whether it is watched. They are appended by
`Kind: check` commits, which also rewrite monitoring/, WATCHING and FRESHNESS. Standard library only.
"""
import argparse
import json
import sys
from pathlib import Path


def load(root: Path):
    recs = []
    for p in sorted((root / "data" / "checks").glob("20??-??.jsonl")):
        recs += [json.loads(l) for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]
    recs.sort(key=lambda r: r["started"])
    src = root / "data" / "checks" / "sources.json"
    sources = json.loads(src.read_text(encoding="utf-8")).get("sources", []) if src.exists() else []
    return recs, sources


def show(r):
    s, p = r.get("seen") or {}, r.get("gap") or []
    print(f"{r['started']}  {r['source']:<22} {r['corpus']:<34} {r['outcome']:<13} read {len(r.get('requests') or []):>4}  "
          f"+{len(s.get('added', []))} ~{len(s.get('changed', []))} -{len(s.get('removed', []))}  "
          f"not published {len(p)} (no reason {r.get('unexplained', 0)})  "
          f"{' '.join(f['flag'] for f in r.get('flags', []))}  {r['check_id']}")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", default=str(Path(__file__).resolve().parent.parent))
    ap.add_argument("--day")
    ap.add_argument("--act")
    ap.add_argument("--source")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    recs, sources = load(Path(a.root))
    rs = recs
    if a.day:
        rs = [r for r in rs if r["started"].startswith(a.day)]
    if a.source:
        rs = [r for r in rs if r["source"] == a.source]
    if a.act:
        rs = [r for r in rs if a.act in json.dumps([r.get("seen"), r.get("published"), [g["id"] for g in r.get("gap", [])]])]
    if not (a.day or a.source or a.act):
        last = {}
        for r in rs:
            last[(r["source"], r["corpus"])] = r
        rs = list(last.values())
        for s in sources:
            if s.get("state") != "watched":
                print(f"{'':20}  {s['id']:<22} {s.get('state')}")
    for r in rs:
        if a.json:
            print(json.dumps(r, ensure_ascii=False, sort_keys=True))
            continue
        show(r)
        if a.act:
            for part in ("seen", "published"):
                for k, v in (r.get(part) or {}).items():
                    if a.act in v:
                        print(f"    {part} {k}")
            for g in r.get("gap", []):
                if g["id"] == a.act:
                    print(f"    not published: {g['reason'] or 'no reason'} ({g.get('detail', '')})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
