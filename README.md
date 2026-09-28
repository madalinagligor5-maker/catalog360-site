# Catalog360.ro – site static

Fișiere: `index.html` (CSS și JS incluse, fără dependențe), `robots.txt`, `sitemap.xml`, `assets/`.

## Deploy pe Vercel

Proiectul este HTML/CSS/JS static. `vercel.json` setează explicit presetul **Other**, fără comandă de build, și publică direct fișierele din rădăcina proiectului.

## De completat înainte de lansare
1. **Fotografie hero** – caută `IMAGINE HERO`; folosește o fotografie reală (WebP, ~1440px lățime, alt text descriptiv).
2. **Formular Scor Digital360** – caută `TODO producție` în script și conectează endpoint-ul (email, CRM etc.).
3. **GTM / GA4 / Search Console** – decomentează snippet-urile din `<head>` și setează ID-urile. Evenimente trimise în dataLayer: `cta_click`, `generate_lead`.
4. **Date firmă** – footer (`Date firmă`), plus `address`/`telephone` în Schema ProfessionalService când există sediu public.
5. **Imagine Open Graph** – adaugă un vizual 1200×630 și reactivează meta-tagurile `og:image`.
6. **Durate din FAQ** – verifică termenele (2–3 / 3–6 săptămâni).

## SEO
- Un singur H1, H2/H3 ierarhic, canonical, OG, Schema (Organization, ProfessionalService, Service ×3, WebSite).
- FAQPage nu este marcat intenționat: Google afișează rich results FAQ doar pentru site-uri guvernamentale/medicale autoritare.
- BreadcrumbList se adaugă pe subpagini (/seo-local, /creare-site-salon etc.), apoi fiecare pagină nouă intră în sitemap.xml.
