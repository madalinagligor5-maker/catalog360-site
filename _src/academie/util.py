import html


def C(cod, lang="python"):
    """Bloc de cod pentru teorie (escape HTML)."""
    return f'<pre data-lang="{lang}"><code>{html.escape(cod.strip(chr(10)), quote=False)}</code></pre>'


def O(text, eticheta="ieșire"):
    return f'<pre class="out" data-lang="{eticheta}"><code>{html.escape(text.strip(chr(10)), quote=False)}</code></pre>'


def T(cap, *randuri):
    """Tabel simplu: T(["a","b"], ["x","y"], ...). Celulele sunt HTML."""
    h = '<div class="tbl"><table><tr>' + "".join(f"<th>{c}</th>" for c in cap) + "</tr>"
    for r in randuri:
        h += "<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>"
    return h + "</table></div>"


def _ruleaza_py(cod):
    import io, contextlib
    import sys
    out = io.StringIO()
    vechi = sys.stdin
    sys.stdin = io.StringIO("")      # un exemplu de teorie nu citește date
    try:
        with contextlib.redirect_stdout(out):
            exec(compile(cod, "exemplu.py", "exec"), {"__name__": "__main__"})
    except EOFError:
        raise SystemExit("Exemplu de teorie care citește date (input):\n" + cod)
    finally:
        sys.stdin = vechi
    return out.getvalue()


def _ruleaza_cpp(cod, intrare=""):
    import os, subprocess, tempfile
    with tempfile.TemporaryDirectory() as d:
        src, exe = os.path.join(d, "p.cpp"), os.path.join(d, "p")
        with open(src, "w", encoding="utf-8") as f:
            f.write(cod)
        r = subprocess.run(["g++", "-std=c++17", "-O1", "-o", exe, src], capture_output=True, text=True)
        if r.returncode:
            raise SystemExit("Eroare de compilare în exemplu:\n" + r.stderr + cod)
        r = subprocess.run([exe], input=intrare, capture_output=True, text=True, cwd=d, timeout=10)
        return r.stdout


def CO(cod, lang="python", intrare=""):
    """Bloc de cod + ieșirea lui, calculată prin rulare (nu scrisă de mână)."""
    cod = cod.strip("\n")
    out = _ruleaza_cpp(cod, intrare) if lang == "c++" else _ruleaza_py(cod)
    h = C(cod, lang)
    if intrare:
        h += O(intrare, "intrare")
    return h + (O(out) if out.strip() else "")


CPP_ANTET = "#include <iostream>\n#include <string>\n#include <cstring>\n#include <fstream>\nusing namespace std;\n"


def QZ(intro, cod, opts, a, why, main=True, antet=None):
    """Întrebare „Ce afișează?” în C++: corpul `cod` este verificat la build.
    main=True: `cod` se pune în main(); altfel `cod` este programul (fără antet)."""
    antet = CPP_ANTET if antet is None else antet
    complet = antet + ("int main() {\n" + cod + "\n    return 0;\n}\n" if main else cod)
    return (f"{intro}{C(cod, 'c++')}", opts, a, why, complet)
