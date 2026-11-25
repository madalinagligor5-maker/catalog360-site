import random
from util import P, T
from culegere_01 import SFAT

LECTII = []
R = random.Random(11)

# ---------------------------------------------------------------- 7. Subprograme, recursivitate, backtracking
LECTII.append(dict(
    id="g7", nr="7", scurt="Funcții, recursivitate, backtracking", titlu="Capitolul 7 – Subprograme, recursivitate și backtracking",
    programa="Programa cap. 5.A (*): subprograme, subprograme recursive; cap. 4: Backtracking, Divide et impera; cap. 3 (*): generare sistematică",
    obiective=["funcții recursive cu caz de bază corect", "backtracking cu condiții de continuare", "generare în ordine lexicografică"],
    teorie=SFAT + "<p>La problemele care cer o funcție, scrie funcția și programul care o folosește; verificatorul testează doar ce se afișează.</p>",
    exercitii=[
        P("Apariții recursive ale unei cifre", "ușor", "Scrie o funcție <strong>recursivă</strong> <code>nr(n, c)</code> care întoarce de câte ori apare cifra c în n. Se citesc n și c; afișează rezultatul (pentru n = 0 și c = 0 rezultatul este 1).",
          "def nr(n, c):\n    if n < 10:\n        return 1 if n == c else 0\n    return (1 if n % 10 == c else 0) + nr(n // 10, c)\n\nn, c = map(int, input().split())\nprint(nr(n, c))",
          "2026 2", "0 0", "11111 1", "123 9"),
        P("Biți de 1", "ușor", "Scrie o funcție recursivă care întoarce reprezentarea în baza 2 a lui n (ca șir) și una care întoarce numărul de biți de 1. Se citește n; afișează reprezentarea și numărul de biți de 1.",
          "def b2(n):\n    return str(n) if n < 2 else b2(n // 2) + str(n % 2)\n\ndef unu(n):\n    return 0 if n == 0 else n % 2 + unu(n // 2)\n\nn = int(input())\nprint(b2(n), unu(n))",
          "13", "0", "1", "1023", "1024"),
        P("Palindrom recursiv", "mediu", "Scrie o funcție recursivă care verifică dacă un text este palindrom ignorând caracterele care nu sunt litere și diferențele dintre litere mari și mici. Afișează <code>DA</code>/<code>NU</code>.",
          "def pal(s, i, j):\n    if i >= j:\n        return True\n    if not s[i].isalpha():\n        return pal(s, i + 1, j)\n    if not s[j].isalpha():\n        return pal(s, i, j - 1)\n    return s[i].lower() == s[j].lower() and pal(s, i + 1, j - 1)\n\ns = input()\nprint('DA' if pal(s, 0, len(s) - 1) else 'NU')",
          "Ele fac cafele", "Ana are", "A man, a plan, a canal: Panama", "!!"),
        P("Sume de numere prime distincte", "dificil", "Se citește n (2 ≤ n ≤ 60). Afișează toate modurile de a scrie n ca sumă de numere prime distincte, termenii în ordine crescătoare, câte o descompunere pe linie (<code>2+3+5</code>), în ordine lexicografică; dacă nu există, afișează <code>nu exista</code>.",
          "n = int(input())\npr = [p for p in range(2, n + 1) if all(p % d for d in range(2, int(p ** 0.5) + 1))]\nx, sol = [], []\ndef bt(i, s):\n    if s == n:\n        sol.append('+'.join(map(str, x))); return\n    for j in range(i, len(pr)):\n        if s + pr[j] > n:\n            break\n        x.append(pr[j]); bt(j + 1, s + pr[j]); x.pop()\nbt(0, 0)\nprint('\\n'.join(sol) if sol else 'nu exista')",
          "10", "2", "4", "30"),
        P("Parole fără litere alăturate egale", "mediu", "Se citesc un șir de litere distincte și k (k ≤ 5). Afișează, în ordine lexicografică, toate șirurile de lungime k formate cu aceste litere (o literă poate fi folosită de mai multe ori), în care două poziții vecine nu au aceeași literă.",
          "s = sorted(input().strip())\nk = int(input())\nx = []\ndef bt():\n    if len(x) == k:\n        print(''.join(x)); return\n    for c in s:\n        if not x or x[-1] != c:\n            x.append(c); bt(); x.pop()\nbt()",
          "ab\n3", "abc\n2", "z\n1"),
        P("Plata unei sume", "mediu", "Pe prima linie S, pe a doua valorile distincte ale monedelor (fiecare monedă se poate folosi de oricâte ori). Afișează numărul de moduri de a plăti exact S (ordinea monedelor nu contează).",
          "S = int(input())\nm = list(map(int, input().split()))\nd = [1] + [0] * S\nfor c in m:\n    for s in range(c, S + 1):\n        d[s] += d[s - c]\nprint(d[S])",
          "10\n1 2 5", "3\n2", "0\n1 2", "500\n1 5 10 50 100 200"),
        P("Permutări fără vecini consecutivi", "mediu", "Se citește n (n ≤ 8). Afișează numărul de permutări ale lui {1, …, n} în care oricare două elemente alăturate nu diferă prin 1, apoi prima astfel de permutare în ordine lexicografică (sau <code>-</code>).",
          "n = int(input())\nx, f = [], [False] * (n + 1)\ncnt, prima = 0, None\ndef bt():\n    global cnt, prima\n    if len(x) == n:\n        cnt += 1\n        if prima is None:\n            prima = x[:]\n        return\n    for v in range(1, n + 1):\n        if not f[v] and (not x or abs(x[-1] - v) != 1):\n            f[v] = True; x.append(v); bt(); x.pop(); f[v] = False\nbt()\nprint(cnt)\nprint(*prima if prima else ['-'])",
          "4", "1", "3", "8"),
        P("Drumuri în labirint", "dificil", "Pe prima linie n și m (n·m ≤ 25), apoi n linii cu caracterele <code>.</code> (liber), <code>#</code> (zid), <code>S</code> (start), <code>E</code> (ieșire). Afișează numărul de drumuri de la S la E care se deplasează sus/jos/stânga/dreapta fără a trece de două ori prin aceeași celulă.",
          "n, m = map(int, input().split())\ng = [list(input().strip()) for _ in range(n)]\nfor i in range(n):\n    for j in range(m):\n        if g[i][j] == 'S':\n            si, sj = i, j\ncnt = 0\ndef bt(i, j):\n    global cnt\n    if g[i][j] == 'E':\n        cnt += 1; return\n    c = g[i][j]; g[i][j] = '#'\n    for a, b in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):\n        if 0 <= a < n and 0 <= b < m and g[a][b] != '#':\n            bt(a, b)\n    g[i][j] = c\nbt(si, sj)\nprint(cnt)",
          "3 3\nS..\n.#.\n..E", "2 2\nS#\n#E", "3 4\nS...\n....\n...E"),
        P("Submulțimi cu suma pară", "mediu", "Se citesc n și k, apoi n numere naturale distincte. Afișează, în ordine lexicografică după poziții, toate submulțimile de k elemente (în ordinea din listă) cu suma pară, câte una pe linie, sau <code>0</code>.",
          "n, k = map(int, input().split())\nv = list(map(int, input().split()))\nx, gasit = [], False\ndef bt(i):\n    global gasit\n    if len(x) == k:\n        if sum(x) % 2 == 0:\n            print(*x); gasit = True\n        return\n    for j in range(i, n):\n        x.append(v[j]); bt(j + 1); x.pop()\nbt(0)\nif not gasit:\n    print(0)",
          "4 2\n1 2 3 4", "3 3\n1 2 4", "3 2\n2 4 6"),
        P("Fibonacci pentru n uriaș", "dificil", "Se citesc n (0 ≤ n ≤ 10<sup>18</sup>) și m (2 ≤ m ≤ 10<sup>9</sup>). Afișează F(n) mod m (F(0) = 0, F(1) = 1), folosind exponențierea rapidă a matricei [[1, 1], [1, 0]].",
          "def mul(A, B, m):\n    return [[(A[0][0]*B[0][0] + A[0][1]*B[1][0]) % m, (A[0][0]*B[0][1] + A[0][1]*B[1][1]) % m],\n            [(A[1][0]*B[0][0] + A[1][1]*B[1][0]) % m, (A[1][0]*B[0][1] + A[1][1]*B[1][1]) % m]]\n\ndef putere(A, n, m):\n    if n == 0:\n        return [[1 % m, 0], [0, 1 % m]]\n    H = putere(A, n // 2, m)\n    H = mul(H, H, m)\n    return mul(H, A, m) if n % 2 else H\n\nn, m = map(int, input().split())\nprint(putere([[1, 1], [1, 0]], n, m)[0][1])",
          "10 1000", "0 7", "1 7", "90 1000000007", "1000000000000000000 1000000007"),
    ],
))

# ---------------------------------------------------------------- 8. Algoritmi clasici
inter = "\n".join(f"{a} {a + R.randint(1, 50)}" for a in (R.randint(0, 100000) for _ in range(3000)))
LECTII.append(dict(
    id="g8", nr="8", scurt="Algoritmi: sortare, căutare, greedy, PD, BFS", titlu="Capitolul 8 – Algoritmi clasici",
    programa="Programa cap. 3 și 4: sortare, căutare binară, Greedy, programare dinamică, parcurgeri",
    obiective=["alegerea algoritmului după dimensiunea datelor", "căutarea binară pe răspuns", "greedy demonstrat și programare dinamică"],
    teorie=SFAT,
    exercitii=[
        P("Sortare stabilă după notă", "mediu", "Pe prima linie n, apoi n linii <code>nume nota</code>. Afișează elevii în ordinea descrescătoare a notei; la note egale, în ordinea din fișierul de intrare (sortare stabilă).",
          "n = int(input())\nv = [input().split() for _ in range(n)]\nfor nume, nota in sorted(v, key=lambda e: -int(e[1])):\n    print(nume, nota)",
          "5\nDan 8\nAna 10\nIon 8\nEla 10\nRadu 7", "1\nX 5"),
        P("Tăierea lemnelor", "dificil", "Pe prima linie n și M, pe a doua înălțimile a n copaci. Un utilaj taie toți copacii la înălțimea H (ce depășește H se colectează). Afișează cea mai mare valoare întreagă H pentru care se colectează cel puțin M metri de lemn. Căutare binară pe H.",
          "n, M = map(int, input().split())\nh = list(map(int, input().split()))\nst, dr = 0, max(h)\nwhile st < dr:\n    mij = (st + dr + 1) // 2\n    if sum(x - mij for x in h if x > mij) >= M:\n        st = mij\n    else:\n        dr = mij - 1\nprint(st)",
          "4 7\n20 15 10 17", "5 20\n4 42 40 26 46", "1 1\n1", "3 0\n5 5 5"),
        P("Reuniunea intervalelor", "mediu", "Pe prima linie n, apoi n intervale închise <code>a b</code>. Afișează intervalele obținute prin unirea celor care se suprapun sau se ating (au un capăt comun), sortate crescător, câte unul pe linie.",
          "n = int(input())\nv = sorted(tuple(map(int, input().split())) for _ in range(n))\nr = []\nfor a, b in v:\n    if r and a <= r[-1][1]:\n        r[-1][1] = max(r[-1][1], b)\n    else:\n        r.append([a, b])\nfor a, b in r:\n    print(a, b)",
          "4\n1 3\n8 10\n2 6\n15 18", "2\n1 4\n4 5", "1\n0 0", "3000\n" + inter),
        P("Scara cu 1, 2 sau 3 trepte", "mediu", "Se citește n (n ≤ 10<sup>5</sup>). În câte moduri se poate urca o scară cu n trepte, făcând pași de 1, 2 sau 3 trepte? Afișează rezultatul modulo 1 000 000 007 (pentru n = 0 există un mod).",
          "n = int(input())\nM = 10**9 + 7\nd = [1, 1, 2]\nfor i in range(3, n + 1):\n    d.append((d[-1] + d[-2] + d[-3]) % M)\nprint(d[n] % M)",
          "4", "0", "1", "100000"),
        P("Subșir crescător maximal în O(n log n)", "dificil", "Pe prima linie n (n ≤ 10<sup>5</sup>), pe a doua n numere întregi. Afișează lungimea celui mai lung subșir strict crescător. Soluția O(n²) depășește timpul – folosește <code>bisect</code>.",
          "from bisect import bisect_left\nn = int(input())\nt = []\nfor x in map(int, input().split()):\n    i = bisect_left(t, x)\n    if i == len(t):\n        t.append(x)\n    else:\n        t[i] = x\nprint(len(t))",
          "8\n5 2 8 6 3 6 9 7", "1\n4", "5\n5 5 5 5 5", "10000\n" + " ".join(str(R.randint(1, 10**6)) for _ in range(10000))),
        P("Numărul minim de săli", "dificil", "Pe prima linie n, apoi n activități <code>inceput sfarsit</code> (sfârșitul este exclus: o activitate care începe la ora la care se termină alta poate folosi aceeași sală). Afișează numărul minim de săli necesare.",
          "n = int(input())\nev = []\nfor _ in range(n):\n    a, b = map(int, input().split())\n    ev.append((a, 1)); ev.append((b, -1))\nev.sort()\ncur = best = 0\nfor _, t in ev:\n    cur += t\n    best = max(best, cur)\nprint(best)",
          "4\n1 4\n2 5\n4 6\n5 7", "1\n0 10", "3\n1 2\n2 3\n3 4", "3000\n" + inter),
        P("Ieșirea din labirint", "mediu", "Pe prima linie n și m, apoi grila cu <code>.</code>, <code>#</code>, <code>S</code>, <code>E</code>. Afișează numărul minim de pași (sus/jos/stânga/dreapta) de la S la E, sau <code>-1</code>. Folosește BFS.",
          "from collections import deque\nn, m = map(int, input().split())\ng = [input().strip() for _ in range(n)]\nfor i in range(n):\n    for j in range(m):\n        if g[i][j] == 'S': s = (i, j)\n        if g[i][j] == 'E': e = (i, j)\nd = {s: 0}\nq = deque([s])\nwhile q:\n    x, y = q.popleft()\n    for a, b in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):\n        if 0 <= a < n and 0 <= b < m and g[a][b] != '#' and (a, b) not in d:\n            d[(a, b)] = d[(x, y)] + 1\n            q.append((a, b))\nprint(d.get(e, -1))",
          "4 5\nS..#.\n.#...\n.#.#.\n...#E", "2 2\nS#\n#E", "1 2\nSE"),
        P("Rucsac cu obiectele alese", "dificil", "Pe prima linie n și G, apoi n linii <code>greutate valoare</code>. Rucsac 0/1: afișează valoarea maximă și, pe linia următoare, numerele de ordine (de la 1) ale obiectelor alese, crescător (oricare soluție optimă se acceptă? Nu: alege-o pe cea dată de reconstituirea standard, de la ultimul obiect spre primul, pe tabelul d[i][c]).",
          "n, G = map(int, input().split())\no = [tuple(map(int, input().split())) for _ in range(n)]\nd = [[0] * (G + 1) for _ in range(n + 1)]\nfor i in range(1, n + 1):\n    g, v = o[i - 1]\n    for c in range(G + 1):\n        d[i][c] = d[i - 1][c]\n        if g <= c and d[i - 1][c - g] + v > d[i][c]:\n            d[i][c] = d[i - 1][c - g] + v\nc, ales = G, []\nfor i in range(n, 0, -1):\n    if d[i][c] != d[i - 1][c]:\n        ales.append(i)\n        c -= o[i - 1][0]\nprint(d[n][G])\nprint(*sorted(ales) if ales else ['-'])",
          "4 7\n1 1\n3 4\n4 5\n5 7", "1 3\n5 10", "3 10\n5 10\n4 40\n6 30"),
        P("Perechi cu diferența k", "mediu", "Pe prima linie n și k (k ≥ 1), pe a doua n numere întregi distincte. Afișează numărul de perechi neordonate cu diferența (în valoare absolută) exact k. O(n) cu o mulțime.",
          "n, k = map(int, input().split())\ns = set(map(int, input().split()))\nprint(sum(1 for x in s if x + k in s))",
          "5 2\n1 5 3 4 2", "3 10\n1 2 3", "10000 7\n" + " ".join(map(str, R.sample(range(10**6), 10000)))),
    ],
))
# corectăm enunțul rucsacului (fără întrebarea retorică)
LECTII[-1]["exercitii"][7]["enunt"] = ("Pe prima linie n și G, apoi n linii <code>greutate valoare</code>. Rucsac 0/1: afișează valoarea maximă, iar pe linia următoare numerele de ordine (de la 1) ale obiectelor alese, crescător. "
    "Pentru că pot exista mai multe soluții optime, reconstituie soluția astfel: construiește tabelul d[i][c] (cele mai bune valori cu primele i obiecte și capacitatea c) și, pornind de la i = n, c = G, consideră obiectul i ales dacă d[i][c] ≠ d[i−1][c].")

# ---------------------------------------------------------------- 9. POO
LECTII.append(dict(
    id="g9", nr="9", scurt="Programare orientată pe obiecte", titlu="Capitolul 9 – Programare orientată pe obiecte",
    programa="Programa cap. 5.A: clasă, membri, obiecte, constructor, clasă derivată; cap. 1: modelul obiectual",
    obiective=["clase cu metode speciale (__init__, __str__, __add__, __lt__)", "moștenire și suprascriere", "modelarea unei probleme cu obiecte"],
    teorie=SFAT,
    exercitii=[
        P("Vectori în plan", "mediu", "Scrie clasa <code>Vector</code> (x, y întregi) cu <code>__add__</code>, <code>__sub__</code>, <code>__mul__</code> (înmulțire cu un număr întreg), <code>lungime()</code> și <code>__str__</code> (format <code>(x, y)</code>). Se citesc doi vectori și un număr k (pe trei linii). Afișează a + b, a − b, a · k și lungimea lui a + b cu 2 zecimale.",
          "class Vector:\n    def __init__(self, x, y):\n        self.x, self.y = x, y\n    def __add__(self, o):\n        return Vector(self.x + o.x, self.y + o.y)\n    def __sub__(self, o):\n        return Vector(self.x - o.x, self.y - o.y)\n    def __mul__(self, k):\n        return Vector(self.x * k, self.y * k)\n    def lungime(self):\n        return (self.x ** 2 + self.y ** 2) ** 0.5\n    def __str__(self):\n        return f'({self.x}, {self.y})'\n\na = Vector(*map(int, input().split()))\nb = Vector(*map(int, input().split()))\nk = int(input())\nprint(a + b)\nprint(a - b)\nprint(a * k)\nprint(f'{(a + b).lungime():.2f}')",
          "1 2\n2 2\n3", "0 0\n0 0\n5", "-3 4\n3 -4\n-1"),
        P("Coadă din două stive", "dificil", "Implementează clasa <code>Coada</code> folosind <strong>două liste folosite ca stive</strong> (doar append și pop()), cu metodele <code>adauga(x)</code> și <code>scoate()</code>. Pe prima linie n, apoi comenzi <code>in x</code> / <code>out</code>. La <code>out</code> afișează elementul scos sau <code>vida</code>.",
          "class Coada:\n    def __init__(self):\n        self.a, self.b = [], []\n    def adauga(self, x):\n        self.a.append(x)\n    def scoate(self):\n        if not self.b:\n            while self.a:\n                self.b.append(self.a.pop())\n        return self.b.pop() if self.b else None\n\nq = Coada()\nfor _ in range(int(input())):\n    c = input().split()\n    if c[0] == 'in':\n        q.adauga(int(c[1]))\n    else:\n        r = q.scoate()\n        print('vida' if r is None else r)",
          "7\nin 1\nin 2\nout\nin 3\nout\nout\nout", "1\nout"),
        P("Biblioteca", "dificil", "Clasele <code>Carte</code> (titlu, disponibilă) și <code>Biblioteca</code> (dicționar titlu → Carte) cu metodele <code>adauga</code>, <code>imprumuta</code>, <code>returneaza</code>, <code>disponibile</code>. Pe prima linie n, apoi comenzi: <code>add titlu</code>, <code>borrow titlu</code> (afișează <code>ok</code>, <code>indisponibila</code> sau <code>inexistenta</code>), <code>return titlu</code> (<code>ok</code> sau <code>eroare</code> dacă nu era împrumutată/nu există), <code>list</code> (titlurile disponibile, alfabetic, pe o linie, sau <code>-</code>).",
          "class Carte:\n    def __init__(self, titlu):\n        self.titlu = titlu\n        self.disponibila = True\n\nclass Biblioteca:\n    def __init__(self):\n        self.carti = {}\n    def adauga(self, t):\n        self.carti.setdefault(t, Carte(t))\n    def imprumuta(self, t):\n        if t not in self.carti:\n            return 'inexistenta'\n        c = self.carti[t]\n        if not c.disponibila:\n            return 'indisponibila'\n        c.disponibila = False\n        return 'ok'\n    def returneaza(self, t):\n        c = self.carti.get(t)\n        if c is None or c.disponibila:\n            return 'eroare'\n        c.disponibila = True\n        return 'ok'\n    def disponibile(self):\n        return sorted(t for t, c in self.carti.items() if c.disponibila)\n\nb = Biblioteca()\nfor _ in range(int(input())):\n    cmd, *rest = input().split()\n    if cmd == 'add':\n        b.adauga(rest[0])\n    elif cmd == 'borrow':\n        print(b.imprumuta(rest[0]))\n    elif cmd == 'return':\n        print(b.returneaza(rest[0]))\n    else:\n        print(*b.disponibile() or ['-'])",
          "9\nadd Ion\nadd Enigma\nborrow Ion\nborrow Ion\nlist\nreturn Ion\nreturn Ion\nborrow Baltagul\nlist", "2\nlist\nreturn X"),
        P("Figuri geometrice", "dificil", "Clasa de bază <code>Figura</code> are metodele <code>arie()</code> și <code>perimetru()</code>; clasele derivate: <code>Cerc(r)</code>, <code>Dreptunghi(a, b)</code>, <code>Triunghi(a, b, c)</code> (arie cu formula lui Heron). Pe prima linie n, apoi linii <code>C r</code>, <code>D a b</code> sau <code>T a b c</code>. Afișează figurile în ordinea descrescătoare a ariei, câte una pe linie: <code>tip arie perimetru</code> (2 zecimale; tip = litera de intrare; π = math.pi; la arii egale, ordinea de intrare).",
          "import math\nclass Figura:\n    tip = '?'\n    def arie(self): return 0\n    def perimetru(self): return 0\nclass Cerc(Figura):\n    tip = 'C'\n    def __init__(self, r): self.r = r\n    def arie(self): return math.pi * self.r ** 2\n    def perimetru(self): return 2 * math.pi * self.r\nclass Dreptunghi(Figura):\n    tip = 'D'\n    def __init__(self, a, b): self.a, self.b = a, b\n    def arie(self): return self.a * self.b\n    def perimetru(self): return 2 * (self.a + self.b)\nclass Triunghi(Figura):\n    tip = 'T'\n    def __init__(self, a, b, c): self.a, self.b, self.c = a, b, c\n    def perimetru(self): return self.a + self.b + self.c\n    def arie(self):\n        p = self.perimetru() / 2\n        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))\nf = []\nfor _ in range(int(input())):\n    t, *x = input().split()\n    x = list(map(float, x))\n    f.append(Cerc(*x) if t == 'C' else Dreptunghi(*x) if t == 'D' else Triunghi(*x))\nfor o in sorted(f, key=lambda o: -o.arie()):\n    print(o.tip, f'{o.arie():.2f}', f'{o.perimetru():.2f}')",
          "3\nC 1\nD 2 3\nT 3 4 5", "1\nD 1 1"),
    ],
))
