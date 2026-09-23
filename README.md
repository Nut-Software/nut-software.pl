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

Nie zmieniaj rekordu `panel` (`138.2.171.118`) ani pozostałych rekordów subdomeny. Nie dodawaj `CNAME` do repozytorium, dopóki rekordy DNS nie zostaną ustawione, ponieważ adres pod `github.io` przekieruje wtedy na jeszcze niedziałającą domenę.

Treści kontaktowe i opis działalności należy uzgodnić z właścicielem przed rozszerzeniem strony o szczegółową ofertę.
