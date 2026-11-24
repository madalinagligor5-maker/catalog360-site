from util import C, CO, O, T, QZ

LECTII = []
H = "#include <iostream>\n#include <string>\nusing namespace std;\n\n"

LECTII.append(dict(
    id="c6", nr="6", scurt="struct și date mixte", titlu="Structuri (struct) și date organizate în modele mixte",
    programa="Programa 5.B: structuri de date pentru date neomogene (înregistrări) – definire, declarare, acces la câmp, atribuiri; elemente de limbaj pentru modele mixte",
    obiective=["definirea unui tip struct și declararea variabilelor", "accesul la câmpuri cu . și ->", "tablouri de structuri: citire, sortare, căutare", "atribuirea între structuri (copiere câmp cu câmp)"],
    teorie=f"""
{CO(H + '''struct Elev {
    string nume;
    int clasa;
    double medie;
};

int main() {
    Elev e[3] = {{"Ana", 9, 9.5}, {"Dan", 10, 8.75}, {"Ioana", 9, 9.8}};
    int n = 3;
    for (int i = 0; i < n - 1; i++)              // sortare după medie, descrescător
        for (int j = i + 1; j < n; j++)
            if (e[j].medie > e[i].medie) {
                Elev aux = e[i]; e[i] = e[j]; e[j] = aux;   // atribuire între structuri
            }
    for (int i = 0; i < n; i++)
        cout << e[i].nume << " (" << e[i].clasa << ") " << e[i].medie << "\\n";
    Elev *p = &e[0];
    cout << p->nume << " " << (*p).medie << "\\n";    // p->camp este (*p).camp
    return 0;
}''', "c++")}
<ul>
<li><code>struct</code> grupează date de tipuri diferite într-un singur tip. Câmpurile se accesează cu <code>.</code> (variabilă) sau <code>-&gt;</code> (pointer).</li>
<li>Atribuirea <code>a = b</code> între structuri copiază toate câmpurile; comparația <code>a == b</code> nu este definită implicit.</li>
<li>Modele mixte: tablouri de structuri, structuri care conțin tablouri (<code>int note[10];</code>), tablouri bidimensionale.</li>
</ul>
""",
    quiz=[QZ("Ce afișează programul?", 'struct P { int x, y; };\nint main() {\n    P a = {1, 2}, b;\n    b = a;\n    b.x = 5;\n    cout << a.x << " " << b.x << " " << b.y;\n    return 0;\n}', ["1 5 2", "5 5 2", "1 5 0", "eroare"], 0, "Atribuirea copiază; modificarea lui b nu afectează a.", main=False),
          ("Cum accesezi câmpul medie printr-un pointer p la o structură?", ["p.medie", "p->medie", "*p.medie", "&amp;p.medie"], 1, "p->medie, echivalent cu (*p).medie."),
          ("Ce operație NU este definită implicit pentru două variabile struct?", ["atribuirea a = b", "accesul a.x", "comparația a == b", "transmiterea ca parametru"], 2, "== trebuie scris (supraîncărcat) de programator.")],
    exercitii=[
        dict(tip="aplicatie", titlu="Clasament cu struct", nivel="mediu", enunt="<p>Citește n concurenți (nume și punctaj). Afișează-i în ordinea descrescătoare a punctajului, iar la egalitate alfabetic, folosind un tablou de structuri și o sortare scrisă de tine.</p>",
             cod_model=H + 'struct Concurent { string nume; int p; };\n\nint main() {\n    Concurent v[100];\n    int n;\n    cin >> n;\n    for (int i = 0; i < n; i++) cin >> v[i].nume >> v[i].p;\n    for (int i = 0; i < n - 1; i++)\n        for (int j = i + 1; j < n; j++)\n            if (v[j].p > v[i].p || (v[j].p == v[i].p && v[j].nume < v[i].nume)) {\n                Concurent aux = v[i]; v[i] = v[j]; v[j] = aux;\n            }\n    for (int i = 0; i < n; i++) cout << i + 1 << ". " << v[i].nume << " " << v[i].p << "\\n";\n    return 0;\n}', intrare="4\nDan 80\nAna 95\nIon 80\nRadu 70",
             criterii=["am definit struct cu câmpurile necesare", "condiția de ordonare tratează și egalitatea", "interschimb structuri întregi (nu doar un câmp)"]),
    ],
))

LECTII.append(dict(
    id="c7", nr="7", scurt="Fișiere text", titlu="Fișiere text în C++",
    programa="Programa 5.B: fișiere text – clase și metode uzuale: deschidere, citire, scriere, închidere",
    obiective=["clasele ifstream și ofstream", "citirea până la sfârșitul fișierului", "scrierea în fișier", "citirea linie cu linie cu getline"],
    teorie=f"""
{C('''#include <fstream>
using namespace std;

int main() {
    ifstream fin("date.in");            // deschidere pentru citire
    ofstream fout("date.out");          // deschidere pentru scriere (golește fișierul)
    int x, suma = 0, cnt = 0;
    while (fin >> x) {                  // citește până când nu mai reușește (sfârșit de fișier)
        suma += x;
        cnt++;
    }
    fout << cnt << " " << suma << "\\n";
    fin.close();
    fout.close();
    return 0;
}''', "c++")}
<ul>
<li><code>ifstream</code> (citire) și <code>ofstream</code> (scriere) se folosesc exact ca <code>cin</code> și <code>cout</code>. Pentru adăugare la final: <code>ofstream f("x.txt", ios::app);</code></li>
<li>Verifică deschiderea: <code>if (!fin) {{ cout &lt;&lt; "nu exista"; return 1; }}</code></li>
<li><code>while (fin &gt;&gt; x)</code> este forma corectă de citire până la final; <code>while (!fin.eof())</code> poate prelucra ultima valoare de două ori.</li>
<li>Linie cu linie: <code>string linie; while (getline(fin, linie)) {{ … }}</code></li>
</ul>
""",
    quiz=[("Ce clasă se folosește pentru scrierea într-un fișier?", ["ifstream", "ofstream", "iostream", "fstreamout"], 1, "o = output."),
          ("Ce face <code>ofstream f(\"a.txt\");</code> dacă fișierul există?", ["adaugă la final", "îl golește", "dă eroare", "îl citește"], 1, "Implicit fișierul este trunchiat; pentru adăugare: ios::app."),
          ("Care este forma recomandată de citire a tuturor numerelor?", ["while (!f.eof())", "while (f >> x)", "for (;;) f >> x;", "do f >> x; while (true);"], 1, "Condiția devine falsă exact când citirea eșuează.")],
    exercitii=[
        dict(tip="aplicatie", titlu="Medii din fișier", nivel="mediu", enunt="<p>Fișierul <code>note.in</code> conține pe prima linie n, apoi n linii cu numele elevului și 3 note. Scrie în <code>medii.out</code> numele și media (2 zecimale) fiecărui elev, iar pe ultima linie numele elevului cu media maximă.</p>",
             cod_model='#include <fstream>\n#include <iostream>\n#include <iomanip>\n#include <string>\nusing namespace std;\n\nint main() {\n    ifstream fin("note.in");\n    ofstream fout("medii.out");\n    int n, a, b, c;\n    string nume, best;\n    double mx = -1;\n    fin >> n;\n    fout << fixed << setprecision(2);\n    for (int i = 0; i < n; i++) {\n        fin >> nume >> a >> b >> c;\n        double m = (a + b + c) / 3.0;\n        fout << nume << " " << m << "\\n";\n        if (m > mx) { mx = m; best = nume; }\n    }\n    fout << best << "\\n";\n    fin.close(); fout.close();\n    return 0;\n}', fisiere={"note.in": "3\nAna 9 10 10\nDan 7 8 6\nIoana 10 9 9\n"},
             criterii=["deschid fișierele cu ifstream/ofstream", "citesc din fin, nu din cin", "media este reală, cu 2 zecimale", "închid fișierele"]),
    ],
))

LECTII.append(dict(
    id="c8", nr="8", scurt="Pointeri și memorie dinamică", titlu="Pointeri și alocarea dinamică a memoriei",
    programa="Programa 5.B: pointeri – declarare, alocare și eliberare dinamică; operatorii & și *, atribuiri, adunarea cu un întreg, scăderea a două adrese",
    obiective=["ce este o adresă și un pointer", "operatorii &amp; (adresă) și * (dereferențiere)", "aritmetica pointerilor pe tablouri", "new / delete și new[] / delete[]"],
    teorie=f"""
{CO(H + '''int main() {
    int x = 10;
    int *p = &x;                 // p memorează adresa lui x
    *p = 25;                     // modificăm x prin p
    cout << x << " " << *p << "\\n";

    int v[] = {10, 20, 30, 40, 50};
    int *a = v;                  // v este adresa primului element
    int *b = &v[3];
    cout << *(a + 2) << " " << b - a << " " << *b + 1 << " " << *(b + 1) << "\\n";
    a++;                         // a indică acum v[1]
    cout << *a << " " << a[1] << "\\n";   // a[1] este *(a + 1)

    int n = 4;
    int *t = new int[n];         // tablou alocat dinamic
    for (int i = 0; i < n; i++) t[i] = i * i;
    cout << t[3] << "\\n";
    delete[] t;                  // eliberarea memoriei
    t = nullptr;                 // evităm folosirea unei adrese eliberate

    int *q = new int(7);         // un singur întreg
    cout << *q << "\\n";
    delete q;
    return 0;
}''', "c++")}
<ul>
<li><code>p + k</code> avansează cu k <em>elemente</em> (nu octeți); diferența a doi pointeri din același tablou = numărul de elemente dintre ei.</li>
<li><code>*p + 1</code> ≠ <code>*(p + 1)</code>: primul adună 1 la valoare, al doilea ia elementul următor.</li>
<li>Fiecare <code>new</code> are perechea <code>delete</code>, fiecare <code>new[]</code> perechea <code>delete[]</code>. Memoria nealocată corect: <em>memory leak</em>; folosirea după <code>delete</code>: comportament nedefinit.</li>
<li>Listele înlănțuite din C++ se construiesc cu structuri care conțin un pointer la următorul nod: <code>struct Nod {{ int info; Nod *urm; }};</code></li>
</ul>
""",
    quiz=[QZ("Ce afișează secvența?", 'int v[] = {2, 4, 6, 8};\nint *p = v + 1;\ncout << *p << " " << *(p + 2) << " " << *p + 2;', ["4 8 6", "4 6 6", "2 6 4", "4 8 8"], 0, "p indică v[1]; *(p+2) este v[3]; *p + 2 = 4 + 2."),
          QZ("Ce afișează secvența?", 'int a = 5, b = 9;\nint *p = &a, *q = &b;\n*p = *q;\nq = p;\n*q = 1;\ncout << a << " " << b;', ["1 9", "9 9", "1 1", "5 1"], 0, "a primește 9, apoi q indică a și a devine 1; b rămâne 9."),
          ("Cum eliberezi memoria alocată cu <code>new int[100]</code>?", ["delete p;", "delete[] p;", "free(p);", "p = nullptr;"], 1, "new[] → delete[]."),
          ("Ce valoare are <code>q - p</code> dacă p = &amp;v[2] și q = &amp;v[7]?", ["5", "20", "adresa v[5]", "7"], 0, "Numărul de elemente dintre ele.")],
    exercitii=[
        dict(tip="aplicatie", titlu="Tablou alocat dinamic", nivel="mediu", enunt="<p>Citește n, alocă dinamic un tablou de n întregi, citește elementele, afișează-le în ordine inversă folosind <strong>doar pointeri</strong> (fără indici), apoi eliberează memoria.</p>",
             cod_model='#include <iostream>\nusing namespace std;\n\nint main() {\n    int n;\n    cin >> n;\n    int *v = new int[n];\n    for (int *p = v; p < v + n; p++) cin >> *p;\n    for (int *p = v + n - 1; p >= v; p--) cout << *p << " ";\n    cout << "\\n";\n    delete[] v;\n    return 0;\n}', intrare="5\n1 2 3 4 5",
             criterii=["aloc cu new int[n]", "parcurg cu pointeri (p++ / p--)", "nu depășesc limitele v ... v + n − 1", "eliberez cu delete[]"]),
    ],
))

LECTII.append(dict(
    id="c9", nr="9", scurt="Clase și obiecte", titlu="Programare orientată pe obiecte: clase, obiecte, constructori, destructori",
    programa="Programa 5.B: clasă, membri (date și metode), obiecte, biblioteci, instanțierea unei clase predefinite, niveluri de acces, constructor, destructor, supraîncărcarea metodelor",
    obiective=["definirea unei clase cu date private și metode publice", "constructori (inclusiv supraîncărcați) și destructor", "ordinea apelurilor constructor/destructor", "supraîncărcarea metodelor; clasele predefinite (string)"],
    teorie=f"""
{CO(H + '''class Cont {
private:                          // accesibil doar din metodele clasei
    string titular;
    double sold;
public:                           // interfața clasei
    Cont() : titular("anonim"), sold(0) { cout << "[C-implicit] "; }
    Cont(string t, double s = 0) : titular(t), sold(s) { cout << "[C-" << t << "] "; }
    ~Cont() { cout << "[D-" << titular << "] "; }

    void depune(double suma) { if (suma > 0) sold += suma; }
    void depune(int bancnote, int valoare) { depune((double)bancnote * valoare); }  // supraîncărcare
    double getSold() const { return sold; }
};

int main() {
    Cont a("Ana", 100);
    a.depune(50.0);
    a.depune(3, 10);
    cout << "\\nsold Ana: " << a.getSold() << "\\n";
    {
        Cont b;                   // constructorul implicit
        cout << "\\n";
    }                             // b este distrus la ieșirea din bloc
    cout << "\\nfinal main\\n";
    return 0;
}                                 // aici este distrus a''', "c++")}
<ul>
<li>Niveluri de acces: <code>private</code> (implicit în <code>class</code>), <code>protected</code> (și în clasele derivate), <code>public</code> (implicit în <code>struct</code>). Datele se țin private, iar accesul se face prin metode (încapsulare).</li>
<li><strong>Constructorul</strong> are numele clasei, fără tip returnat, și se apelează automat la crearea obiectului; poate fi supraîncărcat. <strong>Destructorul</strong> <code>~Clasa()</code> este unic, fără parametri, apelat automat la distrugerea obiectului (ieșirea din bloc, <code>delete</code>).</li>
<li>Obiectele locale se distrug în ordinea inversă creării.</li>
<li>Clase predefinite: <code>string</code>, <code>ifstream</code>, <code>vector</code> – se instanțiază și se folosesc prin metodele lor (<code>s.length()</code>).</li>
</ul>
""",
    quiz=[QZ("Ce afișează programul?", 'class A {\n    int x;\npublic:\n    A(int v) : x(v) { cout << "C" << x << " "; }\n    ~A() { cout << "D" << x << " "; }\n};\nint main() {\n    A a(1);\n    A b(2);\n    return 0;\n}', ["C1 C2 D2 D1", "C1 C2 D1 D2", "C1 D1 C2 D2", "C2 C1 D1 D2"], 0, "Distrugerea se face în ordine inversă construirii.", main=False),
          QZ("Ce afișează programul?", 'class Calc {\npublic:\n    int f(int a) { return a * 2; }\n    int f(int a, int b) { return a + b; }\n    double f(double a) { return a / 2; }\n};\nint main() {\n    Calc c;\n    cout << c.f(3) << " " << c.f(3, 4) << " " << c.f(3.0);\n    return 0;\n}', ["6 7 1.5", "1.5 7 6", "6 7 6", "eroare"], 0, "Se alege varianta după numărul și tipul argumentelor.", main=False),
          ("Membrii declarați fără specificator într-o <code>class</code> sunt:", ["public", "private", "protected", "statici"], 1, "În struct ar fi public."),
          ("Ce afirmație despre destructor este adevărată?", ["poate fi supraîncărcat", "are parametri", "este unic și fără parametri", "returnează int"], 2, "~Clasa(), unul singur.")],
    exercitii=[
        dict(tip="aplicatie", titlu="Clasa Fractie", nivel="dificil", enunt="<p>Scrie clasa <code>Fractie</code> cu numărător și numitor privați, un constructor care simplifică fracția, metoda <code>aduna(Fractie f)</code> care întoarce suma și metoda <code>afiseaza()</code>. Afișează 1/2 + 1/3 și 6/8.</p>",
             cod_model=H + 'class Fractie {\n    int a, b;\n    static int cmmdc(int x, int y) { while (y) { int r = x % y; x = y; y = r; } return x < 0 ? -x : x; }\npublic:\n    Fractie(int x = 0, int y = 1) {\n        int d = cmmdc(x, y);\n        if (y < 0) d = -d;\n        a = x / d; b = y / d;\n    }\n    Fractie aduna(Fractie f) const { return Fractie(a * f.b + f.a * b, b * f.b); }\n    void afiseaza() const { cout << a << "/" << b << "\\n"; }\n};\n\nint main() {\n    Fractie x(1, 2), y(1, 3);\n    x.aduna(y).afiseaza();\n    Fractie(6, 8).afiseaza();\n    return 0;\n}',
             criterii=["datele sunt private", "constructorul simplifică (cmmdc) și normalizează semnul", "aduna întoarce un obiect nou, fără a modifica operanzii", "metodele care nu modifică obiectul sunt const"]),
    ],
))

LECTII.append(dict(
    id="c10", nr="10", scurt="Moștenire și polimorfism", titlu="Clase derivate: moștenire și polimorfism",
    programa="Programa 5.B: clasă derivată",
    obiective=["sintaxa moștenirii publice", "ordinea constructorilor/destructorilor la moștenire", "redefinirea metodelor și funcțiile virtuale", "de ce destructorul bazei trebuie să fie virtual"],
    teorie=f"""
{CO(H + '''class Figura {
protected:
    string nume;
public:
    Figura(string n) : nume(n) { cout << "C-" << nume << " "; }
    virtual double arie() const { return 0; }
    virtual ~Figura() { cout << "D-" << nume << " "; }
};

class Dreptunghi : public Figura {
    double L, l;
public:
    Dreptunghi(double a, double b) : Figura("Dr"), L(a), l(b) { cout << "C-Dreptunghi "; }
    double arie() const override { return L * l; }
    ~Dreptunghi() { cout << "D-Dreptunghi "; }
};

class Cerc : public Figura {
    double r;
public:
    Cerc(double x) : Figura("Cerc"), r(x) {}
    double arie() const override { return 3.14 * r * r; }
};

int main() {
    Figura *f[2] = {new Dreptunghi(2, 3), new Cerc(1)};
    cout << "\\n";
    for (int i = 0; i < 2; i++) cout << f[i]->arie() << " ";   // polimorfism
    cout << "\\n";
    for (int i = 0; i < 2; i++) delete f[i];
    cout << "\\n";
    return 0;
}''', "c++")}
<ul>
<li><code>class D : public B</code> – D moștenește membrii lui B; membrii <code>protected</code> ai lui B sunt accesibili în D, cei <code>private</code> nu.</li>
<li>Construcție: întâi constructorul bazei (apelat în lista de inițializare), apoi al derivatei; distrugere: invers.</li>
<li>Prin <code>virtual</code>, apelul <code>f-&gt;arie()</code> pe un pointer la bază execută metoda clasei reale a obiectului (<strong>polimorfism</strong>). Fără <code>virtual</code> s-ar apela <code>Figura::arie()</code>.</li>
<li>Destructorul bazei trebuie să fie <code>virtual</code> când obiectele derivate se șterg prin pointeri la bază; altfel destructorul derivatei nu se apelează.</li>
</ul>
""",
    quiz=[QZ("Ce afișează programul?", 'class B {\npublic:\n    B() { cout << "B"; }\n    ~B() { cout << "~B"; }\n};\nclass D : public B {\npublic:\n    D() { cout << "D"; }\n    ~D() { cout << "~D"; }\n};\nint main() {\n    D x;\n    return 0;\n}', ["BD~D~B", "DB~B~D", "BD~B~D", "D~D"], 0, "Baza se construiește prima și se distruge ultima.", main=False),
          QZ("Ce afișează programul?", 'class A {\npublic:\n    void f() { cout << "A"; }\n    virtual void g() { cout << "A"; }\n};\nclass B : public A {\npublic:\n    void f() { cout << "B"; }\n    void g() override { cout << "B"; }\n};\nint main() {\n    A *p = new B();\n    p->f();\n    p->g();\n    delete p;\n    return 0;\n}', ["AB", "BB", "AA", "BA"], 0, "f nu este virtuală (se alege după tipul pointerului), g este virtuală (după tipul obiectului).", main=False),
          ("Membrii <code>private</code> ai clasei de bază sunt, în clasa derivată:", ["accesibili direct", "inaccesibili direct", "copiați ca public", "șterși"], 1, "Doar protected și public sunt accesibili în derivată."),
          ("Ce permite cuvântul cheie <code>virtual</code>?", ["moștenirea multiplă", "apelul metodei clasei reale prin pointer la bază", "accesul la membrii privați", "crearea de obiecte fără constructor"], 1, "Legare dinamică (polimorfism).")],
    exercitii=[
        dict(tip="aplicatie", titlu="Angajat și Manager", nivel="dificil", enunt="<p>Clasa <code>Angajat</code> (nume, salariu – protected) are metoda virtuală <code>venit()</code>. Clasa derivată <code>Manager</code> adaugă un bonus și redefinește <code>venit()</code>. Într-un tablou de pointeri la <code>Angajat</code>, memorează un angajat și un manager și afișează venitul total.</p>",
             cod_model=H + 'class Angajat {\nprotected:\n    string nume;\n    double salariu;\npublic:\n    Angajat(string n, double s) : nume(n), salariu(s) {}\n    virtual double venit() const { return salariu; }\n    virtual ~Angajat() {}\n};\n\nclass Manager : public Angajat {\n    double bonus;\npublic:\n    Manager(string n, double s, double b) : Angajat(n, s), bonus(b) {}\n    double venit() const override { return salariu + bonus; }\n};\n\nint main() {\n    Angajat *v[2] = {new Angajat("Ana", 4000), new Manager("Dan", 6000, 1500)};\n    double total = 0;\n    for (int i = 0; i < 2; i++) total += v[i]->venit();\n    cout << total << "\\n";\n    for (int i = 0; i < 2; i++) delete v[i];\n    return 0;\n}',
             criterii=["Manager moștenește public din Angajat", "constructorul derivatei apelează constructorul bazei", "venit() este virtual în bază", "destructorul bazei este virtual; eliberez memoria"]),
    ],
))
