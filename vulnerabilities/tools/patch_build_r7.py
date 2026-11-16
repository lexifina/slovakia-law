"""Seventh round for a country's build_vulns.py (found by the Vietnam run), idempotent:
 - lapsed-limit reviews are matched on 400 characters of context, not 80 (two flags with the same opening words shared a review);
 - a file deleted before the repository moved its act folders (data/paths.json) is linked under its old folder.

    python -X utf8 patch_build_r7.py <build_vulns.py> [...]
"""
import sys

OLD_LINK = '    return f"https://github.com/lexifina/{REPO}/blob/{_last[path]}/{path}" if _last.get(path) else ""\n'
NEW_LINK = '''    if not _last.get(path):  # deleted before the repository moved its act folders: look it up under its old folder (data/paths.json)
        head, _, name = path.rpartition("/")
        old = f"{OLD_FOLDER[head]}/{name}" if head in OLD_FOLDER else ""
        return f"https://github.com/lexifina/{REPO}/blob/{_last[old]}/{old}" if old and _last.get(old) else ""
    return f"https://github.com/lexifina/{REPO}/blob/{_last[path]}/{path}"


def _old_folders():
    """paths.json maps each act's old folder (its id) to its folder since the move; the detectors read today's folders"""
    out = subprocess.run(["git", "-C", GIT, "show", f"{PIN}:data/paths.json"], capture_output=True)
    if out.returncode:
        return {}
    p = json.loads(out.stdout.decode("utf-8")).get("paths", {})
    return {v: k for k, v in p.items()} if isinstance(p, dict) else {}


OLD_FOLDER = _old_folders()
'''
for f in sys.argv[1:]:
    s = open(f, encoding="utf-8").read()
    n = 0
    a, b = '.replace("\\n", " ")[:80] if det == "lapsed_limit"', '.replace("\\n", " ")[:400] if det == "lapsed_limit"'
    if a in s:
        s = s.replace(a, b); n += 1
    elif b not in s:
        print(f, "WARNING: context key not found")
    if "OLD_FOLDER = _old_folders()" not in s:
        if OLD_LINK in s:
            s = s.replace(OLD_LINK, NEW_LINK); n += 1
        else:
            print(f, "WARNING: link line not found")
    # (found by the France run) retroactive-date flags had an empty path, so none counted as law texts and notices/decisions
    # could not be told from law: give each the first file its act's commit wrote
    # (found by the Kosovo run) the alphabetically first file could be an English translation (en/...) or a file the commit
    # deleted (an act it repealed): prefer a law file, then one the commit wrote
    NEW_FP = ('FIRST_PATH, _key = {}, {}\n'
              'for _c, _p, _st in con.sql(f"""select commit, path, status\n'
              '    from \'{os.path.join(SCR, "index", "changes", REPO + ".parquet").replace(chr(92), "/")}\'""").fetchall():\n'
              '    _k = (kind_of(_p), _st == "D", _p)\n'
              '    if _c not in _key or _k < _key[_c]:\n'
              '        FIRST_PATH[_c], _key[_c] = _p, _k')
    OLD_FP = ('FIRST_PATH = dict(con.sql(f"""select commit, min(path)\n'
              '    from \'{os.path.join(SCR, "index", "changes", REPO + ".parquet").replace(chr(92), "/")}\' group by 1""").fetchall())')
    if OLD_FP in s:
        s = s.replace(OLD_FP, NEW_FP); n += 1
    if "FIRST_PATH = dict(" not in s and "FIRST_PATH, _key = {}, {}" not in s:
        a = '    add("retroactive_date", d, path="", '
        if s.count(a) == 1:
            s = s.replace(a, '    add("retroactive_date", d, path=FIRST_PATH.get(first, ""), ')
            i = s[:s.index('path=FIRST_PATH.get(first, ""), ')].rindex("\nfor ")  # before the loop that adds them
            s = s[:i] + ('\n# retroactive dates are per act, not per file: the path is the first file the act\'s commit on that day wrote,\n'
                         '# so kind_of can tell notices, circulars and decisions from law\n' + NEW_FP) + s[i:]
            n += 1
        else:
            print(f, "WARNING: retroactive add line found", s.count(a), "times")
    open(f, "w", encoding="utf-8", newline="\n").write(s)
    print(f, "patched", n)
