from util import C, CO, O, T

LECTII = []

# ------------------------------------------------------------------ 13
LECTII.append(dict(
    id="l13", nr="13", scurt="Algoritmi pentru proba practică", titlu="Algoritmi clasici pentru proba practică",
    programa="Programa capitolul 3 (*): serii de valori, prelucrări numerice, generare sistematică, sortări, căutare binară, interclasare",
    obiective=["ciurul lui Eratostene și exponențierea rapidă", "metoda bulelor și sortarea prin numărare", "căutarea binară iterativă și varianta „prima poziție ≥ x”",
               "generarea cu itertools și fără", "alegerea algoritmului în funcție de dimensiunea datelor"],
    teorie=f"""
<h3>Cât de mari pot fi datele?</h3>
{T(["n până la aproximativ", "Complexitate acceptabilă în Python (câteva secunde)", "Exemple"],
   ["10", "O(n!) , O(2ⁿ·n)", "permutări, submulțimi"],
   ["2 000 – 5 000", "O(n²)", "bule, selecție, două bucle imbricate"],
   ["10⁵ – 10⁶", "O(n log n) sau O(n)", "sorted, căutare binară, frecvențe, ciur"],
   ["10¹² (o singură valoare)", "O(√n) sau O(log n)", "primalitate, exponențiere rapidă"])}
{CO('''def ciur(n):                        # toate numerele prime ≤ n
    prim = [True] * (n + 1)
    prim[0] = prim[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if prim[i]:
            for j in range(i * i, n + 1, i):
                prim[j] = False
    return [i for i in range(n + 1) if prim[i]]

def bule(v):                        # sortare prin metoda bulelor, cu oprire timpurie
    n = len(v)
    for k in range(n - 1):
        schimb = False
        for i in range(n - 1 - k):
            if v[i] > v[i + 1]:
                v[i], v[i + 1] = v[i + 1], v[i]
                schimb = True
        if not schimb:
            break

def prima_poz(v, x):                # prima poziție cu v[i] >= x (v sortat)
    st, dr = 0, len(v)              # răspunsul poate fi și len(v)
    while st < dr:
        m = (st + dr) // 2
        if v[m] < x:
            st = m + 1
        else:
            dr = m
    return st

print(ciur(30))
w = [5, 1, 4, 2]; bule(w); print(w)
print(prima_poz([1, 3, 3, 7, 9], 3), prima_poz([1, 3, 3, 7, 9], 8), prima_poz([1, 3], 10))''')}
<p>În biblioteca standard: <code>bisect.bisect_left(v, x)</code> face exact ce face <code>prima_poz</code>. La examen poți fi rugat să implementezi algoritmul, deci învață-l și „de mână”.</p>
<h3>Generare sistematică</h3>
{CO('''from itertools import product, permutations, combinations
print(list(product([0, 1], repeat=2)))       # produs cartezian
print(list(permutations("abc", 2))[:4])      # aranjamente
print(list(combinations(range(1, 5), 2)))    # combinări''')}
""",
    rezolvate=[
        dict(titlu="Sortare prin numărare (listă de frecvențe)", enunt="Se dau note întregi de la 1 la 10. Afișează-le sortate și nota cea mai frecventă.",
             cod='v = list(map(int, input().split()))\nf = [0] * 11\nfor x in v:\n    f[x] += 1\nprint(*[x for x in range(1, 11) for _ in range(f[x])])\nprint(f.index(max(f)))', intrare="7 9 10 7 5 9 7 8",
             explicatie="Complexitate O(n + 10) – mai bună decât orice sortare prin comparații, pentru că valorile sunt dintr-un domeniu mic."),
    ],
    exercitii=[
        dict(titlu="Câte prime în interval", nivel="mediu", enunt="Se citesc a și b (2 ≤ a ≤ b ≤ 10<sup>6</sup>). Afișează câte numere prime sunt în [a, b]. O testare individuală a fiecărui număr este prea lentă – folosește ciurul lui Eratostene.",
             sol="a, b = map(int, input().split())\nprim = bytearray([1]) * (b + 1)\nprim[0] = prim[1] = 0\nfor i in range(2, int(b ** 0.5) + 1):\n    if prim[i]:\n        prim[i * i::i] = bytearray(len(range(i * i, b + 1, i)))\nprint(sum(prim[a:b + 1]))",
             teste=[{"in": "2 30"}, {"in": "14 16"}, {"in": "2 2"}, {"in": "1 1000000"}]),
        dict(titlu="Metoda bulelor – numărul de interschimbări", nivel="mediu", enunt="Pe o linie se dau numere întregi. Sortează-le cu metoda bulelor și afișează lista sortată, apoi numărul total de interschimbări efectuate.",
             sol="v = list(map(int, input().split()))\nn, cnt = len(v), 0\nfor k in range(n - 1):\n    for i in range(n - 1 - k):\n        if v[i] > v[i + 1]:\n            v[i], v[i + 1] = v[i + 1], v[i]\n            cnt += 1\nprint(*v)\nprint(cnt)",
             teste=[{"in": "5 1 4 2 8"}, {"in": "1 2 3"}, {"in": "3 2 1"}, {"in": "2 2 1"}]),
        dict(titlu="Căutare binară – număr de apariții", nivel="dificil", enunt="Pe prima linie o listă sortată crescător, pe a doua câteva valori x. Pentru fiecare x afișează de câte ori apare în listă, folosind <strong>căutare binară</strong> (două căutări: prima poziție ≥ x și prima poziție &gt; x).",
             sol="def prima(v, x):\n    st, dr = 0, len(v)\n    while st < dr:\n        m = (st + dr) // 2\n        if v[m] < x:\n            st = m + 1\n        else:\n            dr = m\n    return st\n\nv = list(map(int, input().split()))\nfor x in map(int, input().split()):\n    print(prima(v, x + 1) - prima(v, x))",
             teste=[{"in": "1 3 3 3 7 9 9\n3 9 4 0 10 1"}, {"in": "5\n5 6"}]),
        dict(titlu="Generarea șirurilor binare", nivel="mediu", enunt="Se citește n (1 ≤ n ≤ 10). Afișează în ordine lexicografică toate șirurile de n biți care <strong>nu</strong> conțin doi de 1 alăturați, câte unul pe linie.",
             sol="from itertools import product\nn = int(input())\nfor t in product('01', repeat=n):\n    s = ''.join(t)\n    if '11' not in s:\n        print(s)",
             teste=[{"in": "3"}, {"in": "1"}, {"in": "5"}]),
        dict(titlu="Interclasare fără duplicate", nivel="mediu", enunt="Se dau două liste sortate crescător (posibil cu valori repetate), pe două linii. Afișează valorile care apar în <strong>ambele</strong> liste, o singură dată fiecare, crescător, folosind un algoritm de tip interclasare (doi indici); dacă nu există, afișează <code>-</code>.",
             sol="a = list(map(int, input().split()))\nb = list(map(int, input().split()))\ni = j = 0\nrez = []\nwhile i < len(a) and j < len(b):\n    if a[i] < b[j]:\n        i += 1\n    elif a[i] > b[j]:\n        j += 1\n    else:\n        if not rez or rez[-1] != a[i]:\n            rez.append(a[i])\n        i += 1\n        j += 1\nprint(*rez if rez else ['-'])",
             teste=[{"in": "1 2 2 4 6 8\n2 2 3 4 8 8 9"}, {"in": "1 2\n3 4"}, {"in": "5 5 5\n5"}]),
    ],
    quiz=[("Ce complexitate are ciurul lui Eratostene?", ["O(n²)", "O(n log log n)", "O(√n)", "O(2ⁿ)"], 1, "Practic aproape liniar."),
          ("Pentru n = 10⁵ valori, ce sortare scrisă de tine este potrivită?", ["bulelor", "selecție", "interclasare", "permutări"], 2, "O(n log n); metodele O(n²) ar face ~10¹⁰ pași."),
          ("Ce întoarce <code>bisect_left([1, 3, 3, 7], 3)</code>?", ["1", "2", "3", "0"], 0, "Prima poziție cu valoare ≥ 3.")],
))

# ------------------------------------------------------------------ 14
LECTII.append(dict(
    id="l14", nr="14", scurt="Clase și obiecte (POO)", titlu="Programare orientată pe obiecte: clase, obiecte, moștenire",
    programa="Programa 5.A: clasă, membri (date și metode), obiecte, biblioteci, niveluri de acces, constructor, destructor/finalizer, clasă derivată; capitolul 1: modelul obiectual",
    obiective=["definirea unei clase cu constructor și metode", "atribute de instanță și de clasă", "niveluri de acces prin convenție și name mangling", "moștenire, super() și suprascriere", "metode speciale: __str__, __eq__, __lt__"],
    teorie=f"""
{CO('''class ContBancar:
    banca = "Banca Școlii"                 # atribut de CLASĂ (comun tuturor obiectelor)

    def __init__(self, titular, sold=0):   # constructorul
        self.titular = titular             # atribut public
        self._sold = sold                  # „protejat” – convenție: nu-l folosi din afară
        self.__pin = "0000"                # „privat” – redenumit intern _ContBancar__pin

    def depune(self, suma):
        if suma <= 0:
            raise ValueError("suma trebuie să fie pozitivă")
        self._sold += suma

    def sold(self):
        return self._sold

    def __str__(self):                     # folosit de print()
        return f"{self.titular}: {self._sold} lei"

class ContEconomii(ContBancar):            # clasă derivată
    def __init__(self, titular, sold=0, dobanda=0.05):
        super().__init__(titular, sold)    # constructorul clasei de bază
        self.dobanda = dobanda

    def aplica_dobanda(self):
        self._sold = round(self._sold * (1 + self.dobanda), 2)

    def __str__(self):                     # suprascriere (polimorfism)
        return super().__str__() + f" (economii, {self.dobanda:.0%})"

a = ContBancar("Ana", 100); a.depune(50)
b = ContEconomii("Dan", 200); b.aplica_dobanda()
for c in (a, b):
    print(c)
print(isinstance(b, ContBancar), ContBancar.banca)''')}
<ul>
<li><code>self</code> este obiectul curent; se scrie explicit ca prim parametru al metodelor.</li>
<li>Python nu are <code>private</code>/<code>public</code> ca C++: <code>_x</code> este o convenție, iar <code>__x</code> este doar redenumit (<em>name mangling</em>).</li>
<li><strong>Finalizer</strong>: <code>__del__</code> este apelat când obiectul nu mai are referințe; momentul nu este garantat, deci resursele se eliberează explicit (metodă <code>close()</code>, <code>with</code>).</li>
<li>Metode speciale: <code>__str__</code> (afișare), <code>__eq__</code> (<code>==</code>), <code>__lt__</code> (<code>&lt;</code>, permite <code>sorted</code>), <code>__len__</code>, <code>__add__</code> (<code>+</code>).</li>
<li>„Biblioteci”: clasele predefinite (<code>list</code>, <code>str</code>, <code>dict</code>…) și cele din module (<code>datetime.date</code>, <code>fractions.Fraction</code>) se folosesc la fel: instanțiere, apoi acces la membri cu punct.</li>
</ul>
""",
    rezolvate=[
        dict(titlu="Clasa Fractie", enunt="O clasă pentru fracții, cu simplificare și adunare prin operatorul +.",
             cod='from math import gcd\n\nclass Fractie:\n    def __init__(self, a, b):\n        if b == 0:\n            raise ZeroDivisionError("numitor nul")\n        d = gcd(a, b) * (1 if b > 0 else -1)\n        self.a, self.b = a // d, b // d\n\n    def __add__(self, alta):\n        return Fractie(self.a * alta.b + alta.a * self.b, self.b * alta.b)\n\n    def __str__(self):\n        return f"{self.a}/{self.b}"\n\nprint(Fractie(1, 2) + Fractie(1, 3), Fractie(6, -8))'),
    ],
    exercitii=[
        dict(titlu="Clasa Dreptunghi", nivel="ușor", enunt="Completează clasa <code>Dreptunghi</code> cu metodele <code>arie()</code>, <code>perimetru()</code> și <code>este_patrat()</code>. Programul citește n dreptunghiuri (lungime lățime) și afișează pentru fiecare aria, perimetrul și <code>patrat</code>/<code>nu</code>.",
             start='class Dreptunghi:\n    def __init__(self, L, l):\n        self.L = L\n        self.l = l\n\n    # adaugă metodele aici\n\nn = int(input())\nfor _ in range(n):\n    L, l = map(int, input().split())\n    d = Dreptunghi(L, l)\n    print(d.arie(), d.perimetru(), "patrat" if d.este_patrat() else "nu")\n',
             sol='class Dreptunghi:\n    def __init__(self, L, l):\n        self.L = L\n        self.l = l\n\n    def arie(self):\n        return self.L * self.l\n\n    def perimetru(self):\n        return 2 * (self.L + self.l)\n\n    def este_patrat(self):\n        return self.L == self.l\n\nn = int(input())\nfor _ in range(n):\n    L, l = map(int, input().split())\n    d = Dreptunghi(L, l)\n    print(d.arie(), d.perimetru(), "patrat" if d.este_patrat() else "nu")',
             teste=[{"in": "2\n3 4\n5 5"}, {"in": "1\n1 10"}]),
        dict(titlu="Elevi sortați cu __lt__", nivel="mediu", enunt="Scrie clasa <code>Elev</code> (nume, medie) cu metodele <code>__lt__</code> (ordinea: medie descrescător, apoi nume crescător) și <code>__str__</code> (afișează <code>nume medie</code>, media cu două zecimale). Programul citește n elevi și îi afișează cu <code>for e in sorted(lista): print(e)</code>.",
             sol='class Elev:\n    def __init__(self, nume, medie):\n        self.nume = nume\n        self.medie = medie\n\n    def __lt__(self, alt):\n        return (-self.medie, self.nume) < (-alt.medie, alt.nume)\n\n    def __str__(self):\n        return f"{self.nume} {self.medie:.2f}"\n\nn = int(input())\nlista = []\nfor _ in range(n):\n    nume, m = input().split()\n    lista.append(Elev(nume, float(m)))\nfor e in sorted(lista):\n    print(e)',
             teste=[{"in": "3\nDan 8.5\nAna 9.25\nIon 8.5"}, {"in": "1\nX 10"}]),
        dict(titlu="Moștenire: angajați", nivel="dificil", enunt="Clasa <code>Angajat</code> are nume și salariu de bază; metoda <code>venit()</code> întoarce salariul. Clasa derivată <code>Manager</code> are în plus un bonus, iar <code>venit()</code> întoarce salariul + bonusul. Se citesc n linii de forma <code>A nume salariu</code> sau <code>M nume salariu bonus</code>. Afișează fiecare nume cu venitul, apoi venitul total.",
             sol='class Angajat:\n    def __init__(self, nume, salariu):\n        self.nume = nume\n        self.salariu = salariu\n\n    def venit(self):\n        return self.salariu\n\nclass Manager(Angajat):\n    def __init__(self, nume, salariu, bonus):\n        super().__init__(nume, salariu)\n        self.bonus = bonus\n\n    def venit(self):\n        return super().venit() + self.bonus\n\nn = int(input())\nlista = []\nfor _ in range(n):\n    p = input().split()\n    if p[0] == "A":\n        lista.append(Angajat(p[1], int(p[2])))\n    else:\n        lista.append(Manager(p[1], int(p[2]), int(p[3])))\nfor a in lista:\n    print(a.nume, a.venit())\nprint(sum(a.venit() for a in lista))',
             teste=[{"in": "3\nA Ana 4000\nM Dan 6000 1500\nA Ion 3500"}, {"in": "1\nM X 1 1"}]),
    ],
    quiz=[("Cum se numește constructorul în Python?", ["constructor", "__init__", "__new__", "numele clasei"], 1, "__init__ inițializează obiectul."),
          ("Ce se întâmplă cu un atribut numit <code>__pin</code> într-o clasă <code>Cont</code>?", ["devine inaccesibil complet", "este redenumit _Cont__pin", "este șters", "devine atribut de clasă"], 1, "Name mangling."),
          ("Ce face <code>super().__init__(...)</code>?", ["creează o clasă nouă", "apelează constructorul clasei de bază", "șterge obiectul", "apelează __str__"], 1, "Reutilizează inițializarea din bază."),
          ("Ce metodă specială folosește <code>print(obiect)</code>?", ["__repr__ doar", "__str__", "__print__", "__init__"], 1, "__str__ (cu __repr__ ca rezervă).")],
))

# ------------------------------------------------------------------ 15
LECTII.append(dict(
    id="l15", nr="15", scurt="Interfețe grafice cu tkinter", titlu="Interfețe grafice simple cu tkinter",
    programa="Programa 5.A: biblioteca tkinter – Tk, Label, Button, Entry, Text, Frame, Canvas; afișarea mesajelor; pack, grid, place, get",
    obiective=["structura unei aplicații tkinter și bucla de evenimente", "widget-urile cerute de programă", "gestionarii de geometrie pack, grid, place", "citirea datelor cu get() și afișarea mesajelor", "separarea logicii de interfață"],
    teorie=f"""
<div class="note warn"><b>Atenție:</b> tkinter deschide ferestre, deci nu poate rula în această pagină. Copiază exemplele în IDLE, Thonny sau VS Code pe calculatorul tău. În Linux, dacă lipsește, se instalează pachetul <code>python3-tk</code>.</div>
{C('''import tkinter as tk
from tkinter import messagebox

def calculeaza():                          # funcția apelată la clic (eveniment)
    text = e_n.get().strip()               # Entry.get() întoarce str
    if not text.isdigit():
        messagebox.showerror("Eroare", "Introduceți un număr natural!")
        return
    n = int(text)
    l_rez.config(text=f"Suma cifrelor: {sum(int(c) for c in text)}")
    t_div.delete("1.0", tk.END)            # golește caseta Text
    t_div.insert(tk.END, " ".join(str(d) for d in range(1, n + 1) if n % d == 0))

fer = tk.Tk()                              # fereastra principală
fer.title("Numere")
cadru = tk.Frame(fer, padx=12, pady=12)    # container
cadru.pack()

tk.Label(cadru, text="n =").grid(row=0, column=0, sticky="e")
e_n = tk.Entry(cadru, width=12)
e_n.grid(row=0, column=1)
tk.Button(cadru, text="Calculează", command=calculeaza).grid(row=0, column=2, padx=6)
l_rez = tk.Label(cadru, text="")
l_rez.grid(row=1, column=0, columnspan=3)
t_div = tk.Text(cadru, width=40, height=4)  # casetă text pe mai multe linii
t_div.grid(row=2, column=0, columnspan=3)

c = tk.Canvas(fer, width=200, height=80, bg="white")
c.pack(pady=6)
c.create_rectangle(10, 10, 90, 70, fill="lightblue")
c.create_oval(110, 10, 170, 70, outline="green", width=3)
c.create_text(100, 75, text="Canvas")

fer.mainloop()                             # bucla de evenimente''')}
{T(["Element", "Rol", "Metode / opțiuni importante"],
   ["<code>Tk()</code>", "fereastra principală", "<code>title()</code>, <code>geometry(\"400x300\")</code>, <code>mainloop()</code>"],
   ["<code>Label</code>", "text (sau imagine) afișat", "<code>text=</code>, <code>config(text=…)</code>, <code>font=</code>, <code>fg=</code>, <code>bg=</code>"],
   ["<code>Button</code>", "buton", "<code>command=funcție</code> (fără paranteze!)"],
   ["<code>Entry</code>", "casetă de text pe o linie", "<code>get()</code>, <code>delete(0, tk.END)</code>, <code>insert(0, \"text\")</code>"],
   ["<code>Text</code>", "casetă pe mai multe linii", "<code>get(\"1.0\", tk.END)</code>, <code>insert(tk.END, …)</code>, <code>delete(\"1.0\", tk.END)</code>"],
   ["<code>Frame</code>", "container pentru grupare", "în el se așază alte widget-uri"],
   ["<code>Canvas</code>", "suprafață de desen", "<code>create_line</code>, <code>create_rectangle</code>, <code>create_oval</code>, <code>create_text</code>"],
   ["<code>messagebox</code>", "ferestre de mesaj", "<code>showinfo</code>, <code>showwarning</code>, <code>showerror</code>, <code>askyesno</code>"])}
<ul>
<li><code>pack()</code> – așază widget-urile unul după altul (<code>side=\"left\"</code>, <code>fill</code>, <code>expand</code>); <code>grid(row, column)</code> – tabel (<code>columnspan</code>, <code>sticky</code>); <code>place(x=…, y=…)</code> – poziție absolută. <strong>Nu amesteca pack și grid în același container.</strong></li>
<li>Greșeala clasică: <code>command=calculeaza()</code> apelează funcția o singură dată, la crearea butonului; corect este <code>command=calculeaza</code>.</li>
<li>Bună practică pentru examen și pentru testare: scrie logica în funcții separate de interfață (de exemplu <code>suma_cifre(n)</code>), iar handler-ul doar citește, apelează funcția și afișează.</li>
</ul>
""",
    rezolvate=[], exercitii=[
        dict(titlu="Logica unui convertor (fără fereastră)", nivel="mediu", enunt="Pentru o aplicație tkinter care convertește temperaturi, scrie funcția <code>converteste(text, sens)</code>: <code>text</code> este conținutul casetei Entry, iar <code>sens</code> este <code>\"CF\"</code> (Celsius → Fahrenheit) sau <code>\"FC\"</code>. Întoarce rezultatul ca șir cu o zecimală sau <code>\"Eroare\"</code> dacă textul nu este număr. Programul de test citește linii <code>sens text</code> și afișează rezultatele.",
             start='def converteste(text, sens):\n    # completează\n    pass\n\nn = int(input())\nfor _ in range(n):\n    sens, text = input().split(maxsplit=1)\n    print(converteste(text, sens))\n',
             sol='def converteste(text, sens):\n    try:\n        x = float(text.replace(",", "."))\n    except ValueError:\n        return "Eroare"\n    r = x * 9 / 5 + 32 if sens == "CF" else (x - 32) * 5 / 9\n    return f"{r:.1f}"\n\nn = int(input())\nfor _ in range(n):\n    sens, text = input().split(maxsplit=1)\n    print(converteste(text, sens))',
             teste=[{"in": "4\nCF 100\nFC 32\nCF 36,6\nFC abc"}, {"in": "1\nCF -40"}]),
    ],
    quiz=[("Ce metodă citește textul dintr-un Entry?", ["text()", "get()", "read()", "value()"], 1, "Entry.get() întoarce un str."),
          ("Care este legarea corectă a unui buton?", ["command=f()", "command=f", "onclick=f", "command=\"f\""], 1, "Se transmite funcția, nu rezultatul apelului."),
          ("Ce instrucțiune pornește bucla de evenimente?", ["fer.run()", "fer.start()", "fer.mainloop()", "tk.loop()"], 2, "mainloop() ține fereastra deschisă și tratează evenimentele."),
          ("Ce gestionar de geometrie folosește coordonate absolute?", ["pack", "grid", "place", "frame"], 2, "place(x=…, y=…).")],
))

# ------------------------------------------------------------------ 16
LECTII.append(dict(
    id="l16", nr="16", scurt="Simulare probă practică", titlu="Simulare: probleme de tip probă practică",
    programa="Combină capitolele 1, 2, 3, 5.A (marcate cu * în programă). Lucrează contra cronometru: aproximativ 20–30 de minute pe problemă.",
    obiective=["citirea atentă a enunțului: format de intrare/ieșire, restricții, cazuri limită", "alegerea structurilor de date și a algoritmului potrivit", "testarea pe cazuri limită înainte de a preda"],
    teorie=f"""
<h3>Lista de verificare înainte de predare</h3>
<ol>
<li>Citesc exact datele cerute (de la tastatură sau din fișier) și în ordinea dată?</li>
<li>Afișez exact formatul cerut (spații, linii noi, zecimale), fără mesaje în plus?</li>
<li>Am testat: un singur element, toate elementele egale, valori negative, 0, valoarea maximă?</li>
<li>Complexitatea se încadrează pentru dimensiunea maximă a datelor?</li>
<li>Codul este lizibil: nume sugestive, funcții, comentarii scurte?</li>
</ol>
<div class="note">Problemele de mai jos sunt construite după tipul cerințelor din programă (prelucrări de serii, cifre, șiruri, liste, dicționare, fișiere). Nu sunt subiecte oficiale.</div>
""",
    rezolvate=[], exercitii=[
        dict(titlu="Biblioteca", nivel="dificil", enunt="Fișierul <code>imprumuturi.txt</code> conține pe fiecare linie un împrumut: <code>nume_elev titlu_carte zile</code> (titlul este un singur cuvânt). Afișează: (1) numărul de elevi distincți; (2) cartea împrumutată de cele mai multe ori (la egalitate, prima alfabetic); (3) elevii care au cel puțin un împrumut de peste 14 zile, sortați alfabetic, pe o linie, sau <code>nimeni</code>.",
             sol='elevi = set()\nfrecv = {}\nintarziati = set()\nwith open("imprumuturi.txt") as f:\n    for linie in f:\n        p = linie.split()\n        if len(p) < 3:\n            continue\n        nume, carte, zile = p[0], p[1], int(p[2])\n        elevi.add(nume)\n        frecv[carte] = frecv.get(carte, 0) + 1\n        if zile > 14:\n            intarziati.add(nume)\nprint(len(elevi))\nprint(min(frecv, key=lambda c: (-frecv[c], c)))\nprint(*sorted(intarziati) if intarziati else ["nimeni"])',
             teste=[{"fisiere": {"imprumuturi.txt": "Ana Ion 10\nDan Amintiri 20\nAna Amintiri 3\nRadu Ion 15\nDan Baltagul 7\n"}},
                    {"fisiere": {"imprumuturi.txt": "X Carte 1\n"}},
                    {"fisiere": {"imprumuturi.txt": "B Zbor 30\nA Alfa 30\nB Alfa 1\nA Zbor 2\n\n"}}]),
        dict(titlu="Numere cu cifre distincte", nivel="dificil", enunt="Se citesc a și b (1 ≤ a ≤ b ≤ 10<sup>6</sup>). Afișează câte numere din [a, b] au toate cifrele distincte și cel mai mare astfel de număr (sau <code>-1</code> dacă nu există).",
             sol="a, b = map(int, input().split())\ncnt, mx = 0, -1\nfor x in range(a, b + 1):\n    s = str(x)\n    if len(set(s)) == len(s):\n        cnt += 1\n        mx = x\nprint(cnt, mx)",
             teste=[{"in": "1 20"}, {"in": "11 11"}, {"in": "1 1000000"}, {"in": "987650 987660"}]),
        dict(titlu="Statistici pe clase", nivel="dificil", enunt="Pe prima linie n, apoi n linii <code>nume clasa nota1 nota2 ...</code> (cel puțin o notă). Pentru fiecare clasă, în ordine alfabetică, afișează <code>clasa media_clasei elevul_cu_media_maxima</code>, unde media clasei este media mediilor elevilor, cu două zecimale (la egalitate de medii la elevi, primul alfabetic).",
             sol='n = int(input())\nclase = {}\nfor _ in range(n):\n    p = input().split()\n    note = list(map(int, p[2:]))\n    clase.setdefault(p[1], []).append((p[0], sum(note) / len(note)))\nfor c in sorted(clase):\n    v = clase[c]\n    medie = sum(m for _, m in v) / len(v)\n    best = min(v, key=lambda e: (-e[1], e[0]))[0]\n    print(c, f"{medie:.2f}", best)',
             teste=[{"in": "5\nAna 9A 9 10\nDan 9B 7 8\nIon 9A 10 10 9\nEla 9B 8 7\nRadu 10A 6"}, {"in": "2\nB 9A 8\nA 9A 8"}]),
        dict(titlu="Parolă validă", nivel="mediu", enunt="Se citește n, apoi n parole (câte una pe linie, fără spații). O parolă este validă dacă are cel puțin 8 caractere, cel puțin o literă mare, o literă mică, o cifră și un caracter care nu este literă sau cifră. Pentru fiecare, afișează <code>valida</code> sau lista problemelor separate prin virgulă, în ordinea: <code>scurta,fara_mare,fara_mica,fara_cifra,fara_simbol</code>.",
             sol='n = int(input())\nfor _ in range(n):\n    p = input()\n    probleme = []\n    if len(p) < 8:\n        probleme.append("scurta")\n    if not any(c.isupper() for c in p):\n        probleme.append("fara_mare")\n    if not any(c.islower() for c in p):\n        probleme.append("fara_mica")\n    if not any(c.isdigit() for c in p):\n        probleme.append("fara_cifra")\n    if all(c.isalnum() for c in p):\n        probleme.append("fara_simbol")\n    print(",".join(probleme) if probleme else "valida")',
             teste=[{"in": "4\nParola#2026\nabc\nPAROLA123\nparola_lunga1"}, {"in": "1\nAa1!aaaa"}]),
    ],
    quiz=[("Programul tău afișează „Rezultatul este: 5”, iar enunțul cere doar „5”. La un evaluator automat:", ["primești punctajul", "testul pică", "primești jumătate", "depinde"], 1, "Ieșirea trebuie să fie identică."),
          ("Pentru n ≤ 10⁶ numere, o soluție cu două bucle imbricate pe n:", ["este perfectă", "depășește timpul", "dă eroare de sintaxă", "consumă puțină memorie"], 1, "≈10¹² operații.")],
))
