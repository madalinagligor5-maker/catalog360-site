from util import C, CO, O, T, QZ

LECTII = []
H = "#include <iostream>\nusing namespace std;\n\n"

LECTII.append(dict(
    id="c1", nr="1", scurt="De la Python la C++", titlu="De la Python la C++: structura programului, tipuri, citire și afișare",
    programa="Programa 5.B: sintaxă, medii de programare, vocabular, identificatori, constante, tipuri de date simple, variabile, operatori, structura programelor, comentarii, expresii, citire/scriere",
    obiective=["cum arată, se compilează și se rulează un program C++", "tipurile simple și declararea variabilelor", "cin și cout", "diferențele de operatori față de Python (/, %, ++, conversii)"],
    teorie=f"""
<p>C++ este un limbaj <strong>compilat</strong>: compilatorul (g++, MSVC) transformă sursa <code>.cpp</code> într-un executabil; erorile de sintaxă și de tip apar înainte de rulare. Medii uzuale: Code::Blocks, Visual Studio, Dev-C++, VS Code + compilator.</p>
{CO(H + '''int main() {                 // execuția începe în funcția main
    int n;                   // variabilele se declară cu tip
    cin >> n;                // citire de la tastatură
    cout << "Patratul lui " << n << " este " << n * n << endl;
    return 0;                // 0 = program încheiat cu succes
}''', "c++", "7")}
{T(["", "Python", "C++"],
   ["blocuri", "indentare", "acolade <code>{ }</code>; instrucțiunile se termină cu <code>;</code>"],
   ["variabile", "fără tip declarat", "<code>int x = 5; double y; char c = 'a'; bool ok = true;</code>"],
   ["întregi", "precizie nelimitată", "<code>int</code> (de regulă 4 octeți, ±2·10⁹), <code>long long</code> (8 octeți, ±9·10¹⁸); depășirea nu este semnalată"],
   ["împărțire", "<code>7 / 2 == 3.5</code>, <code>7 // 2 == 3</code>", "între întregi <code>7 / 2 == 3</code>; <code>7 / 2.0 == 3.5</code>"],
   ["negative", "<code>-7 // 2 == -4</code>, <code>-7 % 3 == 2</code>", "<code>-7 / 2 == -3</code> (trunchiere spre 0), <code>-7 % 3 == -1</code>"],
   ["incrementare", "<code>x += 1</code>", "<code>x++</code>, <code>++x</code>, <code>x += 1</code>"],
   ["logici", "<code>and or not</code>", "<code>&amp;&amp; || !</code>"],
   ["conversie", "<code>int(x)</code>", "<code>(int)x</code>, <code>(double)a / b</code>"],
   ["afișare", "<code>print(a, b)</code>", "<code>cout &lt;&lt; a &lt;&lt; ' ' &lt;&lt; b &lt;&lt; '\\n';</code>"])}
{CO(H + '''int main() {
    int a = 7, b = 2;
    cout << a / b << " " << a % b << " " << (double)a / b << "\\n";
    cout << -7 / 2 << " " << -7 % 3 << "\\n";
    int x = 5;
    int y = x++;             // y primește 5, apoi x devine 6 (postincrementare)
    int z = ++x;             // x devine 7, apoi z primește 7 (preincrementare)
    cout << x << " " << y << " " << z << "\\n";
    char c = 'A' + 2;        // caracterele sunt coduri numerice
    cout << c << " " << (int)c << "\\n";
    return 0;
}''', "c++")}
""",
    quiz=[QZ("Ce afișează secvența?", 'int a = 17, b = 5;\ncout << a / b << " " << a % b;', ["3.4 2", "3 2", "3 2.0", "4 2"], 1, "Împărțirea între întregi dă câtul."),
          QZ("Ce afișează secvența?", 'int x = 3;\nint y = x++ + 2;\ncout << x << " " << y;', ["4 5", "4 6", "3 5", "3 6"], 0, "x++ folosește valoarea veche (3), apoi x devine 4."),
          QZ("Ce afișează secvența?", 'cout << -9 / 4 << " " << -9 % 4;', ["-2 -1", "-3 3", "-2 1", "-3 -1"], 0, "Trunchiere spre 0; restul are semnul deîmpărțitului."),
          ("Ce tip folosești pentru un produs care poate ajunge la 10¹⁵?", ["int", "long long", "char", "bool"], 1, "int are aproximativ ±2·10⁹."),
          ("Unde începe execuția unui program C++?", ["la prima linie", "în funcția main", "la primul #include", "în prima funcție definită"], 1, "main este punctul de intrare.")],
    exercitii=[
        dict(tip="aplicatie", titlu="Media a trei note", nivel="ușor", enunt="<p>Scrie un program C++ care citește trei note întregi și afișează media cu exact două zecimale. Indiciu: <code>#include &lt;iomanip&gt;</code>, apoi <code>cout &lt;&lt; fixed &lt;&lt; setprecision(2)</code>.</p>",
             cod_model='#include <iostream>\n#include <iomanip>\nusing namespace std;\n\nint main() {\n    int a, b, c;\n    cin >> a >> b >> c;\n    double m = (a + b + c) / 3.0;      // 3.0, ca împărțirea să fie reală\n    cout << fixed << setprecision(2) << m << "\\n";\n    return 0;\n}', intrare="9 10 8",
             criterii=["am inclus bibliotecile necesare și am scris funcția main", "am declarat variabilele cu tipuri potrivite", "am evitat împărțirea întreagă (3.0 sau conversie)", "am afișat cu două zecimale"]),
        dict(tip="aplicatie", titlu="Interschimbare și ultima cifră", nivel="ușor", enunt="<p>Citește două numere naturale a și b. Interschimbă valorile lor folosind o variabilă auxiliară, apoi afișează a, b și suma ultimelor lor cifre.</p>",
             cod_model=H + 'int main() {\n    int a, b, aux;\n    cin >> a >> b;\n    aux = a; a = b; b = aux;\n    cout << a << " " << b << " " << a % 10 + b % 10 << "\\n";\n    return 0;\n}', intrare="123 45",
             criterii=["interschimbarea folosește trei atribuiri", "ultima cifră se obține cu % 10", "afișarea are separatori între valori"]),
    ],
))

LECTII.append(dict(
    id="c2", nr="2", scurt="Instrucțiuni de control", titlu="Instrucțiunile C++: if, switch, while, do-while, for",
    programa="Programa 5.B: instrucțiuni; cap. 2: structuri fundamentale",
    obiective=["if/else și operatorul condițional", "switch cu break", "cele trei bucle și diferența dintre while și do-while", "capcanele frecvente: = în loc de ==, ; după if/for, acoladele lipsă"],
    teorie=f"""
{CO(H + '''int main() {
    int n = 2026, s = 0;
    while (n > 0) {              // test inițial: se poate să nu se execute deloc
        s += n % 10;
        n /= 10;
    }
    cout << "suma cifrelor: " << s << "\\n";

    int k = 0;
    do {                         // test final: corpul se execută cel puțin o dată
        k++;
    } while (k < 0);
    cout << "k = " << k << "\\n";

    for (int i = 1; i <= 10; i += 3)   // inițializare; condiție; pas
        cout << i << " ";
    cout << "\\n";

    int zi = 3;
    switch (zi) {
        case 1: cout << "luni"; break;
        case 2: cout << "marti"; break;
        case 3: cout << "miercuri"; break;
        default: cout << "alta zi";
    }
    cout << "\\n" << (s % 2 == 0 ? "suma para" : "suma impara") << "\\n";
    return 0;
}''', "c++")}
<div class="note warn"><b>Capcane:</b> <code>if (x = 5)</code> atribuie și este mereu adevărat (compilează!); <code>for (...);</code> cu <code>;</code> are corp vid; fără acolade, doar prima instrucțiune aparține lui <code>if</code>/<code>for</code>; fără <code>break</code>, <code>switch</code> continuă în cazurile următoare (fall-through).</div>
""",
    quiz=[QZ("Ce afișează secvența?", 'int x = 2;\nswitch (x) {\n    case 1: cout << "A";\n    case 2: cout << "B";\n    case 3: cout << "C";\n    default: cout << "D";\n}', ["B", "BC", "BCD", "D"], 2, "Fără break, execuția continuă în cazurile următoare."),
          QZ("Ce afișează secvența?", 'int i = 10;\ndo {\n    cout << i << " ";\n    i++;\n} while (i < 5);', ["nimic", "10", "10 11", "eroare"], 1, "do-while execută corpul o dată înainte de test."),
          QZ("Ce afișează secvența?", 'int s = 0;\nfor (int i = 1; i <= 5; i++);\n    s++;\ncout << s;', ["5", "1", "0", "6"], 1, "; după for face corpul vid; s++ se execută o singură dată."),
          QZ("Ce afișează secvența?", 'int x = 0;\nif (x = 3) cout << "DA " << x;\nelse cout << "NU";', ["NU", "DA 3", "DA 0", "eroare de compilare"], 1, "x = 3 este o atribuire, iar valoarea 3 este adevărată."),
          ("Ce buclă se execută cel puțin o dată?", ["while", "for", "do-while", "niciuna"], 2, "Testul este la final.")],
    exercitii=[
        dict(tip="aplicatie", titlu="Numere prime într-un interval", nivel="mediu", enunt="<p>Citește a și b. Afișează numerele prime din [a, b] și câte sunt, folosind o variabilă de tip <code>bool</code> și testul până la √x (<code>d * d &lt;= x</code>).</p>",
             cod_model=H + 'int main() {\n    int a, b, cnt = 0;\n    cin >> a >> b;\n    for (int x = a; x <= b; x++) {\n        bool prim = x >= 2;\n        for (int d = 2; d * d <= x && prim; d++)\n            if (x % d == 0) prim = false;\n        if (prim) { cout << x << " "; cnt++; }\n    }\n    cout << "\\n" << cnt << "\\n";\n    return 0;\n}', intrare="10 30",
             criterii=["tratez corect 0 și 1", "testez divizorii doar până la √x", "opresc testarea la primul divizor găsit", "număr și afișez corect"]),
        dict(tip="aplicatie", titlu="Meniu cu switch", nivel="ușor", enunt="<p>Citește un caracter <code>+ - * /</code> și două numere întregi; afișează rezultatul operației folosind <code>switch</code>. La împărțire cu 0 afișează <code>imposibil</code>; la alt caracter, <code>operatie necunoscuta</code>.</p>",
             cod_model=H + 'int main() {\n    char op; int a, b;\n    cin >> op >> a >> b;\n    switch (op) {\n        case \'+\': cout << a + b; break;\n        case \'-\': cout << a - b; break;\n        case \'*\': cout << a * b; break;\n        case \'/\':\n            if (b == 0) cout << "imposibil";\n            else cout << (double)a / b;\n            break;\n        default: cout << "operatie necunoscuta";\n    }\n    cout << "\\n";\n    return 0;\n}', intrare="/ 7 2",
             criterii=["fiecare case se încheie cu break", "împărțirea la zero este tratată", "împărțirea dă rezultat real", "există ramura default"]),
    ],
))

LECTII.append(dict(
    id="c3", nr="3", scurt="Tablouri", titlu="Tablouri unidimensionale (și bidimensionale)",
    programa="Programa 5.B: tablouri unidimensionale pentru memorarea listelor – declarare, acces la un element",
    obiective=["declararea și parcurgerea tablourilor", "indicii de la 0 și depășirea limitelor", "algoritmii clasici pe tablouri în C++", "matricele ca tablouri bidimensionale"],
    teorie=f"""
{CO(H + '''int main() {
    int v[100];                  // dimensiunea maximă se fixează la compilare
    int n = 6;
    int date[] = {{5, 2, 9, 1, 7, 3}};
    for (int i = 0; i < n; i++) v[i] = date[i];

    int mx = v[0], poz = 0;
    for (int i = 1; i < n; i++)
        if (v[i] > mx) {{ mx = v[i]; poz = i; }}
    cout << "maxim " << mx << " pe pozitia " << poz << "\\n";

    for (int i = 0; i < n - 1; i++)        // sortare prin selecție
        for (int j = i + 1; j < n; j++)
            if (v[j] < v[i]) {{ int aux = v[i]; v[i] = v[j]; v[j] = aux; }}
    for (int i = 0; i < n; i++) cout << v[i] << " ";
    cout << "\\n";

    int a[3][3] = {{{{1, 2, 3}}, {{4, 5, 6}}, {{7, 8, 9}}}};
    int sd = 0;
    for (int i = 0; i < 3; i++) sd += a[i][i];
    cout << "diagonala: " << sd << "\\n";
    return 0;
}}'''.replace("{{", "{").replace("}}", "}"), "c++")}
<ul>
<li>Indicii sunt de la 0 la n − 1. C++ <strong>nu verifică</strong> depășirea: <code>v[100]</code> într-un tablou de 100 de elemente este comportament nedefinit (poate „merge”, poate strica alte variabile).</li>
<li>Tablourile globale sunt inițializate cu 0; cele locale nu (conțin valori reziduale) – inițializează-le: <code>int f[10] = {{0}};</code></li>
<li>Un tablou transmis unei funcții se transmite prin adresă: modificările din funcție se văd în apelant.</li>
<li>Pentru dimensiune variabilă se folosește <code>vector&lt;int&gt;</code> (din <code>&lt;vector&gt;</code>), dar programa cere tablourile clasice.</li>
</ul>
""",
    quiz=[QZ("Ce afișează secvența?", 'int v[5] = {4, 8, 15, 16, 23};\nint s = 0;\nfor (int i = 1; i < 5; i += 2) s += v[i];\ncout << s;', ["24", "42", "39", "23"], 0, "Pozițiile 1 și 3: 8 + 16."),
          QZ("Ce afișează secvența?", 'int f[10] = {0};\nint x = 30322;\nwhile (x) { f[x % 10]++; x /= 10; }\ncout << f[3] << f[2] << f[0];', ["212", "221", "122", "211"], 1, "Cifrele 3, 0, 3, 2, 2: f[3] = 2, f[2] = 2, f[0] = 1, deci se afișează 2, 2, 1."),
          ("Care este ultimul indice valid pentru <code>int v[50];</code>?", ["50", "49", "51", "0"], 1, "Indicii sunt de la 0 la 49."),
          ("Ce se întâmplă la accesarea <code>v[60]</code> pentru <code>int v[50]</code>?", ["eroare de compilare", "excepție IndexError", "comportament nedefinit", "se returnează 0"], 2, "C++ nu verifică limitele.")],
    exercitii=[
        dict(tip="aplicatie", titlu="Inserare și ștergere într-un tablou", nivel="mediu", enunt="<p>Citește n și n numere. Inserează valoarea 0 pe poziția 2 (deplasând elementele spre dreapta), apoi șterge primul element negativ (deplasând spre stânga). Afișează tabloul după fiecare operație.</p>",
             cod_model=H + 'int main() {\n    int v[101], n;\n    cin >> n;\n    for (int i = 0; i < n; i++) cin >> v[i];\n    for (int i = n; i > 2; i--) v[i] = v[i - 1];   // de la dreapta la stânga!\n    v[2] = 0; n++;\n    for (int i = 0; i < n; i++) cout << v[i] << " ";\n    cout << "\\n";\n    int p = -1;\n    for (int i = 0; i < n && p == -1; i++) if (v[i] < 0) p = i;\n    if (p != -1) {\n        for (int i = p; i < n - 1; i++) v[i] = v[i + 1];\n        n--;\n    }\n    for (int i = 0; i < n; i++) cout << v[i] << " ";\n    cout << "\\n";\n    return 0;\n}', intrare="5\n4 -2 7 -1 9",
             criterii=["la inserare deplasez de la final spre poziție", "actualizez n după fiecare operație", "tratez cazul în care nu există negativ", "nu depășesc dimensiunea tabloului"]),
        dict(tip="aplicatie", titlu="Căutare binară în C++", nivel="mediu", enunt="<p>Citește n, un tablou sortat crescător și o valoare x. Afișează poziția lui x (căutare binară) sau -1.</p>",
             cod_model=H + 'int main() {\n    int v[1000], n, x;\n    cin >> n;\n    for (int i = 0; i < n; i++) cin >> v[i];\n    cin >> x;\n    int st = 0, dr = n - 1, poz = -1;\n    while (st <= dr && poz == -1) {\n        int m = (st + dr) / 2;\n        if (v[m] == x) poz = m;\n        else if (v[m] < x) st = m + 1;\n        else dr = m - 1;\n    }\n    cout << poz << "\\n";\n    return 0;\n}', intrare="7\n2 5 8 12 16 23 38\n23",
             criterii=["condiția buclei este st <= dr", "mijlocul se recalculează la fiecare pas", "capetele se mută cu m + 1 / m − 1", "afișez -1 când nu găsesc"]),
    ],
))

LECTII.append(dict(
    id="c4", nr="4", scurt="Funcții și recursivitate", titlu="Subprograme: funcții, parametri prin valoare și prin referință, recursivitate",
    programa="Programa 5.B: subprograme, subprograme recursive",
    obiective=["definirea, declararea (prototipul) și apelul funcțiilor", "transmiterea prin valoare vs. prin referință (&)", "funcțiile void și cele care întorc o valoare", "recursivitatea în C++"],
    teorie=f"""
{CO(H + '''int sumaCifre(int n) {               // întoarce o valoare
    int s = 0;
    while (n) { s += n % 10; n /= 10; }
    return s;
}

void dubleaza(int x, int &y) {       // x prin valoare, y prin REFERINȚĂ
    x *= 2;
    y *= 2;
}

long long fact(int n) {              // recursivă
    if (n <= 1) return 1;
    return n * fact(n - 1);
}

void afisVector(int v[], int n) {    // tabloul se transmite prin adresă
    for (int i = 0; i < n; i++) cout << v[i] << " ";
    cout << "\\n";
}

int main() {
    int a = 5, b = 5;
    dubleaza(a, b);
    cout << sumaCifre(2026) << " " << a << " " << b << " " << fact(10) << "\\n";
    int v[] = {3, 1, 4};
    afisVector(v, 3);
    return 0;
}''', "c++")}
<ul>
<li>O funcție trebuie <strong>declarată înainte de apel</strong>: fie definită mai sus, fie printr-un prototip (<code>int sumaCifre(int n);</code>) înaintea lui <code>main</code>.</li>
<li><strong>Prin valoare</strong>: funcția lucrează pe o copie. <strong>Prin referință</strong> (<code>int &amp;y</code>): numele y este un alt nume pentru variabila din apel – modificările rămân.</li>
<li>Variabilele locale dispar la ieșirea din funcție; cele globale sunt vizibile peste tot (și inițializate cu 0).</li>
</ul>
""",
    quiz=[QZ("Ce afișează programul?", 'void f(int a, int &b) {\n    a = a + b;\n    b = a * 2;\n}\nint main() {\n    int x = 3, y = 4;\n    f(x, y);\n    cout << x << " " << y << " ";\n    f(y, x);\n    cout << x << " " << y;\n    return 0;\n}', ["3 14 34 14", "7 14 34 14", "3 14 3 14", "3 4 3 4"], 0, "Doar parametrul transmis prin referință se modifică în apelant.", main=False),
          QZ("Ce afișează programul?", 'void g(int n) {\n    if (n < 1) return;\n    cout << n;\n    g(n - 2);\n    cout << n;\n}\nint main() {\n    g(5);\n    return 0;\n}', ["531135", "135531", "53135", "531"], 0, "Prima afișare la „coborâre”, a doua la „revenire”.", main=False),
          QZ("Ce afișează programul?", 'int f(int n) {\n    if (n == 0) return 0;\n    if (n % 2 == 0) return f(n / 10) + n % 10;\n    return f(n / 10);\n}\nint main() {\n    cout << f(28374);\n    return 0;\n}', ["14", "4", "22", "10"], 0, "Suma cifrelor pare ale lui n: 2 + 8 + 4.", main=False),
          ("Ce înseamnă <code>int &amp;x</code> ca parametru?", ["pointer la x", "transmitere prin referință", "adresa lui x", "x este constant"], 1, "x devine un alias al argumentului.")],
    exercitii=[
        dict(tip="aplicatie", titlu="Funcție cmmdc și simplificarea unei fracții", nivel="mediu", enunt="<p>Scrie funcția <code>int cmmdc(int a, int b)</code> (Euclid) și funcția <code>void simplifica(int &amp;a, int &amp;b)</code>. Programul citește o fracție a/b și afișează forma ireductibilă.</p>",
             cod_model=H + 'int cmmdc(int a, int b) {\n    while (b) { int r = a % b; a = b; b = r; }\n    return a;\n}\n\nvoid simplifica(int &a, int &b) {\n    int d = cmmdc(a, b);\n    a /= d; b /= d;\n}\n\nint main() {\n    int a, b;\n    cin >> a >> b;\n    simplifica(a, b);\n    cout << a << "/" << b << "\\n";\n    return 0;\n}', intrare="84 36",
             criterii=["cmmdc întoarce valoarea cu return", "simplifica primește parametri prin referință", "nu folosesc variabile globale", "funcțiile sunt definite înainte de main (sau am prototip)"]),
        dict(tip="aplicatie", titlu="Funcție recursivă pentru putere", nivel="mediu", enunt="<p>Scrie o funcție recursivă <code>long long putere(long long a, int n)</code> care calculează aⁿ prin exponențiere rapidă și afișează 3¹⁵ și 2⁴⁰.</p>",
             cod_model=H + 'long long putere(long long a, int n) {\n    if (n == 0) return 1;\n    long long p = putere(a, n / 2);\n    if (n % 2 == 0) return p * p;\n    return p * p * a;\n}\n\nint main() {\n    cout << putere(3, 15) << " " << putere(2, 40) << "\\n";\n    return 0;\n}',
             criterii=["există cazul de bază n == 0", "apelul recursiv se face o singură dată pe nivel (p salvat)", "folosesc long long pentru rezultate mari"]),
    ],
))

LECTII.append(dict(
    id="c5", nr="5", scurt="Clasa string", titlu="Șiruri de caractere: clasa string",
    programa="Programa 5.B: clasa string – concatenare, acces la un caracter, comparare lexicografică; inserare, ștergere, căutare",
    obiective=["declararea, citirea (cin și getline) și afișarea unui string", "operatorii +, [], ==, &lt;", "metodele insert, erase, find, substr, length", "diferența față de char[] din C"],
    teorie=f"""
{CO('''#include <iostream>
#include <string>
using namespace std;

int main() {
    string s = "informatica";
    cout << s.length() << " " << s[0] << " " << s.substr(2, 4) << "\\n";
    s.insert(0, "ora de ");          // inserare pe poziția 0
    cout << s << "\\n";
    s.erase(0, 7);                   // șterge 7 caractere de la poziția 0
    cout << s.find("ma") << "\\n";   // poziția primei apariții
    if (s.find("xyz") == string::npos) cout << "negasit\\n";
    s[0] = 'I';                      // string este MUTABIL în C++
    cout << s + "!" << " " << (string("abc") < string("abd")) << "\\n";
    s.replace(0, 4, "Mate");          // înlocuiește 4 caractere de la poziția 0
    cout << s << "\\n";
    return 0;
}''', "c++")}
<ul>
<li><code>cin &gt;&gt; s</code> citește un singur cuvânt (până la spațiu); <code>getline(cin, s)</code> citește toată linia. Atenție: după <code>cin &gt;&gt; n</code>, un <code>getline</code> citește restul liniei curente (șir vid) – se folosește <code>cin.ignore()</code> înainte.</li>
<li><code>find</code> întoarce <code>string::npos</code> când nu găsește. <code>substr(poz, lungime)</code>.</li>
<li>Spre deosebire de Python, <code>string</code> este mutabil: <code>s[i] = 'x'</code> este permis.</li>
<li>Șirurile de tip C (<code>char s[100]</code>) se termină cu caracterul <code>'\\0'</code> și folosesc funcțiile din <code>&lt;cstring&gt;</code>: <code>strlen</code>, <code>strcpy</code>, <code>strcat</code>, <code>strcmp</code>, <code>strstr</code>.</li>
</ul>
""",
    quiz=[QZ("Ce afișează secvența?", 'string s = "bacalaureat";\ncout << s.find("a") << " " << s.find("a", 2) << " " << s.length();', ["1 3 11", "1 1 11", "0 3 11", "1 3 10"], 0, "find caută de la poziția dată."),
          QZ("Ce afișează secvența?", 'string s = "programare";\ns.erase(3, 4);\ns.insert(0, "X");\ncout << s;', ["Xproare", "Xprore", "Xprogre", "proXare"], 0, "Se șterg „gram” (pozițiile 3–6), rămâne „proare”."),
          QZ("Ce afișează secvența?", 'string a = "Zebra", b = "ana";\ncout << (a < b) << (a.length() > b.length());', ["11", "01", "10", "00"], 0, "'Z' (90) < 'a' (97); 5 > 3."),
          ("Ce citește <code>getline(cin, s)</code>?", ["un cuvânt", "un caracter", "toată linia", "tot fișierul"], 2, "Până la caracterul de linie nouă.")],
    exercitii=[
        dict(tip="aplicatie", titlu="Numărarea cuvintelor și majuscule", nivel="mediu", enunt="<p>Citește o propoziție cu <code>getline</code> (cuvinte separate prin câte un spațiu). Afișează numărul de cuvinte și propoziția cu prima literă a fiecărui cuvânt transformată în majusculă.</p>",
             cod_model='#include <iostream>\n#include <string>\nusing namespace std;\n\nint main() {\n    string s;\n    getline(cin, s);\n    int cuv = 0;\n    for (int i = 0; i < (int)s.length(); i++)\n        if (s[i] != \' \' && (i == 0 || s[i - 1] == \' \')) {\n            cuv++;\n            if (s[i] >= \'a\' && s[i] <= \'z\') s[i] = s[i] - \'a\' + \'A\';\n        }\n    cout << cuv << "\\n" << s << "\\n";\n    return 0;\n}', intrare="ana are mere si pere",
             criterii=["folosesc getline pentru linia întreagă", "detectez începutul de cuvânt (primul caracter sau după spațiu)", "transform litera prin diferența de coduri sau toupper", "număr corect cuvintele"]),
        dict(tip="aplicatie", titlu="Înlocuirea tuturor aparițiilor", nivel="dificil", enunt="<p>Citește un text, un cuvânt a și un cuvânt b (pe linii separate). Înlocuiește toate aparițiile lui a cu b folosind <code>find</code>, <code>erase</code> și <code>insert</code> și afișează textul.</p>",
             cod_model='#include <iostream>\n#include <string>\nusing namespace std;\n\nint main() {\n    string t, a, b;\n    getline(cin, t); getline(cin, a); getline(cin, b);\n    size_t p = t.find(a);\n    while (p != string::npos) {\n        t.erase(p, a.length());\n        t.insert(p, b);\n        p = t.find(a, p + b.length());   // continuăm DUPĂ textul inserat\n    }\n    cout << t << "\\n";\n    return 0;\n}', intrare="un mar si un par si un mar\nmar\nmăr",
             criterii=["caut din nou după poziția textului inserat (evit bucla infinită când b conține a)", "folosesc string::npos pentru oprire", "erase + insert (sau replace) cu lungimile corecte"]),
    ],
))
