from util import T

LECTII = []
VERIF = '<div class="note warn"><b>Atenție la terminologie:</b> formulările exacte (denumiri de documente, tipuri de curriculum, niveluri de performanță) se verifică în documentele curriculare în vigoare în anul concursului (planuri-cadru, programe școlare, standarde, metodologii publicate de minister).</div>'

LECTII.append(dict(
    id="m1", nr="1", scurt="Curriculumul național", titlu="Curriculumul național: concepte, componente, tipuri",
    programa="Programa E.1: curriculum național – componente, tipuri, produse și documente curriculare, termeni de referință, practici moderne",
    obiective=["ce înseamnă curriculum în sens larg și în sens restrâns", "componentele curriculumului național și ce stabilește fiecare document", "tipurile de curriculum (după decizie, după formă de educație, după realizare)", "unde se încadrează disciplinele informatice"],
    teorie=f"""
<p><strong>Curriculum</strong> în sens larg: ansamblul experiențelor de învățare pe care școala le oferă elevilor (formale și nonformale). În sens restrâns: sistemul documentelor care planifică învățarea – plan-cadru, programe, manuale, ghiduri.</p>
<p>Curriculumul național reprezintă ansamblul coerent al planurilor-cadru și al programelor școlare din învățământul preuniversitar, la care se adaugă standardele naționale de evaluare și produsele curriculare. Cadrul legal actual este Legea învățământului preuniversitar nr. 198/2023.</p>
{T(["Document / produs", "Ce stabilește", "Cine îl folosește și cum"],
   ["<strong>Planul-cadru de învățământ</strong>", "disciplinele, ariile curriculare, numărul de ore pe săptămână pe ani și profiluri, ponderea trunchiului comun și a curriculumului la decizia școlii", "școala – pentru încadrare și orar"],
   ["<strong>Programa școlară</strong>", "nota de prezentare, competențele generale și specifice, activitățile de învățare, conținuturile, sugestiile metodologice (și de evaluare)", "profesorul – documentul de bază pentru proiectare"],
   ["<strong>Standardele naționale de evaluare</strong>", "ce trebuie să știe și să poată face elevul; descriptori de performanță pe niveluri (programa de concurs menționează: De bază, Consolidat, Avansat)", "profesorul și evaluatorii externi"],
   ["<strong>Manualul școlar</strong>", "o variantă de operaționalizare a programei; alternative aprobate prin catalogul manualelor", "elevul și profesorul; nu înlocuiește programa"],
   ["<strong>Auxiliare, ghiduri metodologice, softuri educaționale</strong>", "resurse suplimentare", "profesorul alege în funcție de clasă"])}
<h3>Tipuri de curriculum</h3>
{T(["Criteriu", "Tipuri"],
   ["după cine decide", "<strong>curriculum nucleu / trunchi comun</strong> (obligatoriu, stabilit la nivel național); <strong>curriculum la decizia școlii</strong> – în Legea 198/2023 <strong>CDEOȘ</strong> (curriculum la decizia elevului din oferta școlii); la învățământul profesional și tehnic – <strong>curriculum în dezvoltare locală (CDL)</strong>, elaborat împreună cu operatorii economici"],
   ["după forma educației", "formal (școala), nonformal (activități extracurriculare organizate: cercuri, concursuri), informal (influențe spontane: familie, internet, media)"],
   ["după nivelul de realizare", "scris (documentele), predat (ce face profesorul), învățat (ce achiziționează elevul), evaluat, ascuns/implicit (valori și comportamente transmise indirect)"],
   ["alte concepte", "curriculum de bază, curriculum diferențiat/adaptat (pentru elevi cu nevoi speciale sau capabili de performanță)"])}
<h3>Termeni de referință</h3>
<ul>
<li><strong>Aria curriculară</strong>: grupare de discipline cu obiective și metodologii comune (de ex. Limbă și comunicare, Matematică și științe ale naturii, Om și societate, Arte, Educație fizică și sport, <strong>Tehnologii</strong>, Consiliere și orientare). Disciplinele informatice se regăsesc în aria <em>Tehnologii</em> (verifică încadrarea exactă în planul-cadru al nivelului de învățământ).</li>
<li><strong>Disciplina</strong>: unitate de conținut predată cu un număr de ore din planul-cadru (Informatică și TIC – gimnaziu; Informatică, TIC – liceu).</li>
<li><strong>Practici moderne</strong>: curriculum centrat pe competențe și pe elev, abordări integrate (inter-/transdisciplinare), flexibilitate (CDEOȘ, parcursuri diferențiate), folosirea resurselor digitale.</li>
</ul>
{VERIF}
""",
    exercitii=[
        dict(tip="aplicatie", titlu="Documentul potrivit", enunt="<p>Precizați în ce document curricular găsește un profesor de informatică fiecare informație: a) numărul de ore de Informatică pe săptămână la clasa a X-a, profil real, specializarea matematică-informatică; b) competențele specifice pentru clasa a IX-a; c) nivelul de performanță „Avansat” pentru finalul unui ciclu; d) o succesiune concretă de lecții și exerciții despre algoritmi de sortare.</p>",
             model="<p>a) <strong>planul-cadru</strong>; b) <strong>programa școlară</strong> a disciplinei, clasa a IX-a; c) <strong>standardele naționale de evaluare</strong> (descriptorii de performanță); d) <strong>manualul</strong> sau un auxiliar/ghid – produse curriculare care operaționalizează programa.</p>",
             criterii=["am identificat corect toate cele 4 documente", "am folosit denumirile oficiale (plan-cadru, programă școlară, standarde naționale de evaluare)", "am precizat că manualul operaționalizează programa, nu o înlocuiește"]),
        dict(tip="aplicatie", titlu="Formal, nonformal, informal", enunt="<p>Clasificați situațiile: 1) lecția despre structura repetitivă; 2) cercul de robotică după ore; 3) un elev învață singur Python din clipuri online; 4) participarea la olimpiada de informatică; 5) discuțiile despre jocuri video cu prietenii. Argumentați pentru una dintre ele.</p>",
             model="<p>1) formal; 2) nonformal; 3) informal (învățare spontană, neorganizată instituțional; unii autori o consideră autodidaxie – argumentați); 4) nonformal (activitate organizată, extracurriculară); 5) informal.</p><p><em>Argument (exemplu)</em>: cercul de robotică este nonformal pentru că este organizat intenționat, cu obiective educaționale, de școală, dar în afara programului obligatoriu și fără evaluare pentru catalog.</p>",
             criterii=["clasificările corecte", "argumentul folosește criteriul intenționalității și al cadrului instituțional"]),
    ],
    quiz=[("Ce document stabilește numărul de ore alocat fiecărei discipline?", ["programa școlară", "planul-cadru", "manualul", "standardele de evaluare"], 1, "Planul-cadru."),
          ("În Legea 198/2023, curriculumul la decizia elevului din oferta școlii se numește:", ["CDȘ", "CDEOȘ", "CDL", "trunchi comun"], 1, "CDEOȘ; CDL este specific învățământului profesional și tehnic."),
          ("Manualul școlar este:", ["documentul principal care stabilește competențele", "o variantă de operaționalizare a programei", "obligatoriu identic pentru toate școlile", "parte a planului-cadru"], 1, "Există manuale alternative aprobate."),
          ("Ce tip de curriculum se referă la valorile transmise indirect, prin climatul școlii?", ["scris", "ascuns", "formal", "nucleu"], 1, "Curriculumul ascuns (implicit)."),
          ("Aria curriculară în care se încadrează disciplinele informatice este:", ["Matematică și științe ale naturii", "Tehnologii", "Om și societate", "Arte"], 1, "Tehnologii (verifică planul-cadru al nivelului).")],
))

LECTII.append(dict(
    id="m2", nr="2", scurt="Competențe", titlu="Sistemul de competențe",
    programa="Programa E.1: competențe transversale, competențe-cheie și atribute prioritare, competențe generale, competențe specifice",
    obiective=["definiția competenței", "cele 8 competențe-cheie europene", "relația competență generală – competență specifică – activitate de învățare – conținut", "cum citești și derivi competențele din programă"],
    teorie=f"""
<p><strong>Competența</strong> este un ansamblu structurat de <strong>cunoștințe, abilități (deprinderi) și atitudini</strong> dezvoltate prin învățare, care permit rezolvarea unor probleme în contexte diverse.</p>
<h3>Competențele-cheie (Recomandarea Consiliului UE, 2018)</h3>
<ol><li>competența de alfabetizare;</li><li>competența multilingvistică;</li><li>competența matematică și competența în științe, tehnologie și inginerie;</li><li><strong>competența digitală</strong>;</li><li>competența personală, socială și de a învăța să înveți;</li><li>competența civică;</li><li>competența antreprenorială;</li><li>competența de sensibilizare și exprimare culturală.</li></ol>
<p>Disciplinele informatice contribuie direct la competența digitală și la cea matematică/științe/tehnologie, dar și la „a învăța să înveți”, la cea antreprenorială (proiecte, produse digitale) și la cea civică (etică, siguranță online). Profilul absolventului descrie și <strong>atributele prioritare</strong> urmărite la finalul fiecărui ciclu – se citesc din documentele de politică curriculară în vigoare.</p>
{T(["Nivel", "Caracteristici", "Exemplu (informatică)"],
   ["<strong>Competențe transversale</strong>", "comune mai multor discipline", "colaborare, rezolvarea de probleme, gândire critică, comunicare"],
   ["<strong>Competențe generale</strong>", "definite pe disciplină, pentru un ciclu de școlaritate; formulate amplu", "„Elaborarea algoritmilor de rezolvare a problemelor” (formulare ilustrativă)"],
   ["<strong>Competențe specifice</strong>", "derivate din cele generale, pentru un an de studiu; sunt asociate cu conținuturi și activități de învățare", "„Implementarea algoritmilor de căutare și sortare într-un limbaj de programare” (ilustrativ)"],
   ["<strong>Activități de învățare</strong>", "ce fac efectiv elevii pentru a-și forma competența", "„implementarea căutării binare și testarea pe cazuri limită”"])}
<p>În proiectare se pornește întotdeauna de la <strong>competențele specifice din programă</strong> (copiate exact, cu numerotarea lor), nu de la conținuturi. Conținuturile sunt mijloacele prin care se formează competențele.</p>
<p><strong>Structura unei competențe</strong> (pentru a o „citi” corect): verb de acțiune (ce face elevul) + obiectul acțiunii (conținutul) + contextul / condițiile.</p>
<div class="note warn"><b>Notă:</b> formulările de competențe din această lecție sunt <em>ilustrative</em>. La examen și în proiectare se folosesc formulările exacte din programa școlară a clasei.</div>
""",
    exercitii=[
        dict(tip="aplicatie", titlu="De la competență la activități", enunt="<p>Pentru competența specifică (ilustrativă) „Utilizarea structurilor repetitive în implementarea algoritmilor”, propuneți trei activități de învățare graduale și conținutul asociat.</p>",
             model="<p><strong>Conținut</strong>: structurile repetitive (cu test inițial, cu test final, cu număr cunoscut de pași) în limbajul studiat.</p><ol><li>identificarea, în secvențe de pseudocod date, a numărului de execuții ale corpului buclei (nivel de recunoaștere / înțelegere);</li><li>completarea unor programe lacunare care calculează suma cifrelor și numărul de divizori (aplicare dirijată);</li><li>elaborarea unui program care determină cel mai lung platou dintr-un șir de numere și testarea lui pe cazuri limită (aplicare independentă, analiză).</li></ol>",
             criterii=["activitățile sunt formulate din perspectiva elevului", "sunt graduale (de la recunoaștere la creare)", "sunt legate explicit de conținut", "cel puțin o activitate presupune utilizarea calculatorului"]),
        dict(tip="aplicatie", titlu="Competențe-cheie într-un proiect", enunt="<p>Elevii de clasa a VII-a realizează în echipe o prezentare digitală despre siguranța online pentru colegii mai mici. Identificați trei competențe-cheie dezvoltate și argumentați pentru fiecare.</p>",
             model="<ul><li><strong>digitală</strong> – creează conținut digital (prezentare), folosesc aplicații colaborative, aplică reguli de siguranță online;</li><li><strong>personală, socială și de a învăța să înveți</strong> – lucrează în echipă, își împart sarcinile, își evaluează progresul;</li><li><strong>civică</strong> – promovează comportamente responsabile în spațiul digital pentru comunitatea școlii;</li><li>(acceptabil și: <strong>alfabetizare</strong> – structurarea și redactarea mesajului, adaptat publicului).</li></ul>",
             criterii=["am numit competențe-cheie din lista oficială (2018)", "fiecare argument face legătura cu o acțiune concretă a elevilor"]),
    ],
    quiz=[("O competență este un ansamblu structurat de:", ["obiective și conținuturi", "cunoștințe, abilități și atitudini", "metode și mijloace", "note și calificative"], 1, "Definiția uzuală în documentele curriculare."),
          ("Competențele specifice se formulează:", ["pentru un ciclu", "pentru un an de studiu", "pentru fiecare lecție", "pentru aria curriculară"], 1, "Derivă din cele generale."),
          ("Câte competențe-cheie are cadrul european din 2018?", ["6", "8", "10", "12"], 1, "Opt."),
          ("De la ce se pornește în proiectarea didactică?", ["de la manual", "de la conținuturi", "de la competențele specifice din programă", "de la metodele preferate"], 2, "Conținuturile sunt mijloace pentru formarea competențelor."),
          ("„Colaborarea” este un exemplu de competență:", ["specifică", "transversală", "generală de disciplină", "de evaluare"], 1, "Comună mai multor discipline.")],
))

LECTII.append(dict(
    id="m3", nr="3", scurt="Standarde și niveluri cognitive", titlu="Standarde naționale de evaluare, niveluri de performanță și taxonomia obiectivelor",
    programa="Programa E.1: standarde naționale de evaluare – standarde de învățare, descriptori ai nivelului de performanță (De bază, Consolidat, Avansat)",
    obiective=["rolul standardelor în evaluare", "cum construiești descriptori pe trei niveluri", "taxonomia revizuită a lui Bloom și verbele potrivite fiecărui nivel"],
    teorie=f"""
<p><strong>Standardele de învățare</strong> descriu ce trebuie să știe și să poată face elevul la finalul unei etape de școlaritate. <strong>Descriptorii de performanță</strong> descriu cum arată această performanță pe niveluri; programa de concurs menționează nivelurile <strong>De bază, Consolidat, Avansat</strong>. Ele asigură o evaluare <em>criterială</em> (raportare la standard, nu la ceilalți elevi).</p>
<h3>Cum se scriu descriptorii pe niveluri (exemplu ilustrativ)</h3>
{T(["Nivel", "Descriptor pentru „implementarea unui algoritm de sortare”"],
   ["De bază", "aplică un algoritm de sortare dat pe un exemplu, pas cu pas; implementează metoda cu sprijin (schelet de program)"],
   ["Consolidat", "implementează independent o metodă de sortare, o testează pe cazuri obișnuite și limită"],
   ["Avansat", "alege și justifică metoda potrivită în funcție de date (dimensiune, domeniul valorilor), compară complexitățile, adaptează algoritmul (sortare după mai multe criterii)"])}
<h3>Taxonomia revizuită a lui Bloom (Anderson și Krathwohl)</h3>
{T(["Nivel cognitiv", "Verbe potrivite", "Exemplu la informatică"],
   ["a-și aminti", "a defini, a enumera, a recunoaște", "enumeră structurile fundamentale ale programării structurate"],
   ["a înțelege", "a explica, a exemplifica, a clasifica", "explică diferența dintre while și do-while"],
   ["a aplica", "a calcula, a implementa, a executa", "implementează căutarea binară"],
   ["a analiza", "a compara, a depista erori, a organiza", "identifică eroarea care face programul să intre în buclă infinită"],
   ["a evalua", "a argumenta, a alege, a justifica", "alege și justifică algoritmul potrivit pentru n = 10⁶"],
   ["a crea", "a proiecta, a construi, a elabora", "proiectează o aplicație cu interfață grafică pentru gestiunea notelor"])}
<p>Verbele „a ști”, „a înțelege” (fără precizare), „a cunoaște” nu sunt observabile – se evită în obiectivele operaționale și în itemi.</p>
""",
    exercitii=[
        dict(tip="aplicatie", titlu="Descriptori pe trei niveluri", enunt="<p>Elaborați descriptori de performanță pe nivelurile De bază, Consolidat, Avansat pentru: „utilizarea formulelor și a funcțiilor în calcul tabelar” (TIC).</p>",
             model="<ul><li><strong>De bază</strong>: introduce formule simple cu operatori aritmetici și funcțiile SUM/AVERAGE, cu sprijin; copiază formula prin tragere.</li><li><strong>Consolidat</strong>: folosește independent funcții uzuale (COUNTIF, IF, MAX, ROUND), referințe relative și absolute corecte, explică erorile de tip #DIV/0!.</li><li><strong>Avansat</strong>: combină funcții (IF imbricat, VLOOKUP/XLOOKUP), alege soluția potrivită unei probleme reale (de ex. calculul automat al mediilor și al situației la învățătură), validează datele și verifică rezultatele.</li></ul>",
             criterii=["fiecare nivel conține acțiuni observabile", "nivelurile sunt clar diferențiate prin complexitate și autonomie", "descriptorii sunt specifici conținutului cerut"]),
        dict(tip="aplicatie", titlu="Clasificare Bloom", enunt="<p>Încadrați pe niveluri cognitive: a) „Scrieți definiția grafului conex.” b) „Care dintre algoritmii Prim și Kruskal este mai potrivit pentru un graf cu foarte puține muchii? Argumentați.” c) „Implementați algoritmul BFS.” d) „Găsiți și corectați eroarea din funcția dată.” e) „Proiectați un joc educativ pentru clasa a V-a.”</p>",
             model="<p>a) a-și aminti; b) a evalua; c) a aplica; d) a analiza; e) a crea.</p>",
             criterii=["toate încadrările corecte", "pot justifica fiecare încadrare prin verbul și sarcina cerută"]),
    ],
    quiz=[("Evaluarea care raportează performanța elevului la un standard este:", ["normativă", "criterială", "sumativă", "inițială"], 1, "Criterială."),
          ("Ce nivel cognitiv corespunde sarcinii „Comparați metoda bulelor cu sortarea prin interclasare”?", ["a aplica", "a analiza", "a-și aminti", "a crea"], 1, "Compararea este analiză."),
          ("Care verb NU este potrivit pentru un obiectiv operațional?", ["să implementeze", "să identifice", "să înțeleagă", "să compare"], 2, "Nu este observabil și măsurabil."),
          ("Nivelurile de performanță menționate de programa de concurs sunt:", ["Suficient, Bine, Foarte bine", "De bază, Consolidat, Avansat", "Minim, Mediu, Maxim", "Începător, Intermediar, Expert"], 1, "Conform programei de concurs.")],
))

LECTII.append(dict(
    id="m4", nr="4", scurt="Planificarea și unitatea de învățare", titlu="Proiectarea didactică I: planificarea calendaristică și proiectul unității de învățare",
    programa="Programa E.1: planificare și proiectare didactică – planificare calendaristică, proiectul unității de învățare",
    obiective=["etapele proiectării: de la programă la lecție", "structura planificării calendaristice", "structura proiectului unității de învățare", "cum stabilești o unitate de învățare"],
    teorie=f"""
<h3>Etapele proiectării</h3>
<ol><li><strong>Lectura personalizată a programei</strong> – competențele specifice, conținuturile, sugestiile metodologice, numărul de ore din planul-cadru.</li>
<li><strong>Planificarea calendaristică</strong> (anuală/semestrială) – asocierea competențelor cu conținuturile, gruparea în unități de învățare, alocarea timpului.</li>
<li><strong>Proiectarea secvențială</strong> – proiectul fiecărei unități de învățare (și, opțional, proiecte de lecție).</li></ol>
<p><strong>Unitatea de învățare</strong> este o structură didactică deschisă și flexibilă, unitară tematic, care formează un comportament specific (competențele vizate), se desfășoară pe o perioadă determinată și se încheie cu evaluare.</p>
<h3>Planificarea calendaristică – rubricile uzuale</h3>
{T(["Unitatea de învățare", "Competențe specifice", "Conținuturi", "Nr. ore", "Săptămâna", "Observații"],
   ["Algoritmi elementari", "1.1, 1.2, 2.1 (numerele din programă)", "prelucrarea cifrelor; divizibilitate; algoritmul lui Euclid", "6", "S5–S7", "evaluare la final"])}
<h3>Proiectul unității de învățare – rubricile uzuale</h3>
{T(["Conținuturi (detalieri)", "Competențe specifice", "Activități de învățare", "Resurse", "Evaluare"],
   ["algoritmul lui Euclid (prin împărțiri)", "1.2", "aplicarea pas cu pas pe exemple; implementare; testare", "materiale: laborator, mediu de programare, fișe; forme de organizare: frontal, individual; timp: 2 ore", "observare sistematică; probă practică"])}
<p>Proiectul unității răspunde la întrebările: <em>De ce voi face?</em> (competențe) – <em>Ce voi face?</em> (conținuturi) – <em>Cu ce voi face?</em> (resurse) – <em>Cum voi face?</em> (activități) – <em>Cât s-a realizat?</em> (evaluare).</p>
<p>Formatul exact (rubrici, antet) se stabilește prin ghidurile metodologice și precizările în vigoare; la examen contează coerența: aceleași competențe din planificare apar în proiectul unității, iar fiecare activitate are resurse și evaluare.</p>
""",
    exercitii=[
        dict(tip="aplicatie", titlu="O secvență de planificare", enunt="<p>Pentru clasa a IX-a, realizați un fragment de planificare calendaristică pentru unitatea de învățare „Structuri de date liniare – liste” (6 ore). Folosiți rubricile uzuale; notați competențele specifice cu numere generice (de ex. 2.1) dacă nu aveți programa la îndemână.</p>",
             model="<div class='tbl'><table><tr><th>Unitatea de învățare</th><th>Competențe specifice</th><th>Conținuturi</th><th>Nr. ore</th><th>Săptămâna</th><th>Observații</th></tr><tr><td>Liste</td><td>2.1, 2.2, 3.1</td><td>Lista – memorare, acces la elemente, parcurgere; operații: inserare, ștergere, căutare; metode predefinite; algoritmi pe liste (maxim, numărare, inversare)</td><td>6</td><td>S10–S12</td><td>ultima oră – evaluare practică</td></tr></table></div>",
             criterii=["unitatea are un titlu tematic unitar", "competențele sunt asociate conținuturilor", "timpul este realist și include evaluarea", "conținuturile sunt detaliate"]),
        dict(tip="aplicatie", titlu="Proiectul unei unități de învățare", enunt="<p>Realizați proiectul unității de învățare „Căutare și sortare” (4 ore, liceu), cu toate rubricile, pentru două dintre lecții.</p>",
             model="<div class='tbl'><table><tr><th>Conținuturi</th><th>Comp. spec.</th><th>Activități de învățare</th><th>Resurse</th><th>Evaluare</th></tr><tr><td>Căutarea secvențială și căutarea binară</td><td>2.1</td><td>- aplicarea pas cu pas a căutării binare pe o listă dată (joc „ghicește numărul”)<br>- implementarea ambelor metode<br>- compararea numărului de comparații</td><td>laborator; mediu de programare; fișă de lucru; frontal + individual; 2 ore</td><td>observare sistematică; fișă de evaluare cu 3 itemi</td></tr><tr><td>Sortarea prin selecție și metoda bulelor</td><td>2.2</td><td>- simularea pe cartonașe (activitate „unplugged”, pe grupe)<br>- implementarea și afișarea listei după fiecare pas<br>- analiza numărului de interschimbări</td><td>cartonașe; calculatoare; pe grupe, apoi individual; 2 ore</td><td>probă practică; autoevaluare după grilă</td></tr></table></div>",
             criterii=["toate cele 5 rubrici sunt completate", "activitățile sunt variate (unplugged, implementare, analiză)", "resursele includ materiale, forme de organizare și timp", "evaluarea este precizată pentru fiecare secvență"]),
    ],
    quiz=[("Care este primul pas al proiectării didactice?", ["proiectul de lecție", "lectura personalizată a programei", "alegerea manualului", "testul inițial"], 1, "Se pornește de la programă."),
          ("Unitatea de învățare se încheie obligatoriu cu:", ["temă pentru acasă", "evaluare", "proiect de grup", "test grilă"], 1, "Face parte din definiția ei."),
          ("La ce întrebare răspunde rubrica „Resurse”?", ["De ce voi face?", "Cu ce voi face?", "Cât s-a realizat?", "Ce voi face?"], 1, "Materiale, forme de organizare, timp."),
          ("Ce document asociază unitățile de învățare cu săptămânile anului școlar?", ["proiectul de lecție", "planificarea calendaristică", "programa", "planul-cadru"], 1, "Planificarea calendaristică.")],
))

LECTII.append(dict(
    id="m5", nr="5", scurt="Proiectul de lecție", titlu="Proiectarea didactică II: proiectul de lecție și obiectivele operaționale",
    programa="Programa E.1: proiect de lecție, proiectarea activității de învățare",
    obiective=["structura unui proiect de lecție", "operaționalizarea obiectivelor (comportament, condiții, criteriu)", "un model complet de proiect pentru o lecție de informatică"],
    teorie=f"""
<h3>Structura proiectului de lecție</h3>
<ol><li><strong>Date de identificare</strong>: unitatea de învățământ, clasa, disciplina, profesorul, data, unitatea de învățare, tema (subiectul) lecției, tipul lecției.</li>
<li><strong>Competențe specifice</strong> (din programă) și <strong>obiective operaționale</strong> (derivate).</li>
<li><strong>Strategia didactică</strong>: metode și procedee, mijloace de învățământ, forme de organizare, resurse de timp, bibliografie.</li>
<li><strong>Desfășurarea lecției (scenariul)</strong>: pe etape – timp, activitatea profesorului, activitatea elevilor, metode/mijloace/forme, evaluare.</li></ol>
<h3>Obiectivul operațional</h3>
<p>Se formulează din perspectiva elevului și are trei componente (după R. Mager): <strong>comportamentul observabil</strong> (verb de acțiune), <strong>condițiile</strong> de realizare și <strong>criteriul de reușită</strong> (nivelul minim acceptabil).</p>
<p>Exemplu: „La finalul lecției, elevii vor fi capabili <em>să implementeze</em> căutarea binară într-o listă sortată (comportament), <em>folosind mediul de programare și fișa de lucru</em> (condiții), <em>astfel încât programul să treacă cel puțin 4 din cele 5 teste date</em> (criteriu).”</p>
<p>Un proiect are de regulă 3–5 obiective operaționale; fiecare obiectiv trebuie urmărit în scenariu și verificat în evaluare.</p>
""",
    exercitii=[
        dict(tip="aplicatie", titlu="Operaționalizați", enunt="<p>Transformați în obiective operaționale corecte: a) „Elevii să cunoască instrucțiunea for.” b) „Profesorul va explica referințele absolute.” c) „Elevii să înțeleagă importanța parolelor puternice.”</p>",
             model="<ul><li>a) „Elevii vor fi capabili să scrie o secvență cu instrucțiunea for care afișează numerele pare dintr-un interval citit, rezolvând corect cel puțin 2 din 3 cerințe ale fișei.”</li><li>b) „Elevii vor fi capabili să folosească referințe absolute pentru a copia corect o formulă de calcul al prețului cu TVA, pe un tabel dat, fără erori de calcul.”</li><li>c) „Elevii vor fi capabili să evalueze 5 parole date și să justifice pentru cel puțin 4 dacă sunt puternice, pe baza a cel puțin două criterii (lungime, varietatea caracterelor).”</li></ul>",
             criterii=["fiecare obiectiv este formulat din perspectiva elevului", "verbul este observabil și măsurabil", "apar condițiile", "apare criteriul de reușită"]),
        dict(tip="aplicatie", titlu="Proiect de lecție complet", enunt="<p>Elaborați proiectul unei lecții mixte de 50 de minute cu tema „Funcții definite de utilizator” (Python, liceu): date de identificare, 3 obiective operaționale, strategie didactică și scenariul pe etape.</p>",
             model="<p><strong>Date</strong>: Clasa a X-a, Informatică; unitatea de învățare: Subprograme; tema: Funcții definite de utilizator; tipul lecției: mixtă.</p><p><strong>Competență specifică</strong>: (din programă) – de exemplu, utilizarea subprogramelor în rezolvarea problemelor.</p><p><strong>Obiective operaționale</strong> – elevii vor fi capabili: O1 să identifice antetul, parametrii și valoarea returnată într-o funcție dată (3 din 3 elemente); O2 să definească o funcție care calculează suma cifrelor și să o apeleze pentru valori citite (testată pe 3 cazuri); O3 să refactorizeze un program dat, înlocuind codul repetat cu un apel de funcție.</p><p><strong>Strategie</strong>: inductiv-deductivă; metode – conversația euristică, demonstrația, exercițiul, problematizarea, învățarea asistată de calculator; mijloace – calculatoare, videoproiector, fișă de lucru; forme – frontal, individual, în perechi.</p><div class='tbl'><table><tr><th>Etapa (timp)</th><th>Profesor</th><th>Elevi</th><th>Metode / forme</th><th>Evaluare</th></tr><tr><td>Moment organizatoric (2')</td><td>verifică prezența, pornirea calculatoarelor</td><td>se pregătesc</td><td>frontal</td><td>–</td></tr><tr><td>Captarea atenției (3')</td><td>arată un program cu aceeași secvență copiată de 3 ori: „Ce ar trebui modificat dacă găsim o greșeală?”</td><td>observă problema duplicării</td><td>problematizare</td><td>–</td></tr><tr><td>Reactualizare (5')</td><td>întrebări despre funcțiile predefinite folosite (len, max, round)</td><td>răspund, dau exemple</td><td>conversație</td><td>orală</td></tr><tr><td>Anunțarea temei și a obiectivelor (2')</td><td>prezintă tema și obiectivele pe înțelesul elevilor</td><td>notează</td><td>expunere</td><td>–</td></tr><tr><td>Dirijarea învățării (13')</td><td>construiește împreună cu elevii funcția suma_cifre: def, parametri, return, apel; explică variabilele locale</td><td>urmăresc, răspund, execută pas cu pas (O1)</td><td>demonstrație, conversație euristică; frontal</td><td>observare</td></tr><tr><td>Obținerea performanței (15')</td><td>monitorizează, oferă sprijin diferențiat</td><td>rezolvă fișa: O2 (individual), O3 (în perechi)</td><td>exercițiu, IAC</td><td>evaluare formativă</td></tr><tr><td>Feedback și evaluare (7')</td><td>discută erorile frecvente (print în loc de return), apreciază</td><td>răspund la un test rapid de 3 itemi</td><td>conversație, test</td><td>test formativ</td></tr><tr><td>Retenție și transfer (3')</td><td>tema: funcție prim(n) folosită pentru a afișa numerele prime dintr-un interval</td><td>notează tema</td><td>explicație</td><td>–</td></tr></table></div>",
             criterii=["datele de identificare și tipul lecției sunt precizate", "obiectivele sunt operaționale (comportament, condiții, criteriu)", "strategia este coerentă cu obiectivele", "scenariul respectă momentele lecției mixte și timpul total", "fiecare obiectiv este urmărit în scenariu și în evaluare"]),
    ],
    quiz=[("Care sunt componentele unui obiectiv operațional (Mager)?", ["conținut, metodă, mijloc", "comportament observabil, condiții, criteriu de reușită", "timp, loc, formă", "competență, activitate, evaluare"], 1, "Comportament – condiții – criteriu."),
          ("Obiectivele operaționale se formulează din perspectiva:", ["profesorului", "elevului", "inspectorului", "manualului"], 1, "Ce va fi capabil elevul să facă."),
          ("Ce element NU face parte din strategia didactică într-un proiect de lecție?", ["metodele", "mijloacele", "formele de organizare", "numele directorului"], 3, "Strategia = metode, mijloace, forme de organizare, resurse."),
          ("Câte obiective operaționale are, de obicei, o lecție?", ["unul singur", "3–5", "10–15", "câte competențe are programa"], 1, "Un număr realist, verificabil în timpul lecției.")],
))

LECTII.append(dict(
    id="m6", nr="6", scurt="Lecția: tipuri și momente", titlu="Lecția: tipuri de lecții, momentele lecției, activități de învățare",
    programa="Programa E.2: lecția, unitate didactică fundamentală – tipuri de lecții, momente ale lecției, activități de învățare",
    obiective=["tipurile de lecții și variantele lor", "cele 9 momente ale lecției mixte și rolul fiecăruia", "specificul lecției de laborator la informatică"],
    teorie=f"""
{T(["Tip de lecție", "Scop dominant", "Exemplu la informatică"],
   ["de comunicare / însușire de noi cunoștințe", "transmiterea și înțelegerea noilor conținuturi", "introducerea noțiunii de graf"],
   ["de formare de priceperi și deprinderi", "exersarea, aplicarea (frecventă la laborator)", "implementarea algoritmilor pe tablouri"],
   ["de fixare și sistematizare (recapitulare)", "consolidarea, structurarea cunoștințelor", "recapitulare înainte de lucrarea semestrială"],
   ["de verificare și apreciere", "evaluarea", "lucrare practică la calculator"],
   ["<strong>mixtă (combinată)</strong>", "îmbină toate scopurile; cea mai frecventă", "aproape orice lecție nouă"])}
<h3>Momentele (evenimentele) lecției mixte</h3>
{T(["Moment", "Ce se urmărește"],
   ["1. Moment organizatoric", "condiții de lucru: prezență, materiale, calculatoare pornite"],
   ["2. Captarea atenției", "motivarea elevilor: o situație-problemă, o întrebare, un joc"],
   ["3. Reactualizarea cunoștințelor anterioare (verificarea temei)", "„ancorele” necesare noii învățări"],
   ["4. Anunțarea temei și a obiectivelor", "elevii știu ce vor învăța și de ce"],
   ["5. Prezentarea conținutului și dirijarea învățării", "noile cunoștințe, prin metode active"],
   ["6. Obținerea performanței", "elevii aplică independent ce au învățat"],
   ["7. Asigurarea feedback-ului", "corectarea erorilor, întărirea răspunsurilor corecte"],
   ["8. Evaluarea performanței", "verificarea atingerii obiectivelor"],
   ["9. Asigurarea retenției și a transferului", "tema, aplicații în contexte noi"])}
<p>Succesiunea corespunde evenimentelor instruirii descrise de R. Gagné. Etapele nu sunt rigide: în funcție de tipul lecției, unele se comprimă sau se repetă.</p>
<h3>Lecția de laborator la informatică</h3>
<ul><li>Raportul optim: un elev la un calculator; reguli de siguranță și de utilizare a laboratorului anunțate la începutul anului.</li><li>Alternanța: scurtă demonstrație frontală → lucru individual/în perechi → discuție a erorilor.</li><li>Sarcini diferențiate (de bază + suplimentare) pentru ritmuri diferite; fișe de lucru cu teste de verificare a programelor.</li><li>Salvarea și organizarea fișierelor elevilor (portofoliu digital).</li></ul>
""",
    exercitii=[
        dict(tip="aplicatie", titlu="Captarea atenției", enunt="<p>Propuneți câte o modalitate de captare a atenției pentru lecțiile: a) „Căutarea binară”; b) „Securitatea parolelor”; c) „Grafuri – noțiuni introductive”.</p>",
             model="<ul><li>a) jocul „Ghicește numărul dintre 1 și 1000 în cel mult 10 întrebări de tip mai mare/mai mic”;</li><li>b) un test de 30 de secunde: cât timp ar dura spargerea parolelor „123456”, „ana2010” și „Ceai!Verde_în-ploaie” (folosind un estimator online sau un tabel pregătit);</li><li>c) o hartă cu orașe și drumuri: „Care este cel mai scurt traseu?” / problema podurilor din Königsberg.</li></ul>",
             criterii=["fiecare propunere este legată de tema lecției", "implică activ elevii (întrebare, joc, problemă)", "este realizabilă în 2–4 minute"]),
        dict(tip="aplicatie", titlu="Identificați etapa", enunt="<p>În ce moment al lecției apar următoarele activități? a) Elevii rezolvă singuri fișa cu 3 probleme. b) „Ce am învățat ora trecută despre liste?” c) Profesorul anunță: „Azi vom învăța să sortăm o listă și să comparăm două metode.” d) Tema: „Modificați programul ca să sorteze descrescător.”</p>",
             model="<p>a) obținerea performanței; b) reactualizarea cunoștințelor; c) anunțarea temei și a obiectivelor; d) asigurarea retenției și a transferului.</p>",
             criterii=["toate cele patru etape identificate corect"]),
    ],
    quiz=[("Care este cel mai frecvent tip de lecție?", ["de verificare", "mixtă", "de recapitulare", "de comunicare"], 1, "Lecția mixtă."),
          ("Momentul în care elevii aplică independent noile cunoștințe este:", ["dirijarea învățării", "obținerea performanței", "captarea atenției", "reactualizarea"], 1, "Obținerea performanței."),
          ("Tema pentru acasă aparține momentului:", ["evaluarea performanței", "asigurarea retenției și a transferului", "feedback", "moment organizatoric"], 1, "Retenție și transfer."),
          ("Succesiunea momentelor lecției mixte este inspirată de:", ["taxonomia lui Bloom", "evenimentele instruirii (Gagné)", "teoria inteligențelor multiple", "metoda mozaicului"], 1, "R. Gagné.")],
))

LECTII.append(dict(
    id="m7", nr="7", scurt="Strategii și metode didactice", titlu="Strategii didactice și metode de învățământ",
    programa="Programa E.2: tipuri de strategii didactice; metode didactice: observarea, exercițiul, modelarea, problematizarea, demonstrarea, învățarea prin descoperire, expunerea, conversația, aplicațiile practice, instruirea programată, învățarea asistată de calculator",
    obiective=["definiția și clasificarea strategiilor didactice", "metodele din programă și aplicarea lor la informatică", "diferența dintre metodă și procedeu"],
    teorie=f"""
<p><strong>Strategia didactică</strong> este modul de combinare a metodelor, procedeelor, mijloacelor și formelor de organizare pentru atingerea obiectivelor. <strong>Metoda</strong> este calea de organizare a învățării; <strong>procedeul</strong> este o componentă/operație a metodei (un procedeu poate deveni metodă în alt context).</p>
{T(["Criteriu", "Tipuri de strategii"],
   ["logica gândirii", "<strong>inductive</strong> (de la exemple la regulă), <strong>deductive</strong> (de la regulă la exemple), <strong>analogice</strong> (prin modele), <strong>transductive</strong> (explicații prin metafore), <strong>mixte</strong>"],
   ["gradul de dirijare", "<strong>algoritmice</strong> (pași prestabiliți, dirijare strictă), <strong>euristice</strong> (descoperire, problematizare), <strong>mixte</strong>"],
   ["forma de organizare", "frontale, individuale, pe grupe, combinate"])}
{T(["Metodă", "Esența", "La informatică"],
   ["Expunerea sistematică", "prezentarea organizată a cunoștințelor (prelegere, explicație, povestire)", "scurtă, pentru noțiuni noi (modelul relațional), susținută vizual"],
   ["Conversația", "dialog: catehetică (de verificare), <strong>euristică</strong> (de descoperire), de consolidare", "„Ce se întâmplă dacă lista este sortată? Putem căuta mai repede?”"],
   ["Demonstrația", "prezentarea unui obiect, fenomen sau acțiuni-model", "rularea pas cu pas a unui program cu urmărirea variabilelor"],
   ["Observarea", "examinarea dirijată a unui fenomen", "observarea comportamentului unui program pentru date diferite"],
   ["Modelarea", "lucrul cu modele simplificate ale realității", "scheme logice, diagrame E-R, simularea unui robot virtual"],
   ["Problematizarea", "crearea unor situații-problemă (contradicție între ce știu și ce trebuie)", "„Programul merge pentru 5, dar nu pentru 0 – de ce?”"],
   ["Învățarea prin descoperire", "elevul găsește singur regula (dirijat sau independent)", "efectul referințelor absolute descoperit experimentând"],
   ["Exercițiul", "repetarea conștientă pentru formarea deprinderilor", "probleme graduale pe același algoritm"],
   ["Aplicațiile practice / lucrările de laborator", "realizarea unor produse", "proiecte, programe, documente, site-uri"],
   ["Instruirea programată", "conținut în pași mici, cu răspuns activ și feedback imediat (Skinner: liniară; Crowder: ramificată)", "tutoriale interactive, platforme cu evaluator automat"],
   ["Învățarea asistată de calculator (IAC)", "calculatorul ca mijloc de predare, exersare, simulare, evaluare", "softuri educaționale, simulări, teste online"])}
""",
    exercitii=[
        dict(tip="aplicatie", titlu="Strategie inductivă vs. deductivă", enunt="<p>Descrieți predarea temei „Structura alternativă if–elif–else” printr-o strategie inductivă și printr-una deductivă.</p>",
             model="<p><strong>Inductivă</strong>: elevii primesc 4 programe care atribuie calificative după punctaj, unele cu if-uri succesive, unele cu elif; rulează programele pentru aceleași date, observă că variantele cu if-uri independente afișează mai multe calificative, analizează diferența și formulează regula: într-un lanț if–elif–else se execută cel mult o ramură, prima adevărată; apoi o aplică.</p><p><strong>Deductivă</strong>: profesorul prezintă sintaxa și regula de execuție, o ilustrează pe un exemplu, apoi elevii rezolvă exerciții graduale de aplicare.</p>",
             criterii=["la inductivă se pornește de la exemple/experiment și se ajunge la regulă", "la deductivă regula este dată la început", "ambele descrieri sunt concrete pentru tema cerută"]),
        dict(tip="aplicatie", titlu="Conversația euristică", enunt="<p>Scrieți un set de 5 întrebări de conversație euristică prin care elevii descoperă algoritmul de determinare a maximului dintr-o listă.</p>",
             model="<ol><li>Dacă vă dau numerele unul câte unul, pe cartonașe, cum ați afla care este cel mai mare fără să le vedeți pe toate deodată?</li><li>Ce trebuie să țineți minte după fiecare cartonaș?</li><li>Cu ce valoare ar trebui să începeți? De ce nu cu 0?</li><li>Ce faceți când apare un număr mai mare decât cel reținut?</li><li>Cum ați scrie asta ca pași pentru calculator?</li></ol>",
             criterii=["întrebările conduc pas cu pas spre algoritm", "nu oferă direct răspunsul", "includ cazul-capcană (inițializarea)"]),
    ],
    quiz=[("O strategie care merge de la exemple concrete la o regulă generală este:", ["deductivă", "inductivă", "algoritmică", "analogică"], 1, "Inductivă."),
          ("Conversația prin care elevii sunt conduși să descopere noi cunoștințe este:", ["catehetică", "euristică", "de verificare", "expozitivă"], 1, "Euristică."),
          ("Instruirea programată se bazează pe:", ["prelegeri lungi", "pași mici, răspuns activ și feedback imediat", "lucrul pe grupe mari", "memorare"], 1, "Principiile lui Skinner/Crowder."),
          ("Rularea pas cu pas a unui program în fața clasei este un exemplu de:", ["demonstrație", "problematizare", "exercițiu", "instruire programată"], 0, "Demonstrație."),
          ("Situația „programul funcționează pentru 5, dar nu pentru 0” ilustrează:", ["problematizarea", "expunerea", "observarea", "exercițiul"], 0, "Creează o situație-problemă.")],
))
