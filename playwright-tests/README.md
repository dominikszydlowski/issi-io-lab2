# Rozwiązanie – Testowanie nawigacji strony Wydziału Informatyki AGH

## 1. Przygotowanie środowiska

Do wykonania testów wykorzystano:
- Python
- Playwright
- pytest
- uv – do zarządzania zależnościami i uruchamiania testów

Dodanie wymaganych bibliotek:

```bash
cd playwright-tests
uv add --dev pytest pytest-playwright
```

Instalacja przeglądarek:

```bash
cd playwright-tests
uv run playwright install chromium firefox
```
## 2. Przygotowane testy

### Test 1 – Strona główna

### Test 2 – Podstrona „O Wydziale”

### Test 3 – Sekcja „Nasze kierunki”

### Test 4 – Zmiana adresu URL

## 3. Uruchomienie testów za pomocą pytest

Wszystkie przygotowane testy można uruchomić poleceniem:

```bash
cd playwright-tests
uv run pytest -v
```
## 4. Uruchomienie testów w Firefox i Chromium

```bash
cd playwright-tests
uv run pytest  --browser firefox -v
uv run pytest  --browser chromium -v
```
## 5. Uruchomienie testów w trybie headed

```bash
uv run pytest tests/test_agh.py --browser firefox --headed --slowmo 1000 -v
```