"""Simulări de probă scrisă (structură orientativă: 3 subiecte × 30 p + 10 p din oficiu).
Câmpuri speciale verificate de build.py:
- grila: 'verif' = (cod, limbaj) – ieșirea trebuie să coincidă cu varianta corectă;
- deschis: 'calc' = [(cod_python, intrare), ...] – ieșirile înlocuiesc {R0}, {R1}... în model;
           'cod_model' (+ 'lang', 'intrare') – rulat, cu ieșirea afișată;
           'sql' = (script_creare, [interogări]) – rulat în SQLite, rezultatele afișate.
"""
from util import C, T, CPP_ANTET


def cpp(body):
    return CPP_ANTET + "int main() {\n" + body + "\n    return 0;\n}\n"


def G(enunt, opts, a, p=2, cod=None, lang="python", verif=None):
    d = dict(tip="grila", enunt=enunt, opts=opts, a=a, p=p)
    if cod:
        d["cod"], d["lang"] = cod, lang
    if verif:
        d["verif"] = verif
    return d


def D(enunt, p, barem, model, **kw):
    d = dict(tip="deschis", enunt=enunt, p=p, barem=barem, model=model)
    d.update(kw)
    return d


DB1 = """
CREATE TABLE elevi (id_elev INTEGER PRIMARY KEY, nume VARCHAR(40) NOT NULL, clasa VARCHAR(5) NOT NULL, media REAL);
CREATE TABLE absente (id_absenta INTEGER PRIMARY KEY, id_elev INTEGER NOT NULL REFERENCES elevi(id_elev), data DATE NOT NULL, motivata CHAR(1) DEFAULT 'N' CHECK (motivata IN ('D','N')));
INSERT INTO elevi VALUES (1,'Pop Ana','9A',9.45),(2,'Dinu Dan','9A',8.10),(3,'Ilie Ion','9B',7.25),(4,'Marin Ioana','9A',9.80),(5,'Stan Radu','9B',6.90);
INSERT INTO absente VALUES (1,2,'2026-10-01','N'),(2,2,'2026-10-02','N'),(3,2,'2026-10-05','N'),(4,3,'2026-10-01','D'),(5,3,'2026-10-07','N'),(6,5,'2026-10-02','N'),(7,5,'2026-10-03','N'),(8,5,'2026-10-04','N'),(9,5,'2026-10-09','N'),(10,1,'2026-10-09','D');
"""

METODICA_CRIT = "Răspunsul folosește terminologia de specialitate și exemplele sunt aplicate pe tema dată"

SIMULARI = []

# =============================================================== SIMULAREA 1
SIMULARI.append(dict(id="s1", titlu="Simularea 1", tema="liste, frecvențe, SQL, metodica lecției despre liste", subiecte=[
    dict(titlu="Subiectul I", punctaj=30, itemi=[
        G("Ce afișează secvența Python?", ["[1, 4, 1] 2", "[4, 1, 3] 2", "[1, 4] 2", "[5, 1, 4] 1"], 0,
          cod="v = [3, 1, 4, 1, 5]\nprint(v[1:4][::-1], v.count(1))", verif=("v = [3, 1, 4, 1, 5]\nprint(v[1:4][::-1], v.count(1))", "python")),
        G("Ce afișează secvența C++?", ["313.5", "3.513.5", "313", "3 1 3.5"], 0,
          cod='int a = 7, b = 2;\ncout << a / b << a % b << (double)a / b;', lang="c++", verif=(cpp('int a = 7, b = 2;\ncout << a / b << a % b << (double)a / b;'), "c++")),
        G("Un graf neorientat conex are 6 noduri și 8 muchii. Numărul minim de muchii care trebuie eliminate pentru a obține un arbore parțial este:", ["2", "3", "5", "8"], 1),
        G("Complexitatea căutării binare într-o listă sortată cu n elemente este:", ["O(n)", "O(log n)", "O(n log n)", "O(1)"], 1),
        G("Clauza SQL în care se pun condițiile pe rezultatele funcțiilor agregate (pe grupuri) este:", ["WHERE", "ORDER BY", "HAVING", "SELECT"], 2),
        G("Câte adrese de gazdă utilizabile are o subrețea cu masca /27?", ["32", "30", "27", "62"], 1),
        D("""<p>Se consideră algoritmul scris în pseudocod (<code>[x]</code> = partea întreagă, <code>%</code> = restul împărțirii):</p>""" + C("""citește n (număr natural)
s ← 0; p ← 1
cât timp n > 0 execută
    c ← n % 10
    dacă c % 3 = 0 atunci
        s ← s + c * p; p ← p * 10
    n ← [n / 10]
scrie s""", "pseudocod") + """<ol type="a"><li>Scrieți ce se afișează pentru n = 2369. (4 p)</li><li>Scrieți toate numerele din intervalul [20, 30] pentru care se afișează 0. (4 p)</li><li>Scrieți programul Python corespunzător algoritmului. (6 p)</li><li>Scrieți în pseudocod un algoritm echivalent care folosește în locul structurii <em>cât timp</em> o structură repetitivă de tip <em>repetă … până când</em>. (4 p)</li></ol>""",
          18, [("a) răspuns corect", 4), ("b) toate numerele cerute, fără altele (2 p dacă lipsește/apare în plus un singur număr)", 4),
               ("c) citire și afișare corecte", 1), ("c) structura repetitivă și condiția", 2), ("c) structura alternativă și calculele", 2), ("c) sintaxă corectă (indentare, operatori //, %)", 1),
               ("d) structura repetă … până când cu condiția corectă (n = 0)", 2), ("d) tratarea cazului n = 0 (echivalență pentru orice n)", 2)],
          """<p>a) Cifrele divizibile cu 3, de la dreapta: 9, 6, 3 ⇒ se afișează <strong>{R0}</strong>.</p><p>b) <strong>{R1}</strong> (cifra 0 este divizibilă cu 3, dar adaugă 0 la s; numerele care conțin 3, 6 sau 9 dau un rezultat nenul).</p>""" + C("""n = int(input())
s, p = 0, 1
while n > 0:
    c = n % 10
    if c % 3 == 0:
        s += c * p
        p *= 10
    n //= 10
print(s)""") + C("""citește n
s ← 0; p ← 1
dacă n > 0 atunci
    repetă
        c ← n % 10
        dacă c % 3 = 0 atunci
            s ← s + c * p; p ← p * 10
        n ← [n / 10]
    până când n = 0
scrie s""", "pseudocod"),
          calc=[("""n = 2369
s, p = 0, 1
while n > 0:
    c = n % 10
    if c % 3 == 0:
        s += c * p; p *= 10
    n //= 10
print(s)""", ""), ("""r = []
for x in range(20, 31):
    n, s, p = x, 0, 1
    while n > 0:
        c = n % 10
        if c % 3 == 0:
            s += c * p; p *= 10
        n //= 10
    if s == 0:
        r.append(x)
print(', '.join(map(str, r)))""", "")]),
    ]),
    dict(titlu="Subiectul al II-lea", punctaj=30, itemi=[
        D("<p>Se citesc n (1 ≤ n ≤ 1000) și apoi n numere naturale. Scrieți un program Python care afișează, în ordine crescătoare, valorile care apar de cel puțin două ori (fiecare o singură dată), separate prin spațiu, sau mesajul <code>nu exista</code>.</p>",
          10, [("citirea corectă a datelor", 2), ("determinarea frecvențelor (dicționar, listă de frecvențe sau numărare)", 3), ("selectarea corectă a valorilor cu frecvență ≥ 2, fiecare o dată", 2), ("afișare în ordine crescătoare, în formatul cerut", 2), ("tratarea cazului „nu exista”", 1)],
          "<p>Rezolvare posibilă (dicționar de frecvențe):</p>", cod_model="""n = int(input())
v = list(map(int, input().split()))
f = {}
for x in v:
    f[x] = f.get(x, 0) + 1
r = sorted(x for x in f if f[x] >= 2)
print(*r if r else ['nu exista'])""", intrare="8\n5 3 8 3 5 5 1 9"),
        D("<p>Fișierul <code>bac.txt</code> conține cel mult 10<sup>6</sup> numere naturale din intervalul [0, 100], separate prin spații. Se cere afișarea, în ordine crescătoare, a numerelor de <strong>exact două cifre</strong> care <strong>nu</strong> apar în fișier, separate prin spațiu.</p><ol type='a'><li>Descrieți în limbaj natural o metodă eficientă din punctul de vedere al timpului de executare și al memoriei, justificând eficiența. (2 p)</li><li>Scrieți programul Python corespunzător metodei. (8 p)</li></ol>",
          10, [("a) descrierea metodei (vector de apariții indexat după valoare, o singură parcurgere)", 1), ("a) justificarea eficienței: timp liniar în numărul de valori, memorie constantă (101 elemente)", 1),
               ("b) deschiderea fișierului și citirea tuturor valorilor", 2), ("b) marcarea aparițiilor", 2), ("b) parcurgerea valorilor 10..99 și selectarea celor neapărute", 2), ("b) afișarea în formatul cerut", 1), ("b) program eficient (fără căutări repetate în listă)", 1)],
          "<p>a) Se folosește un vector <code>ap</code> cu 101 componente, inițial 0; la citirea fiecărei valori x se marchează <code>ap[x] = 1</code>. La final se parcurg valorile 10..99 și se afișează cele nemarcate. Datele se parcurg o singură dată (timp liniar), iar memoria nu depinde de numărul de valori din fișier.</p>",
          cod_model="""ap = [0] * 101
with open('bac.txt') as f:
    for linie in f:
        for x in linie.split():
            ap[int(x)] = 1
print(*[x for x in range(10, 100) if not ap[x]])""", fisiere={"bac.txt": " ".join(str(x) for x in range(0, 101) if x % 7 and x % 11) + "\n"}),
        D("<p>Se consideră tabelele <code>ELEVI(id_elev, nume, clasa, media)</code> și <code>ABSENTE(id_absenta, id_elev, data, motivata)</code>, unde <code>motivata</code> are valorile <code>'D'</code> sau <code>'N'</code>. Scrieți comenzi SQL pentru:</p><ol type='a'><li>numele și media elevilor din clasa 9A, în ordinea descrescătoare a mediei; (3 p)</li><li>numele elevilor care au mai mult de 2 absențe nemotivate și numărul acestora; (4 p)</li><li>crearea tabelei <code>ABSENTE</code>, cu cheie primară, cheie externă spre <code>ELEVI</code>, valoarea implicită <code>'N'</code> și constrângere pentru valorile permise ale câmpului <code>motivata</code>. (3 p)</li></ol>",
          10, [("a) proiecție, selecție și ordonare corecte", 3), ("b) join corect între tabele", 1), ("b) condiția motivata = 'N' în WHERE", 1), ("b) GROUP BY și COUNT", 1), ("b) condiția pe grup în HAVING", 1),
               ("c) tipuri de date și cheie primară", 1), ("c) cheie externă", 1), ("c) DEFAULT și CHECK", 1)],
          "<p>Rezolvare (rulată pe date de test):</p>",
          sql=(DB1, ["SELECT nume, media FROM elevi WHERE clasa = '9A' ORDER BY media DESC;",
                     "SELECT e.nume, COUNT(*) AS nr_absente\nFROM elevi e JOIN absente a ON a.id_elev = e.id_elev\nWHERE a.motivata = 'N'\nGROUP BY e.id_elev, e.nume\nHAVING COUNT(*) > 2;",
                     "CREATE TABLE absente2 (\n  id_absenta INTEGER PRIMARY KEY,\n  id_elev    INTEGER NOT NULL REFERENCES elevi(id_elev),\n  data       DATE NOT NULL,\n  motivata   CHAR(1) DEFAULT 'N' CHECK (motivata IN ('D', 'N'))\n);"]),
          nota="La c) tabela s-a numit <code>absente2</code> doar pentru a o putea crea alături de cea existentă în baza de test; în răspuns se scrie <code>ABSENTE</code>. În Oracle se folosesc tipurile <code>NUMBER</code>, <code>VARCHAR2</code>."),
    ]),
    dict(titlu="Subiectul al III-lea", punctaj=30, itemi=[
        D("<p>Pentru o lecție cu tema „Liste – metode ale clasei list” (Python, clasa a IX-a):</p><ol type='a'><li>formulați o competență specifică (ilustrativă) și două obiective operaționale derivate din aceasta; (6 p)</li><li>descrieți modul în care aplicați, în cadrul lecției, două metode didactice, dintre care una activ-participativă; (8 p)</li><li>elaborați un item de tip alegere multiplă și un item de tip rezolvare de problemă, cu barem, care să evalueze obiectivele formulate; (10 p)</li><li>precizați două avantaje ale evaluării formative realizate cu un test online la finalul lecției și o măsură de prevenire a erorilor de notare la itemul subiectiv. (6 p)</li></ol>",
          30, [("a) competență formulată corect (verb + conținut + context)", 2), ("a) două obiective operaționale cu comportament observabil, condiții și criteriu (2 × 2 p)", 4),
               ("b) prima metodă: denumire și aplicare concretă pe temă (etape, sarcini)", 4), ("b) metoda activ-participativă: aplicare concretă pe temă", 4),
               ("c) item cu alegere multiplă corect construit (premisă, distractori plauzibili)", 3), ("c) item de rezolvare de problemă formulat clar", 3), ("c) bareme corecte, analitic la problemă", 2), ("c) itemii evaluează obiectivele formulate", 2),
               ("d) două avantaje ale evaluării formative online", 4), ("d) măsură de prevenire a erorilor de notare", 2)],
          """<p><strong>a)</strong> Competență specifică (ilustrativă): „Utilizarea metodelor clasei list în rezolvarea problemelor.” O1 – elevii vor fi capabili să aleagă metoda potrivită (append, insert, pop, index, count, sort) pentru 5 operații descrise, rezolvând corect cel puțin 4; O2 – elevii vor fi capabili să scrie un program care elimină dintr-o listă valorile negative și sortează lista rămasă, programul trecând toate testele date.</p>
<p><strong>b)</strong> <em>Demonstrația</em>: profesorul rulează în fața clasei, pas cu pas, o secvență cu <code>append</code>, <code>insert</code>, <code>pop</code>, afișând lista după fiecare operație; elevii anticipează rezultatul înainte de rulare. <em>Învățarea prin descoperire în perechi</em> (activ-participativă): fiecare pereche primește o fișă cu câte o metodă necunoscută (<code>index</code>, <code>count</code>, <code>remove</code>), o testează pe exemple, formulează regula de funcționare și o prezintă colegilor; profesorul validează.</p>
<p><strong>c)</strong> Item cu alegere multiplă: „Ce afișează <code>v = [5, 2, 7]; v.insert(1, 9); print(v)</code>? a) [5, 9, 2, 7] b) [9, 5, 2, 7] c) [5, 2, 9, 7] d) [5, 2, 7, 9]” – barem: a – 2 p (distractori: confuzia poziției cu valoarea, inserarea la început, append). Item de rezolvare de problemă: „Scrieți un program care citește o listă de numere întregi, elimină valorile negative și afișează lista rămasă sortată crescător.” – barem (6 p): citire 1 p; eliminarea negativelor 2 p; sortare 1 p; afișare 1 p; tratarea listei vide 1 p.</p>
<p><strong>d)</strong> Avantaje: feedback imediat pentru elev și profesor; profesorul identifică pe loc erorile frecvente și le reia în ora următoare (funcția de reglare). Măsură: corectarea pe baza baremului analitic stabilit dinainte, aplicat la fel tuturor lucrărilor (eventual lucrări anonimizate) – previne efectul halo și efectul de contrast.</p>"""),
    ]),
]))

# =============================================================== SIMULAREA 2
SIMULARI.append(dict(id="s2", titlu="Simularea 2", tema="recursivitate, șiruri, programare dinamică, învățare automată, metodica bazelor de date", subiecte=[
    dict(titlu="Subiectul I", punctaj=30, itemi=[
        G("Ce afișează secvența Python?", ["{1, 2, 5} 3", "{1, 2, 2, 5} 4", "{5, 2, 1} 3", "[1, 2, 5] 3"], 0,
          cod="s = {2, 5, 1, 2, 5}\nd = {'a': 1, 'b': 2}\nd['a'] += d['b']\nprint(s, d['a'])", verif=("s = {2, 5, 1, 2, 5}\nd = {'a': 1, 'b': 2}\nd['a'] += d['b']\nprint(s, d['a'])", "python")),
        G("Ce afișează secvența C++?", ["4 8 6", "4 6 6", "2 6 4", "4 8 8"], 0,
          cod='int v[] = {2, 4, 6, 8};\nint *p = v + 1;\ncout << *p << " " << *(p + 2) << " " << *p + 2;', lang="c++",
          verif=(cpp('int v[] = {2, 4, 6, 8};\nint *p = v + 1;\ncout << *p << " " << *(p + 2) << " " << *p + 2;'), "c++")),
        G("Ce afișează programul?", ["531135", "135531", "53135", "5311"], 0,
          cod="def g(n):\n    if n < 1:\n        return\n    print(n, end='')\n    g(n - 2)\n    print(n, end='')\n\ng(5)", verif=("def g(n):\n    if n < 1:\n        return\n    print(n, end='')\n    g(n - 2)\n    print(n, end='')\n\ng(5)", "python")),
        G("Câte grafuri parțiale are un graf neorientat cu 5 noduri și 4 muchii (inclusiv graful însuși și cel fără muchii)?", ["8", "16", "32", "20"], 1),
        G("Într-un min-heap memorat în vector (indexare de la 1), părintele nodului de pe poziția 9 se află pe poziția:", ["3", "4", "5", "8"], 1),
        G("Celula C2 conține formula <code>=A2*$B$1</code>. După copierea în C5, formula devine:", ["=A5*$B$1", "=A2*$B$4", "=A5*$B$4", "=D5*$B$1"], 0),
        D("<p>Se consideră funcția:</p>" + C("""def f(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return f(n // 10) + n % 10
    return f(n // 10)""") + "<ol type='a'><li>Ce valoare are <code>f(28374)</code>? (4 p)</li><li>Câte apeluri ale funcției f (inclusiv primul) se fac pentru calculul lui <code>f(28374)</code>? (4 p)</li><li>Scrieți o variantă iterativă a funcției. (6 p)</li><li>Dați exemplu de un număr de 4 cifre distincte n pentru care f(n) = 20 și justificați. (4 p)</li></ol>",
          18, [("a) valoare corectă", 4), ("b) număr de apeluri corect", 4), ("c) structura repetitivă corectă", 3), ("c) selectarea cifrelor pare și acumularea", 2), ("c) returnarea rezultatului", 1), ("d) exemplu corect (cifre distincte, suma cifrelor pare = 20)", 3), ("d) justificare", 1)],
          "<p>a) f calculează suma cifrelor pare: 8 + 4 + 2 ⇒ <strong>{R0}</strong>.</p><p>b) Câte un apel pentru fiecare cifră, plus apelul cu n = 0 ⇒ <strong>{R1}</strong> apeluri.</p>" + C("""def f(n):
    s = 0
    while n > 0:
        if n % 2 == 0:
            s += n % 10      # cifra este pară exact când n este par
        n //= 10
    return s""") + "<p>d) De exemplu <strong>{R2}</strong>: cifrele pare 8, 6, 4, 2 au suma 20 (orice număr de 4 cifre distincte, toate pare, cu suma 20, de ex. 8642, 2468).</p>",
          calc=[("def f(n):\n    if n == 0: return 0\n    if n % 2 == 0: return f(n // 10) + n % 10\n    return f(n // 10)\nprint(f(28374))", ""),
                ("c = 0\ndef f(n):\n    global c\n    c += 1\n    if n == 0: return 0\n    if n % 2 == 0: return f(n // 10) + n % 10\n    return f(n // 10)\nf(28374)\nprint(c)", ""),
                ("def f(n):\n    if n == 0: return 0\n    if n % 2 == 0: return f(n // 10) + n % 10\n    return f(n // 10)\nassert f(8642) == 20\nprint(8642)", "")]),
    ]),
    dict(titlu="Subiectul al II-lea", punctaj=30, itemi=[
        D("<p>Se citește un text format din cuvinte (litere mici) separate prin câte un spațiu. Scrieți un program Python care afișează cuvântul cu cele mai multe vocale (primul, la egalitate) și numărul acestora. Vocalele sunt a, e, i, o, u.</p>",
          10, [("citirea textului și separarea cuvintelor", 2), ("numărarea vocalelor unui cuvânt", 3), ("determinarea maximului, primul la egalitate", 3), ("afișarea în formatul cerut", 2)],
          "<p>Rezolvare posibilă:</p>", cod_model="""cuvinte = input().split()
best, nv = '', -1
for w in cuvinte:
    k = sum(1 for c in w if c in 'aeiou')
    if k > nv:
        best, nv = w, k
print(best, nv)""", intrare="programarea este o activitate frumoasa"),
        D("<p>Fișierul <code>teren.in</code> conține pe prima linie n și m (n, m ≤ 100), apoi o matrice n × m de numere naturale (cantitatea de aur din fiecare parcelă). Un robot pornește din colțul stânga-sus și ajunge în colțul dreapta-jos deplasându-se doar spre dreapta sau în jos, colectând aurul din parcelele prin care trece. Scrieți un program Python care afișează cantitatea maximă de aur colectată. Precizați metoda de programare folosită și complexitatea.</p>",
          10, [("citirea corectă din fișier", 2), ("identificarea metodei (programare dinamică) și relația de recurență", 2), ("tratarea primei linii și a primei coloane", 2), ("calculul corect pentru restul matricei", 2), ("afișare + complexitatea O(n · m)", 2)],
          "<p>Programare dinamică: S[i][j] = a[i][j] + max(S[i−1][j], S[i][j−1]); complexitate O(n · m) în timp.</p>",
          cod_model="""with open('teren.in') as f:
    n, m = map(int, f.readline().split())
    a = [list(map(int, f.readline().split())) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if i == 0 and j > 0:
            a[i][j] += a[i][j - 1]
        elif j == 0 and i > 0:
            a[i][j] += a[i - 1][j]
        elif i > 0 and j > 0:
            a[i][j] += max(a[i - 1][j], a[i][j - 1])
print(a[n - 1][m - 1])""", fisiere={"teren.in": "3 4\n1 3 1 5\n2 9 1 1\n4 2 8 1\n"}),
        D("<p>Învățare automată.</p><ol type='a'><li>Punctele de antrenare sunt: A: (1, 1), (2, 1), (3, 2); B: (4, 4), (5, 4), (4, 5). Clasificați punctul (4, 3) cu algoritmul KNN pentru k = 3 (distanța euclidiană), precizând cei trei vecini. (4 p)</li><li>Pentru datele (1, 2), (2, 4), (3, 5), (4, 4), (5, 5), determinați dreapta de regresie liniară y = a·x + b. (3 p)</li><li>Un clasificator testat pe 100 de exemple are TP = 8, FN = 2, FP = 4, TN = 86. Calculați precizia și recall-ul și precizați care metrică este mai importantă la depistarea unei boli. (3 p)</li></ol>",
          10, [("a) distanțele și cei 3 vecini corecți", 2), ("a) clasa corectă", 2), ("b) a și b corecte", 3), ("c) precizia și recall-ul corecte", 2), ("c) justificarea: recall (nu trebuie ratate cazurile pozitive)", 1)],
          "<p>a) Distanțele până la (4, 3): (4, 4) → 1 [B]; (3, 2) → √2 [A]; (5, 4) → √2 [B]; restul sunt mai departe. Vecinii: B, A, B ⇒ clasa <strong>{R0}</strong>.</p><p>b) <strong>{R1}</strong>.</p><p>c) Precizia = TP/(TP + FP) = 8/12 ≈ <strong>{R2}</strong>; recall = TP/(TP + FN) = 8/10 = <strong>{R3}</strong>. La depistarea unei boli contează mai mult <strong>recall-ul</strong>: un bolnav ratat (FN) este mai grav decât o alarmă falsă.</p>",
          calc=[("import math\nP = [((1,1),'A'),((2,1),'A'),((3,2),'A'),((4,4),'B'),((5,4),'B'),((4,5),'B')]\nv = sorted(P, key=lambda t: math.dist(t[0], (4, 3)))[:3]\nc = [x[1] for x in v]\nprint(max(set(c), key=c.count))", ""),
                ("x = [1,2,3,4,5]; y = [2,4,5,4,5]\nmx, my = sum(x)/5, sum(y)/5\na = sum((p-mx)*(q-my) for p, q in zip(x, y)) / sum((p-mx)**2 for p in x)\nb = my - a * mx\nprint(f'y = {a:.1f}x + {b:.1f}'.replace('.', ','))", ""),
                ("print(f'{8/12:.3f}'.replace('.', ','))", ""), ("print(f'{8/10:.1f}'.replace('.', ','))", "")]),
    ]),
    dict(titlu="Subiectul al III-lea", punctaj=30, itemi=[
        D("<p>Pentru unitatea de învățare „Interogarea bazelor de date – SQL” (clasa a XII-a):</p><ol type='a'><li>realizați un fragment de proiect al unității de învățare pentru două lecții, cu rubricile uzuale; (10 p)</li><li>descrieți aplicarea metodei mozaicului în cadrul unității; (8 p)</li><li>construiți matricea de specificații pentru testul de la finalul unității (3 conținuturi, 3 niveluri cognitive); (6 p)</li><li>precizați două avantaje și o limită ale portofoliului ca metodă de evaluare la această unitate. (6 p)</li></ol>",
          30, [("a) rubricile uzuale complete (conținuturi, competențe, activități, resurse, evaluare)", 4), ("a) activități de învățare concrete și variate", 3), ("a) coerență competențe – activități – evaluare", 3),
               ("b) etapele mozaicului în ordinea corectă", 4), ("b) sarcini concrete pe SQL pentru experți", 2), ("b) evaluarea individuală la final", 2),
               ("c) matrice corectă (conținuturi pe linii, niveluri pe coloane, total 100%)", 4), ("c) ponderi justificate", 2),
               ("d) două avantaje", 4), ("d) o limită", 2)],
          """<p><strong>a)</strong></p><div class='tbl'><table><tr><th>Conținuturi</th><th>Comp. spec.</th><th>Activități de învățare</th><th>Resurse</th><th>Evaluare</th></tr><tr><td>Interogări simple: SELECT, WHERE, ORDER BY</td><td>(din programă)</td><td>formularea în limbaj natural a cerințelor și traducerea lor în SQL; rularea interogărilor pe baza de date a școlii; corectarea unor interogări greșite</td><td>laborator, SGBD, fișă de lucru; frontal + individual; 1 oră</td><td>observare sistematică; fișă cu 3 interogări</td></tr><tr><td>Grupare: funcții agregate, GROUP BY, HAVING</td><td>(din programă)</td><td>„de ce nu merge COUNT în WHERE?” (problematizare); statistici pe clase; comparare WHERE vs. HAVING</td><td>laborator; în perechi; 1 oră</td><td>test formativ online</td></tr></table></div>
<p><strong>b)</strong> Grupe de bază de 4; fiecare membru devine expert pe o temă: 1 – JOIN, 2 – funcții agregate, 3 – subinterogări, 4 – DML (INSERT/UPDATE/DELETE). Experții lucrează împreună pe fișe cu exemple pe baza de date a clasei, apoi revin în grupele de bază, predau colegilor și rezolvă împreună o sarcină comună. La final – test individual.</p>
<p><strong>c)</strong></p><div class='tbl'><table><tr><th>Conținut \\ nivel</th><th>A înțelege</th><th>A aplica</th><th>A analiza</th><th>Total</th></tr><tr><td>SELECT, WHERE, ORDER BY</td><td>10%</td><td>20%</td><td>–</td><td>30%</td></tr><tr><td>Funcții agregate, grupare</td><td>10%</td><td>15%</td><td>10%</td><td>35%</td></tr><tr><td>JOIN și subinterogări</td><td>5%</td><td>20%</td><td>10%</td><td>35%</td></tr><tr><td>Total</td><td>25%</td><td>55%</td><td>20%</td><td>100%</td></tr></table></div>
<p><strong>d)</strong> Avantaje: surprinde progresul pe parcursul unității (interogările din ce în ce mai complexe); implică elevul în autoevaluare. Limită: timp mare de evaluare (și risc de preluare a interogărilor de la colegi – se reduce prin prezentare orală).</p>"""),
    ]),
]))

# =============================================================== SIMULAREA 3
SIMULARI.append(dict(id="s3", titlu="Simularea 3", tema="C++, backtracking, grafuri, TIC și rețele, metodica TIC la gimnaziu", subiecte=[
    dict(titlu="Subiectul I", punctaj=30, itemi=[
        G("Ce afișează secvența C++?", ["Xproare", "Xprore", "Xprogre", "proXare"], 0,
          cod='string s = "programare";\ns.erase(3, 4);\ns.insert(0, "X");\ncout << s;', lang="c++", verif=(cpp('string s = "programare";\ns.erase(3, 4);\ns.insert(0, "X");\ncout << s;'), "c++")),
        G("Se generează în ordine lexicografică submulțimile cu 3 elemente ale mulțimii {1, 2, 3, 4, 5}. Ce soluție urmează după {1, 4, 5}?", ["{2, 3, 4}", "{1, 5, 6}", "{2, 4, 5}", "{1, 3, 5}"], 0),
        G("Algoritmul lui Dijkstra NU funcționează corect pentru grafuri care au:", ["cicluri", "muchii cu cost negativ", "noduri izolate", "peste 100 de noduri"], 1),
        G("Ce afișează secvența Python?", ["1101 13", "1011 11", "1101 11", "13 1101"], 0,
          cod="n = 13\nprint(bin(n)[2:], int('1101', 2))", verif=("n = 13\nprint(bin(n)[2:], int('1101', 2))", "python")),
        G("Un router lucrează, în modelul OSI, în principal la nivelul:", ["fizic", "legătură de date", "rețea", "aplicație"], 2),
        G("În Regulamentul UE privind inteligența artificială, un sistem care evaluează automat elevii este încadrat, de regulă, în categoria de risc:", ["minim", "limitat", "ridicat", "inacceptabil"], 2),
        D("<p>Se consideră programul C++:</p>" + C("""struct Elev { string nume; int nota; };

int main() {
    Elev v[4] = {{"Ana", 9}, {"Dan", 7}, {"Ioana", 10}, {"Radu", 7}};
    int k = 0;
    for (int i = 1; i < 4; i++)
        if (v[i].nota < v[k].nota) k = i;
    v[k].nota += 2;
    for (int i = 0; i < 4; i++) cout << v[i].nume[0] << v[i].nota << " ";
    return 0;
}""", "c++") + "<ol type='a'><li>Ce afișează programul? (6 p)</li><li>Ce modificare minimă a condiției din instrucțiunea <code>if</code> face ca nota mărită să fie cea a lui Radu? Justificați. (4 p)</li><li>Rescrieți secvența de determinare a lui k ca funcție care primește tabloul și numărul de elemente și întoarce poziția. (8 p)</li></ol>",
          18, [("a) afișare complet corectă (3 p dacă doar nota modificată e corectă)", 6), ("b) modificarea corectă (&lt;=)", 2), ("b) justificarea (ultima poziție cu nota minimă)", 2),
               ("c) antetul funcției corect (tablou + n)", 3), ("c) corpul funcției", 3), ("c) apelul în main", 2)],
          "<p>a) Nota minimă este 7, prima dată la Dan (poziția 1) ⇒ Dan primește 9. Se afișează:</p>{R0}<p>b) Condiția <code>v[i].nota &lt;= v[k].nota</code> reține <em>ultima</em> poziție cu nota minimă ⇒ Radu.</p>" + C("""int pozMin(Elev v[], int n) {
    int k = 0;
    for (int i = 1; i < n; i++)
        if (v[i].nota < v[k].nota) k = i;
    return k;
}
// în main: int k = pozMin(v, 4);""", "c++"),
          calc_cpp=[CPP_ANTET + """struct Elev { string nume; int nota; };
int main() {
    Elev v[4] = {{"Ana", 9}, {"Dan", 7}, {"Ioana", 10}, {"Radu", 7}};
    int k = 0;
    for (int i = 1; i < 4; i++)
        if (v[i].nota < v[k].nota) k = i;
    v[k].nota += 2;
    for (int i = 0; i < 4; i++) cout << v[i].nume[0] << v[i].nota << " ";
    return 0;
}"""]),
    ]),
    dict(titlu="Subiectul al II-lea", punctaj=30, itemi=[
        D("<p>Se citesc n și k (1 ≤ k ≤ n ≤ 10). Scrieți un program Python care afișează, în ordine lexicografică, toate submulțimile cu k elemente ale mulțimii {1, …, n} în care oricare două elemente alăturate diferă prin cel puțin 2, câte una pe linie. Precizați metoda folosită.</p>",
          10, [("precizarea metodei (backtracking)", 1), ("generarea combinărilor în ordine lexicografică", 4), ("condiția de continuare (diferență ≥ 2)", 3), ("afișarea soluțiilor în formatul cerut", 2)],
          "<p>Backtracking; condiția de continuare: x[k] ≥ x[k−1] + 2.</p>", cod_model="""n, k = map(int, input().split())
x = []
def bt(start):
    if len(x) == k:
        print(*x)
        return
    for v in range(start, n + 1):
        x.append(v)
        bt(v + 2)
        x.pop()
bt(1)""", intrare="6 3"),
        D("<p>Fișierul <code>graf.in</code> conține pe prima linie n și m, apoi m muchii ale unui graf neorientat, iar pe ultima linie un nod s. Scrieți un program Python care afișează, pentru fiecare nod 1..n, distanța minimă (în număr de muchii) de la s, sau -1 pentru nodurile inaccesibile. Precizați algoritmul și complexitatea.</p>",
          10, [("citirea din fișier și construirea listelor de adiacență", 3), ("BFS corect cu coadă", 4), ("tratarea nodurilor inaccesibile", 1), ("afișare și complexitatea O(n + m)", 2)],
          "<p>Parcurgere în lățime (BFS), complexitate O(n + m).</p>", cod_model="""from collections import deque
with open('graf.in') as f:
    n, m = map(int, f.readline().split())
    L = [[] for _ in range(n + 1)]
    for _ in range(m):
        x, y = map(int, f.readline().split())
        L[x].append(y); L[y].append(x)
    s = int(f.readline())
d = [-1] * (n + 1)
d[s] = 0
q = deque([s])
while q:
    x = q.popleft()
    for y in L[x]:
        if d[y] == -1:
            d[y] = d[x] + 1
            q.append(y)
print(*d[1:])""", fisiere={"graf.in": "7 6\n1 2\n1 3\n2 4\n3 4\n4 5\n6 7\n1\n"}),
        D("<p>TIC și rețele.</p><ol type='a'><li>În B2:B31 se află mediile elevilor. Scrieți formulele pentru: numărul de elevi cu media cel puțin 5; media clasei rotunjită la două zecimale; în C2, calificativul „FB” (≥ 9), „B” (≥ 7), „S” (≥ 5) sau „I”, pentru a fi copiat în jos. (4 p)</li><li>Ce culoare are un link aflat în <code>&lt;nav id=\"meniu\"&gt;&lt;ul&gt;&lt;li class=\"activ\"&gt;&lt;a&gt;</code> la trecerea mouse-ului, dacă există regulile <code>nav ul li a:hover {color: red}</code>, <code>#meniu .activ a {color: green}</code>, <code>.activ a {color: blue}</code>? Justificați prin specificitate. (3 p)</li><li>Pentru adresa 172.16.45.130/20 determinați adresa rețelei, adresa de broadcast și numărul de gazde. (3 p)</li></ol>",
          10, [("a) COUNTIF corect", 1), ("a) ROUND(AVERAGE) corect", 1), ("a) IF imbricat cu referință relativă", 2), ("b) culoarea corectă", 1), ("b) justificarea prin specificitate (id)", 2), ("c) adresa rețelei și broadcast", 2), ("c) numărul de gazde", 1)],
          "<p>a) <code>=COUNTIF(B2:B31;\">=5\")</code> · <code>=ROUND(AVERAGE(B2:B31);2)</code> · <code>=IF(B2&gt;=9;\"FB\";IF(B2&gt;=7;\"B\";IF(B2&gt;=5;\"S\";\"I\")))</code></p><p>b) <strong>Verde</strong>: specificitățile sunt (0,1,4), (1,1,1), (0,1,1); regula cu id are specificitatea cea mai mare și se aplică și la hover.</p><p>c) {R0}</p>",
          calc=[("import ipaddress\nn = ipaddress.ip_interface('172.16.45.130/20').network\nprint(f'rețeaua {n.network_address}, broadcast {n.broadcast_address}, {n.num_addresses - 2} gazde')", "")]),
    ]),
    dict(titlu="Subiectul al III-lea", punctaj=30, itemi=[
        D("<p>Pentru o lecție de Informatică și TIC la clasa a VII-a, cu tema „Siguranța în mediul online”:</p><ol type='a'><li>precizați tipul lecției și formulați trei obiective operaționale; (6 p)</li><li>descrieți desfășurarea a trei momente ale lecției (captarea atenției, dirijarea învățării, obținerea performanței), cu activitatea profesorului, a elevilor și metodele folosite; (12 p)</li><li>propuneți un proiect de grup ca metodă complementară de evaluare: sarcina, produsul și o grilă cu 4 criterii; (8 p)</li><li>numiți două efecte perturbatoare care pot apărea la evaluarea proiectelor și o măsură pentru fiecare. (4 p)</li></ol>",
          30, [("a) tipul lecției", 1), ("a) trei obiective operaționale corecte (comportament, condiții, criteriu)", 5),
               ("b) captarea atenției: activitate concretă și motivantă", 4), ("b) dirijarea învățării: metode active, rolurile profesorului și elevilor", 4), ("b) obținerea performanței: sarcini individuale/în grup, legate de obiective", 4),
               ("c) sarcina și produsul proiectului", 4), ("c) grilă cu 4 criterii clare", 4),
               ("d) două efecte numite corect", 2), ("d) măsuri potrivite", 2)],
          """<p><strong>a)</strong> Lecție mixtă. O1 – să identifice cel puțin 4 din 5 indicii de phishing într-un mesaj dat; O2 – să evalueze 5 parole și să justifice pentru cel puțin 4 dacă sunt puternice, folosind cel puțin două criterii; O3 – să configureze setările de confidențialitate ale unui profil fictiv conform unei liste de verificare, respectând toate cele 5 cerințe.</p>
<p><strong>b)</strong> <em>Captarea atenției</em> (3'): profesorul arată un mesaj „Ai câștigat un telefon – confirmă datele aici” și întreabă câți l-ar deschide; elevii votează și argumentează (problematizare). <em>Dirijarea învățării</em> (15'): ciorchine pe tema „pericole online” completat cu propunerile elevilor; profesorul sistematizează (phishing, parole slabe, date personale, cyberbullying) și demonstrează pe exemple reale anonimizate; elevii notează regulile de protecție. <em>Obținerea performanței</em> (15'): pe grupe, elevii analizează fișe cu mesaje, parole și profiluri (O1–O3), apoi fiecare grupă prezintă concluziile; profesorul oferă feedback.</p>
<p><strong>c)</strong> Proiect pe grupe (2 săptămâni): „Ghid de siguranță online pentru colegii de clasa a V-a” – produs: prezentare digitală de 6–8 diapozitive și un afiș. Grilă (1–4 puncte/criteriu): corectitudinea informațiilor; adecvarea la public (limbaj, exemple); calitatea produsului digital (structură, design, surse citate); colaborarea și prezentarea orală.</p>
<p><strong>d)</strong> Efectul halo – evaluarea pe criteriile grilei, separat pe fiecare criteriu, fără a ține cont de rezultatele anterioare ale grupei; efectul de contrast – evaluarea fiecărui proiect raportat la grilă, nu la proiectul prezentat anterior (eventual evaluare cu doi evaluatori sau evaluare între colegi pe aceeași grilă).</p>"""),
    ]),
]))
