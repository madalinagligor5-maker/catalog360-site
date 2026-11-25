import random
from util import P, T
from culegere_01 import SFAT

LECTII = []
R = random.Random(7)


def mat(n, m, a, b):
    return "\n".join(" ".join(str(R.randint(a, b)) for _ in range(m)) for _ in range(n))


CITM = "Pe prima linie n și m, apoi n linii cu câte m numere întregi."

# ---------------------------------------------------------------- 4. Matrice
LECTII.append(dict(
    id="g4", nr="4", scurt="Matrice", titlu="Capitolul 4 – Matrice (liste de liste)",
    programa="Programa cap. 1 (*): modelul mixt – liste de liste; cap. 5.A (*): modele mixte",
    obiective=["parcurgeri pe linii, coloane, diagonale, chenare", "vecinii unei celule fără depășirea marginilor", "programare dinamică pe matrice"],
    teorie=SFAT,
    exercitii=[
        P("Linia cu suma maximă", "ușor", CITM + " Afișează numărul liniei (de la 1) cu suma maximă (prima, la egalitate) și suma ei.",
          "n, m = map(int, input().split())\na = [list(map(int, input().split())) for _ in range(n)]\ns = [sum(l) for l in a]\nprint(s.index(max(s)) + 1, max(s))",
          "3 3\n1 2 3\n9 0 0\n4 5 0", "1 2\n-1 -2", "2 2\n5 5\n6 4"),
        P("Matrice simetrică", "ușor", "Se citește n și o matrice pătratică n × n. Afișează <code>DA</code> dacă este simetrică față de diagonala principală, altfel <code>NU</code>.",
          "n = int(input())\na = [list(map(int, input().split())) for _ in range(n)]\nprint('DA' if all(a[i][j] == a[j][i] for i in range(n) for j in range(n)) else 'NU')",
          "3\n1 2 3\n2 5 6\n3 6 9", "2\n1 2\n3 4", "1\n7"),
        P("Rotire cu 90°", "mediu", CITM + " Afișează matricea rotită cu 90° în sensul acelor de ceasornic (m linii cu n valori).",
          "n, m = map(int, input().split())\na = [list(map(int, input().split())) for _ in range(n)]\nfor j in range(m):\n    print(*[a[i][j] for i in range(n - 1, -1, -1)])",
          "2 3\n1 2 3\n4 5 6", "1 1\n9", "3 2\n1 2\n3 4\n5 6"),
        P("Puncte șa", "mediu", CITM + " Un element este punct șa dacă este minim pe linia lui și maxim pe coloana lui. Afișează pozițiile (linie coloană, de la 1) ale punctelor șa, câte una pe linie, în ordinea parcurgerii pe linii, sau <code>nu exista</code>.",
          "n, m = map(int, input().split())\na = [list(map(int, input().split())) for _ in range(n)]\nmn = [min(l) for l in a]\nmx = [max(a[i][j] for i in range(n)) for j in range(m)]\nr = [(i + 1, j + 1) for i in range(n) for j in range(m) if a[i][j] == mn[i] == mx[j]]\nif r:\n    for p in r:\n        print(*p)\nelse:\n    print('nu exista')",
          "3 3\n3 8 9\n2 7 1\n5 6 4", "2 2\n1 2\n2 1", "2 3\n5 5 5\n5 5 5"),
        P("Sumele pe chenare", "mediu", "Se citește n și o matrice n × n. Afișează sumele elementelor de pe fiecare chenar (pătrat concentric), de la exterior spre interior.",
          "n = int(input())\na = [list(map(int, input().split())) for _ in range(n)]\nr = []\nfor k in range((n + 1) // 2):\n    s = 0\n    for i in range(k, n - k):\n        for j in range(k, n - k):\n            if i in (k, n - 1 - k) or j in (k, n - 1 - k):\n                s += a[i][j]\n    r.append(s)\nprint(*r)",
          "4\n1 1 1 1\n1 2 2 1\n1 2 2 1\n1 1 1 1", "3\n1 2 3\n4 5 6\n7 8 9", "1\n5"),
        P("Matricea spirală", "mediu", "Se citește n. Construiește matricea n × n care conține numerele 1, 2, …, n² așezate în spirală, în sensul acelor de ceasornic, din colțul stânga-sus, și afișeaz-o (valorile separate prin spațiu).",
          "n = int(input())\na = [[0] * n for _ in range(n)]\nx = y = 0\ndx, dy = 0, 1\nfor k in range(1, n * n + 1):\n    a[x][y] = k\n    nx, ny = x + dx, y + dy\n    if not (0 <= nx < n and 0 <= ny < n and a[nx][ny] == 0):\n        dx, dy = dy, -dx\n        nx, ny = x + dx, y + dy\n    x, y = nx, ny\nfor l in a:\n    print(*l)",
          "4", "1", "3"),
        P("Vârfuri locale", "mediu", CITM + " Afișează câte elemente sunt strict mai mari decât toți vecinii lor (sus, jos, stânga, dreapta – doar cei care există).",
          "n, m = map(int, input().split())\na = [list(map(int, input().split())) for _ in range(n)]\nc = 0\nfor i in range(n):\n    for j in range(m):\n        if all(a[i][j] > a[x][y] for x, y in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)) if 0 <= x < n and 0 <= y < m):\n            c += 1\nprint(c)",
          "3 4\n1 5 1 2\n2 1 3 9\n7 2 1 4", "1 1\n5", "2 2\n3 3\n3 3"),
        P("Produsul a două matrice", "mediu", "Pe prima linie n, m, p; apoi matricea A (n × m) și matricea B (m × p). Afișează A · B.",
          "n, m, p = map(int, input().split())\nA = [list(map(int, input().split())) for _ in range(n)]\nB = [list(map(int, input().split())) for _ in range(m)]\nfor i in range(n):\n    print(*[sum(A[i][k] * B[k][j] for k in range(m)) for j in range(p)])",
          "2 3 2\n1 2 3\n4 5 6\n7 8\n9 10\n11 12", "1 1 1\n3\n4", "2 2 2\n1 0\n0 1\n5 6\n7 8"),
        P("Drumul de sumă maximă", "dificil", CITM + " Pornind din colțul stânga-sus și mergând doar la dreapta sau în jos până în colțul dreapta-jos, afișează suma maximă care se poate aduna.",
          "n, m = map(int, input().split())\na = [list(map(int, input().split())) for _ in range(n)]\nfor i in range(n):\n    for j in range(m):\n        if i == 0 and j == 0:\n            continue\n        sus = a[i-1][j] if i else None\n        st = a[i][j-1] if j else None\n        a[i][j] += max(x for x in (sus, st) if x is not None)\nprint(a[n-1][m-1])",
          "3 3\n1 3 1\n1 5 1\n4 2 1", "1 1\n-5", "2 3\n-1 -2 -3\n-4 -5 -6", "60 60\n" + mat(60, 60, -100, 100)),
        P("Cel mai mare pătrat de 1", "dificil", "Pe prima linie n și m, apoi n linii cu câte m cifre 0/1 (lipite). Afișează latura celui mai mare pătrat format doar din 1. Programare dinamică: L[i][j] = 1 + min(stânga, sus, diagonală).",
          "n, m = map(int, input().split())\ng = [input().strip() for _ in range(n)]\nL = [[0] * m for _ in range(n)]\nbest = 0\nfor i in range(n):\n    for j in range(m):\n        if g[i][j] == '1':\n            L[i][j] = 1 if i == 0 or j == 0 else 1 + min(L[i-1][j], L[i][j-1], L[i-1][j-1])\n            best = max(best, L[i][j])\nprint(best)",
          "4 5\n10100\n10111\n11111\n10011", "2 2\n00\n00", "3 3\n111\n111\n111"),
        P("Sume pe dreptunghiuri", "dificil", CITM + " Urmează q și q linii <code>x1 y1 x2 y2</code> (colțurile unui dreptunghi, de la 1). Afișează suma fiecărui dreptunghi, folosind sume parțiale 2D (fiecare interogare în O(1)).",
          "n, m = map(int, input().split())\na = [list(map(int, input().split())) for _ in range(n)]\nS = [[0] * (m + 1) for _ in range(n + 1)]\nfor i in range(n):\n    for j in range(m):\n        S[i+1][j+1] = a[i][j] + S[i][j+1] + S[i+1][j] - S[i][j]\nq = int(input())\nfor _ in range(q):\n    x1, y1, x2, y2 = map(int, input().split())\n    print(S[x2][y2] - S[x1-1][y2] - S[x2][y1-1] + S[x1-1][y1-1])",
          "3 3\n1 2 3\n4 5 6\n7 8 9\n3\n1 1 3 3\n2 2 3 3\n1 2 1 2", "1 1\n5\n1\n1 1 1 1"),
    ],
))

# ---------------------------------------------------------------- 5. Dicționare, mulțimi, tupluri
LECTII.append(dict(
    id="g5", nr="5", scurt="Dicționare, mulțimi, tupluri", titlu="Capitolul 5 – Dicționare, mulțimi și tupluri",
    programa="Programa cap. 1 (*): modelul neliniar (mulțime), modelul asociativ (dicționar); cap. 5.A (*): clasele set, dict, tuple",
    obiective=["frecvențe și grupări cu dicționare", "operații de mulțimi", "sortarea cu chei compuse (tupluri)"],
    teorie=SFAT,
    exercitii=[
        P("Mediile elevilor", "ușor", "Pe prima linie n, apoi n linii <code>nume nota</code> (un elev poate apărea de mai multe ori). Afișează, alfabetic, fiecare nume cu media notelor lui (2 zecimale).",
          "n = int(input())\nd = {}\nfor _ in range(n):\n    nume, nota = input().split()\n    d.setdefault(nume, []).append(int(nota))\nfor nume in sorted(d):\n    print(nume, f'{sum(d[nume]) / len(d[nume]):.2f}')",
          "5\nDan 7\nAna 9\nDan 10\nAna 10\nIon 5", "1\nX 10"),
        P("Primul caracter unic", "ușor", "Se citește un cuvânt. Afișează primul caracter care apare o singură dată, sau <code>-</code>.",
          "s = input()\nf = {}\nfor c in s:\n    f[c] = f.get(c, 0) + 1\nprint(next((c for c in s if f[c] == 1), '-'))",
          "programare", "aabb", "x", "abcabcd"),
        P("Grupuri de anagrame", "mediu", "Se citesc cuvinte (litere mici) pe o linie. Grupează anagramele: afișează fiecare grup pe o linie, cu cuvintele sortate alfabetic; grupurile sunt ordonate după primul lor cuvânt.",
          "g = {}\nfor w in input().split():\n    g.setdefault(''.join(sorted(w)), []).append(w)\nfor gr in sorted((sorted(v) for v in g.values()), key=lambda x: x[0]):\n    print(*gr)",
          "mar ram arm cal lac abc", "unu", "ab ba ab"),
        P("Diferența simetrică", "ușor", "Se dau două liste de numere întregi, pe două linii. Afișează, crescător, valorile care apar în exact una dintre ele, sau <code>-</code>.",
          "a, b = set(map(int, input().split())), set(map(int, input().split()))\nr = sorted(a ^ b)\nprint(*r if r else ['-'])",
          "1 2 3 4\n3 4 5 5", "1 2\n2 1", "7\n8"),
        P("Inventarul", "mediu", "Pe prima linie n, apoi n comenzi: <code>add produs cantitate</code>, <code>del produs cantitate</code> (scade; dacă rezultatul este ≤ 0, produsul dispare) sau <code>show</code> (afișează pe o linie produsele în ordine alfabetică sub forma <code>produs:cantitate</code>, separate prin spațiu, sau <code>gol</code>).",
          "n = int(input())\nd = {}\nfor _ in range(n):\n    c = input().split()\n    if c[0] == 'add':\n        d[c[1]] = d.get(c[1], 0) + int(c[2])\n    elif c[0] == 'del':\n        if c[1] in d:\n            d[c[1]] -= int(c[2])\n            if d[c[1]] <= 0:\n                del d[c[1]]\n    else:\n        print(' '.join(f'{k}:{d[k]}' for k in sorted(d)) if d else 'gol')",
          "7\nadd mere 5\nadd pere 2\nshow\ndel mere 3\nadd mere 1\ndel pere 9\nshow", "2\nshow\ndel x 1"),
        P("Cel mai frecvent", "ușor", "Pe o linie, numere întregi. Afișează valoarea cea mai frecventă și frecvența ei; la egalitate, cea mai mică valoare.",
          "f = {}\nfor x in map(int, input().split()):\n    f[x] = f.get(x, 0) + 1\nb = min(f, key=lambda x: (-f[x], x))\nprint(b, f[b])",
          "3 1 3 2 1 3", "5", "2 1 2 1"),
        P("Puncte distincte", "mediu", "Pe prima linie n, apoi n linii cu coordonate întregi <code>x y</code>. Afișează numărul de puncte distincte și punctul cel mai depărtat de origine (la egalitate, cel mai mic ca tuplu (x, y)).",
          "n = int(input())\np = set(tuple(map(int, input().split())) for _ in range(n))\nb = min(p, key=lambda t: (-(t[0]**2 + t[1]**2), t))\nprint(len(p))\nprint(*b)",
          "5\n1 2\n3 4\n1 2\n-4 3\n0 0", "1\n0 0"),
        P("Dicționar de traducere", "mediu", "Pe prima linie n, apoi n perechi <code>cuvant_ro cuvant_en</code>, apoi o propoziție în română. Afișează traducerea cuvânt cu cuvânt; cuvintele necunoscute se scriu între paranteze drepte.",
          "n = int(input())\nd = dict(input().split() for _ in range(n))\nprint(' '.join(d.get(w, f'[{w}]') for w in input().split()))",
          "3\nam are\nmere apples\neu I\neu am mere rosii", "1\na b\nx"),
        P("Cel mai tânăr din fiecare oraș", "mediu", "Pe prima linie n, apoi n linii <code>nume varsta oras</code>. Pentru fiecare oraș, în ordine alfabetică, afișează <code>oras nume</code> pentru cea mai tânără persoană (la egalitate, primul nume alfabetic).",
          "n = int(input())\nd = {}\nfor _ in range(n):\n    nume, v, oras = input().split()\n    t = (int(v), nume)\n    if oras not in d or t < d[oras]:\n        d[oras] = t\nfor o in sorted(d):\n    print(o, d[o][1])",
          "5\nAna 15 Cluj\nDan 14 Iasi\nIon 14 Cluj\nEla 14 Cluj\nRadu 20 Iasi", "1\nX 9 Arad"),
        P("Intersecția a k liste", "mediu", "Pe prima linie k, apoi k linii cu numere întregi. Afișează, crescător, valorile care apar în toate cele k liste, sau <code>-</code>.",
          "k = int(input())\ns = set(map(int, input().split()))\nfor _ in range(k - 1):\n    s &= set(map(int, input().split()))\nprint(*sorted(s) if s else ['-'])",
          "3\n1 2 3 4\n2 3 4 5\n0 2 4", "2\n1\n2", "1\n5 5 1"),
    ],
))

# ---------------------------------------------------------------- 6. Fișiere
LECTII.append(dict(
    id="g6", nr="6", scurt="Fișiere text", titlu="Capitolul 6 – Probleme cu fișiere text",
    programa="Programa cap. 5.A (*): fișiere text – open, citire, scriere, închidere",
    obiective=["citirea datelor așezate oricum în fișier", "scrierea exactă a fișierului de ieșire", "prelucrări tipice de bacalaureat/titularizare"],
    teorie=SFAT + "<p>La problemele cu fișier de ieșire, verificatorul compară conținutul fișierului creat de programul tău (spațiile de la capăt de linie și liniile goale finale nu contează).</p>",
    exercitii=[
        P("Cea mai lungă secvență pară", "mediu", "Fișierul <code>bac.in</code> conține numere naturale, pe oricâte linii. Scrie în <code>bac.out</code> lungimea celei mai lungi secvențe de numere pare aflate pe poziții consecutive (0 dacă nu există).",
          "with open('bac.in') as f:\n    v = list(map(int, f.read().split()))\nbest = cur = 0\nfor x in v:\n    cur = cur + 1 if x % 2 == 0 else 0\n    best = max(best, cur)\nwith open('bac.out', 'w') as g:\n    g.write(str(best) + '\\n')",
          fis=[{"bac.in": "2 4 7 6\n8 10 1\n12\n"}, {"bac.in": "1 3 5\n"}, {"bac.in": "0\n"}], fout="bac.out"),
        P("Catalog CSV", "mediu", "Fișierul <code>catalog.csv</code> are pe fiecare linie <code>nume,clasa,nota</code>. Afișează pe ecran, pentru fiecare clasă (alfabetic), <code>clasa medie numar_elevi</code> (media cu 2 zecimale). Liniile goale se ignoră.",
          "d = {}\nwith open('catalog.csv') as f:\n    for linie in f:\n        linie = linie.strip()\n        if linie:\n            nume, cl, nota = linie.split(',')\n            d.setdefault(cl, []).append(int(nota))\nfor cl in sorted(d):\n    print(cl, f'{sum(d[cl]) / len(d[cl]):.2f}', len(d[cl]))",
          fis=[{"catalog.csv": "Ana,9A,9\nDan,9B,7\nIon,9A,10\n\nEla,10A,8\n"}, {"catalog.csv": "X,1A,5\n"}]),
        P("Numerotarea liniilor", "ușor", "Copiază în <code>text.out</code> liniile nevide din <code>text.in</code>, numerotate: <code>1: text</code>. Liniile formate doar din spații se consideră vide.",
          "k = 0\nwith open('text.in') as f, open('text.out', 'w') as g:\n    for linie in f:\n        if linie.strip():\n            k += 1\n            g.write(f'{k}: {linie.rstrip()}\\n')",
          fis=[{"text.in": "Ana are mere\n\n   \nDan are pere\nsfarsit\n"}, {"text.in": "x\n"}], fout="text.out"),
        P("Numere prime din fișier", "mediu", "Fișierul <code>numere.in</code> conține numere naturale ≤ 10<sup>6</sup>, pe oricâte linii. Scrie în <code>prime.out</code> numerele prime distincte, în ordine descrescătoare, pe o linie, sau <code>0</code> dacă nu există.",
          "def prim(n):\n    if n < 2:\n        return False\n    d = 2\n    while d * d <= n:\n        if n % d == 0:\n            return False\n        d += 1\n    return True\nwith open('numere.in') as f:\n    v = set(map(int, f.read().split()))\nr = sorted((x for x in v if prim(x)), reverse=True)\nwith open('prime.out', 'w') as g:\n    g.write((' '.join(map(str, r)) if r else '0') + '\\n')",
          fis=[{"numere.in": "7 4 11\n7 1 2\n999983\n"}, {"numere.in": "4 6 8 1 0\n"}], fout="prime.out"),
        P("Statistica unui text", "mediu", "Pentru fișierul <code>text.txt</code> afișează pe ecran: numărul de linii, numărul de cuvinte, numărul de caractere (fără caracterele de linie nouă) și litera cea mai frecventă (fără a ține cont de litere mari/mici; la egalitate, prima alfabetic).",
          "with open('text.txt') as f:\n    linii = f.read().split('\\n')\nif linii and linii[-1] == '':\n    linii.pop()\nlit = {}\nfor l in linii:\n    for c in l.lower():\n        if c.isalpha():\n            lit[c] = lit.get(c, 0) + 1\nprint(len(linii), sum(len(l.split()) for l in linii), sum(len(l) for l in linii), min(lit, key=lambda c: (-lit[c], c)))",
          fis=[{"text.txt": "Ana are mere.\nDan are pere!\n"}, {"text.txt": "zz yy\n"}]),
        P("Temperaturi", "mediu", "Fișierul <code>temp.in</code> conține pe fiecare linie <code>zi temperatura</code> (întregi), în ordinea zilelor. Afișează pe prima linie zilele cu temperatura strict peste medie (pe o linie), iar pe a doua cea mai mare diferență (în valoare absolută) dintre două zile consecutive.",
          "z, t = [], []\nwith open('temp.in') as f:\n    for linie in f:\n        if linie.strip():\n            a, b = map(int, linie.split())\n            z.append(a); t.append(b)\nm = sum(t) / len(t)\nprint(*[z[i] for i in range(len(t)) if t[i] > m])\nprint(max((abs(t[i] - t[i-1]) for i in range(1, len(t))), default=0))",
          fis=[{"temp.in": "1 12\n2 15\n3 9\n4 20\n5 18\n"}, {"temp.in": "1 5\n2 -3\n"}]),
        P("Interclasarea a două fișiere", "mediu", "Fișierele <code>a.in</code> și <code>b.in</code> conțin numere întregi sortate crescător. Scrie în <code>c.out</code> toate numerele, sortate, pe o linie, prin interclasare (fără sort).",
          "with open('a.in') as f:\n    a = list(map(int, f.read().split()))\nwith open('b.in') as f:\n    b = list(map(int, f.read().split()))\ni = j = 0\nc = []\nwhile i < len(a) and j < len(b):\n    if a[i] <= b[j]:\n        c.append(a[i]); i += 1\n    else:\n        c.append(b[j]); j += 1\nc += a[i:] + b[j:]\nwith open('c.out', 'w') as g:\n    g.write(' '.join(map(str, c)) + '\\n')",
          fis=[{"a.in": "1 4 9\n", "b.in": "2 3 10 11\n"}, {"a.in": "5\n", "b.in": "1 2 3\n"}], fout="c.out"),
        P("Jurnal de evenimente", "mediu", "Fiecare linie din <code>log.txt</code> are forma <code>HH:MM eveniment</code>. Afișează, pentru fiecare oră în care au avut loc evenimente, în ordine crescătoare, <code>HH numar_evenimente</code>.",
          "f = {}\nwith open('log.txt') as fi:\n    for linie in fi:\n        if linie.strip():\n            h = linie.split(':')[0]\n            f[h] = f.get(h, 0) + 1\nfor h in sorted(f):\n    print(h, f[h])",
          fis=[{"log.txt": "08:15 intrare\n08:59 pauza\n10:00 test\n09:30 iesire\n10:45 intrare\n"}, {"log.txt": "23:59 x\n"}]),
        P("Transpusa în fișier", "mediu", "Fișierul <code>mat.in</code> conține pe prima linie n și m, apoi matricea. Scrie transpusa în <code>mat.out</code>: pe prima linie m și n, apoi matricea transpusă.",
          "with open('mat.in') as f:\n    n, m = map(int, f.readline().split())\n    a = [list(map(int, f.readline().split())) for _ in range(n)]\nwith open('mat.out', 'w') as g:\n    g.write(f'{m} {n}\\n')\n    for j in range(m):\n        g.write(' '.join(str(a[i][j]) for i in range(n)) + '\\n')",
          fis=[{"mat.in": "2 3\n1 2 3\n4 5 6\n"}, {"mat.in": "1 1\n7\n"}], fout="mat.out"),
    ],
))
