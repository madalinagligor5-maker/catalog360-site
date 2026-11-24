from util import C, CO, O, T

LECTII = []

LECTII.append(dict(
    id="a1", nr="1", scurt="Algoritm și complexitate", titlu="Algoritm, corectitudine și complexitate",
    programa="Programa cap. 2: algoritm, gândire computațională, criterii de elaborare a testelor, eficiența algoritmilor",
    obiective=["proprietățile unui algoritm și etapele rezolvării unei probleme", "cum numeri operațiile și ce înseamnă O(n), O(n²), O(log n)",
               "cum alegi un algoritm după dimensiunea datelor", "cum transformi un algoritm O(n²) în unul O(n) sau O(n log n)"],
    teorie=f"""
<p>Un <strong>algoritm</strong> este o succesiune finită de pași clari care transformă datele de intrare în datele de ieșire. Proprietăți: <strong>generalitate</strong>, <strong>finitudine</strong>, <strong>claritate</strong> (determinism), <strong>corectitudine</strong>, <strong>eficiență</strong>. Gândirea computațională înseamnă: descompunere, recunoașterea tiparelor, abstractizare, proiectarea algoritmului.</p>
<h3>Complexitatea în timp</h3>
<p>Numărăm câte operații elementare face algoritmul în funcție de dimensiunea n a datelor și păstrăm doar termenul dominant, fără constante: 3n² + 5n + 7 operații ⇒ <strong>O(n²)</strong>.</p>
{T(["Secvență", "Număr de pași", "Complexitate"],
   ["o buclă de la 1 la n", "n", "O(n)"],
   ["două bucle imbricate de la 1 la n", "n²", "O(n²)"],
   ["<code>for i in range(n): for j in range(i, n)</code>", "n(n+1)/2", "O(n²)"],
   ["<code>while n &gt; 0: n //= 10</code>", "numărul de cifre ≈ log₁₀ n", "O(log n)"],
   ["<code>while i * i &lt;= n: i += 1</code>", "√n", "O(√n)"],
   ["înjumătățirea intervalului (căutare binară)", "log₂ n", "O(log n)"],
   ["sortare prin interclasare", "≈ n log₂ n", "O(n log n)"])}
<p>Ordinea, de la cel mai rapid la cel mai lent: O(1) &lt; O(log n) &lt; O(√n) &lt; O(n) &lt; O(n log n) &lt; O(n²) &lt; O(n³) &lt; O(2ⁿ) &lt; O(n!). Un calculator face orientativ 10⁷–10⁸ operații simple pe secundă în Python (mai multe în C++); cu n = 10⁵, un algoritm O(n²) face 10¹⁰ pași – mult prea mult.</p>
<h3>Trei tehnici care reduc complexitatea</h3>
<ul>
<li><strong>Sume parțiale</strong>: <code>s[i] = v[0] + … + v[i−1]</code>; suma pe intervalul [a, b] este <code>s[b+1] − s[a]</code> în O(1) în loc de O(n).</li>
<li><strong>Doi indici</strong> (two pointers) pe o listă sortată: unul de la stânga, unul de la dreapta.</li>
<li><strong>Memorie suplimentară</strong>: liste de frecvențe, mulțimi, dicționare – testul „am mai văzut valoarea?” devine O(1).</li>
</ul>
{CO('''v = [3, 1, 4, 1, 5, 9, 2, 6]
s = [0]
for x in v:
    s.append(s[-1] + x)          # sume parțiale
print(s[6] - s[2])               # suma v[2..5] = 4 + 1 + 5 + 9''')}
<h3>Corectitudine și testare</h3>
<p>Un algoritm se testează pe: un caz obișnuit, <strong>cazuri limită</strong> (n = 0 sau 1, toate valorile egale, valori negative, valoarea maximă), date care fac fiecare ramură <code>if</code> să se execute, date mari (timp de execuție).</p>
""",
    rezolvate=[dict(titlu="Suma divizorilor în O(√n)", enunt="Divizorii vin în perechi (d, n/d); e suficient să mergem până la √n.",
                    cod='n = int(input())\ns = 0\nd = 1\nwhile d * d <= n:\n    if n % d == 0:\n        s += d\n        if d != n // d:\n            s += n // d\n    d += 1\nprint(s)', intrare="36",
                    explicatie="Pentru 36: perechile (1, 36), (2, 18), (3, 12), (4, 9), iar 6 se adună o singură dată. Pentru n = 10¹² sunt 10⁶ pași în loc de 10¹².")],
    exercitii=[
        dict(titlu="Suma divizorilor pentru n mare", nivel="mediu", enunt="Se citește n (1 ≤ n ≤ 10<sup>12</sup>). Afișează numărul de divizori și suma lor, separate prin spațiu. Un algoritm O(n) depășește timpul.",
             sol="n = int(input())\ncnt = s = 0\nd = 1\nwhile d * d <= n:\n    if n % d == 0:\n        cnt += 1; s += d\n        if d != n // d:\n            cnt += 1; s += n // d\n    d += 1\nprint(cnt, s)",
             teste=[{"in": "36"}, {"in": "1"}, {"in": "97"}, {"in": "999999999989"}, {"in": "735134400000"}]),
        dict(titlu="Interogări de sume", nivel="mediu", enunt="Pe prima linie n și q, pe a doua n numere întregi, apoi q linii cu câte două poziții a b (1 ≤ a ≤ b ≤ n, numerotare de la 1). Pentru fiecare interogare afișează suma elementelor de la a la b. Folosește sume parțiale.",
             sol="n, q = map(int, input().split())\nv = list(map(int, input().split()))\ns = [0]\nfor x in v:\n    s.append(s[-1] + x)\nfor _ in range(q):\n    a, b = map(int, input().split())\n    print(s[b] - s[a - 1])",
             teste=[{"in": "5 3\n1 2 3 4 5\n1 5\n2 3\n4 4"}, {"in": "3 2\n-1 5 -2\n1 1\n1 3"}]),
        dict(titlu="Perechi cu suma S (doi indici)", nivel="dificil", enunt="Pe prima linie o listă de numere întregi <strong>distincte</strong>, sortată crescător, pe a doua S. Afișează toate perechile (a, b), a &lt; b, cu a + b = S, câte una pe linie, în ordinea crescătoare a lui a; dacă nu există, afișează <code>nu exista</code>. Folosește tehnica celor doi indici (O(n)).",
             sol='v = list(map(int, input().split()))\nS = int(input())\ni, j = 0, len(v) - 1\ngasit = False\nwhile i < j:\n    t = v[i] + v[j]\n    if t == S:\n        print(v[i], v[j]); gasit = True\n        i += 1; j -= 1\n    elif t < S:\n        i += 1\n    else:\n        j -= 1\nif not gasit:\n    print("nu exista")',
             teste=[{"in": "1 2 4 5 7 9 11\n11"}, {"in": "1 2 3\n10"}, {"in": "-5 -1 0 1 5\n0"}]),
    ],
    quiz=[("Ce complexitate are <code>for i in range(n): for j in range(n): for k in range(n): ...</code>?", ["O(n)", "O(n²)", "O(n³)", "O(3n)"], 2, "Trei bucle imbricate, fiecare de n ori."),
          ("Cum se simplifică 5n² + 100n + 3?", ["O(n)", "O(n²)", "O(5n²)", "O(100n)"], 1, "Se păstrează termenul dominant, fără constante."),
          ("Care este mai rapid pentru n mare?", ["O(n log n)", "O(n²)", "O(n√n)", "O(2ⁿ)"], 0, "n log n crește cel mai încet dintre ele."),
          ("Câte iterații face <code>while n &gt; 0: n //= 2</code> pentru n = 1000?", ["500", "10", "1000", "3"], 1, "⌊log₂ 1000⌋ + 1 = 10."),
          ("Proprietatea algoritmului de a rezolva o clasă de probleme, nu un singur caz, este:", ["finitudinea", "generalitatea", "claritatea", "eficiența"], 1, "Generalitatea.")],
))

LECTII.append(dict(
    id="a2", nr="2", scurt="Recursivitate și Divide et impera", titlu="Recursivitate și metoda Divide et impera",
    programa="Programa cap. 4: metoda Divide et impera; cap. 3: sortarea prin interclasare, sortarea rapidă, căutarea binară",
    obiective=["cum funcționează stiva de apeluri", "schema Divide et impera: împarte – rezolvă – combină", "sortarea prin interclasare și sortarea rapidă", "recurența T(n) = 2T(n/2) + n ⇒ O(n log n)"],
    teorie=f"""
<p>La fiecare apel, parametrii și variabilele locale se pun pe <strong>stiva de apeluri</strong>; la <code>return</code> se revine în apelant, exact în punctul de după apel. O funcție recursivă are obligatoriu un <strong>caz de bază</strong> și apeluri pe probleme <strong>mai mici</strong>.</p>
<h3>Divide et impera</h3>
<ol><li><strong>Divide</strong>: problema se împarte în subprobleme <em>independente</em> de același tip (de regulă în două jumătăți).</li>
<li><strong>Impera</strong>: subproblemele se rezolvă recursiv; cele elementare direct.</li>
<li><strong>Combină</strong>: soluțiile subproblemelor se compun în soluția problemei.</li></ol>
{CO('''def interclasare(a, b):
    i = j = 0
    c = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i]); i += 1
        else:
            c.append(b[j]); j += 1
    return c + a[i:] + b[j:]

def merge_sort(v):                      # O(n log n), stabilă
    if len(v) <= 1:
        return v
    m = len(v) // 2
    return interclasare(merge_sort(v[:m]), merge_sort(v[m:]))

def quick_sort(v):                      # O(n log n) în medie, O(n²) în cel mai rău caz
    if len(v) <= 1:
        return v
    p = v[len(v) // 2]
    return quick_sort([x for x in v if x < p]) + [x for x in v if x == p] + quick_sort([x for x in v if x > p])

print(merge_sort([38, 27, 43, 3, 9, 82, 10]), quick_sort([5, 1, 5, 0]))''')}
<p><strong>De ce O(n log n)?</strong> Lista se înjumătățește de log₂ n ori; pe fiecare nivel, interclasările costă în total n ⇒ n · log₂ n.</p>
<p><strong>Turnurile din Hanoi</strong>: pentru a muta n discuri de pe A pe C, muți n−1 pe B, discul mare pe C, apoi n−1 de pe B pe C ⇒ M(n) = 2M(n−1) + 1 = 2ⁿ − 1 mutări.</p>
""",
    rezolvate=[dict(titlu="Maximul prin Divide et impera", cod='def maxim(v, st, dr):\n    if st == dr:\n        return v[st]\n    m = (st + dr) // 2\n    return max(maxim(v, st, m), maxim(v, m + 1, dr))\n\nv = [4, 9, 2, 17, 5]\nprint(maxim(v, 0, len(v) - 1))')],
    exercitii=[
        dict(titlu="Turnurile din Hanoi", nivel="mediu", enunt="Se citește n (1 ≤ n ≤ 10). Afișează numărul de mutări, apoi fiecare mutare pe câte o linie, sub forma <code>A C</code> (de pe tija A pe tija C). Discurile sunt inițial pe A și trebuie mutate pe C, cu B intermediar.",
             sol="def hanoi(n, a, b, c, m):\n    if n == 0:\n        return\n    hanoi(n - 1, a, c, b, m)\n    m.append(a + ' ' + c)\n    hanoi(n - 1, b, a, c, m)\n\nn = int(input())\nm = []\nhanoi(n, 'A', 'B', 'C', m)\nprint(len(m))\nprint('\\n'.join(m))",
             teste=[{"in": "2"}, {"in": "1"}, {"in": "3"}, {"in": "6"}]),
        dict(titlu="Sortare prin interclasare", nivel="mediu", enunt="Pe o linie se dau numere întregi. Sortează-le cu <strong>merge sort scris de tine</strong> (fără sort/sorted) și afișează lista sortată.",
             sol="def ms(v):\n    if len(v) <= 1:\n        return v\n    m = len(v) // 2\n    a, b = ms(v[:m]), ms(v[m:])\n    i = j = 0\n    c = []\n    while i < len(a) and j < len(b):\n        if a[i] <= b[j]:\n            c.append(a[i]); i += 1\n        else:\n            c.append(b[j]); j += 1\n    return c + a[i:] + b[j:]\n\nprint(*ms(list(map(int, input().split()))))",
             teste=[{"in": "38 27 43 3 9 82 10"}, {"in": "1"}, {"in": "5 -1 5 0 -1"}]),
        dict(titlu="Numărul de inversiuni", nivel="dificil", enunt="O inversiune este o pereche de poziții i &lt; j cu v[i] &gt; v[j]. Pe prima linie n (n ≤ 100 000), pe a doua n numere. Afișează numărul de inversiuni. Indiciu: numără-le în timpul interclasării – când iei un element din jumătatea dreaptă, el formează inversiuni cu toate elementele rămase în stânga.",
             sol="import sys\nsys.setrecursionlimit(10000)\ndef ms(v):\n    if len(v) <= 1:\n        return v, 0\n    m = len(v) // 2\n    a, x = ms(v[:m])\n    b, y = ms(v[m:])\n    i = j = 0\n    c = []\n    inv = x + y\n    while i < len(a) and j < len(b):\n        if a[i] <= b[j]:\n            c.append(a[i]); i += 1\n        else:\n            c.append(b[j]); j += 1\n            inv += len(a) - i\n    return c + a[i:] + b[j:], inv\n\nn = int(input())\nprint(ms(list(map(int, input().split())))[1])",
             teste=[{"in": "5\n2 4 1 3 5"}, {"in": "3\n1 2 3"}, {"in": "4\n4 3 2 1"}, {"in": "6\n1 1 1 0 0 0"}]),
        dict(titlu="Căutare binară recursivă", nivel="ușor", enunt="Pe prima linie o listă sortată crescător de numere distincte, pe a doua mai multe valori x. Pentru fiecare x afișează poziția lui (de la 0) sau -1, folosind o funcție <strong>recursivă</strong>.",
             sol="def cauta(v, x, st, dr):\n    if st > dr:\n        return -1\n    m = (st + dr) // 2\n    if v[m] == x:\n        return m\n    return cauta(v, x, m + 1, dr) if v[m] < x else cauta(v, x, st, m - 1)\n\nv = list(map(int, input().split()))\nprint(*[cauta(v, x, 0, len(v) - 1) for x in map(int, input().split())])",
             teste=[{"in": "2 5 8 12 16 23 38\n23 2 38 7 100"}, {"in": "5\n5 4"}]),
    ],
    quiz=[("Ce condiție trebuie să îndeplinească subproblemele la Divide et impera?", ["să fie suprapuse", "să fie independente", "să fie rezolvate greedy", "să aibă aceeași soluție"], 1, "Subproblemele suprapuse sunt specifice programării dinamice."),
          ("Câte mutări sunt necesare pentru 5 discuri la Hanoi?", ["25", "31", "32", "10"], 1, "2⁵ − 1 = 31."),
          ("Care sortare are O(n²) în cel mai defavorabil caz?", ["interclasare", "rapidă", "heapsort", "numărare"], 1, "Quicksort cu pivoți nefavorabili."),
          ("Ce se întâmplă fără caz de bază într-o funcție recursivă în Python?", ["returnează None", "RecursionError", "buclă infinită fără eroare", "SyntaxError"], 1, "Se depășește adâncimea maximă a stivei de apeluri.")],
))

LECTII.append(dict(
    id="a3", nr="3", scurt="Metoda Greedy", titlu="Metoda Greedy",
    programa="Programa cap. 4: metoda Greedy",
    obiective=["ideea alegerii optime locale", "problemele clasice: spectacole, rucsac fracționar, plata cu bancnote", "de ce greedy trebuie demonstrat și când nu funcționează"],
    teorie=f"""
<p>Metoda <strong>Greedy</strong> construiește soluția pas cu pas, alegând de fiecare dată elementul care pare cel mai bun în acel moment, fără a reveni asupra alegerii. Schema: se sortează candidații după un criteriu, apoi se parcurg și se adaugă fiecare candidat <em>compatibil</em> cu soluția parțială.</p>
<p>Este rapidă (de obicei O(n log n), din cauza sortării), dar <strong>corectitudinea trebuie demonstrată</strong> pentru fiecare problemă. Contraexemplu clasic: plata sumei 6 cu monede {{1, 3, 4}} – greedy alege 4 + 1 + 1 (3 monede), optimul este 3 + 3 (2 monede).</p>
{T(["Problemă", "Criteriul greedy corect"],
   ["Numărul maxim de spectacole fără suprapunere", "ora de <strong>sfârșit</strong> crescătoare"],
   ["Rucsac fracționar (obiectele se pot tăia)", "raportul valoare / greutate descrescător"],
   ["Plata cu bancnote românești (1, 5, 10, 50, 100, 200, 500)", "cea mai mare bancnotă care încape (sistem canonic)"],
   ["Minimizarea timpului mediu de așteptare la o coadă", "durata serviciului crescătoare"],
   ["Arbore parțial de cost minim, drumuri minime", "Prim, Kruskal, Dijkstra (lecțiile 9–10)"])}
{CO('''spect = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]
spect.sort(key=lambda s: s[1])          # după ora de sfârșit
ales, sfarsit = [], -1
for inceput, final in spect:
    if inceput >= sfarsit:              # compatibil cu ultimul ales
        ales.append((inceput, final))
        sfarsit = final
print(ales)''')}
""",
    rezolvate=[dict(titlu="Rucsac fracționar", cod='G = 50\nobiecte = [(60, 10), (100, 20), (120, 30)]       # (valoare, greutate)\nobiecte.sort(key=lambda o: o[0] / o[1], reverse=True)\ntotal = 0\nfor v, g in obiecte:\n    if g <= G:\n        total += v; G -= g\n    else:\n        total += v * G / g\n        break\nprint(total)')],
    exercitii=[
        dict(titlu="Spectacole", nivel="mediu", enunt="Pe prima linie n, apoi n linii cu ora de început și ora de sfârșit (minute de la miezul nopții) ale unui spectacol. Afișează numărul maxim de spectacole care pot fi vizionate integral (un spectacol poate începe exact când se termină altul).",
             sol="n = int(input())\nv = [tuple(map(int, input().split())) for _ in range(n)]\nv.sort(key=lambda s: s[1])\ncnt, t = 0, -1\nfor a, b in v:\n    if a >= t:\n        cnt += 1; t = b\nprint(cnt)",
             teste=[{"in": "5\n600 660\n630 700\n660 720\n700 800\n720 780"}, {"in": "1\n0 10"}, {"in": "3\n0 100\n10 20\n20 30"}]),
        dict(titlu="Plata cu bancnote", nivel="ușor", enunt="Se citește o sumă S (lei, număr natural). Folosind bancnotele 500, 200, 100, 50, 10, 5, 1, afișează plata cu un număr minim de bancnote: pe fiecare linie <code>valoare x numar</code>, doar pentru bancnotele folosite, în ordine descrescătoare.",
             sol="S = int(input())\nfor b in (500, 200, 100, 50, 10, 5, 1):\n    if S >= b:\n        print(b, 'x', S // b)\n        S %= b",
             teste=[{"in": "1789"}, {"in": "5"}, {"in": "0"}, {"in": "999"}]),
        dict(titlu="Rucsac fracționar", nivel="mediu", enunt="Pe prima linie n și G (capacitatea), apoi n linii <code>valoare greutate</code>. Obiectele se pot tăia. Afișează valoarea maximă cu două zecimale.",
             sol="n, G = map(int, input().split())\nv = [tuple(map(int, input().split())) for _ in range(n)]\nv.sort(key=lambda o: o[0] / o[1], reverse=True)\ntot = 0\nfor val, g in v:\n    if G <= 0:\n        break\n    luat = min(g, G)\n    tot += val * luat / g\n    G -= luat\nprint(f'{tot:.2f}')",
             teste=[{"in": "3 50\n60 10\n100 20\n120 30"}, {"in": "1 5\n10 10"}, {"in": "2 100\n1 1\n2 1"}]),
        dict(titlu="Coada la ghișeu", nivel="mediu", enunt="Pe prima linie n, pe a doua duratele de servire ale celor n persoane. Ele pot fi servite în orice ordine. Afișează timpul total minim de așteptare (suma momentelor la care începe servirea fiecărei persoane).",
             sol="n = int(input())\nv = sorted(map(int, input().split()))\nt = total = 0\nfor d in v:\n    total += t\n    t += d\nprint(total)",
             teste=[{"in": "3\n5 1 3"}, {"in": "1\n7"}, {"in": "4\n2 2 2 2"}]),
    ],
    quiz=[("Ce criteriu greedy dă numărul maxim de spectacole?", ["ora de început crescătoare", "durata crescătoare", "ora de sfârșit crescătoare", "durata descrescătoare"], 2, "Lasă cel mai mult timp pentru restul."),
          ("Pentru monedele {1, 3, 4} și suma 6, greedy dă:", ["optimul, 2 monede", "3 monede, neoptim", "nicio soluție", "1 monedă"], 1, "4 + 1 + 1, dar optimul este 3 + 3."),
          ("Ce trebuie făcut pentru a folosi Greedy corect?", ["nimic", "demonstrat că alegerea locală duce la optim", "generate toate soluțiile", "memorate subproblemele"], 1, "Altfel algoritmul poate fi greșit.")],
))

LECTII.append(dict(
    id="a4", nr="4", scurt="Metoda Backtracking", titlu="Metoda Backtracking",
    programa="Programa cap. 4: metoda Backtracking; cap. 3: metode de generare sistematică",
    obiective=["schema generală a backtracking-ului", "permutări, aranjamente, combinări, submulțimi, partiții", "condiții de continuare (validare) și tăierea ramurilor", "ordinea lexicografică a soluțiilor"],
    teorie=f"""
<p>Backtracking construiește soluția <em>x₁, x₂, …, xₖ</em> element cu element. Pentru poziția curentă încearcă pe rând toate valorile posibile; dacă valoarea respectă <strong>condițiile de continuare</strong>, trece la poziția următoare; când valorile se epuizează, <strong>revine</strong> la poziția anterioară. Complexitatea este exponențială, dar condițiile de continuare taie multe ramuri.</p>
{C('''def bt(k):                       # schema generală
    for v in candidati(k):       # valorile posibile pentru poziția k
        x[k] = v
        if valid(k):             # condiții de continuare
            if solutie(k):
                afiseaza()
            else:
                bt(k + 1)''', "pseudocod")}
{T(["Ce generăm", "Condiția pentru x[k]", "Număr de soluții"],
   ["permutări ale lui {1..n}", "x[k] nu a mai fost folosit", "n!"],
   ["aranjamente de n luate câte p", "x[k] nefolosit; soluție la k = p", "n!/(n−p)!"],
   ["combinări de n luate câte p", "x[k] &gt; x[k−1]", "C(n, p)"],
   ["submulțimi", "x[k] &gt; x[k−1]; fiecare prefix e soluție", "2ⁿ − 1 nevide"],
   ["produs cartezian", "orice valoare", "n₁·n₂·…"],
   ["partiții ale lui n (sume)", "x[k] ≥ x[k−1] și suma ≤ n", "–"])}
{CO('''n = 4
x, folosit = [], [False] * (n + 1)
cnt = 0
def dame(k):                     # problema damelor: x[i] = coloana damei de pe linia i
    global cnt
    if k == n:
        cnt += 1
        if cnt == 1: print(x)
        return
    for c in range(n):
        if all(x[i] != c and abs(x[i] - c) != k - i for i in range(k)):
            x.append(c); dame(k + 1); x.pop()
dame(0); print(cnt)''')}
""",
    rezolvate=[dict(titlu="Partițiile unui număr", enunt="Scrie n ca sumă de numere naturale nenule, în ordine crescătoare a termenilor (fără să numărăm de două ori aceeași descompunere).",
                    cod='n = int(input())\nx = []\ndef bt(rest, minim):\n    if rest == 0:\n        print("+".join(map(str, x)))\n        return\n    for v in range(minim, rest + 1):\n        x.append(v)\n        bt(rest - v, v)\n        x.pop()\nbt(n, 1)', intrare="4")],
    exercitii=[
        dict(titlu="Permutări", nivel="ușor", enunt="Se citește n (1 ≤ n ≤ 7). Afișează toate permutările mulțimii {1, …, n} în ordine lexicografică, fără itertools.",
             sol="n = int(input())\nx, f = [], [False] * (n + 1)\ndef bt():\n    if len(x) == n:\n        print(*x); return\n    for v in range(1, n + 1):\n        if not f[v]:\n            f[v] = True; x.append(v)\n            bt()\n            x.pop(); f[v] = False\nbt()",
             teste=[{"in": "3"}, {"in": "1"}, {"in": "4"}]),
        dict(titlu="Combinări", nivel="ușor", enunt="Se citesc n și p (1 ≤ p ≤ n ≤ 10). Afișează combinările de n luate câte p, în ordine lexicografică.",
             sol="n, p = map(int, input().split())\nx = []\ndef bt(start):\n    if len(x) == p:\n        print(*x); return\n    for v in range(start, n + 1):\n        x.append(v); bt(v + 1); x.pop()\nbt(1)",
             teste=[{"in": "5 3"}, {"in": "3 3"}, {"in": "4 1"}]),
        dict(titlu="Câte soluții pentru n dame", nivel="mediu", enunt="Se citește n (1 ≤ n ≤ 9). Afișează numărul de moduri de a așeza n dame pe o tablă n × n fără să se atace.",
             sol="n = int(input())\nx = []\ncnt = 0\ndef bt(k):\n    global cnt\n    if k == n:\n        cnt += 1; return\n    for c in range(n):\n        if all(x[i] != c and abs(x[i] - c) != k - i for i in range(k)):\n            x.append(c); bt(k + 1); x.pop()\nbt(0)\nprint(cnt)",
             teste=[{"in": "4"}, {"in": "1"}, {"in": "6"}, {"in": "8"}]),
        dict(titlu="Submulțimi cu suma dată", nivel="mediu", enunt="Pe prima linie numere naturale distincte, sortate crescător; pe a doua S. Afișează toate submulțimile cu suma S, câte una pe linie, în ordine lexicografică (după valori), sau <code>0</code> dacă nu există. Folosește condiția de continuare „suma parțială ≤ S”.",
             sol="v = list(map(int, input().split()))\nS = int(input())\nx = []\ngasit = False\ndef bt(i, s):\n    global gasit\n    if s == S and x:\n        print(*x); gasit = True\n    for j in range(i, len(v)):\n        if s + v[j] <= S:\n            x.append(v[j]); bt(j + 1, s + v[j]); x.pop()\nbt(0, 0)\nif not gasit:\n    print(0)",
             teste=[{"in": "1 2 3 4 5 6\n7"}, {"in": "5 10\n3"}, {"in": "2 3 5\n10"}]),
        dict(titlu="Cuvinte din litere", nivel="dificil", enunt="Se citesc un șir de litere distincte și k. Afișează, în ordine lexicografică, toate „cuvintele” de k litere distincte din șir care <strong>nu</strong> au două vocale alăturate (vocale: a, e, i, o, u).",
             sol="s = sorted(input().strip())\nk = int(input())\nx = []\ndef bt():\n    if len(x) == k:\n        print(''.join(x)); return\n    for c in s:\n        if c not in x and not (x and x[-1] in 'aeiou' and c in 'aeiou'):\n            x.append(c); bt(); x.pop()\nbt()",
             teste=[{"in": "abe\n2"}, {"in": "aei\n2"}, {"in": "mare\n3"}]),
    ],
    quiz=[("Ce soluție urmează după 1 4 5 la combinări de 5 luate câte 3?", ["2 3 4", "1 5 6", "2 4 5", "1 4 6"], 0, "Ordinea: 123, 124, 125, 134, 135, 145, 234…"),
          ("Câte aranjamente de 5 luate câte 2 există?", ["10", "20", "25", "120"], 1, "5 · 4 = 20."),
          ("Ce rol au condițiile de continuare?", ["afișează soluția", "elimină din timp ramurile care nu pot duce la soluții", "sortează datele", "memorează subproblemele"], 1, "Reduc drastic numărul de configurații încercate."),
          ("Câte permutări are o mulțime cu 6 elemente?", ["36", "120", "720", "64"], 2, "6! = 720.")],
))

LECTII.append(dict(
    id="a5", nr="5", scurt="Programare dinamică", titlu="Programarea dinamică",
    programa="Programa cap. 4: metoda programării dinamice",
    obiective=["subprobleme suprapuse și substructură optimă", "cum scrii relația de recurență și ordinea de calcul", "problemele clasice: subșir crescător maximal, rucsac 0/1, triunghi, subșir comun, drumuri în grilă", "reconstituirea soluției"],
    teorie=f"""
<p>Programarea dinamică se aplică atunci când problema are <strong>substructură optimă</strong> (soluția optimă conține soluțiile optime ale subproblemelor) și <strong>subprobleme suprapuse</strong> (aceleași subprobleme apar de multe ori). Fiecare subproblemă se rezolvă <em>o singură dată</em>, iar rezultatul se memorează într-un tablou.</p>
<ol><li>Definește starea: ce reprezintă <code>d[i]</code> (sau <code>d[i][j]</code>).</li><li>Scrie relația de recurență.</li><li>Stabilește cazurile de bază și ordinea de completare.</li><li>Rezultatul este într-o anumită celulă (sau maximul tabloului).</li></ol>
{T(["Problemă", "Stare", "Recurență"],
   ["Subșir crescător maximal", "L[i] = lungimea celui mai lung subșir crescător care se termină în v[i]", "L[i] = 1 + max(L[j]), j &lt; i, v[j] &lt; v[i]"],
   ["Rucsac 0/1", "d[c] = valoarea maximă cu capacitatea c", "d[c] = max(d[c], d[c − g] + v), c descrescător"],
   ["Triunghi de numere", "S[i][j] = suma maximă de la (i, j) în jos", "S[i][j] = T[i][j] + max(S[i+1][j], S[i+1][j+1])"],
   ["Cel mai lung subșir comun", "C[i][j] pentru prefixele a[:i], b[:j]", "C[i−1][j−1] + 1 dacă a[i−1] = b[j−1], altfel max(C[i−1][j], C[i][j−1])"],
   ["Drumuri în grilă (doar dreapta/jos)", "D[i][j] = numărul de drumuri până la (i, j)", "D[i][j] = D[i−1][j] + D[i][j−1]"])}
{CO('''from functools import lru_cache
@lru_cache(maxsize=None)          # memoizare: varianta „de sus în jos”
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)
print(fib(80))''')}
""",
    rezolvate=[dict(titlu="Subșir crescător maximal cu reconstituire", cod='v = [5, 2, 8, 6, 3, 6, 9, 7]\nn = len(v)\nL, prec = [1] * n, [-1] * n\nfor i in range(n):\n    for j in range(i):\n        if v[j] < v[i] and L[j] + 1 > L[i]:\n            L[i], prec[i] = L[j] + 1, j\ni = L.index(max(L))\nsir = []\nwhile i != -1:\n    sir.append(v[i]); i = prec[i]\nprint(max(L), sir[::-1])',
                    explicatie="Vectorul <code>prec</code> memorează de unde am venit, ca să putem reconstitui subșirul de la final spre început.")],
    exercitii=[
        dict(titlu="Subșir crescător maximal", nivel="mediu", enunt="Pe prima linie n (n ≤ 1000), pe a doua n numere întregi. Afișează lungimea celui mai lung subșir <strong>strict</strong> crescător (elementele nu trebuie să fie consecutive).",
             sol="n = int(input())\nv = list(map(int, input().split()))\nL = [1] * n\nfor i in range(n):\n    for j in range(i):\n        if v[j] < v[i]:\n            L[i] = max(L[i], L[j] + 1)\nprint(max(L))",
             teste=[{"in": "8\n5 2 8 6 3 6 9 7"}, {"in": "1\n4"}, {"in": "5\n5 4 3 2 1"}, {"in": "6\n1 1 2 2 3 3"}]),
        dict(titlu="Rucsac 0/1", nivel="mediu", enunt="Pe prima linie n și G, apoi n linii <code>greutate valoare</code>. Fiecare obiect poate fi luat cel mult o dată, întreg. Afișează valoarea maximă.",
             sol="n, G = map(int, input().split())\nd = [0] * (G + 1)\nfor _ in range(n):\n    g, v = map(int, input().split())\n    for c in range(G, g - 1, -1):\n        d[c] = max(d[c], d[c - g] + v)\nprint(d[G])",
             teste=[{"in": "4 7\n1 1\n3 4\n4 5\n5 7"}, {"in": "1 3\n5 10"}, {"in": "3 10\n5 10\n4 40\n6 30"}]),
        dict(titlu="Triunghiul de numere", nivel="ușor", enunt="Pe prima linie n, apoi n linii: linia i are i numere. Pornind din vârf, la fiecare pas cobori pe elementul de dedesubt sau pe cel din dreapta-jos. Afișează suma maximă.",
             sol="n = int(input())\nt = [list(map(int, input().split())) for _ in range(n)]\nfor i in range(n - 2, -1, -1):\n    for j in range(i + 1):\n        t[i][j] += max(t[i + 1][j], t[i + 1][j + 1])\nprint(t[0][0])",
             teste=[{"in": "5\n7\n3 8\n8 1 0\n2 7 4 4\n4 5 2 6 5"}, {"in": "1\n9"}, {"in": "3\n1\n2 3\n10 1 1"}]),
        dict(titlu="Cel mai lung subșir comun", nivel="dificil", enunt="Se citesc două cuvinte. Afișează lungimea celui mai lung subșir comun (literele nu trebuie să fie consecutive, dar își păstrează ordinea).",
             sol="a, b = input(), input()\nC = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]\nfor i in range(1, len(a) + 1):\n    for j in range(1, len(b) + 1):\n        C[i][j] = C[i-1][j-1] + 1 if a[i-1] == b[j-1] else max(C[i-1][j], C[i][j-1])\nprint(C[len(a)][len(b)])",
             teste=[{"in": "ALGORITM\nLOGARITM"}, {"in": "abc\ndef"}, {"in": "informatica\nmatematica"}]),
        dict(titlu="Drumuri cu obstacole", nivel="dificil", enunt="Pe prima linie n și m, apoi n linii cu m caractere (<code>.</code> liber, <code>#</code> obstacol). Din colțul stânga-sus te poți deplasa doar la dreapta sau în jos. Afișează numărul de drumuri până în colțul dreapta-jos, modulo 1 000 000 007.",
             sol="n, m = map(int, input().split())\ng = [input() for _ in range(n)]\nM = 10**9 + 7\nd = [[0] * m for _ in range(n)]\nfor i in range(n):\n    for j in range(m):\n        if g[i][j] == '#':\n            continue\n        if i == 0 and j == 0:\n            d[i][j] = 1\n        else:\n            d[i][j] = ((d[i-1][j] if i else 0) + (d[i][j-1] if j else 0)) % M\nprint(d[n-1][m-1])",
             teste=[{"in": "3 3\n...\n.#.\n..."}, {"in": "1 1\n."}, {"in": "2 2\n.#\n#."}, {"in": "3 4\n....\n....\n...."}]),
    ],
    quiz=[("Programarea dinamică se aplică atunci când subproblemele sunt:", ["independente", "suprapuse", "sortate", "de dimensiune egală"], 1, "Rezultatele lor se reutilizează."),
          ("La rucsacul 0/1 cu un singur vector d[c], capacitatea c se parcurge:", ["crescător", "descrescător", "în orice ordine", "doar pentru c par"], 1, "Altfel un obiect ar putea fi folosit de mai multe ori."),
          ("Ce valoare are C[i][j] pentru cel mai lung subșir comun dacă a[i−1] = b[j−1]?", ["C[i−1][j]", "C[i−1][j−1] + 1", "max(C[i−1][j], C[i][j−1])", "0"], 1, "Litera comună prelungește subșirul comun al prefixelor."),
          ("Ce face decoratorul <code>@lru_cache</code>?", ["sortează", "memorează rezultatele apelurilor", "limitează recursivitatea", "paralelizează"], 1, "Memoizare: un apel cu aceiași parametri se calculează o singură dată.")],
))

LECTII.append(dict(
    id="a6", nr="6", scurt="Stive, cozi, liste înlănțuite", titlu="Structuri liniare: stiva, coada, lista înlănțuită",
    programa="Programa cap. 1: modelul liniar – stivă, coadă, liste simplu/dublu înlănțuite, circulare",
    obiective=["operațiile stivei și ale cozii și complexitatea lor", "aplicații: paranteze, forma postfixată, simulări", "implementarea unei liste simplu înlănțuite cu o clasă Nod"],
    teorie=f"""
{T(["Structură", "Principiu", "În Python", "Aplicații"],
   ["Stivă", "LIFO", "<code>list</code>: <code>append</code>, <code>pop()</code>, vârful <code>s[-1]</code>", "paranteze, anularea operațiilor (undo), recursivitate, evaluarea expresiilor"],
   ["Coadă", "FIFO", "<code>collections.deque</code>: <code>append</code>, <code>popleft()</code>", "simulări de așteptare, parcurgerea în lățime (BFS)"],
   ["Listă simplu înlănțuită", "nod = informație + legătură spre următorul", "clasă proprie <code>Nod</code>", "inserări/ștergeri O(1) după un nod cunoscut"])}
{CO('''class Nod:
    def __init__(self, info, urm=None):
        self.info = info
        self.urm = urm

class Lista:
    def __init__(self):
        self.prim = None
    def adauga_inceput(self, x):          # O(1)
        self.prim = Nod(x, self.prim)
    def adauga_final(self, x):            # O(n) fără pointer spre ultimul nod
        nou = Nod(x)
        if self.prim is None:
            self.prim = nou; return
        p = self.prim
        while p.urm is not None:
            p = p.urm
        p.urm = nou
    def sterge(self, x):                  # prima apariție a lui x
        if self.prim and self.prim.info == x:
            self.prim = self.prim.urm; return
        p = self.prim
        while p and p.urm and p.urm.info != x:
            p = p.urm
        if p and p.urm:
            p.urm = p.urm.urm
    def __str__(self):
        v, p = [], self.prim
        while p:
            v.append(str(p.info)); p = p.urm
        return " -> ".join(v) or "(vida)"

L = Lista()
for x in (3, 5, 7): L.adauga_final(x)
L.adauga_inceput(1); L.sterge(5)
print(L)''')}
<p>La lista <strong>dublu înlănțuită</strong> fiecare nod are și legătura <code>prec</code>; la cea <strong>circulară</strong>, ultimul nod indică spre primul (parcurgerea se oprește când revii la nodul de pornire).</p>
<h3>Forma postfixată (poloneză inversă)</h3>
<p>Expresia <code>(3 + 4) * 2</code> se scrie postfixat <code>3 4 + 2 *</code>. Evaluarea cu o stivă: numerele se pun pe stivă; la un operator se scot doi operanzi (întâi cel din dreapta), se calculează și se pune rezultatul.</p>
""",
    rezolvate=[dict(titlu="Simularea unei cozi la casă", cod='from collections import deque\ncoada = deque(["Ana", "Dan", "Ioana"])\ncoada.append("Radu")\nwhile coada:\n    print("servit:", coada.popleft())')],
    exercitii=[
        dict(titlu="Paranteze corecte", nivel="mediu", enunt="Se citesc mai multe linii (prima: n, apoi n expresii) formate din parantezele <code>()[]{}</code>. Pentru fiecare afișează <code>DA</code> dacă parantezele sunt închise corect și în ordinea corectă, altfel <code>NU</code>.",
             sol="n = int(input())\npereche = {')': '(', ']': '[', '}': '{'}\nfor _ in range(n):\n    s = input().strip()\n    st = []\n    ok = True\n    for c in s:\n        if c in '([{':\n            st.append(c)\n        elif not st or st.pop() != pereche[c]:\n            ok = False; break\n    print('DA' if ok and not st else 'NU')",
             teste=[{"in": "5\n([]{})\n([)]\n((\n)\n{[()()]}"}, {"in": "1\n[]"}]),
        dict(titlu="Evaluarea formei postfixate", nivel="mediu", enunt="Se citește o expresie postfixată cu numere întregi și operatorii <code>+ - *</code>, separate prin spații. Afișează valoarea ei.",
             sol="st = []\nfor t in input().split():\n    if t in '+-*':\n        b = st.pop(); a = st.pop()\n        st.append(a + b if t == '+' else a - b if t == '-' else a * b)\n    else:\n        st.append(int(t))\nprint(st[0])",
             teste=[{"in": "3 4 + 2 *"}, {"in": "5 1 2 + 4 * + 3 -"}, {"in": "10 3 -"}, {"in": "7"}]),
        dict(titlu="Josephus cu o coadă", nivel="mediu", enunt="n copii (numerotați 1..n) stau în cerc. Se numără din k în k și copilul la care se ajunge iese din joc; numărătoarea continuă cu următorul. Se citesc n și k. Afișează ordinea ieșirii din joc. Folosește o coadă (deque) ca listă circulară.",
             sol="from collections import deque\nn, k = map(int, input().split())\nq = deque(range(1, n + 1))\nrez = []\nwhile q:\n    q.rotate(-(k - 1))\n    rez.append(q.popleft())\nprint(*rez)",
             teste=[{"in": "7 3"}, {"in": "1 5"}, {"in": "5 1"}, {"in": "6 2"}]),
        dict(titlu="Listă înlănțuită", nivel="dificil", enunt="Completează clasa <code>Lista</code> (simplu înlănțuită) cu metodele <code>adauga_final</code>, <code>inverseaza</code> (inversează legăturile, fără liste Python auxiliare) și <code>__str__</code> (elementele separate prin spațiu sau <code>vida</code>). Programul citește numere, le adaugă la final, afișează lista, o inversează și o afișează din nou.",
             start='class Nod:\n    def __init__(self, info, urm=None):\n        self.info = info\n        self.urm = urm\n\nclass Lista:\n    def __init__(self):\n        self.prim = None\n    # completează metodele\n\nL = Lista()\nfor x in map(int, input().split()):\n    L.adauga_final(x)\nprint(L)\nL.inverseaza()\nprint(L)\n',
             sol='class Nod:\n    def __init__(self, info, urm=None):\n        self.info = info\n        self.urm = urm\n\nclass Lista:\n    def __init__(self):\n        self.prim = None\n        self.ultim = None\n    def adauga_final(self, x):\n        n = Nod(x)\n        if self.prim is None:\n            self.prim = self.ultim = n\n        else:\n            self.ultim.urm = n\n            self.ultim = n\n    def inverseaza(self):\n        prec, p = None, self.prim\n        self.ultim = self.prim\n        while p:\n            p.urm, prec, p = prec, p, p.urm\n        self.prim = prec\n    def __str__(self):\n        v, p = [], self.prim\n        while p:\n            v.append(str(p.info)); p = p.urm\n        return " ".join(v) if v else "vida"\n\nL = Lista()\nfor x in map(int, input().split()):\n    L.adauga_final(x)\nprint(L)\nL.inverseaza()\nprint(L)',
             teste=[{"in": "1 2 3 4"}, {"in": "7"}, {"in": "5 5 9"}]),
    ],
    quiz=[("Ce structură folosește parcurgerea în lățime (BFS)?", ["stiva", "coada", "heap-ul", "dicționarul"], 1, "FIFO: nodurile se vizitează în ordinea descoperirii."),
          ("Cum se scrie postfixat <code>2 * (3 + 4)</code>?", ["2 3 4 + *", "2 3 * 4 +", "* 2 + 3 4", "2 3 4 * +"], 0, "Operanzii păstrează ordinea; operatorul vine după operanzii lui."),
          ("De ce <code>list.pop(0)</code> este lent pentru o coadă mare?", ["nu este lent", "mută toate celelalte elemente: O(n)", "sortează lista", "creează o copie"], 1, "deque.popleft() este O(1)."),
          ("Într-o listă circulară simplu înlănțuită, ultimul nod indică spre:", ["None", "primul nod", "el însuși", "nodul din mijloc"], 1, "De aceea nu există legătură nulă.")],
))
