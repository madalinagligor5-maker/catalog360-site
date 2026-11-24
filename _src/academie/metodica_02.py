from util import T

LECTII = []

LECTII.append(dict(
    id="m8", nr="8", scurt="Metode activ-participative", titlu="Metode activ-participative și forme de organizare",
    programa="Programa E.2: metode didactice activ-participative centrate pe elev; forme de organizare a activității: frontală, individuală, pe grupe",
    obiective=["metodele interactive folosite frecvent la informatică", "pașii de aplicare ai fiecăreia", "avantajele și limitele formelor de organizare", "diferențierea instruirii"],
    teorie=f"""
{T(["Metodă", "Cum se aplică", "Exemplu la informatică / TIC"],
   ["<strong>Brainstorming</strong>", "generarea liberă de idei, fără critică, apoi selecția", "„Ce date ar trebui să rețină aplicația bibliotecii?”"],
   ["<strong>Mozaicul (jigsaw)</strong>", "grupe de bază → grupe de „experți” pe subteme → revenire și predare reciprocă → evaluare", "categoriile de comenzi SQL (DDL, DML, DCL, TCL)"],
   ["<strong>Ciorchinele</strong>", "conceptul central și asocierile lui, într-o schemă", "„Rețele de calculatoare”: tipuri, topologii, dispozitive, protocoale"],
   ["<strong>Știu – Vreau să știu – Am învățat</strong>", "tabel în trei coloane, completat la început și la sfârșit", "lecția despre inteligența artificială"],
   ["<strong>Cubul</strong>", "tema abordată din 6 perspective: descrie, compară, asociază, analizează, aplică, argumentează", "„Stiva”"],
   ["<strong>Gândiți – lucrați în perechi – comunicați</strong> (think-pair-share)", "reflecție individuală, discuție în perechi, prezentare", "„De ce nu funcționează Dijkstra cu costuri negative?”"],
   ["<strong>Turul galeriei</strong>", "grupele expun produsele; celelalte le analizează și lasă feedback", "afișe/prezentări despre securitate online"],
   ["<strong>Învățarea bazată pe proiect</strong>", "un produs realizat într-un interval mai lung, cu etape și evaluare", "o aplicație cu interfață grafică, un site al clasei"],
   ["<strong>Programarea în perechi</strong> (pair programming)", "„pilotul” scrie, „navigatorul” verifică; rolurile se schimbă", "orice lecție de laborator"],
   ["<strong>Clasa inversată</strong> (flipped classroom)", "teoria acasă (video, text), aplicațiile la clasă", "funcții predefinite în calcul tabelar"],
   ["<strong>Activități „unplugged”</strong>", "concepte de informatică fără calculator (cartonașe, jocuri)", "sortarea cu cartonașe, rețele de sortare, numere binare"])}
<h3>Forme de organizare</h3>
{T(["Formă", "Avantaje", "Limite"],
   ["frontală", "eficientă pentru explicații comune, ritm unitar", "elevii au ritmuri diferite; participare inegală"],
   ["individuală", "ritm propriu, sarcini diferențiate, responsabilitate", "lipsa interacțiunii; cere monitorizare atentă"],
   ["pe grupe / în perechi", "cooperare, învățare reciprocă, competențe sociale", "timp mai mare, risc de implicare inegală – roluri clare"])}
<p><strong>Diferențierea</strong>: sarcini pe niveluri (de bază/suplimentare), timp diferit, sprijin diferit (fișe cu indicii, schelet de program), produse diferite. Pentru elevii capabili de performanță – probleme de olimpiadă, proiecte extinse; pentru elevii cu dificultăți – pași mai mici, exemple rezolvate, feedback frecvent.</p>
""",
    exercitii=[
        dict(tip="aplicatie", titlu="Mozaicul la baze de date", enunt="<p>Descrieți aplicarea metodei mozaicului la tema „Comenzi SQL” (clasa a XII-a), cu etape, sarcini și evaluare; precizați două avantaje și două limite.</p>",
             model="<ol><li>Clasa se împarte în grupe de 4 (grupe de bază); fiecare elev primește un număr 1–4: 1 – DDL, 2 – DML, 3 – DCL, 4 – TCL.</li><li>Grupele de experți (toți „1”, toți „2” …) studiază fișa de expert: sintaxă, exemple, un exercițiu pe baza de date a clasei; pregătesc o explicație de 3 minute.</li><li>Revenirea în grupele de bază: fiecare expert își predă partea și rezolvă împreună cu colegii un exercițiu.</li><li>Evaluare: un test individual (sau un script care folosește toate cele 4 categorii); reflecție.</li></ol><p><strong>Avantaje</strong>: responsabilitate individuală, învățare prin predare, cooperare. <strong>Limite</strong>: consumă timp, depinde de calitatea fișelor și a explicațiilor experților – profesorul monitorizează grupele.</p>",
             criterii=["etapele sunt în ordinea corectă (bază → experți → bază → evaluare)", "sarcinile sunt concrete pentru SQL", "există evaluare individuală", "avantaje și limite pertinente"]),
        dict(tip="aplicatie", titlu="Diferențiere", enunt="<p>Pentru o lecție despre prelucrarea cifrelor unui număr, propuneți câte o sarcină pentru nivelul de bază, mediu și avansat.</p>",
             model="<ul><li><strong>Bază</strong>: completați programul dat (cu spații libere) care afișează suma cifrelor unui număr.</li><li><strong>Mediu</strong>: scrieți un program care afișează cifra maximă și de câte ori apare.</li><li><strong>Avansat</strong>: construiți cel mai mare număr care se poate forma cu cifrele unui număr dat și justificați complexitatea soluției.</li></ul>",
             criterii=["sarcinile vizează același conținut", "dificultatea crește clar", "fiecare sarcină poate fi verificată"]),
    ],
    quiz=[("La metoda mozaicului, elevii care studiază aceeași subtemă formează:", ["grupa de bază", "grupa de experți", "grupa de control", "galeria"], 1, "Grupele de experți."),
          ("Ce metodă folosește un tabel în trei coloane: Știu / Vreau să știu / Am învățat?", ["cubul", "ȘVA (KWL)", "ciorchinele", "brainstorming"], 1, "Știu – Vreau să știu – Am învățat."),
          ("La brainstorming, în faza de generare a ideilor:", ["ideile se critică imediat", "nu se critică ideile", "vorbește doar profesorul", "se dau note"], 1, "Critica este amânată."),
          ("„Clasa inversată” înseamnă:", ["elevii predau profesorului", "teoria se studiază acasă, aplicațiile la clasă", "lecția se ține în laborator", "evaluarea se face la început"], 1, "Flipped classroom.")],
))

LECTII.append(dict(
    id="m9", nr="9", scurt="Mijloace și resurse digitale", titlu="Mijloacele de învățământ, software educațional, e-learning și Internetul",
    programa="Programa E.2: mijloacele de învățământ – funcții, tipuri, integrare (clasa și laboratorul, manualul, produsele software, auxiliarele); software educațional; platforme de e-learning; Internetul ca resursă",
    obiective=["funcțiile și clasificarea mijloacelor de învățământ", "tipurile de software educațional", "criterii de alegere a resurselor digitale", "utilizarea responsabilă a platformelor și a Internetului"],
    teorie=f"""
<p><strong>Mijloacele de învățământ</strong> sunt instrumentele materiale și tehnice care sprijină predarea, învățarea și evaluarea.</p>
{T(["Funcție", "Explicație"],
   ["informativ-demonstrativă", "transmit informații, ilustrează"],
   ["formativ-educativă", "dezvoltă operații de gândire, deprinderi"],
   ["de motivare", "stârnesc interesul"],
   ["de evaluare", "permit verificarea (teste online, evaluatoare automate)"],
   ["substitutivă", "înlocuiesc experiența directă greu accesibilă (simulări, laboratoare virtuale)"],
   ["ergonomică / de raționalizare", "economisesc timp și efort"])}
<p><strong>Clasificare</strong>: tradiționale (tabla, fișe, manual, planșe) și moderne (calculatorul, videoproiectorul, tabla interactivă, roboți educaționali, kituri IoT); materiale vs. digitale.</p>
{T(["Tip de software educațional", "Rol", "Exemple"],
   ["tutorial", "predă un conținut nou, pas cu pas", "cursuri interactive"],
   ["de exersare (drill and practice)", "consolidare prin exerciții cu feedback", "platforme de probleme cu evaluator automat"],
   ["de simulare", "modelează fenomene, procese", "simulatoare de rețea, roboți virtuali (Open Roberta), vizualizări de algoritmi"],
   ["joc educațional", "învățare prin joc", "jocuri de programare cu blocuri"],
   ["de testare/evaluare", "teste, chestionare", "formulare online, quiz-uri"],
   ["medii de dezvoltare", "instrumente de lucru", "Scratch, Blockly, Thonny, Code::Blocks, VS Code, App Inventor"])}
<h3>Criterii de alegere</h3>
<ul><li>adecvarea la competențele vizate și la vârsta elevilor;</li><li>corectitudinea științifică și calitatea interfeței (în limba română, dacă se poate);</li><li>accesibilitatea (gratuit, rulează pe echipamentele școlii, funcționează și pe telefon);</li><li>protecția datelor personale (conturi, vârsta minimă, GDPR) și siguranța online;</li><li>posibilitatea de a urmări progresul elevilor.</li></ul>
<p><strong>Platforme de e-learning</strong> (Google Classroom, Microsoft Teams, Moodle): distribuirea resurselor, teme, teste, feedback, comunicare, portofoliu digital. <strong>Internetul</strong> ca resursă: resurse educaționale deschise, documentare, colaborare – cu educație pentru evaluarea critică a surselor și respectarea drepturilor de autor.</p>
""",
    exercitii=[
        dict(tip="aplicatie", titlu="Alegerea mijloacelor", enunt="<p>Pentru clasa a V-a, tema „Structura repetitivă”, propuneți trei mijloace de învățământ și precizați funcția didactică principală a fiecăruia.</p>",
             model="<ul><li>mediu de programare cu blocuri (de ex. Scratch) – <strong>formativ-educativă și de motivare</strong>: efectul repetiției se vede imediat în mișcarea personajului;</li><li>fișă cu un traseu pe grilă (activitate „unplugged”) – <strong>demonstrativă</strong>: elevii simulează repetarea pașilor fără calculator;</li><li>test interactiv pe platforma clasei – <strong>de evaluare</strong>: feedback imediat pentru elev și profesor.</li></ul>",
             criterii=["mijloacele sunt potrivite vârstei", "funcțiile didactice sunt numite corect", "fiecare alegere este justificată"]),
        dict(tip="aplicatie", titlu="Evaluarea unei resurse digitale", enunt="<p>Construiți o grilă cu 5 criterii prin care evaluați o aplicație online de exersare a programării înainte de a o folosi la clasă.</p>",
             model="<div class='tbl'><table><tr><th>Criteriu</th><th>Întrebare de verificare</th></tr><tr><td>Relevanță curriculară</td><td>Exercițiile corespund competențelor și conținuturilor din programă?</td></tr><tr><td>Corectitudine</td><td>Enunțurile și soluțiile sunt corecte, terminologia adecvată?</td></tr><tr><td>Accesibilitate</td><td>Este gratuită, în limba română, funcționează pe echipamentele școlii?</td></tr><tr><td>Siguranță și date personale</td><td>Ce date cere, ce vârstă minimă are, respectă GDPR?</td></tr><tr><td>Feedback și monitorizare</td><td>Oferă feedback elevului și rapoarte profesorului?</td></tr></table></div>",
             criterii=["criteriile sunt distincte și verificabile", "include protecția datelor", "include relevanța față de programă"]),
    ],
    quiz=[("Funcția prin care o simulare înlocuiește o experiență greu accesibilă este:", ["substitutivă", "ergonomică", "estetică", "de evaluare"], 0, "Funcția substitutivă."),
          ("Un program care oferă exerciții repetate cu feedback imediat este un software de tip:", ["tutorial", "simulare", "exersare (drill and practice)", "joc"], 2, "Exersare."),
          ("Care criteriu este obligatoriu când elevii își creează conturi pe o platformă?", ["culoarea interfeței", "protecția datelor personale și vârsta minimă", "numărul de reclame", "popularitatea"], 1, "GDPR și termenii de utilizare."),
          ("Open Roberta Lab este folosit la informatică mai ales ca:", ["procesor de text", "mediu de simulare și programare a roboților", "sistem de operare", "bază de date"], 1, "Robot virtual și programare vizuală.")],
))

LECTII.append(dict(
    id="m10", nr="10", scurt="Evaluarea: funcții, tipuri, metode", titlu="Evaluarea: funcții, tipuri, metode tradiționale și complementare",
    programa="Programa E.3: evaluarea – obiective, caracterizare, funcții, tipologie; metode și instrumente tradiționale și moderne; calitățile instrumentelor de evaluare",
    obiective=["definiția și funcțiile evaluării", "tipurile de evaluare după moment, raportare și evaluator", "metodele tradiționale și cele complementare", "calitățile unui instrument de evaluare"],
    teorie=f"""
<p><strong>Evaluarea</strong> este procesul prin care se obțin informații despre învățare (măsurare), se interpretează (apreciere) și se iau decizii (ameliorare, notare, orientare).</p>
{T(["Funcție", "Exemplu"],
   ["diagnostică", "testul inițial arată ce elevi nu stăpânesc structurile repetitive"],
   ["prognostică", "rezultatele anticipează reușita la clasa de informatică intensivă"],
   ["de selecție / ierarhizare", "concursuri, olimpiade, admitere"],
   ["de certificare", "examene: bacalaureat, atestat"],
   ["motivațională", "feedbackul pozitiv crește implicarea"],
   ["de orientare școlară și profesională", "recomandarea unui profil sau a unei cariere"],
   ["de reglare (feedback)", "profesorul își ajustează predarea"])}
{T(["Criteriu", "Tipuri"],
   ["momentul", "<strong>inițială</strong> (la început – diagnostică/predictivă); <strong>continuă / formativă</strong> (pe parcurs, pentru reglare); <strong>sumativă / cumulativă</strong> (la final de unitate, semestru)"],
   ["raportarea", "<strong>criterială</strong> (față de standarde/obiective); <strong>normativă</strong> (față de rezultatele grupului)"],
   ["evaluatorul", "internă (profesorul clasei) / externă (examene naționale); autoevaluare; evaluare reciprocă (între colegi)"])}
<h3>Metode de evaluare</h3>
<ul>
<li><strong>Tradiționale</strong>: probe orale, probe scrise, <strong>probe practice</strong> (la informatică – rezolvarea unei probleme la calculator, realizarea unui produs digital).</li>
<li><strong>Complementare (alternative)</strong>: <strong>observarea sistematică</strong> (fișă de observare, listă de control/verificare, scală de clasificare), <strong>investigația</strong>, <strong>proiectul</strong>, <strong>portofoliul</strong>, <strong>autoevaluarea</strong>, referatul/eseul, hărțile conceptuale, evaluarea reciprocă.</li>
</ul>
<h3>Calitățile instrumentelor de evaluare</h3>
{T(["Calitate", "Înțeles"],
   ["validitate", "măsoară ceea ce își propune (testul de programare verifică programarea, nu viteza de tastare)"],
   ["fidelitate", "rezultate constante la aplicări repetate sau la evaluatori diferiți"],
   ["obiectivitate", "acord între evaluatori independenți (bareme clare)"],
   ["aplicabilitate", "ușor de administrat și de interpretat în condițiile date"])}
""",
    exercitii=[
        dict(tip="aplicatie", titlu="Portofoliul la TIC", enunt="<p>Proiectați un portofoliu pentru un semestru de TIC (clasa a IX-a): componente, criterii de evaluare, avantaje și limite.</p>",
             model="<p><strong>Componente</strong>: document formatat avansat (stiluri, cuprins automat); prezentare despre siguranța online; registru de calcul cu formule și diagramă; o imagine prelucrată; fișă de autoevaluare și jurnal de reflecție.</p><p><strong>Criterii</strong> (grilă, câte 1–4 puncte): corectitudinea tehnică; utilizarea instrumentelor avansate; adecvarea la public și scop; originalitatea și respectarea drepturilor de autor; respectarea termenelor; calitatea reflecției.</p><p><strong>Avantaje</strong>: evaluează procesul și produsul, implică elevul în propria evaluare, surprinde progresul în timp. <strong>Limite</strong>: timp mare de evaluare, risc de plagiat (redus prin prezentarea orală a portofoliului).</p>",
             criterii=["componentele sunt legate de conținuturile semestrului", "criteriile sunt explicite și punctate", "există componentă de autoevaluare", "avantaje și limite pertinente"]),
        dict(tip="aplicatie", titlu="Tipul și funcția evaluării", enunt="<p>Precizați tipul (după moment) și funcția dominantă: a) un test la începutul clasei a IX-a despre algoritmii din gimnaziu; b) un quiz de 5 minute după explicarea căutării binare; c) lucrarea de la finalul unității „Liste”.</p>",
             model="<p>a) evaluare <strong>inițială</strong>, funcție <strong>diagnostică</strong> (și prognostică); b) evaluare <strong>formativă</strong>, funcție de <strong>reglare/feedback</strong>; c) evaluare <strong>sumativă</strong>, funcție de <strong>certificare</strong> a nivelului atins la finalul unității (și de ierarhizare prin notare).</p>",
             criterii=["tipurile sunt corecte", "funcțiile sunt corelate cu momentul"]),
    ],
    quiz=[("Evaluarea care se realizează pe parcursul învățării, pentru a o regla, este:", ["sumativă", "formativă", "inițială", "normativă"], 1, "Formativă."),
          ("Calitatea unui test de a măsura exact ce și-a propus este:", ["fidelitatea", "validitatea", "aplicabilitatea", "obiectivitatea"], 1, "Validitatea."),
          ("Care este o metodă complementară de evaluare?", ["proba scrisă", "proba orală", "portofoliul", "lucrarea semestrială"], 2, "Portofoliul."),
          ("Compararea rezultatelor unui elev cu media clasei este o evaluare:", ["criterială", "normativă", "formativă", "inițială"], 1, "Raportare la grup."),
          ("Funcția evaluării care identifică dificultățile de învățare este:", ["de certificare", "diagnostică", "de selecție", "motivațională"], 1, "Diagnostică.")],
))

LECTII.append(dict(
    id="m11", nr="11", scurt="Itemi și teste", titlu="Itemii și proiectarea unui test",
    programa="Programa E.3: itemi – definiție, clasificări, caracteristici, domenii de utilizare, reguli de proiectare, modalități de evaluare și notare, avantaje și limite",
    obiective=["clasificarea itemilor (obiectivi, semiobiectivi, subiectivi)", "regulile de proiectare pentru fiecare tip", "baremul de corectare și notare", "matricea de specificații și etapele construirii unui test"],
    teorie=f"""
<p><strong>Itemul</strong> = întrebarea/sarcina + formatul ei + răspunsul așteptat. Un test este format din mai mulți itemi.</p>
{T(["Categorie", "Tipuri", "Avantaje", "Limite"],
   ["<strong>Obiectivi</strong>", "cu alegere duală (A/F); de tip pereche (asociere); cu alegere multiplă (premisă + variante: un răspuns corect și distractori)", "corectare rapidă și obiectivă; acoperă mult conținut", "măsoară mai ales niveluri cognitive simple; ghicire posibilă; distractorii buni se construiesc greu"],
   ["<strong>Semiobiectivi</strong>", "cu răspuns scurt; de completare; întrebări structurate (subîntrebări legate de un suport comun: cod, schemă, tabel)", "răspunsul este construit de elev, ghicirea este limitată", "barem precis; pot exista răspunsuri corecte neprevăzute"],
   ["<strong>Subiectivi</strong> (cu răspuns deschis)", "rezolvare de probleme; eseu structurat; eseu liber", "evaluează niveluri înalte: analiză, creație, rezolvare de probleme", "timp de corectare, subiectivitate – se reduce prin bareme analitice"])}
<h3>Reguli de proiectare (selecție)</h3>
<ul>
<li><strong>Alegere duală</strong>: afirmații clare, fără negații duble, fără „întotdeauna/niciodată” care sugerează răspunsul.</li>
<li><strong>Pereche</strong>: liste omogene, mai multe răspunsuri decât premise (sau răspunsuri folosibile de mai multe ori), instrucțiuni clare.</li>
<li><strong>Alegere multiplă</strong>: premisa formulează o singură problemă; variante de lungimi apropiate; <strong>distractori plauzibili</strong> (proveniți din erori tipice ale elevilor); fără indicii gramaticale; poziția răspunsului corect variază; evitați „toate variantele de mai sus”.</li>
<li><strong>Semiobiectivi</strong>: un singur răspuns corect scurt; spațiul liber spre final; la întrebările structurate subîntrebările sunt independente (o greșeală la a) nu blochează b)).</li>
<li><strong>Subiectivi</strong>: sarcina precizată clar (ce, cum, cât), restricții și criterii comunicate; barem analitic.</li>
</ul>
<h3>Baremul</h3>
<p>Precizează răspunsul corect și punctajul pentru fiecare item și, la itemii complecși, punctajul pe <strong>elemente</strong> (barem analitic). Se acordă de obicei un punctaj din oficiu; nota = punctaj total / 10 (sau după conversia stabilită). Baremul se elaborează <em>odată cu</em> testul.</p>
<h3>Etapele proiectării unui test</h3>
<ol><li>stabilirea scopului și a competențelor/obiectivelor evaluate;</li><li><strong>matricea de specificații</strong> – tabel cu conținuturile pe linii și nivelurile cognitive pe coloane; în celule – ponderea (procent sau număr de itemi);</li><li>alegerea tipurilor de itemi și redactarea lor;</li><li>baremul de corectare și notare;</li><li>aplicarea, corectarea, analiza rezultatelor și măsurile de ameliorare.</li></ol>
{T(["Conținut \\ nivel", "A-și aminti", "A înțelege", "A aplica", "A analiza", "Total"],
   ["Structura alternativă", "5%", "10%", "15%", "–", "30%"],
   ["Structuri repetitive", "5%", "10%", "25%", "10%", "50%"],
   ["Algoritmi pe cifre", "–", "–", "10%", "10%", "20%"],
   ["Total", "10%", "20%", "50%", "20%", "100%"])}
""",
    exercitii=[
        dict(tip="aplicatie", titlu="Patru tipuri de itemi cu barem", enunt="<p>Pentru tema „Structura alternativă” (Python), elaborați un item cu alegere duală, unul cu alegere multiplă, unul de completare și unul de tip rezolvare de problemă, fiecare cu barem.</p>",
             model="<ol><li><strong>Alegere duală</strong>: Încercuiți A dacă afirmația este adevărată sau F dacă este falsă: „Ramura else a unei instrucțiuni if este obligatorie.” (A / F) – <em>barem: F – 1 p.</em></li><li><strong>Alegere multiplă</strong>: Ce afișează secvența <code>x = 7</code>; <code>if x % 2 == 0: print(\"par\")</code> <code>else: print(\"impar\")</code>? a) par b) impar c) 7 d) nimic – <em>barem: b – 1 p.</em> (distractori: a – confuzia condiției; c – confuzia dintre valoare și mesaj; d – necunoașterea lui else).</li><li><strong>Completare</strong>: Completați condiția astfel încât să se afișeze „DA” pentru numerele din [10, 99]: <code>if ______: print(\"DA\")</code> – <em>barem: <code>10 &lt;= n &lt;= 99</code> sau echivalent – 2 p.</em></li><li><strong>Rezolvare de problemă</strong>: Scrieți un program care citește trei numere și afișează cel mai mare, fără funcția max. – <em>barem analitic (5 p.): citire corectă – 1 p.; structură alternativă corectă – 2 p.; tratarea egalităților – 1 p.; afișare corectă – 1 p.</em></li></ol>",
             criterii=["fiecare item respectă regulile tipului său", "distractorii sunt plauzibili și justificați", "baremul este precis, iar la problemă este analitic", "itemii vizează niveluri cognitive diferite"]),
        dict(tip="aplicatie", titlu="Matricea de specificații", enunt="<p>Construiți matricea de specificații pentru un test de 45 de minute la unitatea „Liste” (clasa a IX-a), cu trei conținuturi și patru niveluri cognitive, apoi precizați numărul și tipul itemilor.</p>",
             model="<div class='tbl'><table><tr><th>Conținut \\ nivel</th><th>A-și aminti</th><th>A înțelege</th><th>A aplica</th><th>A analiza</th><th>Total</th></tr><tr><td>Crearea și accesul la elemente</td><td>10%</td><td>10%</td><td>10%</td><td>–</td><td>30%</td></tr><tr><td>Metode ale clasei list</td><td>5%</td><td>10%</td><td>15%</td><td>–</td><td>30%</td></tr><tr><td>Algoritmi pe liste</td><td>–</td><td>–</td><td>25%</td><td>15%</td><td>40%</td></tr><tr><td>Total</td><td>15%</td><td>20%</td><td>50%</td><td>15%</td><td>100%</td></tr></table></div><p><strong>Itemi</strong>: 3 cu alegere duală și 2 cu alegere multiplă (nivelurile a-și aminti/a înțelege), 2 de completare (a aplica), o întrebare structurată pe un program dat (a înțelege/a analiza), o problemă de programat (a aplica/a analiza). Barem pe 90 p. + 10 p. din oficiu.</p>",
             criterii=["matricea are conținuturile pe linii și nivelurile pe coloane", "totalurile sunt corecte (100%)", "ponderile reflectă importanța conținuturilor", "tipurile de itemi sunt potrivite nivelurilor"]),
    ],
    quiz=[("Întrebările structurate sunt itemi:", ["obiectivi", "semiobiectivi", "subiectivi", "de tip pereche"], 1, "Semiobiectivi."),
          ("Distractorii unui item cu alegere multiplă trebuie să fie:", ["evident greșiți", "plauzibili, bazați pe erori tipice", "mai lungi decât răspunsul corect", "identici"], 1, "Altfel itemul nu discriminează."),
          ("Ce conține matricea de specificații?", ["notele elevilor", "conținuturile și nivelurile cognitive, cu ponderi", "baremul", "lista metodelor"], 1, "Planul testului."),
          ("Eseul structurat este un item:", ["obiectiv", "semiobiectiv", "subiectiv", "de completare"], 2, "Cu răspuns deschis."),
          ("Când se elaborează baremul?", ["după corectare", "odată cu testul", "doar la cerere", "după afișarea notelor"], 1, "Asigură obiectivitatea.")],
))

LECTII.append(dict(
    id="m12", nr="12", scurt="Notarea și erorile de evaluare", titlu="Notarea și aprecierea școlară: variabilitate, erori, minimizare",
    programa="Programa E.3: notarea și aprecierea școlară – variabilitatea notării, factori, erori în evaluare / efecte perturbatoare și modalități de minimizare",
    obiective=["de ce aceeași lucrare poate primi note diferite", "efectele perturbatoare clasice", "măsurile de reducere a subiectivității", "feedbackul eficient"],
    teorie=f"""
<p><strong>Variabilitatea notării</strong>: diferențe de notare pentru aceeași performanță – între evaluatori (interindividuală) sau la același evaluator în momente diferite (intraindividuală). Factori: personalitatea și exigența profesorului, condițiile evaluării, ordinea lucrărilor, informațiile anterioare despre elev, lipsa criteriilor clare.</p>
{T(["Eroare / efect", "Descriere"],
   ["efectul „halo”", "aprecierea unei performanțe este influențată de impresia generală despre elev (rezultate bune anterioare, comportament)"],
   ["efectul Pygmalion", "așteptările profesorului influențează performanța și aprecierea elevului (profeția care se autoîmplinește)"],
   ["efectul de contrast", "o lucrare pare mai bună sau mai slabă prin comparație cu cea evaluată imediat înainte"],
   ["efectul de ordine", "nota variază după poziția lucrării în șirul corectat (oboseală, ajustarea exigenței)"],
   ["ecuația personală a examinatorului", "fiecare profesor are propriul nivel de exigență și criterii preferate"],
   ["eroarea de generozitate / de severitate", "notare sistematic prea indulgentă / prea exigentă"],
   ["eroarea tendinței centrale", "evitarea notelor extreme, concentrarea în zona de mijloc"],
   ["eroarea logică", "înlocuirea criteriilor de evaluare cu criterii secundare (forma în locul corectitudinii)"],
   ["efectul de contaminare", "nota este influențată de notele date de alți profesori sau de notele anterioare ale elevului"])}
<h3>Cum se reduce subiectivitatea</h3>
<ul><li>bareme și grile de evaluare clare, comunicate elevilor înainte;</li><li>criterii stabilite înainte de corectare, aplicate la fel pentru toți;</li><li>corectarea „pe item” (același item la toate lucrările), lucrări anonimizate;</li><li>dubla corectare la evaluări importante;</li><li>varietatea metodelor și a momentelor de evaluare;</li><li>autoevaluarea și evaluarea reciprocă, cu criterii;</li><li>reflecția profesorului asupra propriilor tendințe.</li></ul>
<p><strong>Feedbackul eficient</strong> este specific (ce anume este corect/greșit), oferit la timp, orientat spre sarcină și spre pașii următori, nu spre persoană.</p>
""",
    exercitii=[
        dict(tip="aplicatie", titlu="Recunoașteți efectul", enunt="<p>Identificați eroarea și propuneți o măsură de prevenire: a) un elev olimpic primește 10 deși programul lui nu tratează cazul n = 0, pe care l-a depunctat la alți elevi; b) după o lucrare excepțională, următoarea, de nivel mediu, primește o notă mai mică decât merită; c) un profesor nu dă niciodată note sub 5 sau peste 9; d) o lucrare corectă, dar scrisă dezordonat, primește 6.</p>",
             model="<ul><li>a) <strong>efectul halo</strong> – lucrări anonimizate, barem analitic aplicat strict;</li><li>b) <strong>efectul de contrast</strong> – corectarea pe item, recitirea comparativă cu baremul;</li><li>c) <strong>tendința centrală</strong> – raportarea la descriptori de performanță, folosirea întregii scale;</li><li>d) <strong>eroarea logică</strong> – criterii explicite: aspectul are o pondere mică, stabilită dinainte, în barem.</li></ul>",
             criterii=["toate efectele identificate corect", "măsurile sunt concrete și potrivite fiecărui efect"]),
        dict(tip="aplicatie", titlu="Feedback", enunt="<p>Rescrieți feedbackul „Programul tău e slab, mai lucrează” pentru un elev al cărui program calculează greșit media (împărțire întreagă) și nu tratează lista vidă.</p>",
             model="<p>„Citirea și parcurgerea listei sunt corecte. Două lucruri de îmbunătățit: 1) folosești <code>//</code> la calculul mediei, de aceea pentru 9 și 10 obții 9 în loc de 9.5 – înlocuiește cu <code>/</code>; 2) pentru o listă fără elemente programul se oprește cu eroare la împărțirea la zero – adaugă o verificare înainte. Testează apoi cu listele [9, 10] și [].”</p>",
             criterii=["începe cu ce este corect", "numește precis erorile și cauza lor", "indică pașii de corectare", "se referă la sarcină, nu la persoană"]),
    ],
    quiz=[("Supraevaluarea unei lucrări din cauza impresiei bune despre elev este:", ["efectul de contrast", "efectul halo", "tendința centrală", "eroarea logică"], 1, "Efectul halo."),
          ("Profesorul care nu folosește notele extreme manifestă:", ["severitate", "tendința centrală", "efectul Pygmalion", "efectul de ordine"], 1, "Tendința centrală."),
          ("Care măsură reduce efectul halo?", ["corectarea lucrărilor anonimizate", "corectarea seara", "notarea după media anterioară", "evitarea baremului"], 0, "Evaluatorul nu știe al cui este lucrarea."),
          ("Efectul Pygmalion se referă la:", ["oboseala evaluatorului", "influența așteptărilor profesorului", "ordinea lucrărilor", "aspectul lucrării"], 1, "Profeția care se autoîmplinește.")],
))

LECTII.append(dict(
    id="m13", nr="13", scurt="Inter-/transdisciplinar și CDEOȘ", titlu="Demersuri intra-, inter-, transdisciplinare și oferta de curriculum la decizia școlii",
    programa="Programa E.1: demersuri didactice intradisciplinare, interdisciplinare, transdisciplinare; oferte educaționale pentru curriculum, conform planurilor-cadru în vigoare",
    obiective=["diferențele dintre demersurile mono-, intra-, multi-, inter- și transdisciplinare", "exemple de proiecte integrate la informatică", "structura unei oferte de curriculum la decizia școlii (CDEOȘ)"],
    teorie=f"""
{T(["Demers", "Caracteristică", "Exemplu"],
   ["intradisciplinar", "legături între capitole ale aceleiași discipline", "sortarea pregătește căutarea binară și interclasarea"],
   ["multidisciplinar", "aceeași temă tratată în paralel, din perspectiva mai multor discipline", "tema „Apa” la biologie, geografie și informatică (baza de date cu măsurători)"],
   ["interdisciplinar", "transferul de concepte și metode între discipline pentru o temă comună", "statistica (matematică) aplicată în calcul tabelar și în Python"],
   ["transdisciplinar", "o problemă reală care depășește granițele disciplinelor; accent pe competențe transversale", "proiectul „Școala verde”: senzori IoT, analiza datelor, campanie digitală"])}
<h3>Oferta de curriculum la decizia școlii (CDEOȘ)</h3>
<p>Programa unei discipline opționale propuse de profesor are, de regulă, structura: <strong>argument</strong> (necesitate, legătura cu interesele elevilor și resursele școlii) – <strong>competențe generale</strong> – <strong>competențe specifice și activități de învățare</strong> – <strong>conținuturi</strong> – <strong>sugestii metodologice</strong> – <strong>sugestii de evaluare</strong> – <strong>bibliografie</strong>. Se elaborează și se avizează conform metodologiei în vigoare (verifică formatul oficial).</p>
<p>Exemple de opționale potrivite: Robotică și programare vizuală, Dezvoltarea de aplicații mobile (App Inventor), Inteligență artificială pentru începători, Securitate cibernetică, Grafică 3D și imprimare 3D, Pregătire pentru olimpiadă.</p>
""",
    exercitii=[
        dict(tip="aplicatie", titlu="Proiect transdisciplinar", enunt="<p>Descrieți un proiect transdisciplinar de 4 săptămâni pentru clasa a VIII-a care folosește competențe digitale: tema, disciplinele implicate, sarcinile elevilor, produsul final, evaluarea.</p>",
             model="<p><strong>Tema</strong>: „Cât consumă școala noastră?” <strong>Discipline</strong>: Informatică și TIC, matematică, fizică, educație civică. <strong>Sarcini</strong>: colectarea datelor de consum (facturi, citiri de contoare), organizarea lor într-un registru de calcul, calcule și grafice, explicarea fenomenelor fizice (putere, energie), formularea a 5 măsuri de economisire, realizarea unei prezentări pentru consiliul elevilor. <strong>Produs</strong>: raport + prezentare + afiș digital. <strong>Evaluare</strong>: grilă pentru proiect (corectitudinea datelor, calitatea graficelor, argumentarea, colaborarea), autoevaluare și evaluare între colegi.</p>",
             criterii=["problema este reală și relevantă pentru elevi", "integrează cel puțin 3 discipline", "există un produs final concret", "evaluarea are criterii explicite"]),
        dict(tip="aplicatie", titlu="Structura unui opțional", enunt="<p>Elaborați structura (fără a dezvolta complet) unei programe de opțional „Robotică și programare vizuală” (o oră pe săptămână, un an).</p>",
             model="<ol><li><strong>Argument</strong>: interesul elevilor pentru tehnologie, dezvoltarea gândirii algoritmice și a competenței digitale, existența unui simulator gratuit (Open Roberta Lab).</li><li><strong>Competențe generale</strong>: 1. utilizarea mediilor de programare vizuală pentru modelarea comportamentului unui robot; 2. colaborarea în echipă pentru realizarea unui proiect tehnic.</li><li><strong>Competențe specifice + activități</strong> (de ex. 1.1 „Utilizarea senzorilor pentru luarea deciziilor” – programarea unui robot care ocolește obstacole).</li><li><strong>Conținuturi</strong>: structura unui robot; senzori și actuatori; structuri de control în blocuri; proiect final.</li><li><strong>Sugestii metodologice</strong>: învățare prin proiect, provocări graduale, lucru în perechi.</li><li><strong>Sugestii de evaluare</strong>: portofoliu, prezentarea proiectului, grile de autoevaluare.</li><li><strong>Bibliografie și resurse</strong>.</li></ol>",
             criterii=["are toate secțiunile unei programe de opțional", "competențele sunt formulate corect", "conținuturile corespund competențelor", "evaluarea este coerentă cu metodele"]),
    ],
    quiz=[("Aceeași temă tratată în paralel de mai multe discipline, fiecare din perspectiva ei, este un demers:", ["intradisciplinar", "multidisciplinar", "transdisciplinar", "monodisciplinar"], 1, "Multidisciplinar."),
          ("Ce secțiune deschide de obicei programa unui opțional?", ["bibliografia", "argumentul", "evaluarea", "conținuturile"], 1, "Argumentul justifică oferta."),
          ("Un proiect pornit de la o problemă reală, care depășește granițele disciplinelor, este:", ["transdisciplinar", "intradisciplinar", "monodisciplinar", "normativ"], 0, "Transdisciplinar.")],
))

LECTII.append(dict(
    id="m14", nr="14", scurt="Cum rezolvi subiectul de metodică", titlu="Cum rezolvi un subiect de metodică – strategie și model",
    programa="Sinteză: E.1–E.3 aplicate pe un subiect complet",
    obiective=["cum citești cerința și ce verbe de cerință apar", "structura unui răspuns complet", "greșelile frecvente care costă puncte", "un model integral rezolvat"],
    teorie=f"""
<h3>Pași</h3>
<ol><li><strong>Subliniază</strong> elementele cerinței: clasa, tema, tipul lecției, numărul de elemente cerute („trei metode”, „două tipuri de itemi”).</li>
<li><strong>Folosește terminologia</strong> din documentele curriculare și din bibliografia programei (competențe specifice, obiective operaționale, strategie didactică, itemi semiobiectivi etc.).</li>
<li><strong>Contextualizează</strong>: fiecare noțiune teoretică se aplică pe conținutul de informatică cerut – exemplele concrete arată că știi să predai, nu doar să reproduci teorie.</li>
<li><strong>Asigură coerența</strong>: competența → obiectivele → activitățile → metodele → evaluarea trebuie să se lege.</li>
<li><strong>Respectă numărul și ordinea</strong> elementelor cerute; folosește tabele unde ajută (scenariul lecției, matricea de specificații, barem).</li></ol>
<div class="note warn"><b>Greșeli frecvente:</b> obiective neoperaționale („să înțeleagă”); metode numite, dar nedescrise pe tema dată; itemi fără barem; distractori neplauzibili; scenariu fără timp sau fără activitatea elevilor; confuzia competență–obiectiv–conținut; teorie generală fără exemplu de informatică.</div>
<p>Structura exactă a subiectelor și punctajul se stabilesc de comisia națională pentru fiecare sesiune; exersează pe subiectele oficiale din anii anteriori, publicate de minister.</p>
""",
    exercitii=[
        dict(tip="aplicatie", titlu="Subiect integral (model)", enunt="<p><em>Subiect de antrenament, construit după tipul cerințelor din programă (nu este un subiect oficial):</em></p><p>Pentru tema „Algoritmul lui Euclid”, clasa a IX-a:</p><ol><li>formulați o competență specifică (ilustrativă) și două obiective operaționale derivate;</li><li>descrieți aplicarea a două metode didactice în cadrul lecției;</li><li>elaborați doi itemi de tipuri diferite, cu barem, care să evalueze obiectivele formulate;</li><li>precizați două erori de evaluare care pot apărea la corectarea itemului subiectiv și cum le preveniți.</li></ol>",
             model="<p><strong>1.</strong> Competență specifică (ilustrativă): „Implementarea algoritmilor de prelucrare a datelor numerice într-un limbaj de programare.” Obiective: O1 – să aplice algoritmul lui Euclid pas cu pas pentru o pereche de numere dată, completând corect tabelul resturilor; O2 – să implementeze în Python o funcție care determină cmmdc-ul și cmmmc-ul a două numere, programul trecând cel puțin 4 din 5 teste date.</p><p><strong>2.</strong> <em>Conversația euristică</em>: pornind de la întrebarea „Care este cea mai mare latură a pătratelor egale în care putem împărți fără rest o foaie de 84 × 36?”, elevii sunt conduși prin întrebări să observe că cmmdc(84, 36) = cmmdc(36, 84 mod 36) și să formuleze algoritmul. <em>Exercițiul (învățarea asistată de calculator)</em>: elevii implementează funcția și o testează pe cazuri date (numere prime între ele, numere egale, un număr multiplu al celuilalt), cu feedback imediat din teste.</p><p><strong>3.</strong> Item semiobiectiv (O1): „Completați tabelul pașilor algoritmului lui Euclid pentru a = 252, b = 105 și precizați cmmdc-ul.” – barem: resturile 42, 21, 0 – câte 1 p.; cmmdc = 21 – 1 p. Item subiectiv (O2): „Scrieți o funcție cmmdc(a, b) și un program care citește două numere și afișează cmmdc și cmmmc.” – barem analitic: antetul funcției – 1 p.; bucla Euclid corectă – 2 p.; return – 1 p.; cmmmc = a·b // cmmdc – 1 p.; citire/afișare – 1 p.</p><p><strong>4.</strong> <em>Efectul halo</em> – prevenit prin corectarea lucrărilor anonimizate și aplicarea strictă a baremului analitic; <em>efectul de contrast</em> – prevenit prin corectarea pe item (același item la toate lucrările) și raportarea la barem, nu la lucrarea anterioară.</p>",
             criterii=["obiectivele sunt operaționale și derivă din competență", "metodele sunt descrise pe conținutul cerut, nu doar numite", "itemii au tipuri diferite și barem", "itemii evaluează obiectivele formulate (coerență)", "erorile de evaluare sunt numite corect și au măsuri concrete"]),
    ],
    quiz=[("Care formulare este un obiectiv operațional corect?", ["Elevii să cunoască algoritmul lui Euclid.", "Elevii vor înțelege recursivitatea.", "Elevii vor implementa funcția cmmdc, trecând 4 din 5 teste.", "Profesorul va explica cmmdc."], 2, "Comportament observabil + condiții + criteriu."),
          ("Ce asigură coerența unui răspuns la metodică?", ["lungimea răspunsului", "legătura competență – obiective – activități – evaluare", "numărul de citate", "folosirea doar a teoriei"], 1, "Elementele trebuie să se lege."),
          ("Când descrii o metodă didactică într-un subiect, trebuie:", ["doar să o numești", "să o aplici concret pe tema cerută", "să dai definiția din dicționar", "să o eviți"], 1, "Contextualizarea aduce punctajul.")],
))
