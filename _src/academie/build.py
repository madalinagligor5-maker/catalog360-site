"""Generează cursurile site-ului (python.html, algoritmi.html, cpp.html, metodica.html),
pagina principală (index.html) și pagina de teste (teste.html).

- Rezultatele așteptate ale testelor și ieșirile exemplelor rezolvate se calculează
  rulând soluțiile de referință (Python cu CPython, C++ cu g++), nu se scriu de mână.
- Întrebările grilă din toate cursurile și din programa.html intră în banca de teste.

Rulare (din rădăcina repository-ului):  python3 _src/academie/build.py
"""
import contextlib
import html
import importlib
import io
import json
import os
import re
import subprocess
import sys
import tempfile

AICI = os.path.dirname(os.path.abspath(__file__))
RADACINA = os.path.abspath(os.path.join(AICI, "..", ".."))
sys.path.insert(0, AICI)

from cursuri import CURSURI, NAV_SITE  # noqa: E402


# ---------------------------------------------------------------- rulare cod
def ruleaza(cod, intrare="", fisiere=None):
    """Rulează cod Python cu stdin = intrare; întoarce (stdout, fișiere noi)."""
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


def ruleaza_cpp(cod, intrare="", fisiere=None):
    """Compilează (g++ -std=c++17) și rulează; întoarce (stdout, fișiere noi)."""
    fisiere = fisiere or {}
    with tempfile.TemporaryDirectory() as d:
        src = os.path.join(d, "program.cpp")
        with open(src, "w", encoding="utf-8") as f:
            f.write(cod)
        exe = os.path.join(d, "program")
        r = subprocess.run(["g++", "-std=c++17", "-O1", "-Wall", "-o", exe, src], capture_output=True, text=True)
        if r.returncode != 0:
            raise SystemExit("Eroare de compilare C++:\n" + r.stderr + "\n" + cod)
        lucru = os.path.join(d, "lucru")
        os.mkdir(lucru)
        for n, c in fisiere.items():
            with open(os.path.join(lucru, n), "w", encoding="utf-8") as f:
                f.write(c)
        r = subprocess.run([exe], input=intrare, capture_output=True, text=True, cwd=lucru, timeout=10)
        if r.returncode != 0:
            raise SystemExit(f"Programul C++ s-a terminat cu codul {r.returncode}:\n{r.stderr}\n{cod}")
        noi = {}
        for n in sorted(os.listdir(lucru)):
            if n not in fisiere:
                with open(os.path.join(lucru, n), encoding="utf-8") as f:
                    noi[n] = f.read()
        return r.stdout, noi


def executa(cod, lang, intrare="", fisiere=None):
    return ruleaza_cpp(cod, intrare, fisiere) if lang == "c++" else ruleaza(cod, intrare, fisiere)


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


def text_simplu(h):
    """HTML → text pentru identificarea întrebărilor (fără etichete)."""
    return html.unescape(re.sub(r"<[^>]+>", "", h)).strip()


# ---------------------------------------------------------------- un curs
def randeaza_rezolvata(L, k, R, lang_curs):
    lang = R.get("lang", lang_curs)
    corp = f'<p>{R["enunt"]}</p>' if R.get("enunt") else ""
    for n, c in (R.get("fisiere") or {}).items():
        corp += f'<p class="io-lbl">Fișierul <code>{esc(n)}</code></p>' + bloc_iesire(c, "fișier")
    if R.get("cod"):
        out, fis = executa(R["cod"], lang, R.get("intrare", ""), R.get("fisiere"))
        corp += bloc_cod(R["cod"], lang)
        if R.get("intrare"):
            corp += '<p class="io-lbl">Date de intrare</p>' + bloc_iesire(R["intrare"], "intrare")
        if out.strip():
            corp += '<p class="io-lbl">Se afișează</p>' + bloc_iesire(out)
        for n, c in fis.items():
            corp += f'<p class="io-lbl">Fișierul creat <code>{esc(n)}</code></p>' + bloc_iesire(c, "fișier")
    if R.get("rezolvare"):
        corp += R["rezolvare"]
    if R.get("explicatie"):
        corp += f'<div class="note">{R["explicatie"]}</div>'
    return (f'<div class="ex solved"><div class="ex-h"><b>Rezolvată {L["nr"]}.{k}</b>'
            f'<span>{esc(R["titlu"])}</span></div>{corp}</div>')


def randeaza_aplicatie(L, k, eid, E, lang_curs):
    """Exercițiu cu răspuns liber: model de rezolvare + grilă de autoevaluare."""
    model = E.get("model", "")
    if E.get("cod_model"):
        lang = E.get("lang", lang_curs)
        out, fis = executa(E["cod_model"], lang, E.get("intrare", ""), E.get("fisiere"))
        model += bloc_cod(E["cod_model"], lang)
        if E.get("intrare"):
            model += '<p class="io-lbl">Date de intrare</p>' + bloc_iesire(E["intrare"], "intrare")
        if out.strip():
            model += '<p class="io-lbl">Se afișează</p>' + bloc_iesire(out)
        for n, c in fis.items():
            model += f'<p class="io-lbl">Fișierul creat <code>{esc(n)}</code></p>' + bloc_iesire(c, "fișier")
    criterii = ""
    if E.get("criterii"):
        criterii = ('<div class="crit"><p class="io-lbl">Autoevaluare – bifează ce ai în răspunsul tău</p>' +
                    "".join(f'<label><input type="checkbox"> {c}</label>' for c in E["criterii"]) + "</div>")
    camp = ("" if E.get("fara_raspuns") else
            f'<textarea class="ans" placeholder="Scrie aici răspunsul tău (se salvează doar în acest browser)" '
            f'aria-label="Răspunsul tău la aplicația {L["nr"]}.{k}"></textarea>')
    return (f'<div class="ex app" id="{eid}" data-app="{eid}"><div class="ex-h"><b>Aplicația {L["nr"]}.{k}</b>'
            f'<span>{esc(E["titlu"])}</span><span class="lvl">{E.get("nivel", "tip subiect")}</span>'
            f'<span class="st" aria-live="polite"></span></div><div>{E["enunt"]}</div>{camp}'
            f'<details class="sol"><summary>Vezi rezolvarea-model</summary><div class="body">{model}{criterii}</div></details>'
            f'<div class="ide-bar"><label class="done-toggle sm"><input type="checkbox" class="app-ok"> Am rezolvat și am verificat</label></div></div>')


def randeaza_curs(C):
    lectii = []
    for nume in sorted(f for f in os.listdir(AICI) if f.startswith(C["prefix"] + "_") and f.endswith(".py")):
        lectii.extend(importlib.import_module(nume[:-3]).LECTII)
    lang_curs = C.get("lang", "python")
    exercitii_js, aplicatii, sectiuni, nav, banca = {}, [], [], [], []
    total_ex = 0
    for idx, L in enumerate(lectii):
        lid = L["id"]
        parti = [f'<div class="les-head"><span class="les-nr">{esc(L["nr"])}</span><div><h2 id="{lid}-t">{esc(L["titlu"])}</h2>'
                 f'<p class="les-prog">{L.get("programa", "")}</p></div></div>']
        if L.get("obiective"):
            parti.append('<div class="obj"><h3>La finalul lecției vei ști</h3><ul>' +
                         "".join(f"<li>{o}</li>" for o in L["obiective"]) + "</ul></div>")
        parti.append(L["teorie"])
        if L.get("rezolvate"):
            parti.append(f'<h3 class="sec">{L.get("titlu_rezolvate", "Probleme rezolvate")}</h3>')
            for k, R in enumerate(L["rezolvate"], 1):
                parti.append(randeaza_rezolvata(L, k, R, lang_curs))
        auto = [E for E in L.get("exercitii", []) if E.get("tip", "auto") == "auto"]
        if L.get("exercitii"):
            if auto:
                parti.append('<h3 class="sec">Exerciții</h3><p class="hint">La exercițiile de programare scrii codul în editor și apeși '
                             '<b>Verifică</b>: pagina îl rulează pe mai multe teste. Citește datele exact cum cere enunțul și afișează '
                             'doar ce se cere (mesajele din <code>input("...")</code> nu contează).</p>')
            else:
                parti.append('<h3 class="sec">Aplicații</h3><p class="hint">Rezolvă în scris (în caseta de mai jos sau pe hârtie), apoi '
                             'deschide rezolvarea-model și bifează criteriile pe care le îndeplinește răspunsul tău.</p>')
            for k, E in enumerate(L["exercitii"], 1):
                total_ex += 1
                eid = f'{lid}-e{k}'
                if E.get("tip", "auto") != "auto":
                    aplicatii.append(eid)
                    parti.append(randeaza_aplicatie(L, k, eid, E, lang_curs))
                    continue
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
                    f'<span>{esc(E["titlu"])}</span><span class="lvl">{E.get("nivel", "mediu")}</span><span class="st" aria-live="polite"></span></div>'
                    f'<p>{E["enunt"]}</p><p class="io-lbl ex-lbl">Exemplu</p><div class="io-grid">{exemplu}</div>'
                    f'<div class="ide"><textarea placeholder="# Scrie programul aici" spellcheck="false" autocapitalize="off" '
                    f'aria-label="Editor de cod pentru exercițiul {L["nr"]}.{k}"></textarea>'
                    f'<div class="ide-bar"><button type="button" class="btn btn-primary b-check">Verifică</button>'
                    f'<button type="button" class="btn btn-ghost b-run">Rulează cu intrarea</button>'
                    f'<button type="button" class="btn btn-link b-sol">Arată soluția</button>'
                    f'<button type="button" class="btn btn-link b-reset">Resetează</button></div>'
                    f'<details class="stdin"><summary>Intrare pentru „Rulează”</summary><textarea class="in" spellcheck="false" aria-label="Date de intrare">{esc(ex0["in"])}</textarea></details>'
                    f'<div class="res" hidden></div></div></div>')
        if L.get("quiz"):
            q = '<div class="quiz" data-quiz><h3>Test de verificare <span class="score"></span></h3>'
            for k, item in enumerate(L["quiz"], 1):
                intr, opts, a, why = item[:4]
                if not 0 <= a < len(opts):
                    raise SystemExit(f"{lid}: răspuns invalid la întrebarea {k}")
                if len(item) == 5:      # întrebare „ce afișează”: răspunsul corect se verifică prin rulare
                    out, _ = executa(item[4], lang_curs)
                    if norm(out) != norm(text_simplu(opts[a])):
                        raise SystemExit(f"{lid}, întrebarea {k}: programul afișează {out!r}, dar răspunsul marcat corect este {text_simplu(opts[a])!r}")
                    for j, o in enumerate(opts):
                        if j != a and norm(text_simplu(o)) == norm(out):
                            raise SystemExit(f"{lid}, întrebarea {k}: și varianta {j} coincide cu ieșirea")
                q += f'<fieldset class="q" data-a="{a}"><legend>{k}. {intr}</legend><div class="opts">'
                q += "".join(f'<button type="button">{o}</button>' for o in opts)
                q += f'</div><p class="why" hidden>{why}</p></fieldset>'
                banca.append({"s": C["sectiune"], "c": C["scurt"], "l": f'{L["nr"]}. {L["scurt"]}',
                              "u": f'{C["fisier"][:-5]}#{lid}', "q": intr, "o": opts, "a": a, "w": why})
            parti.append(q + "</div>")
        prev = lectii[idx - 1] if idx else None
        nxt = lectii[idx + 1] if idx + 1 < len(lectii) else None
        pn = '<nav class="pn">'
        pn += f'<a href="#{prev["id"]}" class="btn btn-ghost">← {esc(prev["nr"])}. {esc(prev["scurt"])}</a>' if prev else "<span></span>"
        pn += (f'<a href="#{nxt["id"]}" class="btn btn-primary">{esc(nxt["nr"])}. {esc(nxt["scurt"])} →</a>' if nxt
               else f'<a href="{C["urmator"][0]}" class="btn btn-primary">{esc(C["urmator"][1])} →</a>')
        pn += "</nav>"
        parti.append(f'<div class="done-row"><label class="done-toggle"><input type="checkbox" data-done="{lid}"> Am terminat lecția</label></div>{pn}')
        sectiuni.append(f'<section class="lesson" id="{lid}" aria-labelledby="{lid}-t">' + "\n".join(parti) + "</section>")
        nex = len(L.get("exercitii", []))
        nav.append(f'<li><a href="#{lid}"><span class="n">{esc(L["nr"])}</span><span>{esc(L["scurt"])}</span>'
                   f'<span class="cnt" data-cnt="{lid}">{("0/" + str(nex)) if nex else ""}</span></a></li>')

    with open(os.path.join(AICI, "sablon.html"), encoding="utf-8") as f:
        pagina = f.read()
    stats = "".join(f"<span>{s}</span>" for s in C["stats"](len(lectii), total_ex, len(banca)))
    for k, v in {
        "{{TITLU}}": C["titlu"], "{{DESCRIERE}}": C["descriere"], "{{URL}}": C["fisier"][:-5],
        "{{EYEBROW}}": C["eyebrow"], "{{H1}}": C["h1"], "{{LEDE}}": C["lede"], "{{HINT}}": C.get("hint", ""),
        "{{STATS}}": stats, "{{KEY}}": C["cheie"], "{{NAV_SITE}}": nav_site(C["fisier"]),
        "{{NAV}}": "\n".join(nav), "{{LECTII}}": "\n".join(sectiuni), "{{NR_EX}}": str(total_ex),
        "{{DATE_EX}}": json.dumps(exercitii_js, ensure_ascii=False).replace("</", "<\\/"),
        "{{APLICATII}}": json.dumps(aplicatii),
    }.items():
        pagina = pagina.replace(k, v)
    with open(os.path.join(RADACINA, C["fisier"]), "w", encoding="utf-8") as f:
        f.write(pagina)
    print(f'{C["fisier"]}: {len(lectii)} lecții, {total_ex} exerciții/aplicații, {len(banca)} întrebări, {len(pagina)//1024} KB')
    return {"lectii": [(L["id"], L["nr"], L["scurt"], len(L.get("exercitii", []))) for L in lectii],
            "total_ex": total_ex, "banca": banca}


def nav_site(activ):
    h = '<nav class="site-nav" aria-label="Secțiuni"><div class="wrap"><ul>'
    for fis, eticheta in NAV_SITE:
        cur = ' aria-current="page"' if fis == activ else ""
        href = "./" if fis == "index.html" else fis[:-5]
        h += f'<li><a href="{href}"{cur}>{eticheta}</a></li>'
    return h + ("</ul></div></nav><script>(function(){var a=document.querySelector('.site-nav a[aria-current]');"
                "if(a&&a.parentNode.parentNode.scrollWidth>a.parentNode.parentNode.clientWidth)"
                "a.parentNode.parentNode.scrollLeft=a.offsetLeft-16;})();</script>")


# ---------------------------------------------------------------- programa.html → banca de întrebări
def banca_programa():
    with open(os.path.join(RADACINA, "programa.html"), encoding="utf-8") as f:
        s = f.read()
    banca = []
    for m in re.finditer(r'<section class="chapter" id="([^"]+)"[^>]*>.*?<h2 id="[^"]+">(.*?)</h2>(.*?)</section>', s, re.S):
        cid, titlu, corp = m.group(1), text_simplu(m.group(2)), m.group(3)
        sectiune = "Metodică" if cid.startswith("m") else "Programa – teorie"
        for q in re.finditer(r'<fieldset class="q" data-a="(\d)"><legend>(.*?)</legend><div class="opts">(.*?)</div>\s*<p class="why" hidden>(.*?)</p></fieldset>', corp, re.S):
            intr = re.sub(r"^\d+\.\s*", "", q.group(2).strip())
            opts = re.findall(r'<button type="button">(.*?)</button>', q.group(3), re.S)
            banca.append({"s": sectiune, "c": "Programa", "l": titlu, "u": f"programa#{cid}",
                          "q": intr, "o": opts, "a": int(q.group(1)), "w": q.group(4).strip()})
    return banca


def main():
    rezumat = {}
    banca = []
    for C in CURSURI:
        r = randeaza_curs(C)
        rezumat[C["fisier"]] = r
        banca.extend(r["banca"])
    # navigația comună în programa.html (pagină scrisă de mână)
    pp = os.path.join(RADACINA, "programa.html")
    with open(pp, encoding="utf-8") as f:
        sp = f.read()
    sp = re.sub(r"<!--NAV_SITE-->.*?<!--/NAV_SITE-->", lambda m: "<!--NAV_SITE-->" + nav_site("programa.html") + "<!--/NAV_SITE-->", sp, flags=re.S)
    with open(pp, "w", encoding="utf-8") as f:
        f.write(sp)
    bp = banca_programa()
    banca.extend(bp)
    print(f"programa.html: {len(bp)} întrebări preluate în banca de teste")

    with open(os.path.join(AICI, "sablon.html"), encoding="utf-8") as f:
        css = re.search(r"<style>.*?</style>", f.read(), re.S).group(0)
    # teste.html
    with open(os.path.join(AICI, "sablon_teste.html"), encoding="utf-8") as f:
        t = f.read()
    t = (t.replace("{{CSS}}", css).replace("{{NAV_SITE}}", nav_site("teste.html"))
          .replace("{{NR_Q}}", str(len(banca)))
          .replace("{{BANCA}}", json.dumps(banca, ensure_ascii=False).replace("</", "<\\/")))
    with open(os.path.join(RADACINA, "teste.html"), "w", encoding="utf-8") as f:
        f.write(t)
    print(f"teste.html: {len(banca)} întrebări în bancă")

    # index.html (harta pregătirii)
    with open(os.path.join(AICI, "sablon_acasa.html"), encoding="utf-8") as f:
        a = f.read()
    info = {C["fisier"]: {"cheie": C["cheie"], "lectii": [x[0] for x in rezumat[C["fisier"]]["lectii"]],
                          "ex": rezumat[C["fisier"]]["total_ex"]} for C in CURSURI}
    for C in CURSURI:
        r = rezumat[C["fisier"]]
        a = a.replace("{{NL_" + C["prefix"] + "}}", str(len(r["lectii"]))).replace("{{NE_" + C["prefix"] + "}}", str(r["total_ex"]))
    a = (a.replace("{{CSS}}", css).replace("{{NAV_SITE}}", nav_site("index.html")).replace("{{NR_Q}}", str(len(banca)))
          .replace("{{INFO}}", json.dumps(info)))
    with open(os.path.join(RADACINA, "index.html"), "w", encoding="utf-8") as f:
        f.write(a)
    print("index.html: generat")


if __name__ == "__main__":
    main()
