from util import C, O, T

LECTII = []

# ------------------------------------------------------------------ 7
LECTII.append(dict(
    id="l7", nr="7", scurt="Liste (list)", titlu="Liste – clasa list",
    programa="Programa 5.A: clasa list – acces, apartenență, concatenare, multiplicare, relaționare; index, count, pop, insert, append, copy, sort; capitolul 1: modelul liniar",
    obiective=["crearea și citirea listelor", "operatorii și metodele cerute de programă", "diferența dintre sort() și sorted(), dintre copiere și atribuire",
               "lista ca stivă și coada cu deque", "lista de frecvențe"],
    teorie=f"""
{C('''v = [5, 3, 8]
v.append(1)          # [5, 3, 8, 1]       adaugă la final
v.insert(0, 9)       # [9, 5, 3, 8, 1]    inserează pe poziția 0
x = v.pop()          # x = 1, v = [9, 5, 3, 8]   extrage ultimul
y = v.pop(1)         # y = 5, v = [9, 3, 8]      extrage de pe poziția 1
v.remove(8)          # șterge prima apariție a valorii 8 → [9, 3]
del v[0]             # șterge elementul de pe poziția 0 → [3]''')}
{T(["Operator / metodă", "Ce face", "Exemplu"],
   ["<code>v[i]</code>, <code>v[a:b]</code>", "acces / subliste (ca la șiruri, dar listele sunt <strong>mutabile</strong>)", "<code>v[0] = 7</code>; <code>v[1:3] = []</code>"],
   ["<code>in</code>, <code>not in</code>", "apartenență", "<code>3 in [1, 3]</code> → True"],
   ["<code>+</code>, <code>*</code>", "concatenare, multiplicare (liste noi)", "<code>[0] * 5</code> → [0, 0, 0, 0, 0]"],
   ["<code>==</code>, <code>&lt;</code> …", "comparare element cu element (lexicografic)", "<code>[1, 2] &lt; [1, 3]</code> → True"],
   ["<code>index(x)</code>", "prima poziție a lui x (<code>ValueError</code> dacă lipsește)", "<code>[4, 7, 4].index(4)</code> → 0"],
   ["<code>count(x)</code>", "de câte ori apare x", ""],
   ["<code>copy()</code>", "copie (superficială)", "<code>w = v.copy()</code> sau <code>v[:]</code>"],
   ["<code>sort()</code> / <code>sorted(v)</code>", "sortează lista pe loc (întoarce None) / întoarce o listă nouă", "<code>v.sort(reverse=True)</code>; <code>sorted(v, key=len)</code>"],
   ["<code>len, sum, min, max</code>", "funcții predefinite", "<code>sum(v) / len(v)</code>"],
   ["<code>reverse()</code>, <code>extend(w)</code>", "inversare pe loc; adăugarea tuturor elementelor lui w", ""])}
<div class="note warn"><b>Capcane:</b> <code>v = v.sort()</code> face v = None. <code>w = v</code> nu copiază – ambele nume indică aceeași listă. Ștergerea elementelor în timp ce parcurgi lista cu <code>for x in v</code> sare peste elemente – construiește o listă nouă: <code>v = [x for x in v if x % 2 == 0]</code>.</div>
<h3>Liste ca structuri de date (capitolul 1)</h3>
{C('''stiva = []
stiva.append(1); stiva.append(2); stiva.append(3)
print(stiva.pop())          # 3 – LIFO

from collections import deque
coada = deque([1, 2, 3])
coada.append(4)
print(coada.popleft())      # 1 – FIFO, în O(1) (list.pop(0) este O(n))

v = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
f = [0] * 10                # lista de frecvențe pentru valori 0..9
for x in v:
    f[x] += 1
print([x for x in range(10) for _ in range(f[x])])   # sortare prin numărare''')}
{O("3\n1\n[1, 1, 2, 3, 3, 4, 5, 5, 6, 9]")}
<h3>Comprehensiuni de liste</h3>
{C('''patrate = [i * i for i in range(1, 6)]            # [1, 4, 9, 16, 25]
pare = [x for x in v if x % 2 == 0]               # filtrare
v = [int(x) for x in input().split()]             # echivalent cu list(map(int, ...))''')}
""",
    rezolvate=[
        dict(titlu="Eliminarea dublurilor păstrând ordinea", enunt="Se citește o listă de numere. Afișează valorile distincte, în ordinea primei apariții.",
             cod='v = list(map(int, input().split()))\nrez = []\nfor x in v:\n    if x not in rez:\n        rez.append(x)\nprint(*rez)', intrare="3 1 3 2 1 5",
             explicatie="Testul <code>x not in rez</code> parcurge lista: complexitate O(n²). Pentru liste mari se folosește în plus o mulțime cu valorile deja văzute (lecția 8)."),
        dict(titlu="Rotire circulară", enunt="Rotește lista cu k poziții spre dreapta.",
             cod='v = list(map(int, input().split()))\nk = int(input())\nk %= len(v)\nv = v[-k:] + v[:-k] if k else v\nprint(*v)', intrare="1 2 3 4 5\n2"),
    ],
    exercitii=[
        dict(titlu="Inversare și sumă pe poziții pare", nivel="ușor", enunt="Pe o linie se dau numere întregi. Afișează lista în ordine inversă, apoi suma elementelor de pe pozițiile pare (0, 2, 4, …).",
             sol="v = list(map(int, input().split()))\nprint(*v[::-1])\nprint(sum(v[::2]))", teste=[{"in": "1 2 3 4 5"}, {"in": "7"}, {"in": "-1 -2 -3 -4"}]),
        dict(titlu="Pozițiile maximului", nivel="ușor", enunt="Pe o linie se dau numere întregi. Afișează toate pozițiile (de la 0) pe care apare valoarea maximă.",
             sol="v = list(map(int, input().split()))\nm = max(v)\nprint(*[i for i, x in enumerate(v) if x == m])", teste=[{"in": "3 9 2 9 1"}, {"in": "5"}, {"in": "-4 -4 -9"}]),
        dict(titlu="Interclasare", nivel="mediu", enunt="Se dau două liste sortate crescător, pe două linii. Afișează lista sortată obținută prin interclasarea lor, <strong>fără</strong> sort/sorted.",
             sol="a = list(map(int, input().split()))\nb = list(map(int, input().split()))\ni = j = 0\nc = []\nwhile i < len(a) and j < len(b):\n    if a[i] <= b[j]:\n        c.append(a[i]); i += 1\n    else:\n        c.append(b[j]); j += 1\nc += a[i:] + b[j:]\nprint(*c)",
             teste=[{"in": "1 4 9\n2 3 10 11"}, {"in": "5\n1 2 3"}, {"in": "1 1 1\n1 1"}]),
        dict(titlu="Sortare prin selecție", nivel="mediu", enunt="Pe o linie se dau numere întregi. Sortează-le crescător prin metoda selecției minimului și afișează lista <strong>după fiecare pas</strong> (n − 1 linii).",
             sol="v = list(map(int, input().split()))\nn = len(v)\nfor i in range(n - 1):\n    m = i\n    for j in range(i + 1, n):\n        if v[j] < v[m]:\n            m = j\n    v[i], v[m] = v[m], v[i]\n    print(*v)",
             teste=[{"in": "5 2 9 1 7"}, {"in": "3 2 1"}, {"in": "1 2"}]),
        dict(titlu="Simulare stivă", nivel="mediu", enunt="Pe prima linie n, apoi n comenzi: <code>push x</code> sau <code>pop</code>. La fiecare <code>pop</code> afișează valoarea extrasă sau <code>gol</code> dacă stiva este goală. La final afișează conținutul stivei de la bază la vârf (sau <code>vida</code>).",
             sol='n = int(input())\ns = []\nfor _ in range(n):\n    c = input().split()\n    if c[0] == "push":\n        s.append(int(c[1]))\n    elif s:\n        print(s.pop())\n    else:\n        print("gol")\nprint(*s if s else ["vida"])',
             teste=[{"in": "6\npush 1\npush 2\npop\npush 3\npop\npop"}, {"in": "3\npop\npush 5\npush 6"}, {"in": "1\npush 4"}]),
    ],
    quiz=[("Ce valoare are v după <code>v = [3, 1, 2]; v = v.sort()</code>?", ["[1, 2, 3]", "[3, 1, 2]", "None", "eroare"], 2, "sort() sortează pe loc și întoarce None."),
          ("Ce afișează <code>a = [1]; b = a; b.append(2); print(a)</code>?", ["[1]", "[1, 2]", "[2]", "eroare"], 1, "a și b sunt același obiect."),
          ("Ce metodă inserează valoarea 7 pe poziția 2?", ["v.append(2, 7)", "v.insert(2, 7)", "v.insert(7, 2)", "v[2] = 7"], 1, "insert(poziție, valoare); atribuirea v[2] = 7 înlocuiește."),
          ("Ce returnează <code>[1, 2, 3].pop(0)</code>?", ["[2, 3]", "1", "3", "None"], 1, "Elementul extras.")],
))

# ------------------------------------------------------------------ 8
LECTII.append(dict(
    id="l8", nr="8", scurt="Tupluri, mulțimi, dicționare", titlu="Tupluri, mulțimi și dicționare",
    programa="Programa 5.A: clasele tuple, set, dict; capitolul 1: modelul neliniar (mulțime) și modelul asociativ (dicționar)",
    obiective=["tuplul: secvență imutabilă, despachetare", "mulțimea: elemente distincte, operații de mulțimi", "dicționarul: perechi cheie–valoare, frecvențe",
               "cum alegi structura potrivită unei probleme"],
    teorie=f"""
{T(["", "tuple", "set", "dict"],
   ["Scriere", "<code>(1, 2)</code>, <code>(5,)</code>, <code>()</code>", "<code>{{1, 2}}</code>, <code>set()</code> (nu <code>{{}}</code>!)", "<code>{{\"ana\": 9}}</code>, <code>{{}}</code>, <code>dict()</code>"],
   ["Ordine / indici", "da / da", "nu / nu", "păstrează ordinea inserării / acces prin cheie"],
   ["Duplicate", "permise", "eliminate automat", "cheile sunt unice"],
   ["Mutabil", "nu", "da", "da (cheile trebuie să fie imutabile)"],
   ["Test <code>in</code>", "O(n)", "O(1) în medie", "O(1) în medie, după cheie"])}
<h3>Tupluri</h3>
{C('''p = (3, 4)
x, y = p                     # despachetare
t = (1, 2, 3, 2)
print(t[1], t.count(2), t.index(3), t + (4,), 2 in t)
def min_max(v):
    return min(v), max(v)    # o funcție poate întoarce un tuplu
mn, mx = min_max([4, 1, 7])''')}
{O("2 2 2 (1, 2, 3, 2, 4) True")}
<h3>Mulțimi</h3>
{C('''A = {1, 2, 3, 4}; B = {3, 4, 5}
print(A | B, A & B, A - B, A ^ B)     # reuniune, intersecție, diferență, dif. simetrică
print({3, 4} <= A, A == {4, 3, 2, 1})  # incluziune, egalitate (ordinea nu contează)
A.add(9); A.discard(1); A.remove(2)   # remove dă KeyError dacă elementul lipsește
print(len(set("mississippi")))        # 4 litere distincte''')}
{O("{1, 2, 3, 4, 5} {3, 4} {1, 2} {1, 2, 5} True True 4")}
<h3>Dicționare</h3>
{C('''note = {"Ana": 9, "Dan": 7}
note["Ioana"] = 10          # adăugare
note["Dan"] += 1            # modificare
print(note["Ana"], note.get("Mihai", 0), "Dan" in note)
for nume, nota in note.items():
    print(nume, nota)
# frecvența cuvintelor
frecv = {}
for w in "a b a c b a".split():
    frecv[w] = frecv.get(w, 0) + 1
print(frecv)
print(sorted(frecv, key=frecv.get, reverse=True))   # cheile după frecvență''')}
{O("9 0 True\nAna 9\nDan 8\nIoana 10\n{'a': 3, 'b': 2, 'c': 1}\n['a', 'b', 'c']")}
<div class="note"><b>Cum alegi:</b> listă – ordine și poziții; tuplu – grup fix de valori (coordonate, înregistrări); mulțime – „a mai apărut?”, valori distincte, operații de mulțimi; dicționar – asocieri (nume → notă, cuvânt → frecvență).</div>
""",
    rezolvate=[
        dict(titlu="Elevi comuni la două cercuri", enunt="Se dau numele elevilor de la cercul de informatică și de la cel de robotică (câte o linie). Afișează, sortați alfabetic, elevii care sunt la ambele, apoi pe cei care sunt doar la informatică.",
             cod='info = set(input().split())\nrob = set(input().split())\nprint(*sorted(info & rob))\nprint(*sorted(info - rob))', intrare="Ana Dan Ioana Radu\nDan Maria Radu"),
        dict(titlu="Agenda de telefon", enunt="Se citesc n perechi nume telefon, apoi un nume căutat.",
             cod='n = int(input())\nagenda = {}\nfor _ in range(n):\n    nume, tel = input().split()\n    agenda[nume] = tel\ncautat = input()\nprint(agenda.get(cautat, "necunoscut"))', intrare="2\nAna 0722111222\nDan 0744333444\nDan"),
    ],
    exercitii=[
        dict(titlu="Valori distincte", nivel="ușor", enunt="Pe o linie se dau numere întregi. Afișează câte valori distincte sunt, apoi valorile distincte în ordine crescătoare.",
             sol="v = list(map(int, input().split()))\nd = sorted(set(v))\nprint(len(d))\nprint(*d)", teste=[{"in": "3 1 3 2 1 5"}, {"in": "7 7 7"}, {"in": "-1 0 1"}]),
        dict(titlu="Frecvența literelor", nivel="mediu", enunt="Se citește un cuvânt cu litere mici. Afișează, în ordine alfabetică, fiecare literă și de câte ori apare, câte o pereche pe linie (<code>a 3</code>).",
             sol="s = input()\nf = {}\nfor c in s:\n    f[c] = f.get(c, 0) + 1\nfor c in sorted(f):\n    print(c, f[c])", teste=[{"in": "banana"}, {"in": "z"}, {"in": "mississippi"}]),
        dict(titlu="Cuvântul cel mai frecvent", nivel="mediu", enunt="Se citește un text cu cuvinte separate prin spații. Afișează cuvântul care apare de cele mai multe ori și numărul de apariții; la egalitate, cel mai mic alfabetic. Nu se face diferență între litere mari și mici (afișează cu litere mici).",
             sol="f = {}\nfor w in input().lower().split():\n    f[w] = f.get(w, 0) + 1\nbest = min(f, key=lambda w: (-f[w], w))\nprint(best, f[best])",
             teste=[{"in": "Ana are mere ana are pere ANA"}, {"in": "b a"}, {"in": "unu doi unu doi trei"}]),
        dict(titlu="Perechi cu suma dată", nivel="dificil", enunt="Pe prima linie numere întregi <strong>distincte</strong>, pe a doua un număr S. Afișează câte perechi de elemente (neordonate) au suma S. Folosește o mulțime pentru o soluție într-o singură parcurgere.",
             sol="v = list(map(int, input().split()))\nS = int(input())\nvazute = set()\ncnt = 0\nfor x in v:\n    if S - x in vazute:\n        cnt += 1\n    vazute.add(x)\nprint(cnt)",
             teste=[{"in": "1 5 7 -1 3 4\n6"}, {"in": "1 2 3\n100"}, {"in": "10 -10 0 20 -20\n0"}]),
        dict(titlu="Tuplul cel mai mic", nivel="mediu", enunt="Pe prima linie n, apoi n linii cu <code>nume varsta</code>. Afișează numele celui mai tânăr elev; la vârste egale, primul alfabetic. (Indiciu: tuplurile se compară lexicografic.)",
             sol="n = int(input())\nelevi = []\nfor _ in range(n):\n    nume, v = input().split()\n    elevi.append((int(v), nume))\nprint(min(elevi)[1])",
             teste=[{"in": "3\nDan 15\nAna 14\nRadu 16"}, {"in": "3\nMaria 14\nIoana 14\nDan 15"}, {"in": "1\nX 10"}]),
    ],
    quiz=[("Ce tip are <code>x = {}</code>?", ["set", "dict", "tuple", "list"], 1, "Mulțimea vidă se scrie set()."),
          ("Ce afișează <code>print({1, 2} == {2, 1})</code>?", ["True", "False", "eroare", "None"], 0, "La mulțimi ordinea nu contează."),
          ("Ce întoarce <code>d.get(\"x\", 0)</code> dacă cheia lipsește?", ["KeyError", "None", "0", "\"x\""], 2, "Valoarea implicită dată."),
          ("Care poate fi cheie de dicționar?", ["[1, 2]", "{1, 2}", "(1, 2)", "{\"a\": 1}"], 2, "Cheile trebuie să fie imutabile (hashable).")],
))

# ------------------------------------------------------------------ 9
LECTII.append(dict(
    id="l9", nr="9", scurt="Funcții, recursivitate, module", titlu="Funcții (subprograme), recursivitate și module",
    programa="Programa 5.A: subprograme, subprograme recursive; capitolul 4: Divide et impera, Backtracking",
    obiective=["definirea și apelul funcțiilor, parametri cu valori implicite, return multiplu", "variabile locale și globale",
               "ce se întâmplă cu listele transmise ca parametri", "recursivitatea: condiția de oprire, urmărirea apelurilor", "module: math, random"],
    teorie=f"""
{C('''def suma_cifre(n):
    """Întoarce suma cifrelor numărului natural n."""   # docstring
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

def salut(nume, mesaj="Bun venit"):     # parametru cu valoare implicită
    print(f"{mesaj}, {nume}!")

print(suma_cifre(2026))   # 10
salut("Ana")              # Bun venit, Ana!
salut("Dan", mesaj="Salut")''')}
<ul>
<li>O funcție fără <code>return</code> (sau cu <code>return</code> simplu) întoarce <code>None</code>. <code>return a, b</code> întoarce un tuplu.</li>
<li>Variabilele create în funcție sunt <strong>locale</strong>. Pentru a modifica o variabilă globală se declară <code>global x</code> (de evitat; mai bine se transmit parametri și se întoarce rezultatul).</li>
<li><strong>Transmiterea parametrilor</strong>: funcția primește referințe la obiecte. Un obiect <em>imutabil</em> (int, str, tuple) nu poate fi modificat din funcție; un obiect <em>mutabil</em> (listă, dicționar) modificat prin metode (<code>append</code>, <code>v[i] = …</code>) rămâne modificat și în apelant.</li>
</ul>
{C('''def f(x, v):
    x += 1           # x local devine alt obiect; variabila din apelant nu se schimbă
    v.append(x)      # lista este aceeași – modificarea se vede afară

a, L = 5, [1]
f(a, L)
print(a, L)''')}
{O("5 [1, 6]")}
<h3>Recursivitate</h3>
<p>O funcție recursivă se apelează pe ea însăși pentru o problemă mai mică. Obligatoriu: <strong>condiția de oprire</strong> (cazul de bază), altfel apare <code>RecursionError</code> (Python limitează adâncimea la aproximativ 1000 de apeluri).</p>
{C('''def fact(n):
    if n <= 1:                      # cazul de bază
        return 1
    return n * fact(n - 1)          # apel pentru o problemă mai mică

def cmmdc(a, b):
    return a if b == 0 else cmmdc(b, a % b)

def afis(n):                        # ce se afișează înainte / după apel
    if n == 0:
        return
    print(n, end=" ")
    afis(n - 1)
    print(n, end=" ")

print(fact(5), cmmdc(84, 36)); afis(3)''')}
{O("120 12\n3 2 1 1 2 3")}
<h3>Backtracking recursiv (capitolul 4)</h3>
{C('''def permutari(n):
    x, folosit = [], [False] * (n + 1)
    def bt():
        if len(x) == n:
            print(*x)
            return
        for v in range(1, n + 1):
            if not folosit[v]:
                folosit[v] = True; x.append(v)
                bt()
                x.pop(); folosit[v] = False      # revenirea (back)
    bt()

permutari(3)''')}
{O("1 2 3\n1 3 2\n2 1 3\n2 3 1\n3 1 2\n3 2 1")}
<h3>Module</h3>
{C('''import math
from random import randint, choice, shuffle, seed
print(math.sqrt(16), math.gcd(12, 18), math.pi, math.floor(2.7), math.ceil(2.1))
seed(1)                   # aceeași secvență „aleatoare” la fiecare rulare
zar = randint(1, 6)       # întreg între 1 și 6, inclusiv capetele''')}
<p>Un fișier propriu <code>utile.py</code> cu funcții devine modul: <code>import utile</code> și apoi <code>utile.suma_cifre(…)</code>. Blocul <code>if __name__ == "__main__":</code> rulează doar când fișierul este executat direct, nu când este importat.</p>
""",
    rezolvate=[
        dict(titlu="Funcție pentru numere prime", enunt="Afișează numerele prime dintr-un interval [a, b], folosind o funcție.",
             cod='def prim(n):\n    if n < 2:\n        return False\n    d = 2\n    while d * d <= n:\n        if n % d == 0:\n            return False\n        d += 1\n    return True\n\na, b = map(int, input().split())\nprint(*[x for x in range(a, b + 1) if prim(x)])', intrare="10 40"),
        dict(titlu="Căutare binară recursivă (Divide et impera)", enunt="Caută x într-o listă sortată; întoarce poziția sau −1.",
             cod='def cauta(v, x, st, dr):\n    if st > dr:\n        return -1\n    m = (st + dr) // 2\n    if v[m] == x:\n        return m\n    if v[m] < x:\n        return cauta(v, x, m + 1, dr)\n    return cauta(v, x, st, m - 1)\n\nv = [2, 5, 8, 12, 16, 23, 38]\nprint(cauta(v, 23, 0, len(v) - 1), cauta(v, 7, 0, len(v) - 1))'),
    ],
    exercitii=[
        dict(titlu="Funcția oglindit", nivel="ușor", enunt="Scrie funcția <code>oglindit(n)</code> și folosește-o: se citesc numere naturale pe o linie; afișează câte dintre ele sunt palindroame.",
             start="def oglindit(n):\n    # completează\n    pass\n\nv = list(map(int, input().split()))\n",
             sol="def oglindit(n):\n    r = 0\n    while n > 0:\n        r = r * 10 + n % 10\n        n //= 10\n    return r\n\nv = list(map(int, input().split()))\nprint(sum(1 for x in v if oglindit(x) == x))",
             teste=[{"in": "121 12 7 4554 100"}, {"in": "10 20"}, {"in": "0 11"}]),
        dict(titlu="Puterea recursivă", nivel="mediu", enunt="Scrie o funcție <strong>recursivă</strong> <code>putere(a, n)</code> care calculează a<sup>n</sup> prin exponențiere rapidă (a<sup>n</sup> = (a<sup>n/2</sup>)² pentru n par). Se citesc a și n; afișează rezultatul modulo 1 000 000 007.",
             sol="def putere(a, n, m):\n    if n == 0:\n        return 1\n    p = putere(a, n // 2, m)\n    p = p * p % m\n    if n % 2 == 1:\n        p = p * a % m\n    return p\n\na, n = map(int, input().split())\nprint(putere(a, n, 1000000007))",
             teste=[{"in": "2 10"}, {"in": "3 0"}, {"in": "7 1000000000000"}, {"in": "123456789 987654321"}]),
        dict(titlu="Fibonacci cu memoizare", nivel="mediu", enunt="Se citește n (0 ≤ n ≤ 90). Afișează F(n), cu F(0) = 0, F(1) = 1. Varianta recursivă naivă este prea lentă pentru n = 90 – folosește un dicționar ca memorie sau o soluție iterativă.",
             sol="memo = {0: 0, 1: 1}\ndef fib(n):\n    if n not in memo:\n        memo[n] = fib(n - 1) + fib(n - 2)\n    return memo[n]\n\nprint(fib(int(input())))",
             teste=[{"in": "10"}, {"in": "0"}, {"in": "1"}, {"in": "90"}]),
        dict(titlu="Submulțimi (backtracking)", nivel="dificil", enunt="Se citește n (1 ≤ n ≤ 10). Afișează toate submulțimile <strong>nevide</strong> ale mulțimii {1, …, n}, câte una pe linie, în ordine lexicografică (ex. pentru n = 3: 1 / 1 2 / 1 2 3 / 1 3 / 2 / 2 3 / 3).",
             sol="n = int(input())\nx = []\ndef bt(start):\n    for v in range(start, n + 1):\n        x.append(v)\n        print(*x)\n        bt(v + 1)\n        x.pop()\nbt(1)",
             teste=[{"in": "3"}, {"in": "1"}, {"in": "4"}]),
        dict(titlu="Lista modificată de funcție", nivel="mediu", enunt="Scrie funcția <code>dubleaza(v)</code> care înlocuiește <strong>în lista primită</strong> fiecare element cu dublul lui și nu întoarce nimic. Programul citește lista, apelează funcția și afișează lista.",
             start="def dubleaza(v):\n    pass\n\nv = list(map(int, input().split()))\ndubleaza(v)\nprint(*v)\n",
             sol="def dubleaza(v):\n    for i in range(len(v)):\n        v[i] *= 2\n\nv = list(map(int, input().split()))\ndubleaza(v)\nprint(*v)",
             teste=[{"in": "1 2 3"}, {"in": "-5"}, {"in": "0 10 100"}]),
    ],
    quiz=[("Ce întoarce o funcție care nu are instrucțiunea return?", ["0", "None", "False", "eroare"], 1, "Implicit None."),
          ("Ce afișează <code>def f(x): x = 10</code> apoi <code>a = 1; f(a); print(a)</code>?", ["10", "1", "None", "eroare"], 1, "Atribuirea leagă numele local x de alt obiect."),
          ("Ce eroare apare la o recursivitate fără condiție de oprire?", ["ZeroDivisionError", "RecursionError", "SyntaxError", "ValueError"], 1, "Se depășește adâncimea maximă a recursivității."),
          ("Ce face <code>random.seed(5)</code>?", ["generează 5 numere", "fixează punctul de pornire al generatorului", "întoarce un număr între 0 și 5", "amestecă o listă"], 1, "Aceeași sămânță ⇒ aceeași secvență.")],
))

# ------------------------------------------------------------------ 10
LECTII.append(dict(
    id="l10", nr="10", scurt="Fișiere text", titlu="Fișiere text",
    programa="Programa 5.A: fișiere text – funcția open, metode ale clasei TextIOWrapper: citire, scriere, închidere",
    obiective=["deschiderea cu open() și modurile r, w, a", "read, readline, readlines și parcurgerea linie cu linie", "write și închiderea (with)",
               "citirea numerelor dintr-un fișier, indiferent de cum sunt așezate pe linii"],
    teorie=f"""
{T(["Mod", "Efect"],
   ["<code>\"r\"</code> (implicit)", "citire; <code>FileNotFoundError</code> dacă fișierul nu există"],
   ["<code>\"w\"</code>", "scriere; creează fișierul sau îl <strong>golește</strong> dacă există"],
   ["<code>\"a\"</code>", "adăugare la final"],
   ["<code>encoding=\"utf-8\"</code>", "recomandat pentru texte cu diacritice"])}
{C('''f = open("date.in")           # obiect de tip TextIOWrapper
n = int(f.readline())         # o linie (inclusiv '\\n'; int() ignoră spațiile)
v = list(map(int, f.readline().split()))
f.close()                     # obligatoriu fără with

with open("date.out", "w") as g:      # with închide automat fișierul
    g.write(str(max(v)) + "\\n")       # write primește DOAR str și nu adaugă linie nouă
    print(*sorted(v), file=g)         # alternativă comodă: print în fișier''')}
{T(["Metodă", "Întoarce"],
   ["<code>f.read()</code>", "tot conținutul, ca un singur șir"],
   ["<code>f.readline()</code>", "linia următoare (cu <code>\\n</code>); <code>\"\"</code> la sfârșitul fișierului"],
   ["<code>f.readlines()</code>", "lista tuturor liniilor"],
   ["<code>for linie in f:</code>", "parcurgere linie cu linie (eficient pentru fișiere mari)"],
   ["<code>f.write(s)</code>", "scrie șirul s; întoarce numărul de caractere"])}
<div class="note"><b>Trucul pentru date „împrăștiate”:</b> când numerele pot fi pe oricâte linii, citește tot și împarte după spații albe: <code>date = list(map(int, open("date.in").read().split()))</code>. <code>split()</code> fără argument tratează spațiile, tab-urile și liniile noi la fel.</div>
""",
    rezolvate=[
        dict(titlu="Statistici dintr-un fișier", enunt="Fișierul <code>numere.txt</code> conține numere întregi, pe mai multe linii. Scrie în <code>statistici.txt</code> câte numere sunt, suma și media cu două zecimale.",
             fisiere={"numere.txt": "4 8\n15\n16 23 42\n"},
             cod='with open("numere.txt") as f:\n    v = list(map(int, f.read().split()))\nwith open("statistici.txt", "w") as g:\n    g.write(f"{len(v)}\\n{sum(v)}\\n{sum(v) / len(v):.2f}\\n")'),
        dict(titlu="Numărarea liniilor și a cuvintelor", enunt="Afișează numărul de linii nevide și numărul de cuvinte din <code>text.txt</code>.",
             fisiere={"text.txt": "Ana are mere.\n\nDan are pere si prune.\n"},
             cod='linii = cuvinte = 0\nwith open("text.txt", encoding="utf-8") as f:\n    for linie in f:\n        if linie.strip():\n            linii += 1\n            cuvinte += len(linie.split())\nprint(linii, cuvinte)'),
    ],
    exercitii=[
        dict(titlu="Maximul din fișier", nivel="ușor", enunt="Fișierul <code>date.in</code> conține pe prima linie n, iar pe a doua n numere întregi. Scrie în <code>date.out</code> valoarea maximă.",
             fisier_iesire="date.out",
             sol='with open("date.in") as f:\n    n = int(f.readline())\n    v = list(map(int, f.readline().split()))\nwith open("date.out", "w") as g:\n    g.write(str(max(v)) + "\\n")',
             teste=[{"fisiere": {"date.in": "5\n3 8 1 9 4\n"}}, {"fisiere": {"date.in": "3\n-5 -2 -9\n"}}, {"fisiere": {"date.in": "1\n7\n"}}]),
        dict(titlu="Sortare din fișier în fișier", nivel="mediu", enunt="Fișierul <code>numere.in</code> conține numere întregi, așezate pe oricâte linii. Scrie în <code>numere.out</code> numerele sortate crescător, pe o singură linie, separate prin spațiu.",
             fisier_iesire="numere.out",
             sol='with open("numere.in") as f:\n    v = sorted(map(int, f.read().split()))\nwith open("numere.out", "w") as g:\n    print(*v, file=g)',
             teste=[{"fisiere": {"numere.in": "5 3\n9\n1 7\n"}}, {"fisiere": {"numere.in": "42\n"}}, {"fisiere": {"numere.in": "3 -1 2 -1\n\n0\n"}}]),
        dict(titlu="Catalog", nivel="mediu", enunt="Fiecare linie din <code>note.txt</code> conține un nume și notele elevului (ex. <code>Ana 9 10</code>). Afișează pe ecran, pentru fiecare elev, numele și media cu două zecimale, apoi pe ultima linie numele elevului cu media maximă (primul, la egalitate).",
             sol='elevi = []\nwith open("note.txt") as f:\n    for linie in f:\n        p = linie.split()\n        if p:\n            note = list(map(int, p[1:]))\n            elevi.append((p[0], sum(note) / len(note)))\nfor nume, m in elevi:\n    print(nume, f"{m:.2f}")\nprint(max(elevi, key=lambda e: e[1])[0])',
             teste=[{"fisiere": {"note.txt": "Ana 9 10\nDan 7 8 6\nIoana 10 9 9 10\n"}}, {"fisiere": {"note.txt": "X 5\n"}}, {"fisiere": {"note.txt": "A 8 10\nB 9 9\n\n"}}]),
        dict(titlu="Linii cu un cuvânt", nivel="mediu", enunt="Pe prima linie de la tastatură se citește un cuvânt. Scrie în <code>gasit.txt</code> numerele (de la 1) ale liniilor din <code>text.txt</code> care conțin cuvântul ca <em>cuvânt separat</em>, câte unul pe linie; dacă nu există, scrie <code>0</code>.",
             fisier_iesire="gasit.txt",
             sol='w = input()\nrez = []\nwith open("text.txt") as f:\n    for i, linie in enumerate(f, 1):\n        if w in linie.split():\n            rez.append(i)\nwith open("gasit.txt", "w") as g:\n    g.write("\\n".join(map(str, rez)) if rez else "0")\n    g.write("\\n")',
             teste=[{"in": "are", "fisiere": {"text.txt": "Ana are mere\nmerele sunt rosii\nDan are pere\nparere\n"}}, {"in": "x", "fisiere": {"text.txt": "a b\nc\n"}}]),
    ],
    quiz=[("Ce face <code>open(\"f.txt\", \"w\")</code> dacă fișierul există?", ["adaugă la final", "îl golește", "dă eroare", "îl citește"], 1, "Modul w suprascrie."),
          ("Ce întoarce <code>readline()</code> la sfârșitul fișierului?", ["None", "EOFError", "\"\" (șir vid)", "\"\\n\""], 2, "Șirul vid semnalează sfârșitul."),
          ("Ce este greșit în <code>g.write(5)</code>?", ["nimic", "write primește doar șiruri", "lipsește \\n", "trebuie print"], 1, "TypeError: argumentul trebuie să fie str."),
          ("Avantajul lui <code>with open(...) as f:</code> este:", ["citește mai repede", "închide automat fișierul", "creează fișierul", "permite doar citirea"], 1, "Fișierul se închide chiar și la eroare.")],
))

# ------------------------------------------------------------------ 11
LECTII.append(dict(
    id="l11", nr="11", scurt="Modele mixte și matrice", titlu="Date organizate în modele mixte: liste de liste, matrice, liste de înregistrări",
    programa="Programa 5.A: elemente de limbaj pentru operarea cu date organizate în modele mixte; capitolul 1: modelul mixt",
    obiective=["crearea corectă a unei matrice", "parcurgeri: pe linii, pe coloane, diagonale, vecini", "liste de tupluri/dicționare și sortarea cu key", "un mic Flood Fill pe matrice"],
    teorie=f"""
{C('''n, m = 3, 4
a = [[0] * m for _ in range(n)]        # CORECT: n liste distincte
gresit = [[0] * m] * n                 # GREȘIT: de n ori ACEEAȘI listă
gresit[0][0] = 5
print(gresit[1][0])                    # 5 !

# citirea unei matrice: n linii cu câte m numere
# a = [list(map(int, input().split())) for _ in range(n)]''')}
{O("5")}
<h3>Parcurgeri tipice (matrice pătratică n × n)</h3>
{C('''a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
n = len(a)
print([sum(linie) for linie in a])                      # sumele pe linii
print([sum(a[i][j] for i in range(n)) for j in range(n)])  # sumele pe coloane
print([a[i][i] for i in range(n)])                      # diagonala principală
print([a[i][n - 1 - i] for i in range(n)])              # diagonala secundară
print(list(map(list, zip(*a))))                         # transpusa
for linie in a:
    print(*linie)''')}
{O("[6, 15, 24]\n[12, 15, 18]\n[1, 5, 9]\n[3, 5, 7]\n[[1, 4, 7], [2, 5, 8], [3, 6, 9]]\n1 2 3\n4 5 6\n7 8 9")}
<p>Deasupra diagonalei principale: <code>i &lt; j</code>; sub ea: <code>i &gt; j</code>. Vecinii lui (i, j): <code>(i−1, j), (i+1, j), (i, j−1), (i, j+1)</code> – verifică mereu că indicii sunt în matrice.</p>
<h3>Liste de înregistrări</h3>
{C('''elevi = [("Ana", "9A", 9.5), ("Dan", "9B", 8.0), ("Ioana", "9A", 9.5)]
# sortare: medie descrescător, apoi nume crescător
for nume, clasa, medie in sorted(elevi, key=lambda e: (-e[2], e[0])):
    print(nume, medie)
# grupare pe clase cu un dicționar de liste
pe_clase = {}
for nume, clasa, medie in elevi:
    pe_clase.setdefault(clasa, []).append(nume)
print(pe_clase)''')}
{O("Ana 9.5\nIoana 9.5\nDan 8.0\n{'9A': ['Ana', 'Ioana'], '9B': ['Dan']}")}
""",
    rezolvate=[
        dict(titlu="Zone de apă (Flood Fill)", enunt="Într-o hartă, <code>#</code> este uscat și <code>.</code> este apă. Numără lacurile (zone de apă vecine pe orizontală/verticală).",
             cod='harta = ["#..##", "#..#.", "####.", ".#..."]\ng = [list(r) for r in harta]\nn, m = len(g), len(g[0])\nlacuri = 0\nfor i in range(n):\n    for j in range(m):\n        if g[i][j] == ".":\n            lacuri += 1\n            stiva = [(i, j)]\n            g[i][j] = "#"\n            while stiva:\n                x, y = stiva.pop()\n                for a, b in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):\n                    if 0 <= a < n and 0 <= b < m and g[a][b] == ".":\n                        g[a][b] = "#"\n                        stiva.append((a, b))\nprint(lacuri)',
             explicatie="Fiecare celulă de apă găsită pornește o umplere care marchează tot lacul; varianta cu stivă evită limita de recursivitate."),
    ],
    exercitii=[
        dict(titlu="Sumele pe linii și pe coloane", nivel="ușor", enunt="Pe prima linie n și m, apoi n linii cu câte m numere întregi. Afișează pe o linie sumele liniilor, iar pe următoarea sumele coloanelor.",
             sol="n, m = map(int, input().split())\na = [list(map(int, input().split())) for _ in range(n)]\nprint(*[sum(l) for l in a])\nprint(*[sum(a[i][j] for i in range(n)) for j in range(m)])",
             teste=[{"in": "2 3\n1 2 3\n4 5 6"}, {"in": "1 1\n7"}, {"in": "3 2\n-1 1\n0 0\n5 -5"}]),
        dict(titlu="Diagonale", nivel="mediu", enunt="Se citește n și o matrice pătratică n × n. Afișează suma elementelor de pe diagonala principală, suma celor de pe diagonala secundară și suma elementelor aflate strict deasupra diagonalei principale, pe linii separate.",
             sol="n = int(input())\na = [list(map(int, input().split())) for _ in range(n)]\nprint(sum(a[i][i] for i in range(n)))\nprint(sum(a[i][n - 1 - i] for i in range(n)))\nprint(sum(a[i][j] for i in range(n) for j in range(n) if i < j))",
             teste=[{"in": "3\n1 2 3\n4 5 6\n7 8 9"}, {"in": "1\n5"}, {"in": "2\n1 -2\n3 4"}]),
        dict(titlu="Clasament", nivel="mediu", enunt="Pe prima linie n, apoi n linii <code>nume punctaj</code>. Afișează clasamentul: punctaj descrescător, iar la egalitate nume crescător, în formatul <code>loc. nume punctaj</code>. Concurenții cu punctaj egal primesc același loc (ex.: 1, 2, 2, 4).",
             sol="n = int(input())\nv = []\nfor _ in range(n):\n    nume, p = input().split()\n    v.append((nume, int(p)))\nv.sort(key=lambda e: (-e[1], e[0]))\nfor i, (nume, p) in enumerate(v):\n    loc = i + 1 if i == 0 or p != v[i - 1][1] else loc\n    print(f\"{loc}. {nume} {p}\")",
             teste=[{"in": "4\nDan 80\nAna 95\nIon 80\nRadu 70"}, {"in": "1\nX 10"}, {"in": "3\nC 5\nB 5\nA 5"}]),
        dict(titlu="Spirală", nivel="dificil", enunt="Se citesc n, m și o matrice n × m. Afișează elementele parcurse în spirală, în sensul acelor de ceasornic, pornind din colțul stânga-sus, pe o singură linie.",
             sol="n, m = map(int, input().split())\na = [list(map(int, input().split())) for _ in range(n)]\nsus, jos, st, dr = 0, n - 1, 0, m - 1\nrez = []\nwhile sus <= jos and st <= dr:\n    for j in range(st, dr + 1):\n        rez.append(a[sus][j])\n    sus += 1\n    for i in range(sus, jos + 1):\n        rez.append(a[i][dr])\n    dr -= 1\n    if sus <= jos:\n        for j in range(dr, st - 1, -1):\n            rez.append(a[jos][j])\n        jos -= 1\n    if st <= dr:\n        for i in range(jos, sus - 1, -1):\n            rez.append(a[i][st])\n        st += 1\nprint(*rez)",
             teste=[{"in": "3 3\n1 2 3\n4 5 6\n7 8 9"}, {"in": "3 4\n1 2 3 4\n5 6 7 8\n9 10 11 12"}, {"in": "1 3\n1 2 3"}, {"in": "3 1\n1\n2\n3"}]),
    ],
    quiz=[("De ce este greșit <code>[[0] * 3] * 2</code> pentru o matrice?", ["dă eroare", "rândurile sunt aceeași listă", "creează 3 rânduri", "elementele sunt șiruri"], 1, "Modificarea unui rând le modifică pe toate."),
          ("Elementele de sub diagonala principală au:", ["i &lt; j", "i == j", "i &gt; j", "i + j == n − 1"], 2, "Linia mai mare decât coloana."),
          ("Ce sortare dă <code>sorted(v, key=lambda e: (-e[1], e[0]))</code>?", ["după e[1] crescător", "după e[1] descrescător, apoi e[0] crescător", "după e[0] descrescător", "nu sortează"], 1, "Cheia este un tuplu; minusul inversează ordinea numerică.")],
))

# ------------------------------------------------------------------ 12
LECTII.append(dict(
    id="l12", nr="12", scurt="Excepții și validare", titlu="Excepții și validarea datelor",
    programa="Programa capitolul 2: principii de elaborare a unui program, criterii de elaborare a testelor, comunicarea cu programul",
    obiective=["citirea mesajelor de eroare", "try / except / else / finally", "validarea datelor introduse de utilizator", "testarea cu assert"],
    teorie=f"""
{T(["Eroare", "Cauză tipică"],
   ["<code>SyntaxError</code>, <code>IndentationError</code>", "lipsește <code>:</code>, paranteză neînchisă, indentare greșită"],
   ["<code>NameError</code>", "variabilă nedefinită sau scrisă greșit"],
   ["<code>TypeError</code>", "operație între tipuri incompatibile: <code>\"a\" + 1</code>"],
   ["<code>ValueError</code>", "valoare nepotrivită: <code>int(\"12a\")</code>"],
   ["<code>IndexError</code>", "indice în afara listei: <code>v[len(v)]</code>"],
   ["<code>KeyError</code>", "cheie inexistentă în dicționar"],
   ["<code>ZeroDivisionError</code>", "împărțire la zero"],
   ["<code>FileNotFoundError</code>", "fișier inexistent"],
   ["<code>EOFError</code>", "<code>input()</code> când nu mai sunt date"])}
{C('''while True:
    try:
        n = int(input("Un număr natural: "))
        if n < 0:
            raise ValueError("negativ")     # semnalăm noi eroarea
    except ValueError:
        print("Valoare invalidă, încearcă din nou.")
    else:
        break                               # doar dacă nu a apărut nicio excepție
    finally:
        pass                                # se execută mereu (eliberare de resurse)''')}
<ul>
<li><code>except (ValueError, ZeroDivisionError) as e:</code> prinde mai multe tipuri; <code>e</code> conține mesajul.</li>
<li>Nu ascunde erorile cu <code>except:</code> gol – prinde doar ce știi să tratezi.</li>
<li><code>assert conditie, "mesaj"</code> oprește programul dacă o presupunere este falsă – folosit pentru teste: <code>assert suma_cifre(2026) == 10</code>.</li>
</ul>
""",
    rezolvate=[
        dict(titlu="Împărțire sigură", enunt="Citește două valori și afișează câtul, tratând textele invalide și împărțirea la zero.",
             cod='try:\n    a = float(input())\n    b = float(input())\n    print(a / b)\nexcept ValueError:\n    print("trebuie numere")\nexcept ZeroDivisionError:\n    print("impartire la zero")', intrare="7\n0"),
    ],
    exercitii=[
        dict(titlu="Suma valorilor valide", nivel="ușor", enunt="Pe o linie se dau „cuvinte” separate prin spații; unele sunt numere întregi, altele nu. Afișează suma celor care sunt numere întregi (inclusiv negative) și câte valori invalide au fost. Folosește try/except.",
             sol='s = inv = 0\nfor w in input().split():\n    try:\n        s += int(w)\n    except ValueError:\n        inv += 1\nprint(s, inv)',
             teste=[{"in": "3 abc -2 4.5 10"}, {"in": "x y"}, {"in": "1 2 3"}]),
        dict(titlu="Indice sigur", nivel="mediu", enunt="Pe prima linie o listă de numere, pe a doua câțiva indici (pot fi și negativi). Pentru fiecare indice afișează elementul sau <code>indice invalid</code> dacă nu există (folosește IndexError).",
             sol='v = input().split()\nfor w in input().split():\n    try:\n        print(v[int(w)])\n    except IndexError:\n        print("indice invalid")',
             teste=[{"in": "10 20 30\n0 2 3 -1 -4"}, {"in": "5\n0"}]),
        dict(titlu="Validare până la o valoare corectă", nivel="mediu", enunt="Se citesc linii până când apare o notă validă: un întreg între 1 și 10. Pentru fiecare linie invalidă afișează <code>invalid</code>; la final afișează <code>nota X</code>.",
             sol='while True:\n    try:\n        x = int(input())\n        if not 1 <= x <= 10:\n            raise ValueError\n        break\n    except ValueError:\n        print("invalid")\nprint("nota", x)',
             teste=[{"in": "abc\n11\n0\n7"}, {"in": "10"}, {"in": "9.5\n-3\n1"}]),
    ],
    quiz=[("Ce eroare produce <code>\"nota\" + 10</code>?", ["ValueError", "TypeError", "NameError", "SyntaxError"], 1, "Tipuri incompatibile."),
          ("Când se execută ramura <code>else</code> a lui <code>try</code>?", ["mereu", "doar dacă a apărut o excepție", "doar dacă nu a apărut nicio excepție", "niciodată"], 2, "else rulează la succes; finally rulează mereu."),
          ("Ce face <code>raise ValueError(\"x\")</code>?", ["prinde o excepție", "semnalează (aruncă) o excepție", "afișează x", "ignoră eroarea"], 1, "raise aruncă excepția.")],
))
