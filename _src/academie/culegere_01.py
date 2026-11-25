import random
from util import P, T

LECTII = []
R = random.Random(2026)


def lista(n, a, b):
    return " ".join(str(R.randint(a, b)) for _ in range(n))


SFAT = """<div class="note"><b>Cum lucrezi cu culegerea:</b> întâi scrii pe hârtie, apoi copiezi în editor. Pornește <b>Modul examen</b> (sus, în antet): soluțiile dispar, testele devin ascunse și se cronometrează fiecare problemă. Testele includ cazuri limită și, la unele probleme, date mari – o soluție corectă, dar prea lentă, depășește timpul.</div>"""

# ---------------------------------------------------------------- 1. Numere și cifre
LECTII.append(dict(
    id="g1", nr="1", scurt="Numere și cifre", titlu="Capitolul 1 – Numere și cifre",
    programa="Programa cap. 3 (*): prelucrări ale datelor numerice, cifre, divizibilitate, Euclid, ciur, baze de numerație, exponențiere rapidă",
    obiective=["prelucrarea cifrelor fără greșeli la 0 și la numerele cu o cifră", "divizibilitate eficientă (√n, ciur, Legendre)", "conversii între baze"],
    teorie=SFAT + """
<h3>Capcane frecvente în acest capitol</h3>
<ul><li>n = 0 are o cifră; o buclă <code>while n &gt; 0</code> nu o vede.</li><li>Numerele mari (până la 10<sup>18</sup>): în Python nu există depășire, dar algoritmii O(n) devin prea lenți.</li><li>„Cel mult” / „cel puțin”, interval închis sau deschis – citește de două ori restricțiile.</li></ul>""",
    exercitii=[
        P("Cifra de control", "ușor", "Se citește un număr natural n (n ≤ 10<sup>18</sup>). Se înlocuiește repetat n cu suma cifrelor sale până când rămâne o singură cifră. Afișează cifra obținută.",
          "n = int(input())\nwhile n > 9:\n    s = 0\n    while n:\n        s += n % 10\n        n //= 10\n    n = s\nprint(n)",
          "2026", "0", "7", "999999999999999999", "123456789012345678"),
        P("Numere cu suma cifrelor divizibilă cu k", "ușor", "Se citesc a, b și k (1 ≤ a ≤ b ≤ 10<sup>5</sup>, k ≥ 1). Afișează câte numere din [a, b] au suma cifrelor divizibilă cu k.",
          "a, b, k = map(int, input().split())\ncnt = 0\nfor x in range(a, b + 1):\n    s = 0\n    while x:\n        s += x % 10\n        x //= 10\n    if s % k == 0:\n        cnt += 1\nprint(cnt)",
          "1 100 7", "10 10 1", "1 100000 9", "5 5 3"),
        P("Cel mai mare număr din cifre", "ușor", "Se citește un număr natural n. Afișează cel mai mare număr care se poate forma cu toate cifrele lui n.",
          "s = input().strip()\nprint(int(''.join(sorted(s, reverse=True))))",
          "2026", "0", "1000", "987654321", "50505"),
        P("Eliminarea cifrelor impare", "mediu", "Se citește n natural. Afișează numărul obținut prin eliminarea cifrelor impare ale lui n (cifrele rămase își păstrează ordinea; zerourile de la început dispar). Dacă nu rămâne nicio cifră, afișează <code>-1</code>.",
          "n = int(input())\nr, p, gasit = 0, 1, False\nif n == 0:\n    gasit = True\nwhile n:\n    c = n % 10\n    if c % 2 == 0:\n        r += c * p\n        p *= 10\n        gasit = True\n    n //= 10\nprint(r if gasit else -1)",
          "123456", "13579", "0", "2046", "102030", "1"),
        P("Numere perfecte", "mediu", "Un număr este perfect dacă este egal cu suma divizorilor săi mai mici decât el (6 = 1 + 2 + 3). Se citește n (n ≤ 10<sup>6</sup>). Afișează numerele perfecte ≤ n, pe o linie, sau <code>nu exista</code>. Atenție la timp: calculează suma divizorilor pentru toate numerele simultan (ca la ciur).",
          "n = int(input())\ns = [0] * (n + 1)\nfor d in range(1, n // 2 + 1):\n    for m in range(2 * d, n + 1, d):\n        s[m] += d\nrez = [x for x in range(2, n + 1) if s[x] == x]\nprint(*rez if rez else ['nu exista'])",
          "30", "5", "10000", "100000"),
        P("Descompunere în factori primi", "mediu", "Se citește n (2 ≤ n ≤ 10<sup>12</sup>). Afișează descompunerea în factori primi în formatul <code>2^3 * 3 * 5^2</code> (exponentul 1 nu se scrie).",
          "n = int(input())\nf = []\nd = 2\nwhile d * d <= n:\n    e = 0\n    while n % d == 0:\n        n //= d\n        e += 1\n    if e:\n        f.append(f'{d}^{e}' if e > 1 else str(d))\n    d += 1\nif n > 1:\n    f.append(str(n))\nprint(' * '.join(f))",
          "600", "2", "97", "1024", "999999000001", "735134400000"),
        P("Palindroame în baza 2", "mediu", "Se citesc a și b (1 ≤ a ≤ b ≤ 10<sup>5</sup>). Afișează câte numere din [a, b] au reprezentarea în baza 2 palindrom (de ex. 5 = 101₂).",
          "a, b = map(int, input().split())\nprint(sum(1 for x in range(a, b + 1) if bin(x)[2:] == bin(x)[2:][::-1]))",
          "1 10", "6 6", "1 100000", "100 200"),
        P("Al k-lea număr prim", "mediu", "Se citește k (1 ≤ k ≤ 10 000). Afișează al k-lea număr prim (primul este 2).",
          "k = int(input())\nN = 110000\np = bytearray([1]) * (N + 1)\np[0] = p[1] = 0\nfor i in range(2, int(N ** 0.5) + 1):\n    if p[i]:\n        p[i*i::i] = bytearray(len(range(i*i, N + 1, i)))\nc = 0\nfor i in range(N + 1):\n    if p[i]:\n        c += 1\n        if c == k:\n            print(i)\n            break",
          "1", "10", "1000", "10000"),
        P("Conversie între baze", "mediu", "Pe o linie se dau un număr scris în baza b1 (cifre 0–9 și litere mari A–F) și bazele b1 și b2 (2 ≤ b1, b2 ≤ 16). Afișează numărul în baza b2 (litere mari). Nu folosi <code>int(s, b)</code> – scrie conversia de mână.",
          "s, b1, b2 = input().split()\nb1, b2 = int(b1), int(b2)\nC = '0123456789ABCDEF'\nv = 0\nfor ch in s:\n    v = v * b1 + C.index(ch)\nif v == 0:\n    print(0)\nelse:\n    r = ''\n    while v:\n        r = C[v % b2] + r\n        v //= b2\n    print(r)",
          "7EA 16 2", "11111101010 2 10", "0 10 2", "FF 16 8", "2026 10 16", "1 2 16"),
        P("Prime gemene", "ușor", "Două numere prime p și p + 2 se numesc gemene. Se citește n (n ≤ 10<sup>6</sup>). Afișează numărul de perechi de prime gemene cu p + 2 ≤ n, iar pe linia următoare ultima pereche (sau <code>-</code> dacă nu există).",
          "n = int(input())\np = bytearray([1]) * (n + 3)\np[0] = p[1] = 0\nfor i in range(2, int((n + 2) ** 0.5) + 1):\n    if p[i]:\n        p[i*i::i] = bytearray(len(range(i*i, n + 3, i)))\ncnt, ult = 0, None\nfor x in range(2, n - 1):\n    if p[x] and p[x + 2]:\n        cnt += 1\n        ult = (x, x + 2)\nprint(cnt)\nprint(*ult if ult else ['-'])",
          "20", "4", "5", "1000000"),
        P("Zerouri la finalul lui n!", "dificil", "Se citește n (0 ≤ n ≤ 10<sup>12</sup>). Afișează numărul de zerouri de la sfârșitul lui n! (calcularea lui n! este imposibilă – numără factorii 5).",
          "n = int(input())\nz, p = 0, 5\nwhile p <= n:\n    z += n // p\n    p *= 5\nprint(z)",
          "10", "4", "0", "100", "1000000000000"),
        P("Cel mai mic multiplu comun al numerelor 1..n", "mediu", "Se citește n (1 ≤ n ≤ 100). Afișează cmmmc(1, 2, …, n).",
          "from math import gcd\nn = int(input())\nm = 1\nfor i in range(2, n + 1):\n    m = m * i // gcd(m, i)\nprint(m)",
          "10", "1", "20", "100"),
    ],
))

# ---------------------------------------------------------------- 2. Serii și liste
mare = lista(10000, -1000, 1000)
LECTII.append(dict(
    id="g2", nr="2", scurt="Serii de valori și liste", titlu="Capitolul 2 – Serii de valori și liste",
    programa="Programa cap. 3 (*): algoritmi pentru prelucrarea seriilor de valori; cap. 5.A (*): clasa list",
    obiective=["algoritmi într-o singură parcurgere (O(n))", "secvențe, platouri, sume maxime", "frecvențe și resturi"],
    teorie=SFAT + """
<h3>Format comun</h3><p>Dacă nu se precizează altfel, pe prima linie se dă n, iar pe a doua n numere întregi separate prin spații. Unele teste au 20 000 de valori – o soluție O(n²) depășește timpul.</p>""",
    exercitii=[
        P("Liderii", "mediu", "Un element este lider dacă este strict mai mare decât toate elementele aflate la dreapta lui (ultimul este mereu lider). Afișează liderii în ordinea din listă.",
          "n = int(input())\nv = list(map(int, input().split()))\nrez, mx = [], None\nfor x in reversed(v):\n    if mx is None or x > mx:\n        rez.append(x)\n        mx = x\nprint(*rez[::-1])",
          "7\n16 17 4 3 5 2 1", "1\n5", "4\n1 2 3 4", "5\n5 5 5 5 5", f"10000\n{mare}"),
        P("Platoul cel mai lung", "ușor", "Un platou este o secvență de elemente consecutive egale. Afișează lungimea celui mai lung platou și valoarea lui (primul, la egalitate).",
          "n = int(input())\nv = list(map(int, input().split()))\nbest, val, cur = 1, v[0], 1\nfor i in range(1, n):\n    cur = cur + 1 if v[i] == v[i - 1] else 1\n    if cur > best:\n        best, val = cur, v[i]\nprint(best, val)",
          "10\n1 1 2 2 2 3 3 3 2 2", "1\n7", "5\n4 4 9 9 1", "6\n0 0 0 0 0 0"),
        P("Secvența de sumă maximă", "dificil", "Afișează suma maximă a unei secvențe nevide de elemente consecutive (algoritmul lui Kadane, O(n)).",
          "n = int(input())\nv = list(map(int, input().split()))\nbest = cur = v[0]\nfor x in v[1:]:\n    cur = max(x, cur + x)\n    best = max(best, cur)\nprint(best)",
          "9\n-2 1 -3 4 -1 2 1 -5 4", "3\n-5 -2 -9", "1\n7", f"10000\n{mare}"),
        P("Perechi cu suma divizibilă cu k", "dificil", "Pe prima linie n și k, pe a doua n numere naturale. Afișează numărul de perechi (i &lt; j) cu v[i] + v[j] divizibil cu k. Folosește frecvențele resturilor.",
          "n, k = map(int, input().split())\nv = list(map(int, input().split()))\nf = [0] * k\ncnt = 0\nfor x in v:\n    r = x % k\n    cnt += f[(k - r) % k]\n    f[r] += 1\nprint(cnt)",
          "6 3\n1 2 3 4 5 6", "3 5\n1 1 1", "4 1\n7 8 9 10", "10000 7\n" + lista(10000, 0, 10**9)),
        P("Elementul majoritar", "dificil", "Un element este majoritar dacă apare de mai mult de n/2 ori. Afișează-l sau <code>-1</code> dacă nu există.",
          "n = int(input())\nv = list(map(int, input().split()))\ncand, c = None, 0\nfor x in v:\n    if c == 0:\n        cand, c = x, 1\n    elif x == cand:\n        c += 1\n    else:\n        c -= 1\nprint(cand if v.count(cand) * 2 > n else -1)",
          "7\n2 2 1 1 2 2 3", "4\n1 2 1 2", "1\n9", "5\n3 3 3 1 2"),
        P("Zerourile la final", "ușor", "Mută toate zerourile la sfârșitul listei, păstrând ordinea celorlalte elemente. Afișează lista.",
          "n = int(input())\nv = list(map(int, input().split()))\nnz = [x for x in v if x != 0]\nprint(*(nz + [0] * (n - len(nz))))",
          "6\n0 1 0 3 12 0", "3\n0 0 0", "2\n5 7"),
        P("Valori unice", "mediu", "Afișează, în ordinea primei apariții, valorile care apar o singură dată în listă, sau <code>-</code> dacă nu există.",
          "n = int(input())\nv = list(map(int, input().split()))\nf = {}\nfor x in v:\n    f[x] = f.get(x, 0) + 1\nrez = [x for x in v if f[x] == 1]\nprint(*rez if rez else ['-'])",
          "8\n4 5 4 6 7 5 8 6", "4\n1 1 2 2", "1\n3", f"10000\n{mare}"),
        P("Al doilea maxim", "ușor", "Afișează a doua valoare distinctă ca mărime sau <code>nu exista</code>. Fără sortare.",
          "n = int(input())\nv = list(map(int, input().split()))\nm1 = m2 = None\nfor x in v:\n    if m1 is None or x > m1:\n        m1, m2 = x, m1\n    elif x != m1 and (m2 is None or x > m2):\n        m2 = x\nprint(m2 if m2 is not None else 'nu exista')",
          "6\n3 9 2 9 7 1", "3\n5 5 5", "2\n-1 -7", "1\n4"),
        P("Histograma notelor", "ușor", "Se dau n note întregi de la 1 la 10. Pentru fiecare notă care apare, în ordine descrescătoare, afișează o linie <code>nota: ***</code> cu atâtea stelute câte apariții are.",
          "n = int(input())\nv = list(map(int, input().split()))\nf = [0] * 11\nfor x in v:\n    f[x] += 1\nfor nota in range(10, 0, -1):\n    if f[nota]:\n        print(f'{nota}: ' + '*' * f[nota])",
          "8\n7 9 10 7 5 9 7 8", "1\n10", "5\n1 1 1 1 1"),
        P("Reuniune și intersecție", "mediu", "Se dau două liste sortate crescător, pe două linii (fără n). Afișează reuniunea, apoi intersecția lor (fără valori repetate), crescător, folosind interclasarea; o mulțime vidă se afișează ca <code>-</code>.",
          "a = list(map(int, input().split()))\nb = list(map(int, input().split()))\ni = j = 0\nU, I = [], []\ndef add(L, x):\n    if not L or L[-1] != x:\n        L.append(x)\nwhile i < len(a) and j < len(b):\n    if a[i] < b[j]:\n        add(U, a[i]); i += 1\n    elif a[i] > b[j]:\n        add(U, b[j]); j += 1\n    else:\n        add(U, a[i]); add(I, a[i]); i += 1; j += 1\nfor x in a[i:] + b[j:]:\n    add(U, x)\nprint(*U if U else ['-'])\nprint(*I if I else ['-'])",
          "1 2 2 4 7\n2 3 4 4 9", "1 3\n2 4", "5 5\n5"),
        P("Listă munte", "mediu", "O listă este „munte” dacă are cel puțin 3 elemente, crește strict până la un vârf (care nu este la capete) și apoi scade strict. Afișează <code>DA</code> și poziția vârfului (de la 1), sau <code>NU</code>.",
          "n = int(input())\nv = list(map(int, input().split()))\ni = 0\nwhile i + 1 < n and v[i] < v[i + 1]:\n    i += 1\nvf = i\nwhile i + 1 < n and v[i] > v[i + 1]:\n    i += 1\nif n >= 3 and 0 < vf < n - 1 and i == n - 1:\n    print('DA', vf + 1)\nelse:\n    print('NU')",
          "5\n1 3 7 4 2", "4\n1 2 3 4", "5\n1 3 3 2 1", "3\n3 2 1", "3\n1 5 2"),
        P("Secvența cu suma S", "dificil", "Pe prima linie n și S, pe a doua n numere naturale nenule. Afișează pozițiile (de la 1) de început și sfârșit ale primei secvențe de elemente consecutive cu suma exact S (cea care se termină cel mai devreme; la egalitate, cea mai lungă), sau <code>-1</code>. Folosește doi indici (O(n)).",
          "n, S = map(int, input().split())\nv = list(map(int, input().split()))\nst = s = 0\nrez = None\nfor dr in range(n):\n    s += v[dr]\n    while s > S:\n        s -= v[st]; st += 1\n    if s == S:\n        rez = (st + 1, dr + 1)\n        break\nprint(*rez if rez else [-1])",
          "8 12\n1 2 3 7 5 1 1 10", "3 100\n1 2 3", "4 5\n5 1 1 3", "10000 1000000\n" + lista(10000, 1, 100)),
        P("Media între negative", "mediu", "Afișează media aritmetică (2 zecimale) a elementelor pozitive aflate strict între primul și ultimul element negativ, sau <code>nu exista</code> (dacă nu există două negative sau niciun pozitiv între ele).",
          "n = int(input())\nv = list(map(int, input().split()))\nneg = [i for i, x in enumerate(v) if x < 0]\npoz = [x for x in v[neg[0] + 1:neg[-1]] if x > 0] if len(neg) >= 2 else []\nprint(f'{sum(poz) / len(poz):.2f}' if poz else 'nu exista')",
          "8\n3 -1 4 0 5 -2 9 -3", "3\n-1 -2 -3", "4\n1 2 3 4", "5\n-5 1 2 -1 7"),
        P("Sortare după numărul de divizori", "mediu", "Afișează lista sortată descrescător după numărul de divizori, iar la egalitate crescător după valoare. Toate valorile sunt naturale nenule ≤ 10<sup>4</sup>.",
          "def nd(x):\n    c, d = 0, 1\n    while d * d <= x:\n        if x % d == 0:\n            c += 1 if d * d == x else 2\n        d += 1\n    return c\nn = int(input())\nv = list(map(int, input().split()))\nprint(*sorted(v, key=lambda x: (-nd(x), x)))",
          "6\n12 7 6 1 16 10", "1\n9", "4\n2 3 5 7"),
    ],
))

# ---------------------------------------------------------------- 3. Șiruri de caractere
LECTII.append(dict(
    id="g3", nr="3", scurt="Șiruri de caractere", titlu="Capitolul 3 – Șiruri de caractere",
    programa="Programa cap. 5.A (*): clasa str; cap. 1 (*): șir de caractere, liste de șiruri",
    obiective=["prelucrări pe cuvinte și pe caractere", "litere mari/mici, coduri, căutări", "formatarea exactă a ieșirii"],
    teorie=SFAT + """
<h3>Convenții</h3><p>Textele conțin litere ale alfabetului englez, cifre, spații și semnele de punctuație indicate. „Cuvânt” = secvență maximală de caractere fără spațiu, dacă nu se precizează altfel.</p>""",
    exercitii=[
        P("Anagrame", "ușor", "Se citesc două cuvinte (pe linii separate). Afișează <code>DA</code> dacă sunt anagrame (aceleași litere, aceleași frecvențe, fără a ține cont de litere mari/mici), altfel <code>NU</code>.",
          "a, b = input().lower(), input().lower()\nprint('DA' if sorted(a) == sorted(b) else 'NU')",
          "Ramo\nAmor", "abc\nabd", "aab\naba", "a\naa"),
        P("Cuvinte palindrom", "mediu", "Se citește o frază (cuvinte din litere, separate prin spații). Afișează câte cuvinte sunt palindroame (fără a ține cont de litere mari/mici; cuvintele de o literă se numără), apoi palindroamele distincte (scrise cu litere mici), în ordinea primei apariții, sau <code>-</code>.",
          "w = input().lower().split()\np = [x for x in w if x == x[::-1]]\nd = []\nfor x in p:\n    if x not in d:\n        d.append(x)\nprint(len(p))\nprint(*d if d else ['-'])",
          "Ana are un cojoc si un radar Ana", "nimic aici", "a b a"),
        P("Majuscule la început de propoziție", "mediu", "Se citește un text. Transformă în majusculă prima literă a textului și prima literă care urmează după fiecare <code>.</code>, <code>!</code> sau <code>?</code>; restul rămâne neschimbat.",
          "s = input()\nrez = []\nmare = True\nfor c in s:\n    if mare and c.isalpha():\n        rez.append(c.upper()); mare = False\n    else:\n        rez.append(c)\n    if c in '.!?':\n        mare = True\nprint(''.join(rez))",
          "azi e luni. maine e marti! ce zi e poimaine? miercuri.", "  x", "ABC. def"),
        P("Vocala următoare", "ușor", "Înlocuiește fiecare vocală cu vocala următoare din șirul a → e → i → o → u → a, păstrând litera mare/mică. Celelalte caractere rămân neschimbate.",
          "u = 'aeiou'\nrez = ''\nfor c in input():\n    l = c.lower()\n    if l in u:\n        n = u[(u.index(l) + 1) % 5]\n        rez += n.upper() if c.isupper() else n\n    else:\n        rez += c\nprint(rez)",
          "Ana are mere", "UAU!", "xyz"),
        P("Cuvântul cu litere distincte", "mediu", "Se citește o frază. Afișează cel mai lung cuvânt care nu are nicio literă repetată (fără a ține cont de litere mari/mici; primul, la egalitate), sau <code>-</code>.",
          "best = ''\nfor w in input().split():\n    if len(set(w.lower())) == len(w) and len(w) > len(best):\n        best = w\nprint(best or '-')",
          "informatica este frumoasa si utila", "aa bb", "Ana Dan"),
        P("Adresă de e-mail validă", "mediu", "Se citesc n adrese (câte una pe linie). O adresă este validă dacă: conține exact un <code>@</code>; partea dinainte este nevidă și conține doar litere, cifre, <code>.</code>, <code>_</code>; partea de după conține cel puțin un punct, nu începe și nu se termină cu punct și are doar litere, cifre, <code>.</code>, <code>-</code>. Afișează <code>valida</code>/<code>invalida</code> pentru fiecare.",
          "n = int(input())\nfor _ in range(n):\n    s = input().strip()\n    ok = s.count('@') == 1\n    if ok:\n        u, d = s.split('@')\n        ok = (u != '' and all(c.isalnum() or c in '._' for c in u)\n              and '.' in d and d[0] != '.' and d[-1] != '.'\n              and all(c.isalnum() or c in '.-' for c in d))\n    print('valida' if ok else 'invalida')",
          "6\nana.pop@scoala.ro\n@scoala.ro\nana@@x.ro\nion@ro\nprof_1@liceu-tehnic.edu.ro\nana@.ro", "1\na@b.c"),
        P("Suma numerelor din text", "ușor", "Se citește un text. Afișează suma tuturor numerelor naturale care apar în el (un număr = secvență maximală de cifre).",
          "s = input()\ntot, cur, ok = 0, 0, False\nfor c in s + ' ':\n    if c.isdigit():\n        cur = cur * 10 + int(c); ok = True\n    else:\n        if ok:\n            tot += cur\n        cur, ok = 0, False\nprint(tot)",
          "am 3 mere si 12 pere, iar 2026 e anul", "fara numere", "a1b22c333", "007"),
        P("Decomprimare", "mediu", "Se citește un șir de forma literă + număr (numărul poate avea mai multe cifre), de ex. <code>a3b1c12</code>. Afișează șirul decomprimat.",
          "s = input()\nrez = []\ni = 0\nwhile i < len(s):\n    c = s[i]; i += 1\n    k = 0\n    while i < len(s) and s[i].isdigit():\n        k = k * 10 + int(s[i]); i += 1\n    rez.append(c * k)\nprint(''.join(rez))",
          "a3b1c2", "x12", "a1b1c1"),
        P("Cuvinte ordonate", "ușor", "Se citește o frază. Afișează cuvintele sortate crescător după lungime, iar la lungimi egale alfabetic (cu litere mici).",
          "w = input().lower().split()\nprint(*sorted(w, key=lambda x: (len(x), x)))",
          "Ana are mere si pere rosii", "b a", "unu"),
        P("Cuvinte repetate", "mediu", "Se citește un text cu cuvinte separate prin spații (fără a ține cont de litere mari/mici). Afișează cuvintele care apar de cel puțin două ori, câte unul pe linie, cu numărul de apariții (<code>cuvant 3</code>), în ordinea descrescătoare a frecvenței și apoi alfabetic; dacă nu există, afișează <code>-</code>.",
          "f = {}\nfor w in input().lower().split():\n    f[w] = f.get(w, 0) + 1\nr = sorted([w for w in f if f[w] >= 2], key=lambda w: (-f[w], w))\nif r:\n    for w in r:\n        print(w, f[w])\nelse:\n    print('-')",
          "Ana are mere ana are pere si ANA are", "unu doi trei", "b a b a"),
        P("Ordinea inversă a cuvintelor", "ușor", "Se citește o frază (cuvintele pot fi separate prin mai multe spații). Afișează cuvintele în ordine inversă, separate prin câte un spațiu.",
          "print(' '.join(input().split()[::-1]))",
          "Ana  are   mere", "unu", "  a b  "),
        P("Rime", "mediu", "Se citește o listă de cuvinte (pe o linie). Afișează, în ordinea din listă, celelalte cuvinte care se termină cu aceleași două litere ca primul cuvânt (fără a ține cont de litere mari/mici), sau <code>-</code>. Cuvintele au cel puțin două litere.",
          "w = input().split()\nt = w[0][-2:].lower()\nr = [x for x in w[1:] if x[-2:].lower() == t]\nprint(*r if r else ['-'])",
          "carte poarte arte mare parte", "abc xy", "ana Bana cana"),
    ],
))
