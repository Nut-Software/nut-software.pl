# Nut Software

Dwujęzyczna strona wizytówka organizacji Nut Software. Jest to statyczna strona HTML/CSS/JavaScript, publikowana przez GitHub Pages z gałęzi `main` (katalog `/`).

## Lokalny podgląd

```sh
python3 -m http.server 8000
```

Otwórz `http://localhost:8000`.

## Publikacja

GitHub Pages publikuje gałąź `main` (katalog `/`) pod `https://nut-software.github.io/nut-software.pl/`.

Domena docelowa to `nut-software.pl`. Po uzyskaniu dostępu do DNS w Simply.com:

1. Dodaj rekordy `A` dla `@`: `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`.
2. Dodaj rekordy `AAAA` dla `@`: `2606:50c0:8000::153`, `2606:50c0:8001::153`, `2606:50c0:8002::153`, `2606:50c0:8003::153`.
3. Dodaj rekord `CNAME` dla `www` wskazujący na `nut-software.github.io`.
4. Ustaw na GitHub Pages domenę niestandardową `nut-software.pl`.
5. Po propagacji DNS sprawdź HTTPS i włącz `Enforce HTTPS` w ustawieniach Pages.

Nie zmieniaj rekordu `panel` (`138.2.171.118`) ani pozostałych rekordów subdomeny. Plik `CNAME` w repozytorium kieruje adres pod `github.io` na domenę docelową.

Treści kontaktowe i opis działalności należy uzgodnić z właścicielem przed rozszerzeniem strony o szczegółową ofertę.

## Treści, języki i SEO

- Polski: `https://nut-software.pl/`; angielski: `https://nut-software.pl/en/`.
- Obie strony zawierają pełny HTML. Zmiana języka jest zwykłym linkiem i działa bez JavaScriptu; zapisany dawniej język w localStorage nie zmienia adresu ani treści.
- Edytuj teksty w `content/translations.json` i układ w `templates/page.html.tmpl`, a następnie uruchom `python3 scripts/build_site.py`. Zapisz wygenerowane `index.html`, `en/index.html` i `sitemap.xml` w Git przed publikacją. Nie jest potrzebny dodatkowy build na serwerze.
- Canonical, wzajemne hreflang (pl/en/x-default), opisy, Open Graph i JSON-LD powstają ze wspólnego generatora. `Organization`, `WebSite` i `WebPage` opisują rzeczywiste dane firmy.
- Publiczne dane: Nut Software Sebastian Orzechowski, NIP 8741681486, REGON 386776684, **wyłącznie Bydgoszcz, Polska**. Nie dodawaj ulicy, numeru lokalu ani kodu pocztowego do strony, metadanych, schema, źródeł czy dokumentacji. To jawna decyzja właściciela.
- NIP i REGON sprawdzono w publicznym wykazie Ministerstwa Finansów 23.09.2026. Nazwa została podana przez właściciela i znaleziona w katalogu firm. Status VAT nie jest publikowany, ponieważ może się zmieniać.
- `robots.txt` zezwala robotom na dostęp i wskazuje mapę strony. Obejmuje też roboty wyszukiwania AI, np. OAI-SearchBot; dostęp nie gwarantuje indeksacji ani cytowania.
- Galerie i szkice logo mają `noindex, follow`. Pliki logo pozostają dostępne dla robotów oraz użytkowników.
- Grafika podglądu linku: `assets/brand/social-card.png`, 1200 × 630 px.

## Zgłoszenie do wyszukiwarek

1. Zaloguj się na właściwe konto w Google Search Console i dodaj domenę `nut-software.pl`.
2. Dla właściwości domenowej Google wygeneruje rekord TXT. Dodaj go w Simply.com obok istniejących rekordów TXT; nie zastępuj rekordów Zoho ani SPF. Nie zmieniaj rekordów MX lub subdomeny panel.
3. Po weryfikacji zgłoś `https://nut-software.pl/sitemap.xml` i sprawdź oba adresy językowe w inspekcji URL. Poproś o indeksowanie.
4. Analogicznie można dodać stronę w Bing Webmaster Tools, także importując zweryfikowaną właściwość Google.

Weryfikacja właściciela, zgłoszenie mapy i obecność w indeksie to oddzielne kroki. Publikacja strony sama ich nie potwierdza. Dalszy rozwój oferty, specjalizacji i realizacji wymaga treści od właściciela; nie dopisuj niepotwierdzonych klientów, projektów, certyfikatów ani usług.
