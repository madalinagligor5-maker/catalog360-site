# Catalog360.ro – Titularizare Informatică și TIC

Site static: material de pregătire pentru titularizare la Informatică și Tehnologia Informației, structurat după programa de concurs (Anexa 49, MO nr. 972 bis/23.XI.2026).

Fișiere: `index.html` (CSS și JS incluse), `python.html` (Academia Python, servită la `/python`), `assets/logo-catalog360.png`, `robots.txt`, `sitemap.xml`, `vercel.json`.

## Deploy pe Vercel

`vercel.json` setează presetul **Other**, fără comandă de build, și publică direct fișierele din rădăcină. Adresa veche `/titularizare-informatica-tic` redirecționează permanent spre `/`.

## Conținut

- 10 capitole științifice și 3 de metodică, cu teorie, exerciții rezolvate și teste rapide.
- Codul din exemple (Python, C++, SQL) a fost rulat; rezultatele afișate sunt cele reale.
- Progresul utilizatorului se salvează doar în browser (`localStorage`).

## Academia Python (`/python`)

`python.html` este **generat** – nu se editează direct. Sursele sunt în `_src/academie/` (lecțiile în `lectii_*.py`, șablonul în `sablon.html`):

```bash
python3 _src/academie/build.py
```

Scriptul rulează soluțiile de referință ale tuturor exercițiilor și calculează rezultatele așteptate ale testelor, deci acestea nu se scriu de mână. În browser, codul rulează cu Pyodide (Python compilat în WebAssembly) încărcat de pe cdn.jsdelivr.net, într-un Web Worker cu limită de timp. `_src/` nu este publicat (`.vercelignore`).
