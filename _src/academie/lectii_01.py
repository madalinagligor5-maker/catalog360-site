from util import C, O, T

LECTII = []

# ------------------------------------------------------------------ 0
LECTII.append(dict(
    id="l0", nr="0", scurt="Pornire: mediul de lucru", titlu="Pornire: cum lucrezi în Python",
    programa="Programa 5.A: sintaxa limbajului, medii de programare specifice, structura programelor, comentarii",
    obiective=["ce înseamnă că Python este un limbaj interpretat", "ce medii de programare poți folosi la examen și la clasă",
               "cum arată și cum se rulează un program", "cum folosești editorul cu verificare automată din această pagină"],
    teorie=f"""
<h3>Python, limbaj interpretat</h3>
<p>Un program Python (fișier <code>.py</code>) este executat de <strong>interpretor</strong> instrucțiune cu instrucțiune, fără un pas separat de compilare care să producă un fișier executabil (ca la C++). Consecință practică: o eroare de execuție de pe linia 20 apare abia când programul ajunge acolo; liniile de dinainte s-au executat deja. Erorile de sintaxă, în schimb, sunt semnalate înainte de execuție.</p>
<h3>Medii de programare</h3>
{T(["Mediu", "Ce oferă", "Când îl folosești"],
   ["<strong>IDLE</strong>", "vine cu Python; consolă interactivă (<code>&gt;&gt;&gt;</code>) + editor; F5 rulează", "instalare minimă, laboratoare cu calculatoare vechi"],
   ["<strong>Thonny</strong>", "pentru începători: depanator pas cu pas, vezi valorile variabilelor", "la clasă, pentru a explica execuția"],
   ["<strong>Visual Studio Code / PyCharm</strong>", "editoare profesionale, completare automată, depanare", "proiecte mai mari, liceu"],
   ["<strong>Linia de comandă</strong>", "<code>python program.py</code> (Windows: și <code>py program.py</code>)", "rularea cu fișiere de intrare/ieșire"])}
<h3>Primul program</h3>
{C('''# Comentariu: tot ce urmează după # este ignorat de interpretor
nume = input("Cum te numești? ")     # citește un text de la tastatură
print("Bun venit,", nume + "!")       # afișează pe ecran''')}
<ul>
<li>Instrucțiunile se scriu câte una pe linie; nu se pun <code>;</code> la final (se pot folosi pentru a scrie două instrucțiuni pe aceeași linie, dar nu se recomandă).</li>
<li><strong>Indentarea</strong> (spațiile de la începutul liniei) face parte din sintaxă: ea arată ce instrucțiuni aparțin unui <code>if</code>, <code>for</code>, unei funcții. Convenția: 4 spații.</li>
<li>Python face diferența între litere mari și mici: <code>Nume</code> și <code>nume</code> sunt variabile diferite; <code>Print</code> nu există.</li>
</ul>
<h3>Cum folosești exercițiile din această pagină</h3>
<ol>
<li>Citește enunțul și exemplul (intrare → ieșire).</li>
<li>Scrie programul în editorul negru. <kbd>Tab</kbd> indentează, <kbd>Enter</kbd> păstrează indentarea, <kbd>Ctrl</kbd>+<kbd>Enter</kbd> pornește verificarea.</li>
<li><strong>Rulează cu intrarea</strong> – execută programul cu datele din caseta „Intrare”, ca să vezi ce afișează.</li>
<li><strong>Verifică</strong> – programul este rulat pe toate testele; dacă un test pică, vezi intrarea, ce se aștepta și ce a afișat programul tău.</li>
</ol>
<div class="note warn"><b>Regula de aur a evaluatoarelor:</b> afișează exact ce cere enunțul, în formatul cerut – fără mesaje suplimentare de tipul „Rezultatul este:”. Textul din <code>input("...")</code> este ignorat la verificare, deci poți păstra mesaje prietenoase la citire.</div>
""",
    rezolvate=[dict(titlu="Salut personalizat", enunt="Se citește un nume; afișează un mesaj de bun venit.",
                    cod='nume = input("Nume: ")\nprint("Bun venit,", nume + "!")', intrare="Ana")],
    exercitii=[
        dict(titlu="Primul tău program", nivel="ușor",
             enunt="Se citește un nume. Afișează exact <code>Salut, NUME!</code> (de exemplu <code>Salut, Ana!</code>).",
             start='nume = input()\n# completează afișarea\n',
             sol='nume = input()\nprint("Salut, " + nume + "!")',
             teste=[dict(**{"in": "Ana"}), dict(**{"in": "Ion Popescu"}), dict(**{"in": "x"})]),
        dict(titlu="Două linii", nivel="ușor",
             enunt="Se citesc, pe două linii, un oraș și o țară. Afișează pe prima linie țara și pe a doua orașul.",
             sol='oras = input()\ntara = input()\nprint(tara)\nprint(oras)',
             teste=[{"in": "Cluj\nRomânia"}, {"in": "Paris\nFranța"}]),
    ],
    quiz=[("Ce se întâmplă cu textul de după <code>#</code>?", ["este afișat", "este ignorat de interpretor", "produce o eroare", "este citit de la tastatură"], 1, "Este un comentariu."),
          ("În Python, indentarea:", ["este opțională, doar estetică", "face parte din sintaxă", "se folosește doar în funcții", "se înlocuiește cu acolade"], 1, "Blocurile de instrucțiuni se delimitează prin indentare."),
          ("Ce instrucțiune este corectă?", ["Print(\"ok\")", "print \"ok\"", "print(\"ok\")", "echo(\"ok\")"], 2, "Funcția se numește print, cu litere mici, și cere paranteze în Python 3.")],
))

# ------------------------------------------------------------------ 1
LECTII.append(dict(
    id="l1", nr="1", scurt="Variabile, tipuri, citire/scriere", titlu="Variabile, tipuri de date, citire și scriere",
    programa="Programa 5.A: vocabular, identificatori, constante, tipuri scalare de date, variabile/etichete, citirea/scrierea datelor",
    obiective=["ce este o variabilă în Python (o etichetă pentru un obiect)", "tipurile int, float, bool, str și funcția type()",
               "cum citești numere: int(input()), float(input()) și mai multe valori pe o linie", "cum controlezi afișarea cu sep, end și f-string-uri"],
    teorie=f"""
<h3>Variabile = etichete</h3>
<p>În Python, o variabilă este un <strong>nume (etichetă) legat de un obiect</strong> din memorie. Atribuirea <code>x = 5</code> creează obiectul întreg 5 și leagă numele <code>x</code> de el. Variabila nu are un tip fix: <code>x = "cinci"</code> o leagă ulterior de un șir. Tipul îl are obiectul: <code>type(x)</code>.</p>
<p><strong>Identificatori</strong>: litere, cifre și <code>_</code>, nu încep cu cifră, nu pot fi cuvinte cheie (<code>if</code>, <code>for</code>, <code>while</code>, <code>def</code>, <code>class</code>, <code>return</code>, <code>and</code>, <code>or</code>, <code>not</code>, <code>in</code>, <code>is</code>, <code>True</code>, <code>False</code>, <code>None</code>…). Convenția: <code>litere_mici_cu_underscore</code>; constantele se scriu cu majuscule: <code>PI = 3.14159</code> (prin convenție – Python nu le blochează).</p>
{T(["Tip", "Exemple de constante", "Observații"],
   ["<code>int</code>", "<code>0</code>, <code>-17</code>, <code>10**100</code>, <code>0b101</code>, <code>0o17</code>, <code>0xFF</code>", "precizie nelimitată"],
   ["<code>float</code>", "<code>3.14</code>, <code>-0.5</code>, <code>1e-3</code>, <code>2.0</code>", "reprezentare aproximativă (64 de biți)"],
   ["<code>bool</code>", "<code>True</code>, <code>False</code>", "subtip al lui int: True + True == 2"],
   ["<code>str</code>", "<code>'ab'</code>, <code>\"ab\"</code>, <code>'''text pe mai multe linii'''</code>", "imutabil"],
   ["<code>NoneType</code>", "<code>None</code>", "„nicio valoare”"])}
<h3>Atribuiri</h3>
{C('''a = b = 0            # atribuire multiplă: ambele leagă același obiect 0
x, y = 3, 7          # atribuire paralelă (despachetare)
x, y = y, x          # interschimbare fără variabilă auxiliară
n += 1               # n = n + 1 (există și -=, *=, /=, //=, %=, **=)''')}
<h3>Citirea datelor</h3>
<p><code>input()</code> întoarce <strong>întotdeauna un șir de caractere</strong> (fără caracterul de linie nouă). Pentru numere se convertește explicit:</p>
{C('''n = int(input())                    # un întreg pe o linie
x = float(input())                  # un număr real
a, b = map(int, input().split())    # doi întregi pe aceeași linie, separați prin spații
v = list(map(int, input().split())) # toți întregii de pe o linie, într-o listă''')}
<div class="note warn"><b>Capcana clasică:</b> <code>a = input(); b = input(); print(a + b)</code> pentru 2 și 3 afișează <code>23</code> – s-au concatenat două șiruri. Conversia cu <code>int()</code> rezolvă problema.</div>
<h3>Afișarea</h3>
{C('''print(1, 2, 3)               # 1 2 3   (separator implicit: spațiu)
print(1, 2, 3, sep="-")      # 1-2-3
print("a", end="")           # nu trece la linie nouă
print("b")                   # ab
nota = 9.456
print(f"Media: {nota:.2f}")  # Media: 9.46   (f-string, 2 zecimale)
print("Media:", round(nota, 1))''')}
""",
    rezolvate=[
        dict(titlu="Aria și perimetrul dreptunghiului", enunt="Se citesc lungimea și lățimea (numere naturale, pe aceeași linie). Afișează aria și perimetrul, pe linii separate.",
             cod='L, l = map(int, input().split())\nprint(L * l)\nprint(2 * (L + l))', intrare="7 4"),
        dict(titlu="Temperatura", enunt="Se citește o temperatură în grade Celsius (număr real). Afișează-o în Fahrenheit cu o zecimală (F = C · 9/5 + 32).",
             cod='c = float(input())\nf = c * 9 / 5 + 32\nprint(f"{f:.1f}")', intrare="36.6",
             explicatie="<code>{f:.1f}</code> rotunjește la o zecimală doar la afișare; valoarea din variabilă rămâne neschimbată."),
    ],
    exercitii=[
        dict(titlu="Suma a două numere", nivel="ușor", enunt="Se citesc două numere întregi, câte unul pe linie. Afișează suma lor.",
             sol="a = int(input())\nb = int(input())\nprint(a + b)",
             teste=[{"in": "2\n3"}, {"in": "-10\n4"}, {"in": "123456789123\n987654321987"}]),
        dict(titlu="Media aritmetică", nivel="ușor",
             enunt="Se citesc trei numere întregi pe aceeași linie. Afișează media lor aritmetică cu exact două zecimale.",
             sol='a, b, c = map(int, input().split())\nprint(f"{(a + b + c) / 3:.2f}")',
             teste=[{"in": "9 10 8"}, {"in": "1 2 2"}, {"in": "-3 0 4"}]),
        dict(titlu="Interschimbare", nivel="ușor",
             enunt="Se citesc două cuvinte pe aceeași linie. Afișează-le în ordine inversă, separate prin <code>-</code>.",
             sol='a, b = input().split()\na, b = b, a\nprint(a, b, sep="-")',
             teste=[{"in": "mere pere"}, {"in": "unu doi"}]),
        dict(titlu="Ore și minute", nivel="mediu",
             enunt="Se citește un număr natural m de minute. Afișează-l sub forma <code>H ore si M minute</code>.",
             sol='m = int(input())\nprint(m // 60, "ore si", m % 60, "minute")',
             teste=[{"in": "135"}, {"in": "59"}, {"in": "600"}, {"in": "0"}]),
    ],
    quiz=[("Ce tip are valoarea întoarsă de <code>input()</code>?", ["int", "depinde de ce scrie utilizatorul", "str", "float"], 2, "Întotdeauna str; conversia se face explicit."),
          ("Ce afișează <code>print(1, 2, sep=\"\", end=\"!\")</code>?", ["1 2!", "12!", "1,2!", "12"], 1, "sep gol lipește valorile, end înlocuiește linia nouă."),
          ("Care identificator este invalid?", ["_total", "nota2", "2nota", "Nota"], 2, "Un identificator nu poate începe cu o cifră."),
          ("După <code>x, y = 3, 7</code> și <code>x, y = y, x</code>, x are valoarea:", ["3", "7", "10", "eroare"], 1, "Interschimbare prin atribuire paralelă.")],
))

# ------------------------------------------------------------------ 2
LECTII.append(dict(
    id="l2", nr="2", scurt="Expresii și operatori", titlu="Expresii și operatori",
    programa="Programa 5.A: operatori, expresii; capitolul 3: prelucrări ale datelor numerice",
    obiective=["operatorii aritmetici, mai ales //, % și **", "operatorii relaționali (inclusiv comparațiile înlănțuite) și logici",
               "prioritatea operatorilor", "funcții predefinite utile: abs, round, min, max, divmod, int, float, str"],
    teorie=f"""
{T(["Operator", "Semnificație", "Exemplu → rezultat"],
   ["<code>+ - *</code>", "adunare, scădere, înmulțire", "<code>7 * 2</code> → 14"],
   ["<code>/</code>", "împărțire reală (rezultat float mereu)", "<code>7 / 2</code> → 3.5; <code>6 / 2</code> → 3.0"],
   ["<code>//</code>", "câtul împărțirii întregi (rotunjire în jos, spre −∞)", "<code>7 // 2</code> → 3; <code>-7 // 2</code> → −4"],
   ["<code>%</code>", "restul (are semnul împărțitorului)", "<code>7 % 3</code> → 1; <code>-7 % 3</code> → 2"],
   ["<code>**</code>", "ridicare la putere", "<code>2 ** 10</code> → 1024; <code>9 ** 0.5</code> → 3.0"],
   ["<code>== != &lt; &lt;= &gt; &gt;=</code>", "comparații (rezultat bool)", "<code>3 &lt; 5</code> → True"],
   ["<code>and or not</code>", "operatori logici (scurtcircuitați)", "<code>x &gt; 0 and x % 2 == 0</code>"])}
<h3>Prioritate (de la mare la mică)</h3>
<p><code>**</code> → semnul <code>-x</code> → <code>* / // %</code> → <code>+ -</code> → comparații → <code>not</code> → <code>and</code> → <code>or</code>. Atenție: <code>-2 ** 2</code> este −4 (puterea se face prima), iar <code>2 ** 3 ** 2</code> este 2<sup>9</sup> = 512 (puterea se asociază de la dreapta). În caz de dubiu, folosește paranteze.</p>
<h3>Comparații înlănțuite</h3>
<p><code>10 &lt;= x &lt;= 99</code> este echivalent cu <code>10 &lt;= x and x &lt;= 99</code> – „x are două cifre”.</p>
<h3>Ultima cifră, prima cifră, divizibilitate</h3>
{C('''n = 2026
print(n % 10)        # 6  – ultima cifră
print(n // 10)       # 202 – n fără ultima cifră
print(n % 100)       # 26 – ultimele două cifre
print(n % 7 == 0)    # False – n se divide cu 7?
q, r = divmod(n, 7)  # câtul și restul simultan: 289, 3''')}
<h3>Funcții predefinite (built-in)</h3>
{T(["Funcție", "Exemplu"],
   ["<code>abs(x)</code>", "<code>abs(-4)</code> → 4"],
   ["<code>round(x, k)</code>", "<code>round(3.14159, 2)</code> → 3.14; <code>round(2.5)</code> → 2 (rotunjire la par)"],
   ["<code>min, max</code>", "<code>max(3, 9, 4)</code> → 9"],
   ["<code>int, float, str</code>", "<code>int(\"12\")</code> → 12; <code>int(3.9)</code> → 3 (trunchiere); <code>str(5)</code> → \"5\""],
   ["<code>pow(a, n, m)</code>", "a<sup>n</sup> mod m, calculat eficient"],
   ["<code>math.sqrt, math.gcd, math.floor, math.ceil</code>", "necesită <code>import math</code>"])}
<div class="note"><b>Valori logice:</b> sunt considerate „false” în condiții: <code>0</code>, <code>0.0</code>, <code>""</code>, <code>[]</code>, <code>{{}}</code>, <code>None</code>, <code>False</code>. Orice altceva este „adevărat”. Deci <code>if n % 2:</code> înseamnă „dacă n este impar”.</div>
""",
    rezolvate=[
        dict(titlu="Cifrele unui număr de trei cifre", enunt="Se citește un număr natural de exact trei cifre. Afișează suma cifrelor și numărul scris invers.",
             cod='n = int(input())\nu = n % 10\nz = n // 10 % 10\ns = n // 100\nprint(s + z + u)\nprint(u * 100 + z * 10 + s)', intrare="472"),
        dict(titlu="An bisect", enunt="Se citește un an. Afișează True dacă este bisect, altfel False.",
             cod='an = int(input())\nprint(an % 4 == 0 and an % 100 != 0 or an % 400 == 0)', intrare="1900",
             explicatie="<code>and</code> are prioritate față de <code>or</code>, deci expresia se citește: (divizibil cu 4 și nu cu 100) sau divizibil cu 400."),
    ],
    exercitii=[
        dict(titlu="Câtul și restul", nivel="ușor", enunt="Se citesc două numere naturale a și b (b ≠ 0), pe aceeași linie. Afișează câtul și restul împărțirii lui a la b, separate printr-un spațiu.",
             sol="a, b = map(int, input().split())\nprint(a // b, a % b)", teste=[{"in": "17 5"}, {"in": "4 9"}, {"in": "100 10"}]),
        dict(titlu="Ultimele două cifre", nivel="ușor", enunt="Se citește un număr natural n ≥ 10. Afișează suma ultimelor două cifre ale sale.",
             sol="n = int(input())\nprint(n % 10 + n // 10 % 10)", teste=[{"in": "2026"}, {"in": "10"}, {"in": "99"}, {"in": "123456789"}]),
        dict(titlu="Număr de două cifre par", nivel="ușor", enunt="Se citește un număr întreg n. Afișează <code>DA</code> dacă n are exact două cifre și este par, altfel <code>NU</code>. (Poți folosi expresia condițională <code>\"DA\" if ... else \"NU\"</code>.)",
             sol='n = int(input())\nprint("DA" if 10 <= n <= 99 and n % 2 == 0 else "NU")',
             teste=[{"in": "42"}, {"in": "43"}, {"in": "100"}, {"in": "8"}, {"in": "-42"}]),
        dict(titlu="Distanța dintre două puncte", nivel="mediu", enunt="Se citesc coordonatele întregi x1 y1 x2 y2 pe aceeași linie. Afișează distanța dintre puncte cu trei zecimale.",
             sol='x1, y1, x2, y2 = map(int, input().split())\nd = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5\nprint(f"{d:.3f}")',
             teste=[{"in": "0 0 3 4"}, {"in": "1 1 2 2"}, {"in": "-5 2 7 -3"}]),
    ],
    quiz=[("Cât este <code>-7 // 2</code>?", ["-3", "-4", "-3.5", "3"], 1, "// rotunjește în jos (spre −∞)."),
          ("Cât este <code>2 ** 3 ** 2</code>?", ["64", "512", "36", "eroare"], 1, "Puterea se asociază de la dreapta: 2 ** 9."),
          ("Ce valoare are <code>not 0 and 3 &gt; 2</code>?", ["True", "False", "0", "3"], 0, "not 0 este True; True and True este True."),
          ("Cum obții a doua cifră de la dreapta a lui n?", ["n % 100", "n // 10 % 10", "n % 10 // 10", "n // 100"], 1, "Elimini ultima cifră, apoi iei ultima cifră a rezultatului.")],
))

# ------------------------------------------------------------------ 3
LECTII.append(dict(
    id="l3", nr="3", scurt="Decizii: if, elif, else", titlu="Instrucțiunea de decizie: if, elif, else",
    programa="Programa 5.A: instrucțiuni; capitolul 2: structura alternativă",
    obiective=["formele if, if–else, if–elif–else", "blocurile prin indentare și instrucțiunile imbricate", "expresia condițională", "cum alegi ordinea condițiilor"],
    teorie=f"""
{C('''nota = float(input())
if nota >= 9:
    print("Foarte bine")
elif nota >= 7:          # se evaluează doar dacă prima condiție a fost falsă
    print("Bine")
elif nota >= 5:
    print("Suficient")
else:
    print("Insuficient")''')}
<ul>
<li>După condiție urmează <code>:</code>, iar instrucțiunile blocului sunt indentate. Un bloc nu poate fi gol – se folosește <code>pass</code> dacă nu vrei să faci nimic.</li>
<li>La <code>if–elif–else</code> se execută <strong>cel mult o ramură</strong>: prima a cărei condiție este adevărată. Ordinea contează: dacă am începe cu <code>nota &gt;= 5</code>, un 10 ar primi „Suficient”.</li>
<li>Python nu are <code>switch</code> clasic; se folosește lanțul <code>elif</code> (sau, din Python 3.10, <code>match</code>, care nu este cerut de programă).</li>
<li>Expresia condițională: <code>semn = "pozitiv" if x &gt; 0 else "nepozitiv"</code>.</li>
</ul>
<h3>Maximul a trei numere – trei variante</h3>
{C('''a, b, c = map(int, input().split())
# 1) cu if-uri succesive
m = a
if b > m:
    m = b
if c > m:
    m = c
# 2) cu funcția predefinită
m = max(a, b, c)
# 3) cu expresii condiționale
m = a if a >= b and a >= c else (b if b >= c else c)''')}
<div class="note warn"><b>Greșeli frecvente:</b> <code>if x = 5:</code> (atribuire în loc de <code>==</code> – eroare de sintaxă); <code>if x == 1 or 2:</code> (mereu adevărat, pentru că <code>2</code> este „adevărat”; corect: <code>x == 1 or x == 2</code> sau <code>x in (1, 2)</code>); compararea unui șir citit cu un număr (<code>input() == 5</code> este mereu False).</div>
""",
    rezolvate=[
        dict(titlu="Ecuația de gradul I", enunt="Se citesc a și b (întregi). Rezolvă ecuația a·x + b = 0, tratând toate cazurile.",
             cod='a, b = map(int, input().split())\nif a != 0:\n    print(f"x = {-b / a:.2f}")\nelif b == 0:\n    print("o infinitate de solutii")\nelse:\n    print("nu are solutii")', intrare="0 5",
             explicatie="Testele trebuie să acopere toate cele trei ramuri: a ≠ 0; a = 0 și b = 0; a = 0 și b ≠ 0."),
        dict(titlu="Tipul triunghiului", enunt="Se citesc trei lungimi naturale. Afișează dacă pot forma un triunghi și, dacă da, ce fel de triunghi este.",
             cod='a, b, c = map(int, input().split())\nif a + b <= c or a + c <= b or b + c <= a:\n    print("nu formeaza triunghi")\nelif a == b == c:\n    print("echilateral")\nelif a == b or b == c or a == c:\n    print("isoscel")\nelse:\n    print("oarecare")', intrare="5 5 8"),
    ],
    exercitii=[
        dict(titlu="Par sau impar", nivel="ușor", enunt="Se citește un număr întreg. Afișează <code>par</code> sau <code>impar</code>.",
             sol='n = int(input())\nif n % 2 == 0:\n    print("par")\nelse:\n    print("impar")', teste=[{"in": "4"}, {"in": "7"}, {"in": "0"}, {"in": "-3"}]),
        dict(titlu="Calificativ", nivel="ușor", enunt="Se citește un punctaj natural între 0 și 100. Afișează calificativul: <code>FB</code> pentru cel puțin 90, <code>B</code> pentru cel puțin 70, <code>S</code> pentru cel puțin 50, altfel <code>I</code>.",
             sol='p = int(input())\nif p >= 90:\n    print("FB")\nelif p >= 70:\n    print("B")\nelif p >= 50:\n    print("S")\nelse:\n    print("I")',
             teste=[{"in": "95"}, {"in": "90"}, {"in": "70"}, {"in": "69"}, {"in": "50"}, {"in": "0"}]),
        dict(titlu="Ordonare a trei numere", nivel="mediu", enunt="Se citesc trei numere întregi pe aceeași linie. Afișează-le în ordine crescătoare, separate prin spațiu, <strong>fără</strong> a folosi <code>sorted</code> sau <code>sort</code>.",
             sol='a, b, c = map(int, input().split())\nif a > b:\n    a, b = b, a\nif b > c:\n    b, c = c, b\nif a > b:\n    a, b = b, a\nprint(a, b, c)',
             teste=[{"in": "3 1 2"}, {"in": "1 2 3"}, {"in": "3 2 1"}, {"in": "5 5 1"}, {"in": "-1 7 -9"}]),
        dict(titlu="Cadranul", nivel="mediu", enunt="Se citesc coordonatele întregi x și y ale unui punct. Afișează <code>origine</code>, <code>axa Ox</code> (pe Ox, nu în origine), <code>axa Oy</code> (pe Oy, nu în origine) sau numărul cadranului (1, 2, 3, 4).",
             sol='x, y = map(int, input().split())\nif x == 0 and y == 0:\n    print("origine")\nelif y == 0:\n    print("axa Ox")\nelif x == 0:\n    print("axa Oy")\nelif x > 0 and y > 0:\n    print(1)\nelif x < 0 < y:\n    print(2)\nelif x < 0 and y < 0:\n    print(3)\nelse:\n    print(4)',
             teste=[{"in": "0 0"}, {"in": "3 0"}, {"in": "0 -2"}, {"in": "2 5"}, {"in": "-2 5"}, {"in": "-1 -1"}, {"in": "4 -7"}]),
    ],
    quiz=[("Câte ramuri se pot executa într-un <code>if–elif–else</code>?", ["toate cele adevărate", "exact una", "cel mult una", "două"], 2, "Exact una dacă există else; cel mult una în general."),
          ("Ce problemă are <code>if x == 1 or 2:</code>?", ["niciuna", "este mereu adevărată", "eroare de sintaxă", "este mereu falsă"], 1, "2 este interpretat ca adevărat."),
          ("Ce instrucțiune lasă un bloc „gol”?", ["skip", "continue", "pass", "None"], 2, "pass nu face nimic.")],
))

# ------------------------------------------------------------------ 4
LECTII.append(dict(
    id="l4", nr="4", scurt="Bucla for și range", titlu="Structura repetitivă for și funcția range",
    programa="Programa 5.A: instrucțiuni; capitolul 3: algoritmi de bază pentru prelucrarea seriilor de valori",
    obiective=["cum parcurge for o secvență", "toate formele lui range", "șabloanele: sumă, numărare, minim/maxim, căutare", "cum citești n valori"],
    teorie=f"""
<p><code>for</code> parcurge pe rând elementele unei secvențe (listă, șir, interval). Intervalul de numere se generează cu <code>range</code>:</p>
{T(["Apel", "Valori generate"],
   ["<code>range(5)</code>", "0, 1, 2, 3, 4"],
   ["<code>range(2, 6)</code>", "2, 3, 4, 5 (capătul din dreapta nu este inclus)"],
   ["<code>range(1, 10, 3)</code>", "1, 4, 7"],
   ["<code>range(10, 0, -2)</code>", "10, 8, 6, 4, 2"],
   ["<code>range(5, 1)</code>", "nicio valoare – bucla nu se execută"])}
<h3>Șabloane care trebuie știute pe de rost</h3>
{C('''n = int(input())
v = list(map(int, input().split()))    # cele n valori, pe o linie

s = 0                  # suma
cnt = 0                # câte sunt pare
mx = v[0]              # maximul: se inițializează cu PRIMUL element, nu cu 0
poz = -1               # poziția primei valori negative
for i in range(n):
    s += v[i]
    if v[i] % 2 == 0:
        cnt += 1
    if v[i] > mx:
        mx = v[i]
    if v[i] < 0 and poz == -1:
        poz = i
print(s, cnt, mx, poz)''')}
<ul>
<li>Dacă valorile vin <strong>câte una pe linie</strong>: <code>for _ in range(n): x = int(input())</code>.</li>
<li><code>for x in v:</code> parcurge valorile direct; <code>for i, x in enumerate(v):</code> dă și poziția.</li>
<li>Variabila buclei poate fi modificată în corp, dar asta <em>nu</em> schimbă iterațiile următoare (spre deosebire de C++).</li>
</ul>
<h3>Bucle imbricate</h3>
{C('''for i in range(1, 4):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()''')}
{O("1\n1 2\n1 2 3")}
""",
    rezolvate=[
        dict(titlu="Suma divizorilor", enunt="Se citește n natural nenul. Afișează divizorii lui n pe o linie și suma lor pe linia următoare.",
             cod='n = int(input())\ns = 0\nfor d in range(1, n + 1):\n    if n % d == 0:\n        print(d, end=" ")\n        s += d\nprint()\nprint(s)', intrare="12",
             explicatie="Variantă mai eficientă: d până la √n, adunând perechile d și n // d (atenție la pătratele perfecte)."),
        dict(titlu="Tabla înmulțirii", enunt="Se citește n. Afișează tabla înmulțirii cu n de la 1 la 5.",
             cod='n = int(input())\nfor i in range(1, 6):\n    print(f"{n} x {i} = {n * i}")', intrare="7"),
    ],
    exercitii=[
        dict(titlu="Suma primelor n numere", nivel="ușor", enunt="Se citește n natural. Afișează 1 + 2 + … + n și 1² + 2² + … + n², pe linii separate.",
             sol="n = int(input())\ns1 = s2 = 0\nfor i in range(1, n + 1):\n    s1 += i\n    s2 += i * i\nprint(s1)\nprint(s2)",
             teste=[{"in": "3"}, {"in": "10"}, {"in": "0"}, {"in": "1000"}]),
        dict(titlu="Câte numere pare", nivel="ușor", enunt="Pe prima linie se află n, pe a doua n numere întregi. Afișează câte dintre ele sunt pare.",
             sol="n = int(input())\nv = list(map(int, input().split()))\ncnt = 0\nfor x in v:\n    if x % 2 == 0:\n        cnt += 1\nprint(cnt)",
             teste=[{"in": "5\n1 2 3 4 6"}, {"in": "3\n1 3 5"}, {"in": "4\n0 -2 -3 8"}]),
        dict(titlu="Maxim și de câte ori apare", nivel="mediu", enunt="Pe prima linie n, pe a doua n numere întregi. Afișează valoarea maximă și de câte ori apare, separate prin spațiu, folosind o <strong>singură</strong> parcurgere și fără <code>max</code>/<code>count</code>.",
             sol="n = int(input())\nv = list(map(int, input().split()))\nmx, cnt = v[0], 0\nfor x in v:\n    if x > mx:\n        mx, cnt = x, 1\n    elif x == mx:\n        cnt += 1\nprint(mx, cnt)",
             teste=[{"in": "6\n3 9 2 9 1 9"}, {"in": "4\n-5 -2 -7 -2"}, {"in": "1\n7"}, {"in": "5\n1 2 3 4 5"}]),
        dict(titlu="Triunghi de numere", nivel="mediu", enunt="Se citește n. Afișează n linii; linia i conține numerele de la i la 1, descrescător, separate prin spațiu.",
             sol='n = int(input())\nfor i in range(1, n + 1):\n    print(*range(i, 0, -1))',
             teste=[{"in": "4"}, {"in": "1"}, {"in": "6"}]),
        dict(titlu="Secvență crescătoare maximă", nivel="dificil", enunt="Pe prima linie n, pe a doua n numere întregi. Afișează lungimea celei mai lungi secvențe de elemente <strong>consecutive</strong> strict crescătoare.",
             sol="n = int(input())\nv = list(map(int, input().split()))\nbest = cur = 1\nfor i in range(1, n):\n    if v[i] > v[i - 1]:\n        cur += 1\n    else:\n        cur = 1\n    best = max(best, cur)\nprint(best)",
             teste=[{"in": "8\n1 2 3 1 2 3 4 0"}, {"in": "1\n5"}, {"in": "4\n4 3 2 1"}, {"in": "5\n1 2 2 3 4"}]),
    ],
    quiz=[("Ce valori generează <code>range(1, 10, 3)</code>?", ["1 4 7 10", "1 4 7", "3 6 9", "1 3 5 7 9"], 1, "Capătul 10 nu este inclus."),
          ("De câte ori se execută corpul pentru <code>for i in range(5, 1):</code>?", ["4", "5", "0", "la nesfârșit"], 2, "Fără pas negativ, intervalul este vid."),
          ("Cu ce se inițializează corect maximul unei liste cu numere posibil negative?", ["0", "-1", "primul element", "None"], 2, "Primul element este mereu o valoare validă."),
          ("Ce afișează <code>print(*range(3))</code>?", ["range(0, 3)", "[0, 1, 2]", "0 1 2", "3"], 2, "Operatorul * despachetează valorile ca argumente separate.")],
))

# ------------------------------------------------------------------ 5
LECTII.append(dict(
    id="l5", nr="5", scurt="Bucla while, cifre, break", titlu="Structura repetitivă while; prelucrarea cifrelor; break și continue",
    programa="Programa 5.A: instrucțiuni; capitolul 3: cifrele unui număr, divizibilitate, algoritmul lui Euclid, baze de numerație",
    obiective=["când folosești while în loc de for", "algoritmii pe cifre: sumă, inversare, palindrom, cifră maximă", "Euclid, primalitate, conversii între baze",
               "break, continue și ramura else a buclelor"],
    teorie=f"""
<p><code>while condiție:</code> repetă blocul cât timp condiția este adevărată. Se folosește când <strong>nu știi dinainte</strong> numărul de pași (cifrele unui număr, Euclid, citire până la o valoare-santinelă). Python nu are <code>do … while</code>; se simulează cu <code>while True:</code> și <code>break</code>.</p>
{C('''n = int(input())
s = 0          # suma cifrelor
inv = 0        # numărul oglindit
cmax = 0       # cifra maximă
while n > 0:
    c = n % 10             # ultima cifră
    s += c
    inv = inv * 10 + c
    cmax = max(cmax, c)
    n //= 10               # eliminăm ultima cifră
print(s, inv, cmax)''')}
<div class="note warn"><b>Atenție la n = 0:</b> bucla de mai sus nu se execută, deci 0 are „zero cifre”. Dacă se cere numărul de cifre, tratează separat cazul 0 sau folosește <code>len(str(n))</code>. Și: bucla distruge valoarea lui n – păstrează o copie dacă mai ai nevoie de ea (de exemplu la palindrom: <code>n == inv</code>).</div>
<h3>Algoritmi numerici de bază</h3>
{C('''def cmmdc(a, b):              # Euclid
    while b != 0:
        a, b = b, a % b
    return a

def prim(n):                  # încercare până la radical: O(√n)
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True

def in_baza(n, b):            # din baza 10 în baza b (2..10)
    if n == 0:
        return "0"
    s = ""
    while n > 0:
        s = str(n % b) + s
        n //= b
    return s

print(cmmdc(84, 36), prim(97), in_baza(13, 2), int("1101", 2))''')}
{O("12 True 1101 13")}
<h3>break, continue, else</h3>
<ul>
<li><code>break</code> oprește imediat bucla curentă; <code>continue</code> sare la următoarea iterație.</li>
<li>Ramura <code>else</code> a unei bucle se execută doar dacă bucla s-a terminat <strong>fără break</strong> – util pentru „am căutat și n-am găsit”.</li>
</ul>
{C('''# citește numere până la 0 (santinelă) și afișează suma celor pozitive
s = 0
while True:
    x = int(input())
    if x == 0:
        break
    if x < 0:
        continue
    s += x
print(s)''')}
""",
    rezolvate=[
        dict(titlu="Palindrom", enunt="Se citește n natural. Afișează DA dacă n este palindrom (se citește la fel în ambele sensuri), altfel NU.",
             cod='n = int(input())\ncopie, inv = n, 0\nwhile copie > 0:\n    inv = inv * 10 + copie % 10\n    copie //= 10\nprint("DA" if inv == n else "NU")', intrare="12321"),
        dict(titlu="Cifrele pare ale unui număr", enunt="Construiește numărul format din cifrele pare ale lui n, în ordinea din n (algoritm tipic de bacalaureat).",
             cod='n = int(input())\nk, p = 0, 1\nwhile n > 0:\n    c = n % 10\n    if c % 2 == 0:\n        k += c * p\n        p *= 10\n    n //= 10\nprint(k)', intrare="123456",
             explicatie="Cifrele se obțin de la dreapta la stânga; puterea p le așază la locul corect. Dacă n are cifre pare doar 0, rezultatul este 0 – capcană frecventă la subiecte."),
    ],
    exercitii=[
        dict(titlu="Numărul de cifre", nivel="ușor", enunt="Se citește un număr natural n (poate fi 0). Afișează numărul său de cifre, <strong>fără</strong> a-l transforma în șir.",
             sol="n = int(input())\nif n == 0:\n    print(1)\nelse:\n    k = 0\n    while n > 0:\n        k += 1\n        n //= 10\n    print(k)",
             teste=[{"in": "2026"}, {"in": "0"}, {"in": "7"}, {"in": "1000000"}]),
        dict(titlu="Cel mai mare divizor comun", nivel="ușor", enunt="Se citesc două numere naturale nenule. Afișează cmmdc-ul și cmmmc-ul lor, separate prin spațiu (fără <code>math.gcd</code>).",
             sol="a, b = map(int, input().split())\nx, y = a, b\nwhile y:\n    x, y = y, x % y\nprint(x, a * b // x)",
             teste=[{"in": "84 36"}, {"in": "7 13"}, {"in": "10 10"}, {"in": "1 999"}]),
        dict(titlu="Prim sau nu", nivel="mediu", enunt="Se citește n natural (n ≤ 10<sup>12</sup>). Afișează <code>prim</code> sau <code>neprim</code>. Atenție la 0, 1, 2 și la timpul de execuție.",
             sol='n = int(input())\nok = n >= 2\nd = 2\nwhile d * d <= n and ok:\n    if n % d == 0:\n        ok = False\n    d += 1\nprint("prim" if ok else "neprim")',
             teste=[{"in": "97"}, {"in": "1"}, {"in": "2"}, {"in": "0"}, {"in": "49"}, {"in": "999999000001"}, {"in": "1000000007"}]),
        dict(titlu="Conversie în baza 2", nivel="mediu", enunt="Se citește n natural. Afișează reprezentarea lui în baza 2, fără <code>bin</code> și fără <code>format</code>.",
             sol='n = int(input())\nif n == 0:\n    print(0)\nelse:\n    s = ""\n    while n:\n        s = str(n % 2) + s\n        n //= 2\n    print(s)',
             teste=[{"in": "13"}, {"in": "0"}, {"in": "1"}, {"in": "1024"}, {"in": "2026"}]),
        dict(titlu="Suma până la 0", nivel="mediu", enunt="Se citesc numere întregi, câte unul pe linie, până la apariția valorii 0 (care nu face parte din șir). Afișează câte numere au fost și media lor cu două zecimale; dacă primul număr este 0, afișează <code>sir vid</code>.",
             sol='s = k = 0\nwhile True:\n    x = int(input())\n    if x == 0:\n        break\n    s += x\n    k += 1\nif k == 0:\n    print("sir vid")\nelse:\n    print(k, f"{s / k:.2f}")',
             teste=[{"in": "4\n6\n-1\n0"}, {"in": "0"}, {"in": "7\n0"}]),
    ],
    quiz=[("Ce structură lipsește din Python și se simulează cu <code>while True</code> + <code>break</code>?", ["for", "do … while", "if … else", "elif"], 1, "Python nu are bucla cu test final."),
          ("Ramura <code>else</code> a unei bucle <code>while</code> se execută:", ["când condiția este falsă de la început sau devine falsă, fără break", "doar după break", "niciodată", "la fiecare iterație"], 0, "Rulează la terminarea normală."),
          ("Ce calculează <code>inv = inv * 10 + n % 10; n //= 10</code> repetat cât n &gt; 0?", ["suma cifrelor", "oglinditul lui n", "numărul de cifre", "cifra maximă"], 1, "Construiește numărul cu cifrele în ordine inversă."),
          ("Câte iterații face testul de primalitate pentru n = 10<sup>12</sup> + 39 (prim)?", ["aproximativ 10<sup>12</sup>", "aproximativ 10<sup>6</sup>", "aproximativ 12", "aproximativ 500 000"], 1, "Se merge până la √n = 10<sup>6</sup>.")],
))

# ------------------------------------------------------------------ 6
LECTII.append(dict(
    id="l6", nr="6", scurt="Șiruri de caractere (str)", titlu="Șiruri de caractere – clasa str",
    programa="Programa 5.A: clasa str – apartenență, concatenare, multiplicare, acces la caracter/subșir, comparare lexicografică, căutare, înlocuire, separare",
    obiective=["indexarea și felierea (slicing)", "operatorii +, *, in și compararea lexicografică", "metodele cerute de programă: find, replace, split (și join, count, upper, lower, strip)",
               "faptul că str este imutabil și cum construiești un șir nou", "codurile caracterelor: ord și chr"],
    teorie=f"""
{C('''s = "informatica"
print(s[0], s[-1], len(s))     # i a 11
print(s[2:6], s[:4], s[-3:])   # form info ica
print(s[::2], s[::-1])         # ifraia acitamrofni
print("ma" in s, "x" not in s) # True True
print("ab" + "cd", "-" * 5)    # abcd -----''')}
<ul>
<li>Indici de la 0 la <code>len(s) - 1</code>; indicii negativi numără de la final. <code>s[a:b]</code> ia caracterele de la a la b − 1; <code>s[a:b:p]</code> cu pasul p.</li>
<li><strong>Imutabil:</strong> <code>s[0] = "I"</code> produce <code>TypeError</code>. Se construiește un șir nou: <code>s = "I" + s[1:]</code>.</li>
<li><strong>Comparare lexicografică</strong> (ca în dicționar, după codurile Unicode): <code>"Ana" &lt; "Ion"</code>, <code>"abc" &lt; "abd"</code>, <code>"ab" &lt; "abc"</code>; dar <code>"Zebra" &lt; "ana"</code> (majusculele au coduri mai mici) și <code>"10" &lt; "9"</code>.</li>
</ul>
{T(["Metodă", "Efect", "Exemplu → rezultat"],
   ["<code>s.find(t)</code>", "poziția primei apariții a lui t sau −1", "<code>\"banana\".find(\"an\")</code> → 1"],
   ["<code>s.find(t, start)</code>", "caută începând de la start", "<code>\"banana\".find(\"an\", 2)</code> → 3"],
   ["<code>s.index(t)</code>", "ca find, dar <code>ValueError</code> dacă lipsește", ""],
   ["<code>s.count(t)</code>", "numărul de apariții (fără suprapunere)", "<code>\"banana\".count(\"a\")</code> → 3"],
   ["<code>s.replace(a, b)</code>", "șir nou cu a înlocuit de b", "<code>\"a-b-c\".replace(\"-\", \"\")</code> → \"abc\""],
   ["<code>s.split()</code> / <code>s.split(sep)</code>", "listă de cuvinte (după spații) / după separator", "<code>\"1,2,3\".split(\",\")</code> → ['1', '2', '3']"],
   ["<code>sep.join(lista)</code>", "lipește elementele (șiruri) cu sep", "<code>\" \".join([\"a\", \"b\"])</code> → \"a b\""],
   ["<code>upper, lower, capitalize, title</code>", "schimbarea literelor", "<code>\"ana\".capitalize()</code> → \"Ana\""],
   ["<code>strip, lstrip, rstrip</code>", "elimină spațiile (sau caracterele date) de la capete", "<code>\"  x \".strip()</code> → \"x\""],
   ["<code>isdigit, isalpha, isupper, islower</code>", "teste pe caractere", "<code>\"2026\".isdigit()</code> → True"],
   ["<code>startswith, endswith</code>", "prefix / sufix", "<code>\"poza.png\".endswith(\".png\")</code> → True"])}
<h3>Caractere și coduri</h3>
{C('''print(ord("A"), ord("a"), chr(66))      # 65 97 B
c = "d"
print(ord(c) - ord("a"))                # 3 – poziția literei în alfabet
print(chr(ord(c) - 32))                 # D – litera mare corespunzătoare''')}
<h3>Parcurgere și construire</h3>
{C('''s = input()
vocale = 0
rez = ""
for c in s:
    if c in "aeiouAEIOU":
        vocale += 1
    else:
        rez += c          # șir nou fără vocale
print(vocale, rez)''')}
""",
    rezolvate=[
        dict(titlu="Cuvântul cel mai lung", enunt="Se citește o propoziție (cuvinte separate prin spații). Afișează cel mai lung cuvânt (primul, la egalitate) și numărul de cuvinte.",
             cod='cuvinte = input().split()\ncel = ""\nfor w in cuvinte:\n    if len(w) > len(cel):\n        cel = w\nprint(cel, len(cuvinte))', intrare="Ana are mere si pere"),
        dict(titlu="Cifrul lui Cezar", enunt="Criptează un text cu litere mari și spații, deplasând fiecare literă cu k poziții (circular).",
             cod='text = input()\nk = int(input())\nrez = ""\nfor c in text:\n    if "A" <= c <= "Z":\n        rez += chr((ord(c) - ord("A") + k) % 26 + ord("A"))\n    else:\n        rez += c\nprint(rez)', intrare="ZILE BUNE\n3"),
    ],
    exercitii=[
        dict(titlu="Inversare și palindrom", nivel="ușor", enunt="Se citește un cuvânt. Afișează cuvântul inversat, apoi <code>DA</code> sau <code>NU</code> după cum este palindrom (fără a ține cont de litere mari/mici).",
             sol='s = input()\nprint(s[::-1])\nprint("DA" if s.lower() == s.lower()[::-1] else "NU")',
             teste=[{"in": "Cojoc"}, {"in": "python"}, {"in": "a"}]),
        dict(titlu="Numărarea vocalelor", nivel="ușor", enunt="Se citește un text. Afișează numărul de vocale (a, e, i, o, u – mari sau mici).",
             sol='s = input()\nprint(sum(1 for c in s.lower() if c in "aeiou"))',
             teste=[{"in": "Ana are mere"}, {"in": "xyz"}, {"in": "AEIOU aeiou"}]),
        dict(titlu="Inițiale", nivel="ușor", enunt="Se citește un nume complet (cuvinte separate prin spații, posibil mai multe spații). Afișează inițialele cu majuscule, urmate fiecare de punct, lipite (ex.: <code>A.M.P.</code>).",
             sol='print("".join(w[0].upper() + "." for w in input().split()))',
             teste=[{"in": "ana maria pop"}, {"in": "  Ion   Creanga "}, {"in": "x"}]),
        dict(titlu="Apariții ale unui subșir", nivel="mediu", enunt="Pe prima linie un text, pe a doua un cuvânt t. Afișează toate pozițiile la care începe t în text (inclusiv suprapuse), separate prin spațiu, sau <code>-1</code> dacă nu apare. Folosește <code>find</code> cu poziție de start.",
             sol='s = input()\nt = input()\npoz = []\ni = s.find(t)\nwhile i != -1:\n    poz.append(i)\n    i = s.find(t, i + 1)\nprint(*poz if poz else [-1])',
             teste=[{"in": "banana\nana"}, {"in": "abcabcabc\nabc"}, {"in": "informatica\nxyz"}, {"in": "aaaa\naa"}]),
        dict(titlu="Compresie RLE", nivel="dificil", enunt="Se citește un șir nevid de litere. Comprimă grupurile de litere consecutive identice: <code>aaabccdddd</code> → <code>a3b1c2d4</code>.",
             sol='s = input()\nrez = ""\ni = 0\nwhile i < len(s):\n    j = i\n    while j < len(s) and s[j] == s[i]:\n        j += 1\n    rez += s[i] + str(j - i)\n    i = j\nprint(rez)',
             teste=[{"in": "aaabccdddd"}, {"in": "a"}, {"in": "abc"}, {"in": "zzzzzzzzzzzz"}]),
    ],
    quiz=[("Ce afișează <code>\"programare\"[3:7]</code>?", ["gram", "grama", "ogra", "gra"], 0, "Pozițiile 3, 4, 5, 6."),
          ("Care comparație este adevărată?", ["\"10\" &lt; \"9\"", "\"b\" &lt; \"a\"", "\"abc\" &lt; \"ab\"", "\"a\" &lt; \"Z\""], 0, "Se compară caracter cu caracter: '1' &lt; '9'."),
          ("Ce întoarce <code>\"a,b,,c\".split(\",\")</code>?", ["['a','b','c']", "['a','b','','c']", "['a,b,,c']", "eroare"], 1, "Între două virgule consecutive apare șirul vid."),
          ("Ce se întâmplă la <code>s = \"ana\"; s[0] = \"A\"</code>?", ["s devine \"Ana\"", "TypeError", "se creează o copie", "nimic"], 1, "str este imutabil.")],
))
