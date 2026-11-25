# Catalog360.ro – Titularizare Informatică și TIC

Site static de pregătire pentru titularizarea la Informatică și Tehnologia Informației, de la zero, după programa de concurs (Anexa 49, MO nr. 972 bis/23.XI.2026).

## Structură

| Pagină | Fișier | Conținut |
|---|---|---|
| `/` | `index.html` | harta pregătirii, progresul, planul de studiu (generată) |
| `/python` | `python.html` | Python de la zero – exerciții verificate automat în browser (generată) |
| `/culegere` | `culegere.html` | culegere Python de nivel examen – teste ascunse, cazuri limită, mod examen (generată) |
| `/algoritmi` | `algoritmi.html` | algoritmi și structuri de date – exerciții verificate automat (generată) |
| `/cpp` | `cpp.html` | C++ de la zero – exemple compilate, aplicații cu rezolvare-model (generată) |
| `/metodica` | `metodica.html` | metodica predării – aplicații de tip subiect cu grilă de autoevaluare (generată) |
| `/programa` | `programa.html` | sinteză pe toate capitolele programei (scrisă de mână) |
| `/teste` | `teste.html` | generator de teste grilă din toate secțiunile (generată) |
| `/simulari` | `simulari.html` | simulări de probă scrisă cu barem și autoevaluare (generată; sursa: `simulari.py`) |

## Generare

Paginile marcate „generată” **nu se editează direct**. Sursele sunt în `_src/academie/`:
`cursuri.py` (configurația cursurilor și meniul), `python_*.py`, `culegere_*.py`, `algoritmi_*.py`, `cpp_*.py`, `metodica_*.py` (lecțiile),
`sablon*.html` (șabloanele), `util.py`, `build.py`.

```bash
python3 _src/academie/build.py
```

Scriptul:
- rulează soluțiile de referință ale exercițiilor și calculează rezultatele așteptate ale testelor;
- rulează/compilează (g++, C++17) toate exemplele din teorie și le afișează ieșirea reală;
- verifică prin rulare răspunsurile corecte ale întrebărilor „Ce afișează?” din C++;
- strânge toate întrebările grilă (inclusiv din `programa.html`) în banca de teste;
- actualizează meniul comun din `programa.html`;
- verifică simulările: punctajele (90 + 10), baremele, grilele „ce afișează”, ieșirile din rezolvările-model și interogările SQL (rulate în SQLite).

În browser, codul Python rulează cu Pyodide (cdn.jsdelivr.net), într-un Web Worker cu limită de timp. Progresul se salvează în `localStorage`. `_src/` nu este publicat (`.vercelignore`).

## Deploy pe Vercel

`vercel.json`: preset **Other**, fără comandă de build, fișierele din rădăcină publicate direct, `cleanUrls`. Adresa veche `/titularizare-informatica-tic` redirecționează spre `/programa`.
