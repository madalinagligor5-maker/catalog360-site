"""Generează python.html (Academia Python) din lecțiile definite în lectii_*.py.

Rezultatele așteptate ale testelor și ieșirile exemplelor rezolvate se calculează
rulând soluțiile de referință cu CPython, deci nu sunt scrise de mână.
Rulare:  python3 _src/academie/build.py
"""
import html, io, json, os, sys, contextlib, tempfile, builtins, importlib

AICI = os.path.dirname(os.path.abspath(__file__))
RADACINA = os.path.abspath(os.path.join(AICI, "..", ".."))
sys.path.insert(0, AICI)


def ruleaza(cod, intrare="", fisiere=None):
    """Rulează `cod` cu stdin = intrare; întoarce (stdout, fișiere .out/.txt noi)."""
    fisiere = fisiere or {}
    vechi = os.getcwd()
    with tempfile.TemporaryDirectory() as d:
        os.chdir(d)
        try:
            for n, c in fisiere.items():
                with open(n, "w", encoding="utf-8") as f:
                    f.write(c)
            sin = io.StringIO(intrare)
            out = io.StringIO()

            def inp(prompt=""):
                linie = sin.readline()
                if not linie:
                    raise EOFError("EOF when reading a line")
                return linie.rstrip("\n")

            g = {"__name__": "__main__", "input": inp}
            with contextlib.redirect_stdout(out):
                old = sys.stdin
                sys.stdin = sin
                try:
                    exec(compile(cod, "program.py", "exec"), g)
                finally:
                    sys.stdin = old
            noi = {}
            for n in sorted(os.listdir(".")):
                if n not in fisiere:
                    with open(n, encoding="utf-8") as f:
                        noi[n] = f.read()
            return out.getvalue(), noi
        finally:
            os.chdir(vechi)


def norm(t):
    linii = [l.rstrip() for l in t.replace("\r\n", "\n").split("\n")]
    while linii and linii[-1] == "":
        linii.pop()
    return "\n".join(linii)


def esc(t):
    return html.escape(t, quote=False)


def bloc_cod(cod, lang="python"):
    return f'<pre data-lang="{lang}"><code>{esc(cod.strip(chr(10)))}</code></pre>'


def bloc_iesire(t, eticheta="ieșire"):
    return f'<pre class="out" data-lang="{eticheta}"><code>{esc(t.rstrip())}</code></pre>'


def construieste():
    lectii = []
    for nume in sorted(f for f in os.listdir(AICI) if f.startswith("lectii_") and f.endswith(".py")):
        mod = importlib.import_module(nume[:-3])
        lectii.extend(mod.LECTII)

    exercitii_js = {}
    sectiuni, nav = [], []
    total_ex = 0
    for idx, L in enumerate(lectii):
        lid = L["id"]
        parti = []
        parti.append(f'<div class="les-head"><span class="les-nr">{esc(L["nr"])}</span><div><h2 id="{lid}-t">{esc(L["titlu"])}</h2>'
                     f'<p class="les-prog">{L.get("programa","")}</p></div></div>')
        if L.get("obiective"):
            parti.append('<div class="obj"><h3>La finalul lecției vei ști</h3><ul>' +
                         "".join(f"<li>{o}</li>" for o in L["obiective"]) + "</ul></div>")
        parti.append(L["teorie"])
        # probleme rezolvate
        if L.get("rezolvate"):
            parti.append('<h3 class="sec">Probleme rezolvate</h3>')
            for k, R in enumerate(L["rezolvate"], 1):
                out, fis = ruleaza(R["cod"], R.get("intrare", ""), R.get("fisiere"))
                corp = f'<p>{R["enunt"]}</p>'
                if R.get("fisiere"):
                    for n, c in R["fisiere"].items():
                        corp += f'<p class="io-lbl">Fișierul <code>{esc(n)}</code></p>' + bloc_iesire(c, "fișier")
                corp += bloc_cod(R["cod"])
                if R.get("intrare"):
                    corp += '<p class="io-lbl">Date de intrare (tastatură)</p>' + bloc_iesire(R["intrare"], "intrare")
                if out.strip():
                    corp += '<p class="io-lbl">Se afișează</p>' + bloc_iesire(out)
                for n, c in fis.items():
                    corp += f'<p class="io-lbl">Fișierul creat <code>{esc(n)}</code></p>' + bloc_iesire(c, "fișier")
                if R.get("explicatie"):
                    corp += f'<div class="note">{R["explicatie"]}</div>'
                parti.append(f'<div class="ex solved"><div class="ex-h"><b>Rezolvată {L["nr"]}.{k}</b><span>{esc(R["titlu"])}</span></div>{corp}</div>')
        # exercitii interactive
        if L.get("exercitii"):
            parti.append('<h3 class="sec">Exerciții cu verificare automată</h3>'
                         '<p class="hint">Scrie programul în editor și apasă <b>Verifică</b>: pagina îl rulează pe mai multe teste. '
                         'Citește datele exact cum cere enunțul și afișează doar ce se cere (mesajele din <code>input("...")</code> nu contează).</p>')
            for k, E in enumerate(L["exercitii"], 1):
                total_ex += 1
                eid = f'{lid}-e{k}'
                teste = []
                for T in E["teste"]:
                    out, fis = ruleaza(E["sol"], T.get("in", ""), T.get("fisiere"))
                    t = {"in": T.get("in", ""), "fis": T.get("fisiere", {}), "out": norm(out)}
                    if E.get("fisier_iesire"):
                        n = E["fisier_iesire"]
                        if n not in fis:
                            raise SystemExit(f"{eid}: soluția nu a creat {n}")
                        t["fout"] = {n: norm(fis[n])}
                    teste.append(t)
                exercitii_js[eid] = {"teste": teste, "sol": E["sol"].strip("\n") + "\n",
                                     "start": E.get("start", "").strip("\n") + ("\n" if E.get("start") else "")}
                ex0 = teste[0]
                exemplu = ""
                for n, c in ex0["fis"].items():
                    exemplu += f'<div><p class="io-lbl">Fișierul <code>{esc(n)}</code></p>{bloc_iesire(c, "fișier")}</div>'
                if ex0["in"]:
                    exemplu += f'<div><p class="io-lbl">Intrare</p>{bloc_iesire(ex0["in"], "intrare")}</div>'
                if ex0["out"]:
                    exemplu += f'<div><p class="io-lbl">Ieșire</p>{bloc_iesire(ex0["out"])}</div>'
                for n, c in ex0.get("fout", {}).items():
                    exemplu += f'<div><p class="io-lbl">Fișierul <code>{esc(n)}</code></p>{bloc_iesire(c, "fișier")}</div>'
                parti.append(
                    f'<div class="ex task" id="{eid}" data-ex="{eid}"><div class="ex-h"><b>Exercițiul {L["nr"]}.{k}</b>'
                    f'<span>{esc(E["titlu"])}</span><span class="lvl">{E.get("nivel","mediu")}</span><span class="st" aria-live="polite"></span></div>'
                    f'<p>{E["enunt"]}</p><p class="io-lbl ex-lbl">Exemplu</p><div class="io-grid">{exemplu}</div>'
                    f'<div class="ide"><textarea placeholder="# Scrie programul aici" spellcheck="false" autocapitalize="off" aria-label="Editor de cod pentru exercițiul {L["nr"]}.{k}"></textarea>'
                    f'<div class="ide-bar"><button type="button" class="btn btn-primary b-check">Verifică</button>'
                    f'<button type="button" class="btn btn-ghost b-run">Rulează cu intrarea</button>'
                    f'<button type="button" class="btn btn-link b-sol">Arată soluția</button>'
                    f'<button type="button" class="btn btn-link b-reset">Resetează</button></div>'
                    f'<details class="stdin"><summary>Intrare pentru „Rulează”</summary><textarea class="in" spellcheck="false" aria-label="Date de intrare">{esc(ex0["in"])}</textarea></details>'
                    f'<div class="res" hidden></div></div></div>')
        if L.get("quiz"):
            q = '<div class="quiz" data-quiz><h3>Recapitulare <span class="score"></span></h3>'
            for k, (intr, opts, a, why) in enumerate(L["quiz"], 1):
                q += f'<fieldset class="q" data-a="{a}"><legend>{k}. {intr}</legend><div class="opts">'
                q += "".join(f'<button type="button">{o}</button>' for o in opts)
                q += f'</div><p class="why" hidden>{why}</p></fieldset>'
            parti.append(q + "</div>")
        prev = lectii[idx - 1] if idx else None
        nxt = lectii[idx + 1] if idx + 1 < len(lectii) else None
        pn = '<nav class="pn">'
        pn += f'<a href="#{prev["id"]}" class="btn btn-ghost">← {esc(prev["nr"])}. {esc(prev["scurt"])}</a>' if prev else "<span></span>"
        pn += f'<a href="#{nxt["id"]}" class="btn btn-primary">{esc(nxt["nr"])}. {esc(nxt["scurt"])} →</a>' if nxt else ""
        pn += "</nav>"
        parti.append(f'<div class="done-row"><label class="done-toggle"><input type="checkbox" data-done="{lid}"> Am terminat lecția</label></div>{pn}')
        sectiuni.append(f'<section class="lesson" id="{lid}" aria-labelledby="{lid}-t">' + "\n".join(parti) + "</section>")
        nex = len(L.get("exercitii", []))
        nav.append(f'<li><a href="#{lid}"><span class="n">{esc(L["nr"])}</span><span>{esc(L["scurt"])}</span>'
                   f'<span class="cnt" data-cnt="{lid}">{("0/" + str(nex)) if nex else ""}</span></a></li>')

    with open(os.path.join(AICI, "sablon.html"), encoding="utf-8") as f:
        sablon = f.read()
    pagina = (sablon.replace("{{NAV}}", "\n".join(nav))
              .replace("{{LECTII}}", "\n".join(sectiuni))
              .replace("{{NR_LECTII}}", str(len(lectii)))
              .replace("{{NR_EX}}", str(total_ex))
              .replace("{{DATE_EX}}", json.dumps(exercitii_js, ensure_ascii=False).replace("</", "<\\/")))
    with open(os.path.join(RADACINA, "python.html"), "w", encoding="utf-8") as f:
        f.write(pagina)
    print(f"python.html: {len(lectii)} lecții, {total_ex} exerciții, {len(pagina)//1024} KB")


if __name__ == "__main__":
    construieste()
