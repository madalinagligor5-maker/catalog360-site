from util import C, CO, O, T

LECTII = []
GRAF_IN = "Graful se citește astfel: pe prima linie n (noduri, numerotate 1..n) și m (muchii), apoi m linii <code>x y</code>."

LECTII.append(dict(
    id="a7", nr="7", scurt="Grafuri: noțiuni, reprezentare", titlu="Grafuri: noțiuni de bază și reprezentare",
    programa="Programa cap. 1: modelul rețea – graf neorientat/orientat, subgraf, graf parțial, graf transpus, complet, bipartit, conex, tare conex, ponderat, hamiltonian, eulerian",
    obiective=["vocabularul: nod, muchie/arc, grad, lanț/drum, ciclu/circuit", "tipurile de grafuri din programă", "matricea de adiacență, listele de adiacență, lista muchiilor", "formulele care apar în subiecte"],
    teorie=f"""
{T(["Noțiune", "Graf neorientat", "Graf orientat"],
   ["legătură", "muchie [x, y]", "arc (x, y) – de la x la y"],
   ["grad", "d(x) = nr. de muchii incidente; Σd(x) = 2m", "d⁺(x) extern, d⁻(x) intern; Σd⁺ = Σd⁻ = m"],
   ["succesiune de noduri legate", "lanț; elementar dacă nodurile sunt distincte", "drum"],
   ["închisă", "ciclu", "circuit"],
   ["„legat”", "conex: lanț între oricare două noduri", "tare conex: drum de la x la y și de la y la x, pentru orice x, y"],
   ["nr. maxim de legături", "n(n−1)/2 (graf complet)", "n(n−1)"],
   ["nr. de grafuri cu n noduri date", "2<sup>n(n−1)/2</sup>", "4<sup>n(n−1)/2</sup>"])}
<ul>
<li><strong>Graf parțial</strong>: aceleași noduri, o parte din muchii (se elimină muchii) – 2<sup>m</sup> grafuri parțiale. <strong>Subgraf</strong>: o parte din noduri, cu <em>toate</em> muchiile dintre ele (se elimină noduri).</li>
<li><strong>Graf transpus</strong> (orientat): arcele inversate. <strong>Ponderat</strong>: fiecare muchie are un cost.</li>
<li><strong>Bipartit</strong>: nodurile se împart în două mulțimi și orice muchie leagă noduri din mulțimi diferite (⇔ nu are cicluri impare).</li>
<li><strong>Eulerian</strong>: ciclu care folosește fiecare muchie o dată ⇔ conex (fără a număra nodurile izolate) și toate gradele pare. <strong>Hamiltonian</strong>: ciclu elementar prin toate nodurile (nu există o condiție simplă necesară și suficientă; Dirac: d(x) ≥ n/2 este suficientă).</li>
</ul>
{CO('''n, m = 4, 4
muchii = [(1, 2), (1, 3), (2, 3), (3, 4)]
A = [[0] * (n + 1) for _ in range(n + 1)]       # matrice de adiacență, indici 1..n
L = [[] for _ in range(n + 1)]                  # liste de adiacență
for x, y in muchii:
    A[x][y] = A[y][x] = 1
    L[x].append(y); L[y].append(x)
print([sum(A[i]) for i in range(1, n + 1)])     # gradele
print(L[3])''')}
<p>Matricea de adiacență ocupă n² și răspunde în O(1) la „există muchia [x, y]?”; listele de adiacență ocupă n + m și sunt preferate pentru parcurgeri pe grafuri mari.</p>
""",
    rezolvate=[dict(titlu="Grade și noduri izolate", cod='n, m = 5, 4\nmuchii = [(1, 2), (2, 3), (3, 1), (3, 4)]\ngrad = [0] * (n + 1)\nfor x, y in muchii:\n    grad[x] += 1; grad[y] += 1\nprint("grade:", grad[1:])\nprint("izolate:", [i for i in range(1, n + 1) if grad[i] == 0])\nprint("grad maxim:", max(grad), "la nodurile", [i for i in range(1, n + 1) if grad[i] == max(grad)])')],
    exercitii=[
        dict(titlu="Gradele nodurilor", nivel="ușor", enunt=GRAF_IN + " Afișează gradele nodurilor 1..n pe o linie, apoi numărul de noduri cu grad impar.",
             sol="n, m = map(int, input().split())\ng = [0] * (n + 1)\nfor _ in range(m):\n    x, y = map(int, input().split())\n    g[x] += 1; g[y] += 1\nprint(*g[1:])\nprint(sum(1 for d in g[1:] if d % 2))",
             teste=[{"in": "6 7\n1 2\n1 3\n2 3\n3 4\n4 5\n4 6\n5 6"}, {"in": "3 0"}, {"in": "2 1\n1 2"}]),
        dict(titlu="Matricea de adiacență", nivel="ușor", enunt=GRAF_IN + " Afișează matricea de adiacență (n linii cu câte n valori 0/1).",
             sol="n, m = map(int, input().split())\nA = [[0] * n for _ in range(n)]\nfor _ in range(m):\n    x, y = map(int, input().split())\n    A[x-1][y-1] = A[y-1][x-1] = 1\nfor r in A:\n    print(*r)",
             teste=[{"in": "4 4\n1 2\n1 3\n2 3\n3 4"}, {"in": "1 0"}]),
        dict(titlu="Grad intern și extern", nivel="mediu", enunt="Graf <strong>orientat</strong>: pe prima linie n și m, apoi m arce <code>x y</code> (de la x la y). Afișează nodurile care au grad intern egal cu gradul extern (crescător, pe o linie), sau <code>0</code> dacă nu există; pe linia a doua, listele de adiacență ale grafului transpus pentru fiecare nod, sub forma <code>nod: vecini</code> (vecinii crescător).",
             sol="n, m = map(int, input().split())\nde = [0] * (n + 1); di = [0] * (n + 1)\nT = [[] for _ in range(n + 1)]\nfor _ in range(m):\n    x, y = map(int, input().split())\n    de[x] += 1; di[y] += 1\n    T[y].append(x)\negal = [i for i in range(1, n + 1) if de[i] == di[i]]\nprint(*egal if egal else [0])\nfor i in range(1, n + 1):\n    print(f'{i}:', *sorted(T[i]))",
             teste=[{"in": "4 5\n1 2\n2 3\n3 1\n3 4\n4 2"}, {"in": "2 1\n1 2"}]),
        dict(titlu="Eulerian?", nivel="dificil", enunt=GRAF_IN + " Graful este conex. Afișează <code>ciclu eulerian</code> dacă toate gradele sunt pare, <code>lant eulerian</code> dacă exact două noduri au grad impar, altfel <code>nu</code>.",
             sol="n, m = map(int, input().split())\ng = [0] * (n + 1)\nfor _ in range(m):\n    x, y = map(int, input().split())\n    g[x] += 1; g[y] += 1\nk = sum(1 for d in g[1:] if d % 2)\nprint('ciclu eulerian' if k == 0 else 'lant eulerian' if k == 2 else 'nu')",
             teste=[{"in": "6 7\n1 2\n1 3\n2 3\n3 4\n4 5\n4 6\n5 6"}, {"in": "3 3\n1 2\n2 3\n3 1"}, {"in": "4 3\n1 2\n1 3\n1 4"}]),
    ],
    quiz=[("Un graf neorientat cu 7 noduri are cel mult câte muchii?", ["49", "42", "21", "14"], 2, "7 · 6 / 2 = 21."),
          ("Suma gradelor unui graf neorientat cu 9 muchii este:", ["9", "18", "81", "depinde"], 1, "Fiecare muchie contribuie cu 2."),
          ("Prin eliminarea unor muchii (păstrând toate nodurile) se obține un:", ["subgraf", "graf parțial", "graf transpus", "graf complet"], 1, "Graf parțial."),
          ("Câte grafuri neorientate cu 4 noduri date există?", ["16", "64", "4096", "24"], 1, "2⁶ = 64."),
          ("Un graf este bipartit dacă și numai dacă:", ["este conex", "nu are cicluri de lungime impară", "are toate gradele pare", "este complet"], 1, "Teorema lui König.")],
))

LECTII.append(dict(
    id="a8", nr="8", scurt="Parcurgeri BFS și DFS", titlu="Parcurgerea grafurilor: în lățime (BFS) și în adâncime (DFS)",
    programa="Programa cap. 3: metoda de parcurgere în lățime (BFS) și în adâncime (DFS)",
    obiective=["BFS cu o coadă și distanța minimă în număr de muchii", "DFS recursiv și iterativ", "aplicații: componente conexe, verificarea bipartiției, lanțul minim"],
    teorie=f"""
{CO('''from collections import deque

def bfs(L, s, n):
    dist = [-1] * (n + 1)
    dist[s] = 0
    q, ordine = deque([s]), []
    while q:
        x = q.popleft(); ordine.append(x)
        for y in L[x]:
            if dist[y] == -1:          # nevizitat
                dist[y] = dist[x] + 1
                q.append(y)
    return ordine, dist

def dfs(L, x, viz, ordine):
    viz[x] = True; ordine.append(x)
    for y in L[x]:
        if not viz[y]:
            dfs(L, y, viz, ordine)

n = 6
L = [[], [2, 3], [1, 4], [1, 4, 6], [2, 3, 5], [4, 6], [3, 5]]   # vecinii în ordine crescătoare
o, d = bfs(L, 1, n); print(o, d[1:])
o2 = []; dfs(L, 1, [False] * (n + 1), o2); print(o2)''')}
<ul>
<li>Ambele parcurgeri au complexitatea O(n + m) cu liste de adiacență (O(n²) cu matrice).</li>
<li>BFS vizitează nodurile în ordinea distanței față de sursă ⇒ <strong>lanț minim</strong> în graf neponderat. Pentru a reconstitui lanțul se memorează tatăl fiecărui nod.</li>
<li>Numărul de <strong>componente conexe</strong> = de câte ori pornim o nouă parcurgere dintr-un nod nevizitat.</li>
<li>Un graf este <strong>bipartit</strong> dacă îl putem colora cu 2 culori în timpul parcurgerii fără conflict.</li>
<li>Ordinea parcurgerii depinde de ordinea vecinilor – în subiecte se precizează de obicei „vecinii în ordine crescătoare”.</li>
</ul>
""",
    rezolvate=[],
    exercitii=[
        dict(titlu="Parcurgerile BFS și DFS", nivel="ușor", enunt=GRAF_IN + " Pe ultima linie se dă nodul de start s. Vecinii se parcurg în ordine crescătoare. Afișează ordinea BFS pe prima linie și ordinea DFS pe a doua.",
             sol="import sys\nsys.setrecursionlimit(10000)\nfrom collections import deque\nn, m = map(int, input().split())\nL = [[] for _ in range(n + 1)]\nfor _ in range(m):\n    x, y = map(int, input().split())\n    L[x].append(y); L[y].append(x)\nfor v in L: v.sort()\ns = int(input())\nviz = [False] * (n + 1); viz[s] = True\nq, o = deque([s]), []\nwhile q:\n    x = q.popleft(); o.append(x)\n    for y in L[x]:\n        if not viz[y]:\n            viz[y] = True; q.append(y)\nprint(*o)\nviz = [False] * (n + 1); o = []\ndef dfs(x):\n    viz[x] = True; o.append(x)\n    for y in L[x]:\n        if not viz[y]: dfs(y)\ndfs(s)\nprint(*o)",
             teste=[{"in": "6 7\n1 2\n1 3\n2 4\n3 4\n4 5\n5 6\n3 6\n1"}, {"in": "5 4\n1 2\n1 3\n2 4\n2 5\n2"}, {"in": "3 0\n2"}]),
        dict(titlu="Componente conexe", nivel="mediu", enunt=GRAF_IN + " Afișează numărul de componente conexe, apoi, pe câte o linie, nodurile fiecărei componente în ordine crescătoare (componentele ordonate după cel mai mic nod).",
             sol="from collections import deque\nn, m = map(int, input().split())\nL = [[] for _ in range(n + 1)]\nfor _ in range(m):\n    x, y = map(int, input().split())\n    L[x].append(y); L[y].append(x)\nviz = [False] * (n + 1)\ncomp = []\nfor s in range(1, n + 1):\n    if not viz[s]:\n        viz[s] = True; q = deque([s]); c = []\n        while q:\n            x = q.popleft(); c.append(x)\n            for y in L[x]:\n                if not viz[y]:\n                    viz[y] = True; q.append(y)\n        comp.append(sorted(c))\nprint(len(comp))\nfor c in comp:\n    print(*c)",
             teste=[{"in": "7 4\n1 2\n2 3\n4 5\n6 7"}, {"in": "3 0"}, {"in": "4 3\n1 4\n4 2\n2 3"}]),
        dict(titlu="Lanțul minim", nivel="dificil", enunt=GRAF_IN + " Pe ultima linie se dau două noduri a și b. Afișează lungimea (în muchii) a celui mai scurt lanț de la a la b și lanțul (vecinii în ordine crescătoare, deci lanțul găsit de BFS), sau <code>-1</code> dacă nu există.",
             sol="from collections import deque\nn, m = map(int, input().split())\nL = [[] for _ in range(n + 1)]\nfor _ in range(m):\n    x, y = map(int, input().split())\n    L[x].append(y); L[y].append(x)\nfor v in L: v.sort()\na, b = map(int, input().split())\ntata = [0] * (n + 1); d = [-1] * (n + 1); d[a] = 0\nq = deque([a])\nwhile q:\n    x = q.popleft()\n    for y in L[x]:\n        if d[y] == -1:\n            d[y] = d[x] + 1; tata[y] = x; q.append(y)\nif d[b] == -1:\n    print(-1)\nelse:\n    drum = [b]\n    while drum[-1] != a:\n        drum.append(tata[drum[-1]])\n    print(d[b])\n    print(*drum[::-1])",
             teste=[{"in": "6 7\n1 2\n1 3\n2 4\n3 4\n4 5\n5 6\n3 6\n1 5"}, {"in": "4 2\n1 2\n3 4\n1 4"}, {"in": "2 1\n1 2\n2 2"}]),
        dict(titlu="Bipartit?", nivel="dificil", enunt=GRAF_IN + " Afișează <code>DA</code> dacă graful este bipartit, altfel <code>NU</code>. (Graful poate avea mai multe componente conexe.)",
             sol="from collections import deque\nn, m = map(int, input().split())\nL = [[] for _ in range(n + 1)]\nfor _ in range(m):\n    x, y = map(int, input().split())\n    L[x].append(y); L[y].append(x)\nc = [-1] * (n + 1)\nok = True\nfor s in range(1, n + 1):\n    if c[s] == -1:\n        c[s] = 0; q = deque([s])\n        while q and ok:\n            x = q.popleft()\n            for y in L[x]:\n                if c[y] == -1:\n                    c[y] = 1 - c[x]; q.append(y)\n                elif c[y] == c[x]:\n                    ok = False\nprint('DA' if ok else 'NU')",
             teste=[{"in": "4 4\n1 2\n2 3\n3 4\n4 1"}, {"in": "3 3\n1 2\n2 3\n3 1"}, {"in": "5 2\n1 2\n4 5"}]),
    ],
    quiz=[("Ce structură de date folosește BFS?", ["stivă", "coadă", "heap", "matrice"], 1, "Coada asigură ordinea pe niveluri."),
          ("Complexitatea BFS cu liste de adiacență este:", ["O(n²)", "O(n + m)", "O(n · m)", "O(m log n)"], 1, "Fiecare nod și fiecare muchie sunt prelucrate de un număr constant de ori."),
          ("Cum afli numărul de componente conexe?", ["numărul de muchii − n", "de câte ori pornești o parcurgere dintr-un nod nevizitat", "gradul maxim", "n − 1"], 1, "Fiecare parcurgere nouă descoperă o componentă."),
          ("Care parcurgere dă lanțul cu cele mai puține muchii?", ["DFS", "BFS", "ambele", "niciuna"], 1, "BFS vizitează nodurile în ordinea distanței.")],
))

LECTII.append(dict(
    id="a9", nr="9", scurt="Drumuri minime", titlu="Drumuri minime: Dijkstra, Roy-Floyd și Roy-Warshall",
    programa="Programa cap. 3: algoritmul lui Dijkstra, algoritmul Roy-Floyd, algoritmul Roy-Warshall",
    obiective=["Dijkstra pentru drumuri minime de la o sursă (costuri nenegative)", "Roy-Floyd pentru toate perechile", "Roy-Warshall pentru matricea drumurilor (închiderea tranzitivă)"],
    teorie=f"""
{C('''import heapq
def dijkstra(L, s, n):                  # L[x] = [(y, cost), ...]
    INF = float("inf")
    d = [INF] * (n + 1); d[s] = 0
    pq = [(0, s)]
    while pq:
        dx, x = heapq.heappop(pq)
        if dx > d[x]:
            continue                    # intrare veche, deja îmbunătățită
        for y, c in L[x]:
            if d[x] + c < d[y]:
                d[y] = d[x] + c
                heapq.heappush(pq, (d[y], y))
    return d''')}
<p>Varianta clasică din manuale, fără heap: de n ori se alege nodul nefixat cu distanța minimă, se fixează și se relaxează muchiile lui – O(n²). Cu heap: O(m log n). <strong>Nu funcționează cu costuri negative.</strong></p>
{C('''def roy_floyd(d, n):                  # d = matricea costurilor, INF unde nu există muchie, 0 pe diagonală
    for k in range(1, n + 1):           # k – nodul intermediar, OBLIGATORIU bucla exterioară
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if d[i][k] + d[k][j] < d[i][j]:
                    d[i][j] = d[i][k] + d[k][j]

def roy_warshall(a, n):                 # a = matricea de adiacență (0/1)
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if a[i][k] and a[k][j]:
                    a[i][j] = 1''')}
<p>Ambele sunt O(n³). După Roy-Warshall, <code>a[i][j] = 1</code> ⇔ există drum de la i la j; un graf orientat este tare conex ⇔ matricea drumurilor are 1 peste tot în afara diagonalei.</p>
""",
    rezolvate=[],
    exercitii=[
        dict(titlu="Dijkstra", nivel="mediu", enunt="Graf <strong>orientat</strong> ponderat: pe prima linie n, m și sursa s, apoi m linii <code>x y c</code> (arc de la x la y cu costul c ≥ 0). Afișează costul minim de la s la fiecare nod 1..n, pe o linie, cu <code>-1</code> pentru nodurile inaccesibile.",
             sol="import heapq\nn, m, s = map(int, input().split())\nL = [[] for _ in range(n + 1)]\nfor _ in range(m):\n    x, y, c = map(int, input().split())\n    L[x].append((y, c))\nINF = float('inf')\nd = [INF] * (n + 1); d[s] = 0\npq = [(0, s)]\nwhile pq:\n    dx, x = heapq.heappop(pq)\n    if dx > d[x]: continue\n    for y, c in L[x]:\n        if d[x] + c < d[y]:\n            d[y] = d[x] + c; heapq.heappush(pq, (d[y], y))\nprint(*[v if v < INF else -1 for v in d[1:]])",
             teste=[{"in": "5 7 1\n1 2 4\n1 3 1\n3 2 2\n2 4 1\n3 4 5\n4 5 3\n5 1 1"}, {"in": "3 1 2\n1 2 5"}, {"in": "4 4 1\n1 2 0\n2 3 0\n3 4 7\n1 4 10"}]),
        dict(titlu="Roy-Floyd", nivel="mediu", enunt="Graf orientat ponderat: pe prima linie n și m, apoi m arce <code>x y c</code>. Afișează matricea drumurilor minime (n linii), cu <code>-</code> acolo unde nu există drum (pe diagonală 0).",
             sol="n, m = map(int, input().split())\nINF = float('inf')\nd = [[0 if i == j else INF for j in range(n + 1)] for i in range(n + 1)]\nfor _ in range(m):\n    x, y, c = map(int, input().split())\n    d[x][y] = min(d[x][y], c)\nfor k in range(1, n + 1):\n    for i in range(1, n + 1):\n        for j in range(1, n + 1):\n            if d[i][k] + d[k][j] < d[i][j]:\n                d[i][j] = d[i][k] + d[k][j]\nfor i in range(1, n + 1):\n    print(*['-' if d[i][j] == INF else d[i][j] for j in range(1, n + 1)])",
             teste=[{"in": "4 6\n1 2 3\n2 3 2\n3 4 1\n4 1 2\n1 4 7\n2 1 8"}, {"in": "3 1\n1 2 5"}]),
        dict(titlu="Tare conex? (Roy-Warshall)", nivel="dificil", enunt="Graf orientat: pe prima linie n și m, apoi m arce <code>x y</code>. Aplică Roy-Warshall și afișează matricea drumurilor (n linii, valori 0/1, cu a[i][i] = 1 doar dacă i se află pe un circuit), apoi <code>tare conex</code> sau <code>nu</code>.",
             sol="n, m = map(int, input().split())\na = [[0] * (n + 1) for _ in range(n + 1)]\nfor _ in range(m):\n    x, y = map(int, input().split())\n    a[x][y] = 1\nfor k in range(1, n + 1):\n    for i in range(1, n + 1):\n        for j in range(1, n + 1):\n            if a[i][k] and a[k][j]:\n                a[i][j] = 1\nfor i in range(1, n + 1):\n    print(*a[i][1:])\nok = all(a[i][j] for i in range(1, n + 1) for j in range(1, n + 1) if i != j)\nprint('tare conex' if ok else 'nu')",
             teste=[{"in": "4 5\n1 2\n2 3\n3 1\n3 4\n4 3"}, {"in": "3 2\n1 2\n2 3"}]),
    ],
    quiz=[("Ce restricție are algoritmul lui Dijkstra?", ["graful trebuie să fie neorientat", "costurile trebuie să fie nenegative", "graful trebuie să fie complet", "maxim 100 de noduri"], 1, "Costurile negative invalidează fixarea definitivă a nodurilor."),
          ("În Roy-Floyd, bucla pe nodul intermediar k trebuie să fie:", ["cea interioară", "cea exterioară", "oricare", "doar pentru k par"], 1, "Altfel nu se iau în calcul corect toate drumurile prin nodurile 1..k."),
          ("Ce calculează Roy-Warshall?", ["costurile minime", "matricea drumurilor (dacă există drum)", "arborele parțial de cost minim", "gradele"], 1, "Închiderea tranzitivă."),
          ("Complexitatea lui Roy-Floyd este:", ["O(n²)", "O(n³)", "O(m log n)", "O(n + m)"], 1, "Trei bucle imbricate.")],
))

LECTII.append(dict(
    id="a10", nr="10", scurt="Arbore parțial de cost minim", titlu="Arborele parțial de cost minim: Prim și Kruskal",
    programa="Programa cap. 3: algoritmul lui Prim, algoritmul lui Kruskal",
    obiective=["ce este un arbore parțial de cost minim (APM)", "algoritmul lui Kruskal cu structura union-find", "algoritmul lui Prim", "de ce ambele sunt algoritmi greedy"],
    teorie=f"""
<p>Pentru un graf neorientat, conex și ponderat, un <strong>arbore parțial</strong> păstrează toate cele n noduri și n − 1 muchii, fără cicluri. Cel de <strong>cost minim</strong> are suma costurilor minimă (de exemplu, cablarea cea mai ieftină a unor clădiri).</p>
{C('''def kruskal(n, muchii):               # muchii = [(cost, x, y), ...]
    tata = list(range(n + 1))
    def rad(x):                         # rădăcina mulțimii lui x (cu comprimarea drumului)
        while tata[x] != x:
            tata[x] = tata[tata[x]]
            x = tata[x]
        return x
    cost, alese = 0, []
    for c, x, y in sorted(muchii):      # muchiile în ordinea crescătoare a costului
        rx, ry = rad(x), rad(y)
        if rx != ry:                    # nu formează ciclu
            tata[rx] = ry
            cost += c; alese.append((x, y))
    return cost, alese''')}
<p><strong>Prim</strong>: pornește dintr-un nod și adaugă repetat cea mai ieftină muchie care leagă arborele de un nod din afara lui (cu heap: O(m log n)). <strong>Kruskal</strong>: sortează muchiile și le adaugă pe cele care nu închid un ciclu (O(m log m)). Când costurile sunt distincte, APM este unic și ambii algoritmi îl găsesc.</p>
""",
    rezolvate=[],
    exercitii=[
        dict(titlu="Kruskal", nivel="mediu", enunt="Pe prima linie n și m, apoi m muchii <code>x y c</code> ale unui graf neorientat conex. Afișează costul arborelui parțial de cost minim.",
             sol="n, m = map(int, input().split())\nE = []\nfor _ in range(m):\n    x, y, c = map(int, input().split())\n    E.append((c, x, y))\nt = list(range(n + 1))\ndef r(x):\n    while t[x] != x:\n        t[x] = t[t[x]]; x = t[x]\n    return x\ncost = 0\nfor c, x, y in sorted(E):\n    a, b = r(x), r(y)\n    if a != b:\n        t[a] = b; cost += c\nprint(cost)",
             teste=[{"in": "6 9\n1 2 7\n1 3 9\n1 6 14\n2 3 10\n2 4 15\n3 4 11\n3 6 2\n4 5 6\n5 6 9"}, {"in": "2 1\n1 2 5"}, {"in": "4 6\n1 2 1\n1 3 1\n1 4 1\n2 3 1\n2 4 1\n3 4 1"}]),
        dict(titlu="Prim, cu muchiile alese", nivel="dificil", enunt="Aceleași date ca mai sus. Aplică algoritmul lui Prim pornind din nodul 1 și afișează muchiile în ordinea în care sunt adăugate, ca <code>x y c</code> (x – nodul deja în arbore), apoi costul total. La costuri egale, alege muchia cu nodul nou cel mai mic. Folosește heapq cu tupluri (cost, nod_nou, nod_din_arbore).",
             sol="import heapq\nn, m = map(int, input().split())\nL = [[] for _ in range(n + 1)]\nfor _ in range(m):\n    x, y, c = map(int, input().split())\n    L[x].append((y, c)); L[y].append((x, c))\nin_arb = [False] * (n + 1)\nin_arb[1] = True\npq = [(c, y, 1) for y, c in L[1]]\nheapq.heapify(pq)\ntotal = 0\nwhile pq:\n    c, y, x = heapq.heappop(pq)\n    if in_arb[y]: continue\n    in_arb[y] = True\n    print(x, y, c); total += c\n    for z, cz in L[y]:\n        if not in_arb[z]:\n            heapq.heappush(pq, (cz, z, y))\nprint(total)",
             teste=[{"in": "6 9\n1 2 7\n1 3 9\n1 6 14\n2 3 10\n2 4 15\n3 4 11\n3 6 2\n4 5 6\n5 6 9"}, {"in": "3 3\n1 2 1\n2 3 1\n1 3 1"}]),
        dict(titlu="Componente cu union-find", nivel="mediu", enunt="Pe prima linie n și q, apoi q operații: <code>U x y</code> (unește mulțimile lui x și y) sau <code>Q x y</code> (afișează <code>DA</code> dacă x și y sunt în aceeași mulțime, altfel <code>NU</code>). La final afișează numărul de mulțimi.",
             sol="n, q = map(int, input().split())\nt = list(range(n + 1))\ndef r(x):\n    while t[x] != x:\n        t[x] = t[t[x]]; x = t[x]\n    return x\nk = n\nfor _ in range(q):\n    op, x, y = input().split()\n    a, b = r(int(x)), r(int(y))\n    if op == 'U':\n        if a != b:\n            t[a] = b; k -= 1\n    else:\n        print('DA' if a == b else 'NU')\nprint(k)",
             teste=[{"in": "5 6\nU 1 2\nQ 1 2\nQ 1 3\nU 3 4\nU 2 4\nQ 1 3"}, {"in": "3 1\nQ 1 1"}]),
    ],
    quiz=[("Câte muchii are un arbore parțial al unui graf conex cu 10 noduri?", ["10", "9", "45", "depinde de graf"], 1, "n − 1."),
          ("Kruskal adaugă o muchie dacă:", ["are cost minim global", "nu formează ciclu cu muchiile alese", "pleacă din nodul 1", "are cost par"], 1, "Verificarea se face cu union-find."),
          ("Prim și Kruskal sunt algoritmi de tip:", ["backtracking", "greedy", "divide et impera", "programare dinamică"], 1, "Aleg la fiecare pas muchia cea mai ieftină permisă.")],
))

LECTII.append(dict(
    id="a11", nr="11", scurt="Arbori, ABC, heap", titlu="Arbori: vectorul de tați, arbori binari, arbori binari de căutare, ansamblu (heap)",
    programa="Programa cap. 1: modelul ierarhic – arbore cu rădăcină, ordonat, binar, binar de căutare, binar complet, heap; cap. 3: parcurgeri în preordine, inordine, postordine",
    obiective=["vectorul de tați: rădăcină, frunze, niveluri, înălțime", "parcurgerile unui arbore binar", "inserarea și căutarea în ABC", "heap-ul: inserare, extragerea minimului, heapq"],
    teorie=f"""
<ul>
<li><strong>Arbore</strong> = graf conex fără cicluri; n noduri ⇒ n − 1 muchii. Cu rădăcină se memorează prin <strong>vectorul de tați</strong>: <code>tata[rad] = 0</code>. Frunzele sunt nodurile care nu apar în vector. Nivelul (adâncimea) unui nod = numărul de muchii până la rădăcină; înălțimea = nivelul maxim.</li>
<li><strong>Arbore binar</strong>: fiecare nod are cel mult doi fii (stâng, drept). Pe nivelul k: cel mult 2<sup>k</sup> noduri; de înălțime h: cel mult 2<sup>h+1</sup> − 1 noduri.</li>
<li><strong>Arbore binar complet</strong>: toate nivelurile pline, cu excepția ultimului, completat de la stânga. Se memorează într-un vector: fiii nodului i (de la 1) sunt 2i și 2i + 1.</li>
<li><strong>ABC</strong>: stânga &lt; rădăcina &lt; dreapta în fiecare nod; <strong>inordinea</strong> dă cheile sortate. Căutare/inserare în O(h).</li>
<li><strong>Heap (ansamblu)</strong>: arbore binar complet; în min-heap fiecare părinte ≤ fiii. Inserare: urcare (sift-up); extragerea minimului: ultimul element trece în rădăcină și coboară (sift-down) – ambele O(log n). În Python: modulul <code>heapq</code> (min-heap pe o listă).</li>
</ul>
{CO('''class Nod:
    def __init__(self, k):
        self.k, self.st, self.dr = k, None, None

def insereaza(r, k):
    if r is None:
        return Nod(k)
    if k < r.k: r.st = insereaza(r.st, k)
    else:       r.dr = insereaza(r.dr, k)
    return r

def preordine(r):  return [] if r is None else [r.k] + preordine(r.st) + preordine(r.dr)
def inordine(r):   return [] if r is None else inordine(r.st) + [r.k] + inordine(r.dr)
def postordine(r): return [] if r is None else postordine(r.st) + postordine(r.dr) + [r.k]

r = None
for k in [50, 30, 70, 20, 40, 60, 80, 35]:
    r = insereaza(r, k)
print(preordine(r)); print(inordine(r)); print(postordine(r))

import heapq
h = []
for x in [5, 3, 8, 1, 9]:
    heapq.heappush(h, x)
print(h, heapq.heappop(h), h)''')}
""",
    rezolvate=[],
    exercitii=[
        dict(titlu="Vectorul de tați", nivel="mediu", enunt="Pe prima linie n, pe a doua vectorul de tați (tata[i] pentru i = 1..n, 0 pentru rădăcină). Afișează pe linii separate: rădăcina, frunzele (crescător) și înălțimea arborelui.",
             sol="n = int(input())\nt = [0] + list(map(int, input().split()))\nrad = t.index(0, 1)\nfrunze = [i for i in range(1, n + 1) if i not in set(t[1:])]\ndef niv(i):\n    k = 0\n    while t[i]:\n        i = t[i]; k += 1\n    return k\nprint(rad)\nprint(*frunze)\nprint(max(niv(i) for i in range(1, n + 1)))",
             teste=[{"in": "6\n2 0 2 1 1 3"}, {"in": "1\n0"}, {"in": "5\n0 1 2 3 4"}]),
        dict(titlu="Parcurgerile unui ABC", nivel="mediu", enunt="Se citesc chei întregi distincte, pe o linie. Inserează-le, în ordine, într-un arbore binar de căutare inițial vid. Afișează parcurgerile în preordine, inordine și postordine (câte una pe linie) și înălțimea arborelui.",
             sol="import sys\nsys.setrecursionlimit(10000)\nclass N:\n    def __init__(s, k): s.k = k; s.st = s.dr = None\ndef ins(r, k):\n    if r is None: return N(k)\n    if k < r.k: r.st = ins(r.st, k)\n    else: r.dr = ins(r.dr, k)\n    return r\ndef pre(r): return [] if r is None else [r.k] + pre(r.st) + pre(r.dr)\ndef ino(r): return [] if r is None else ino(r.st) + [r.k] + ino(r.dr)\ndef post(r): return [] if r is None else post(r.st) + post(r.dr) + [r.k]\ndef h(r): return -1 if r is None else 1 + max(h(r.st), h(r.dr))\nr = None\nfor k in map(int, input().split()):\n    r = ins(r, k)\nprint(*pre(r)); print(*ino(r)); print(*post(r)); print(h(r))",
             teste=[{"in": "50 30 70 20 40 60 80 35"}, {"in": "1 2 3 4"}, {"in": "8"}]),
        dict(titlu="Cele mai mici k valori (heap)", nivel="mediu", enunt="Pe prima linie n și k, pe a doua n numere întregi. Afișează cele mai mici k valori în ordine crescătoare, folosind <code>heapq</code> (heapify + heappop de k ori).",
             sol="import heapq\nn, k = map(int, input().split())\nv = list(map(int, input().split()))\nheapq.heapify(v)\nprint(*[heapq.heappop(v) for _ in range(k)])",
             teste=[{"in": "8 3\n5 1 9 3 7 2 8 6"}, {"in": "3 3\n3 2 1"}, {"in": "5 1\n-1 -5 0 4 2"}]),
        dict(titlu="Min-heap scris de mână", nivel="dificil", enunt="Implementează un min-heap într-o listă (fără heapq). Pe prima linie n, apoi n comenzi: <code>ins x</code> sau <code>ext</code> (afișează și elimină minimul; <code>gol</code> dacă heap-ul este vid). La final afișează lista internă a heap-ului (sau <code>vid</code>).",
             sol="h = []\ndef ins(x):\n    h.append(x); i = len(h) - 1\n    while i > 0 and h[(i - 1) // 2] > h[i]:\n        p = (i - 1) // 2; h[p], h[i] = h[i], h[p]; i = p\ndef ext():\n    m = h[0]; h[0] = h[-1]; h.pop(); i = 0\n    while True:\n        a, b, c = i, 2 * i + 1, 2 * i + 2\n        if b < len(h) and h[b] < h[a]: a = b\n        if c < len(h) and h[c] < h[a]: a = c\n        if a == i: break\n        h[a], h[i] = h[i], h[a]; i = a\n    return m\nn = int(input())\nfor _ in range(n):\n    c = input().split()\n    if c[0] == 'ins': ins(int(c[1]))\n    else: print(ext() if h else 'gol')\nprint(*h if h else ['vid'])",
             teste=[{"in": "8\nins 5\nins 3\nins 8\nins 1\next\nins 9\nins 2\next"}, {"in": "2\next\nins 4"}]),
    ],
    quiz=[("Ce parcurgere a unui ABC dă cheile sortate crescător?", ["preordine", "inordine", "postordine", "în lățime"], 1, "Stânga – rădăcină – dreapta."),
          ("Într-un arbore binar complet memorat în vector de la poziția 1, fiii nodului 5 sunt:", ["6 și 7", "10 și 11", "9 și 10", "4 și 6"], 1, "2i și 2i + 1."),
          ("Cât costă extragerea minimului dintr-un min-heap cu n elemente?", ["O(1)", "O(log n)", "O(n)", "O(n log n)"], 1, "Elementul coboară pe cel mult înălțimea arborelui."),
          ("Un arbore binar de înălțime 3 are cel mult:", ["7 noduri", "8 noduri", "15 noduri", "16 noduri"], 2, "2⁴ − 1 = 15."),
          ("În vectorul de tați, frunzele sunt nodurile care:", ["au tata = 0", "nu apar ca valoare în vector", "au cel mai mare număr", "apar de două ori"], 1, "Nu sunt tată pentru niciun nod.")],
))

LECTII.append(dict(
    id="a12", nr="12", scurt="Criptare, Fletcher, Flood Fill", titlu="Criptare, verificarea integrității și Flood Fill",
    programa="Programa cap. 3: substituție monoalfabetică, cifrul lui Cezar, cifrul Vigenère, algoritmul lui Fletcher; algoritmi de umplere (Flood Fill)",
    obiective=["cifrurile din programă și cum se sparg", "suma de control Fletcher-16 și de ce detectează inversările", "Flood Fill recursiv și iterativ"],
    teorie=f"""
{T(["Metodă", "Criptare", "Slăbiciune"],
   ["Substituție monoalfabetică", "fiecare literă → litera corespunzătoare dintr-un alfabet permutat (cheia)", "analiza frecvenței literelor"],
   ["Cezar", "c = (p + k) mod 26", "doar 25 de chei – forță brută"],
   ["Vigenère", "litera i se deplasează cu litera i mod |cheie| a cheii (A = 0)", "dacă se află lungimea cheii, devine o serie de cifruri Cezar"])}
{CO('''def vigenere(text, cheie, semn=1):          # semn = -1 pentru decriptare
    rez, j = [], 0
    for c in text:
        if c.isupper():
            d = ord(cheie[j % len(cheie)]) - 65
            rez.append(chr((ord(c) - 65 + semn * d) % 26 + 65)); j += 1
        else:
            rez.append(c)
    return "".join(rez)

def fletcher16(octeti):
    s1 = s2 = 0
    for b in octeti:
        s1 = (s1 + b) % 255
        s2 = (s2 + s1) % 255
    return s2 * 256 + s1

print(vigenere("ATTACK AT DAWN", "LEMON"), fletcher16(b"abcde"), fletcher16(b"AB"), fletcher16(b"BA"))''')}
<p><strong>Fletcher</strong> nu criptează: produce o <em>sumă de control</em> trimisă împreună cu datele; destinatarul o recalculează și detectează modificările. Spre deosebire de o simplă sumă a octeților, a doua sumă (s2) depinde de poziție, deci „AB” și „BA” dau valori diferite.</p>
<p><strong>Flood Fill</strong> marchează toate celulele unei zone pornind dintr-o celulă: DFS (recursiv sau cu stivă) sau BFS (cu coadă). Pentru grile mari se preferă varianta cu stivă/coadă (limita de recursivitate din Python).</p>
""",
    rezolvate=[],
    exercitii=[
        dict(titlu="Spargerea cifrului lui Cezar", nivel="mediu", enunt="Se citește un text criptat cu Cezar (litere mari și spații) și un cuvânt despre care se știe că apare în textul clar. Găsește cheia k (0..25) și afișează k și textul decriptat; dacă sunt mai multe chei posibile, alege-o pe cea mai mică.",
             sol="t = input()\nw = input()\nfor k in range(26):\n    d = ''.join(chr((ord(c) - 65 - k) % 26 + 65) if c.isupper() else c for c in t)\n    if w in d.split():\n        print(k); print(d); break",
             teste=[{"in": "LQIRUPDWLFD HVWH IUXPRDVD\nESTE"}, {"in": "ABC\nABC"}, {"in": "BMFDF\nALECE"}]),
        dict(titlu="Vigenère", nivel="mediu", enunt="Pe prima linie <code>C</code> (criptare) sau <code>D</code> (decriptare), pe a doua cheia (litere mari), pe a treia textul (litere mari, spații și alte semne care rămân neschimbate; cheia avansează doar la litere). Afișează rezultatul.",
             sol="op = input().strip()\nk = input().strip()\nt = input()\ns = 1 if op == 'C' else -1\nr, j = [], 0\nfor c in t:\n    if 'A' <= c <= 'Z':\n        r.append(chr((ord(c) - 65 + s * (ord(k[j % len(k)]) - 65)) % 26 + 65)); j += 1\n    else:\n        r.append(c)\nprint(''.join(r))",
             teste=[{"in": "C\nLEMON\nATTACK AT DAWN"}, {"in": "D\nLEMON\nLXFOPV EF RNHR"}, {"in": "C\nCAT\nPROFESOR, 2026!"}]),
        dict(titlu="Fletcher-16", nivel="ușor", enunt="Se citește o linie de text (caractere ASCII). Afișează suma de control Fletcher-16 a octeților textului, în zecimal, și apoi în hexazecimal cu 4 cifre mari (de exemplu <code>C8F0</code>).",
             sol="s1 = s2 = 0\nfor b in input().encode():\n    s1 = (s1 + b) % 255\n    s2 = (s2 + s1) % 255\nv = s2 * 256 + s1\nprint(v)\nprint(f'{v:04X}')",
             teste=[{"in": "abcde"}, {"in": "abcdef"}, {"in": "Titularizare 2026"}]),
        dict(titlu="Cea mai mare zonă", nivel="dificil", enunt="Pe prima linie n și m, apoi n linii cu m caractere (<code>#</code> uscat, <code>.</code> apă). Afișează numărul de insule (zone de <code>#</code> vecine pe orizontală/verticală) și suprafața celei mai mari insule (0 dacă nu există).",
             sol="n, m = map(int, input().split())\ng = [list(input()) for _ in range(n)]\nnr = mx = 0\nfor i in range(n):\n    for j in range(m):\n        if g[i][j] == '#':\n            nr += 1; g[i][j] = '.'; st = [(i, j)]; s = 0\n            while st:\n                x, y = st.pop(); s += 1\n                for a, b in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):\n                    if 0 <= a < n and 0 <= b < m and g[a][b] == '#':\n                        g[a][b] = '.'; st.append((a, b))\n            mx = max(mx, s)\nprint(nr, mx)",
             teste=[{"in": "4 5\n##...\n##.##\n...#.\n#.###"}, {"in": "2 2\n..\n.."}, {"in": "1 5\n#.#.#"}]),
    ],
    quiz=[("Câte chei utile are cifrul lui Cezar pe alfabetul englez?", ["26", "25", "26!", "13"], 1, "Cheia 0 lasă textul neschimbat."),
          ("Ce scop are algoritmul lui Fletcher?", ["criptare", "verificarea integrității datelor", "compresie", "sortare"], 1, "Este o sumă de control."),
          ("Cum se sparge de obicei o substituție monoalfabetică?", ["forță brută pe 26 de chei", "analiza frecvenței literelor", "nu se poate", "cu Dijkstra"], 1, "Literele frecvente ale limbii rămân frecvente în textul criptat."),
          ("De ce Fletcher detectează inversarea a doi octeți, iar suma simplă nu?", ["folosește modulo 255", "a doua sumă depinde de poziția octeților", "folosește criptare", "nu detectează"], 1, "s2 acumulează sumele parțiale.")],
))
