# Warianty znaku Nut Software

Siedem samodzielnych grafik PNG z kanałem alfa: AWS, Python, Django, React, baza danych, Linux i sam orzech bez skorupki oraz symbolu.

Otwórz `index.html`, aby porównać warianty na jasnym tle i pobrać pliki. `nut-software-logos.zip` zawiera cały zestaw.

Grafiki powstały przy użyciu wbudowanego image_gen. Prompty i pochodzenie zapisano w `generation-prompts.json`. To grafiki rastrowe o rozmiarze 1254 × 1254 px; rysunek skorupki może nieznacznie różnić się między wariantami.

Są przeznaczone do ilustracji poszczególnych technologii. Do małych ikon potrzebne może być uproszczenie detali. Symbole technologii są stylizowanymi nawiązaniami.

## Archiwum projektów — 2026-09-23

W `concepts/` zapisano cztery oryginalne plansze PNG, dwa wstępne szkice HTML/CSS oraz indeks z opisami. `concepts/index.html` pokazuje kolejne etapy projektu. `concepts/manifest.json` przypisuje czytelne nazwy do plików źródłowych.

- `01-walnut-kernel.png`: orzech bez skorupki i symbolu kodu, z prezentacją nazwy.
- `02-shell-lime-code.png`: skorupka i duży tag na limonkowym tle.
- `03-shell-subtle-code.png`: skorupka z subtelnym symbolem; wariant początkowo wskazany do użycia.
- `04-shell-neutral-code.png`: większy tag na neutralnym tle, późniejsza baza wersji technologicznych.

Dalsze porównywanie wariantów poprzedziło zmianę głównego logo strony. To archiwum propozycji, a nie informacja o wdrożeniu konkretnego znaku. Warianty PNG można ponownie edytować generatorem; szkice HTML/CSS są zapisane w formie źródłowej. Wersje wektorowe SVG są dostępne obok plików PNG; patrz sekcja poniżej.

`nut-software-projects.zip` zawiera pełne archiwum: warianty technologiczne, sam orzech, plansze koncepcyjne, szkice, galerie i dokumentację. `nut-software-logos.zip` pozostaje paczką siedmiu samodzielnych znaków.

## SVG i logo używane na stronie

- `nut-logo.svg`: główny znak ze skorupką i subtelnym symbolem kodu, w nagłówku strony.
- `nut-logo-lime.svg`: ten sam znak w kolorze limonkowym, na ciemnym tle sekcji głównej.
- `nut-code.svg`: alternatywa z większym symbolem kodu.
- `nut-{aws,python,django,react,database,linux,plain}.svg`: warianty technologiczne i sam orzech.
- `nut-favicon.svg`: ręcznie uproszczony znak do małych rozmiarów, również jako `/favicon.svg`.
- `/favicon-32.png` i `/apple-touch-icon.png`: eksporty uproszczonego SVG w rozmiarach 32 i 180 px.

SVG zawierają wyłącznie geometrię wektorową, bez osadzonych bitmap i zależności od fontów. Kontury PNG przekształcono w krzywe, oczyszczono drobne artefakty, ujednolicono kolor i wyśrodkowano znaki. Nieznaczne różnice rysunku między źródłowymi wariantami zachowano. Przezroczyste prześwity działają na dowolnym tle. Kolor można zmienić w atrybucie `fill` elementu głównego SVG. Uproszczona ikona ma własne kolory wypełnień i konturów.

Do strony używaj `<img src="assets/brand/nut-logo.svg" width="44" height="44" alt="">` obok tekstowej nazwy firmy. Samodzielny znak powinien mieć opis `alt="Nut Software"`.

Odtworzenie wektorów: zainstaluj Pillow i vtracer 0.6.15, następnie uruchom `python scripts/vectorize_brand.py` z repozytorium. Skrypt czyta zachowane PNG i plansze z `concepts/`; uproszczona ikona jest osobnym, ręcznie opracowanym SVG. Do eksportów PNG użyto Sharp.

`nut-software-vectors.zip` zawiera 11 plików SVG i dokumentację. Pełne archiwum `nut-software-projects.zip` obejmuje także źródłowe PNG, plansze, szkice oraz skrypt wektoryzacji.
